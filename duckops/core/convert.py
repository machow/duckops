from functools import singledispatch
from duckops.prototypes import (
    LiteralLike,
)
from duckops._types import Interval
from siuba.sql.dialects.duckdb import DuckdbColumn
from sqlalchemy import sql


@singledispatch
def convert(scalar: LiteralLike):
    return scalar


@convert.register
def _(scalar: sql.elements.ClauseElement):
    return scalar


@convert.register
def _(scalar: list):
    args = [convert(x) for x in scalar]
    return sql.func.list_pack(*args)


@convert.register
def _(scalar: Interval):
    # TODO: convert used to pass codata as first argument
    return scalar.convert(DuckdbColumn())


# @convert.register
# def _(scalar: SbLazy):
#    from siuba.siu.visitors import CodataVisitor
#    from siuba.siu import strip_symbolic
#
#    visitor = CodataVisitor(dispatch_cls=DuckdbColumn, result_cls=object)
#
#    new_expr = visitor.enter(strip_symbolic(scalar))
#
#
