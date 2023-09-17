from __future__ import annotations

from sqlalchemy import sql

from siuba.sql.dialects.duckdb import DuckdbColumn, DuckdbColumnAgg
from siuba.sql.translate import AggOver, CustomOverClause, CumlOver
from siuba.siu import FormulaArg, strip_symbolic
from siuba.siu.visitors import CallListener


def sql_win(dispatcher, win_type: CustomOverClause | None = None):
    if win_type is None:
        return lambda f: sql_win(f, dispatcher)

    @dispatcher.register(DuckdbColumn)
    def _duckdb_translate(codata, *args, **kwargs):
        return win_type.func(dispatcher.__name__)(codata, *args, **kwargs)

    return dispatcher


def register_agg(f):
    f.register(DuckdbColumn, AggOver.func(f.__name__))

    @f.register
    def _duckdb_translate_agg(codata: DuckdbColumnAgg, *args):
        return getattr(sql.func, f.__name__)(*args)

    return f


class ReplaceFx(CallListener):
    def __init__(self, replacement):
        self.replacement = replacement

    def visit(self, node):
        return super().visit(strip_symbolic(node))

    def exit(self, node):
        res = super().exit(node)
        if isinstance(res, FormulaArg):
            return self.replacement

        return res


class NoArgOver(CumlOver):
    @classmethod
    def func(cls, name: str):
        sa_func = getattr(sql.func, name)

        def f(codata, col, *args, **kwargs):
            # if not isinstance(col, sql.ColumnCollection):
            #    raise TypeError("Must be called with a plain siuba _")

            # if args or kwargs:
            #    raise ValueError("This function does not take additional arguments.")

            return cls(sa_func())

        return f


def to_symbol(dispatcher, args):
    from siuba.siu import create_sym_call, FuncArg
    from duckops.core.convert import convert
    from duckops.core.data_style import LiteralLike

    # TODO: need the dispatch for when it receives the column collection?
    converted = [convert(arg) if isinstance(arg, LiteralLike) else arg for arg in args]
    return create_sym_call(FuncArg(dispatcher), *converted)
