"""Conversion of objects to things sqlalchemy+duckdb can handle.

This includes converting objects like lists to duckdb list syntax.
"""

from functools import singledispatch
from duckops.core.data_style import (
    LiteralLike,
)
from duckops._types import Data
from duckops.core.sql import assign_equals
from duckops._types import List
from sqlalchemy import sql


@singledispatch
def convert(scalar: LiteralLike) -> sql.ClauseElement:
    return scalar


@convert.register
def _(scalar: sql.elements.ClauseElement) -> sql.ClauseElement:
    return scalar


@convert.register
def _(scalar: list) -> sql.ClauseElement:
    args = [convert(x) for x in scalar]
    return sql.func.list_pack(*args)


@convert.register
def _(scalar: dict) -> sql.ClauseElement:
    named_args = [assign_equals(sql.text(k), v) for k, v in scalar.items()]
    return sql.func.struct_pack(*named_args)


@convert.register
def _(scalar: Data) -> sql.ClauseElement:
    # TODO: convert used to pass codata as first argument
    return scalar.to_sqla()


@singledispatch
def convert_result(scalar):
    return scalar


@convert_result.register
def _(scalar: list):
    return List(*scalar)


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
