from __future__ import annotations

from sqlalchemy import sql
from sqlalchemy.sql.expression import FunctionElement
from sqlalchemy.ext.compiler import compiles

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


# Sqlalchemy functions ----


class assign_equals(FunctionElement):
    name = "assign_equals"
    inherit_cache = True


class lambda_function(FunctionElement):
    name = "lambda_function"
    inherit_cache = True


class list_comprehension(FunctionElement):
    # should be 3 entries: body, iterable, ifs
    name = "list_comprehension"
    inherit_cache = True


class extract_infix(FunctionElement):
    name = "extract_infix"
    inherit_cache = True


@compiles(assign_equals)
def _(element, compiler, **kw):
    lhs, rhs = element.clauses
    proc_lhs, proc_rhs = compiler.process(lhs, **kw), compiler.process(rhs, **kw)
    return f"{proc_lhs} := {proc_rhs}"


@compiles(extract_infix)
def _(element, compiler, **kw):
    lhs, rhs = element.clauses
    proc_lhs, proc_rhs = compiler.process(lhs, **kw), compiler.process(rhs, **kw)
    return f"{proc_lhs}[{proc_rhs}]"


@compiles(lambda_function)
def _(element, compiler, **kw):
    # lhs should be called parameter, rhs body
    lhs, rhs = element.clauses
    proc_lhs, proc_rhs = compiler.process(lhs, **kw), compiler.process(rhs, **kw)
    return f"{proc_lhs} -> {proc_rhs}"


@compiles(list_comprehension)
def _(element, compiler, **kw):
    # lhs should be called parameter, rhs body
    procs = [compiler.process(el, **kw) for el in element.clauses]
    body, iterable, *ifs = procs

    str_ifs = "IF ".join([" "] + ifs)
    return f"[{body} for x in {iterable}{str_ifs}]"


def flatten_arg_kwargs(args, kwargs):
    return (*args, *kwargs.values())
