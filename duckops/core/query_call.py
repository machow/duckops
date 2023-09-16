from functools import singledispatch
from sqlalchemy import sql

from siuba.sql.dialects.duckdb import DuckdbColumn
from duckops.prototypes import (
    PdSeries,
    IsLiteral,
    IsConcretePandas,
    IsConcretePolars,
)

from .convert import convert


def compile(expr: sql.ClauseElement) -> str:
    from sqlalchemy.dialects.postgresql import dialect as pg_dialect

    return expr.compile(dialect=pg_dialect(), compile_kwargs={"literal_binds": True})


@singledispatch
def query_call(x, *args, **kwargs):
    """Execute a query and return the resulting data."""
    raise NotImplementedError(f"Unsupported type: {type(x)}")


@query_call.register(IsConcretePandas)
def _pd_query_call(codata, args, func):
    import pandas as pd
    import duckdb

    con = duckdb.connect()

    converted = []
    series_args = {}
    n_cols = 0

    for arg in args:
        if isinstance(arg, PdSeries):
            name = f"col_{n_cols}"
            series_args[name] = arg
            converted.append(sql.column(name))
            n_cols += 1
        else:
            converted.append(convert(arg))

    tmp_df = pd.DataFrame(series_args)  # noqa: F841

    sql_expr = func(DuckdbColumn(), *converted)
    col_query = compile(sql_expr)

    query = f"SELECT {col_query} AS __result__ FROM tmp_df"

    # execute query ----
    res_df = con.execute(query).df()

    res_col = res_df["__result__"]
    res_col.name = None

    return res_col


@query_call.register(IsConcretePolars)
def _pl_query_call(codata, args, func):
    # TODO: could use databackend
    import polars as pl

    # TODO: just using pandas for now
    new_args = [x.to_pandas() if isinstance(x, pl.Series) else x for x in args]

    pandas_result = _pd_query_call(codata, new_args, func)
    return pl.Series(pandas_result)


@query_call.register(IsLiteral)
def _lit_query_call(codata, args, func, kwargs=None):
    import duckdb

    con = duckdb.connect()

    converted_args = [convert(arg) for arg in args]
    if kwargs:
        converted_kwargs = {k: convert(v) for k, v in kwargs.items()}
    else:
        converted_kwargs = {}
    sql_expr = func(DuckdbColumn(), *converted_args, **converted_kwargs)

    compiled = compile(sql_expr)

    res = con.execute(f"SELECT {compiled} AS _tmp_res_")
    fetched = res.fetchall()
    assert len(fetched) == 1
    assert len(fetched[0]) == 1

    return fetched[0][0]
