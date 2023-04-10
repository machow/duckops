from functools import wraps, singledispatch

from siuba.sql.dialects.duckdb import DuckdbColumn, DuckdbColumnAgg, translator
from siuba.siu import symbolic_dispatch, Lazy, Call, str_to_getitem_call
from siuba.siu.dispatchers import NoArgs
from siuba.sql.translate import CustomOverClause, CumlOver

from sqlalchemy import sql
from sqlalchemy.dialects.postgresql import dialect as pg_dialect

from . import _type_backends as be

import duckdb
import pandas as pd


@singledispatch
def _query_call(x, *args, **kwargs):
    """Execute a query and return the resulting data."""
    raise NotImplementedError(f"Unsupported type: {type(x)}")

@_query_call.register(sql.ClauseElement)
def _(clause):
    con = duckdb.connect()

    compiled = compile(clause)

    res = con.execute(f"SELECT {compiled} AS _tmp_res_")
    fetched = res.fetchall()
    assert len(fetched) == 1
    assert len(fetched[0]) == 1

    return fetched[0][0]


@_query_call.register(Call)
def _(clause):
    expr = translator.shape_call(clause, verb_name="_query_call")

    res = expr(None)

    if not isinstance(res, sql.ClauseElement):
        raise TypeError(f"Unsupported result type: {type(res)}")

    return _query_call(res)


@_query_call.register(be.PdSeries)
def _(col, func: Call):
    """Execute a temporary duckdb query, and return the series result

    Note that this assumes func is a transformation, not an aggregate.

    Parameters
    ----------
    col:
        A column of data.
    func:
        A function mapping (codata, sqlalchemy column) -> result. Similar
        to calling the function of interest directly on sql data.
    """

    import pandas as pd

    con = duckdb.connect()

    # create temporary dateframe with a single column ----
    tmp_col_name = "__some_col__"
    tmp_df = pd.DataFrame({tmp_col_name: col})

    # compile func to a sql string ----
    sql_expr = func(DuckdbColumn(), sql.column(tmp_col_name))
    col_query = compile(sql_expr)
    query = f"SELECT {col_query} AS __result__ FROM tmp_df"

    # execute query ----
    res_df = con.execute(query).df()

    res_col = res_df["__result__"]
    res_col.name = None

    return res_col


@_query_call.register(be.PdFrame)
def _(frame, func: Call):
    import pandas as pd

    con = duckdb.connect()
    col_names = list(frame.columns)

    sql_cols = [sql.column(name) for name in col_names]
    sql_expr = func(DuckdbColumn(), *sql_cols)

    col_query = compile(sql_expr)

    tmp_df = frame
    query = f"SELECT {col_query} AS __result__ FROM tmp_df"

    # execute query ----
    res_df = con.execute(query).df()

    res_col = res_df["__result__"]
    res_col.name = None

    return res_col


class NoArgOver(CumlOver):

    @classmethod
    def func(cls, name: str):
        sa_func = getattr(sql.func, name)
        def f(codata, col, *args, **kwargs):
            from siuba.siu.calls import MetaArg
            if not isinstance(col, sql.ColumnCollection):
                raise TypeError("Must be called with a plain siuba _")

            if args or kwargs:
                raise ValueError("This function does not take additional arguments.")

            return cls(sa_func())

        return f


def compile(expr: sql.ClauseElement) -> str:
    return expr.compile(
        dialect=pg_dialect(),
        compile_kwargs = {"literal_binds": True}
    )



def lit(sql: object) -> sql.ClauseElement:
    return Lazy(sql)


def sql_scalar(func_name: str):

    def decorator(f):
        @support_no_args
        @symbolic_dispatch(cls = DuckdbColumn)
        @wraps(f)
        def wrapped(codata: DuckdbColumn, *args):
            return getattr(sql.func, func_name)(*args)

        return wrapped
    
    return decorator


def sql_agg(func_name: str, win_type: CustomOverClause):

    def decorator(f):
        @support_no_args
        @symbolic_dispatch(cls = DuckdbColumnAgg)
        @wraps(f)
        def wrapped(codata: DuckdbColumnAgg, *args):
            return getattr(sql.func, func_name)(*args)

        wrapped.register(DuckdbColumn, win_type.func(func_name))
        return wrapped

    return decorator


def sql_win(func_name: str, win_type: CustomOverClause):

    def decorator(f):
        @support_no_args
        @symbolic_dispatch(cls = DuckdbColumn)
        @wraps(f)
        def wrapped(codata: DuckdbColumn, *args):
            return win_type.func(func_name)(codata, *args)

        return wrapped

    return decorator


def support_no_args(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        from siuba.siu import Call, Symbolic
        from ._types import Data

        # Case 1: no arguments -----
        if not len(args) or len(kwargs):
            return f(NoArgs())

        # Case 2: contains something lazy -----
        everything = [*args, *kwargs.values()]
        if any(isinstance(arg, (Call, Symbolic)) and not isinstance(arg, Data) for arg in everything):
            return f.dispatch(Call)(*args, **kwargs)

        return f(*args, **kwargs)

    return wrapped

