from __future__ import annotations

from abc import ABC
from plum import dispatch
from typing import Union

# concrete data ---
import pandas as pd
import polars as pl
from siuba.siu import Symbolic, Call

# guts ---
from duckops._types import Interval
from duckops._core import _query_call, DuckdbColumn
from duckops import str as str_
from duckops import dt
from sqlalchemy import sql

# Unions ----
# Date, Timestamp, Time, Timestamp with Timezone
# But also, what is Time?
DatetimeLike = Union[Interval]


# Pre-processing steps ----
#   * process all LiteralLike to go into SQL
#   * ConcreteLike dispatch: separate literals and concretes
#   * Handle homogeneous tuples as LiteralLike list


# Generic dispatch functions ----

@dispatch
def date_part(*args, **kwargs):
    return dispatch_on_trait(date_part, args, kwargs)


@dispatch
def date_part(codata: IsLiteral, part: LiteralLike, x: DatetimeLike):
    # TODO: conversions should happen somewhere else
    return _query_call(IsLiteral(), [part, x], date_part)


@dispatch
def date_part(codata: IsConcretePandas, *args: pd.Series | LiteralLike):
    # TODO: need to handle dop literal x concrete
    return _query_call(codata, args, date_part)


@dispatch
def date_part(codata: IsSymbol, *args):
    # Be sure to convert all the args
    return to_symbol(date_part, args)


@dispatch
def date_part(codata: DuckdbColumn, *args):
    return sql.func.date_part(*args)


@dispatch
def concat(*args, **kwargs):
    return dispatch_on_trait(concat, args, kwargs)


@dispatch
def concat(codata: IsLiteral, *args):
    return _query_call(codata, args, concat)


@dispatch
def concat(codata: IsConcretePandas, *args):
    return _query_call(codata, args, concat)


@dispatch
def concat(codata: IsSymbol, *args):
    return to_symbol(concat, args)


@dispatch
def concat(codata: DuckdbColumn, *args):
    return sql.func.concat(*args)


@dispatch
def today(*args, **kwargs):
    return dispatch_on_trait(today, args, kwargs)


@dispatch
def today(codata: IsLiteral):
    return _query_call(codata, tuple(), today)


@dispatch
def today(codata: IsSymbol, x: SymbolLike):
    # TODO: _ only used to invoke laziness
    to_symbol(today, tuple())


@dispatch
def today(codata: DuckdbColumn):
    # TODO: x is a no-op param (from the need to pass in _)
    return sql.func.today()


# struct_pack ----

@dispatch
def struct_pack(*args, **kwargs):
    # TODO: note this func requires named args
    if len(args):
        raise ValueError()

    return dispatch_on_trait(struct_pack, args, kwargs)


@dispatch
def struct_pack(codata: IsLiteral, **kwargs):
    return _query_call(codata, tuple(), struct_pack, kwargs)


@dispatch
def struct_pack(codata: DuckdbColumn, **kwargs):
    named_args = [assign_equals(sql.text(k), v) for k, v in kwargs.items()]

    return sql.func.struct_pack(*named_args)


from sqlalchemy.sql.expression import FunctionElement
from sqlalchemy.ext.compiler import compiles

class assign_equals(FunctionElement):
    name = 'assign_equals'
    inherit_cache = True


@compiles(assign_equals)
def _(element, compiler, **kw):
    lhs, rhs = element.clauses
    proc_lhs, proc_rhs = compiler.process(lhs, **kw), compiler.process(rhs, **kw)
    clauz = compiler.process(element.clauses, **kw)
    print(type(proc_lhs))
    return f"%s := %s" % (proc_lhs, proc_rhs)


# New Types ----

class NamedArg:
    def __init__(self, name, value):
        self.name = name
        self.value = value


# Traits ----

class IsConcrete(ABC): ...
class IsSymbol(ABC): ...
class IsLiteral(ABC): ...


class IsConcretePandas(IsConcrete): ...
class IsConcretePolars(IsConcrete): ...


class ConcreteLike(ABC): ...
class SymbolLike(ABC): ...
class LiteralLike(ABC): ...


ConcreteLike.register(pd.Series)
ConcreteLike.register(pl.Series)
SymbolLike.register(Symbolic)
SymbolLike.register(Call)
LiteralLike.register(int)
LiteralLike.register(float)
LiteralLike.register(bool)
LiteralLike.register(str)
LiteralLike.register(Interval)


def flatten_arg_kwargs(args, kwargs):
    return (*args, *kwargs.values())


def dispatch_on_trait(dispatcher, args, kwargs):
    flat_args = flatten_arg_kwargs(args, kwargs)
    trait = dispatch_style(flat_args)


    # TODO: check if signature is in registry, and fail if not. Otherwise,
    # we will likely infinitely recurse
    return dispatcher(trait, *args, **kwargs)


def dispatch_style(args):
    concretes, literals, symbols = set(), set(), set()

    for arg in args:
        if isinstance(arg, ConcreteLike):
            concretes.add(type(arg))
        elif isinstance(arg, LiteralLike):
            # TODO: Interval is a Call and a Literal
            literals.add(type(arg))
        elif isinstance(arg, SymbolLike):
            symbols.add(type(arg))

    # guards ----
    if len(concretes) > 1:
        _types = "\n  *".join(map(str, concretes))
        raise NotImplementedError(
            "Mixing concrete types not allowed."
            f" Detected these concretes:\n{_types}"
        )

    # trait for dispatch ----
    if not args:
        return IsLiteral()
    elif symbols and concretes:
        raise NotImplementedError()
    elif symbols:
        return IsSymbol()
    elif concretes:
        # TODO: use databackend
        if list(concretes)[0].__module__.startswith("pandas"):
            return IsConcretePandas()
        elif list(concretes)[0].__module__.startswith("polars"):
            return IsConcretePolars()
        else:
            return IsConcrete()
    elif literals:
        return IsLiteral()
  
    _types = "\n  * ".join([""] + [type(arg).__name__ for arg in args])
    raise TypeError(f"Cannot dispatch on this combination of types: \n{_types}")


def to_symbol(dispatcher, args):
    from siuba import _
    from siuba.siu import create_sym_call, FuncArg, strip_symbolic

    # TODO: need the dispatch for when it receives the column collection?
    converted = [
        convert(DuckdbColumn(), arg) if isinstance(arg, LiteralLike) else arg
        for arg in args
    ]
    return create_sym_call(FuncArg(dispatcher), *converted)

@dispatch
def convert(codata: DuckdbColumn, scalar: LiteralLike):
    return scalar


@dispatch
def convert(codata: DuckdbColumn, scalar: Interval):
    # TODO: refactor
    return scalar.convert(codata)

@dispatch
def convert(codata: DuckdbColumn, scalar: NamedArg):
    return sql.literal(f"{scalar.name}:={scalar.value}")


@_query_call.register(IsConcretePandas)
def _pd_query_call(codata, args, func):
    import duckdb
    from duckops._core import compile

    con = duckdb.connect()

    converted = []
    series_args = {}
    n_cols = 0

    for arg in args:
        if isinstance(arg, pd.Series):
            name = f"col_{n_cols}"
            series_args[name] = arg
            converted.append(sql.column(name))
            n_cols += 1
        else:
            converted.append(convert(DuckdbColumn(), arg))

    tmp_df = pd.DataFrame(series_args)

    sql_expr = func(DuckdbColumn(), *converted)
    col_query = compile(sql_expr)

    query = f"SELECT {col_query} AS __result__ FROM tmp_df"

    # execute query ----
    res_df = con.execute(query).df()

    res_col = res_df["__result__"]
    res_col.name = None

    return res_col


@_query_call.register(IsLiteral)
def _lit_query_call(codata, args, func, kwargs=None):
    import duckdb
    from duckops._core import compile

    con = duckdb.connect()

    converted_args = [convert(DuckdbColumn(), arg) for arg in args]
    if kwargs:
        converted_kwargs = {k: convert(DuckdbColumn(), v) for k, v in kwargs.items()}
    else:
        converted_kwargs = {}
    sql_expr = func(DuckdbColumn(), *converted_args, **converted_kwargs)

    compiled = compile(sql_expr)

    res = con.execute(f"SELECT {compiled} AS _tmp_res_")
    fetched = res.fetchall()
    assert len(fetched) == 1
    assert len(fetched[0]) == 1

    return fetched[0][0]


#def sigs_from_paramter_types()


#def return getattr(sql.func, func_name)(*args)