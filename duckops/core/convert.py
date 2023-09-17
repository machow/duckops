"""Conversion of objects to things sqlalchemy+duckdb can handle.

This includes converting objects like lists to duckdb list syntax.
"""

from functools import singledispatch
from duckops.core.data_style import (
    LiteralLike,
)
from duckops._types import Interval
from duckops.core.siuba import DuckdbColumn
from duckops.core.sql import assign_equals
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
def _(scalar: dict):
    named_args = [assign_equals(sql.text(k), v) for k, v in scalar.items()]
    return sql.func.struct_pack(*named_args)


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
