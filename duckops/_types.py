# from ._core import sql_scalar, DuckdbColumn, symbolic_dispatch, support_no_args
from siuba.siu import symbolic_dispatch
from siuba.sql.dialects.duckdb import DuckdbColumn

from sqlalchemy import sql
from sqlalchemy import types as sa_types
from sqlalchemy.ext.compiler import compiles

from functools import singledispatch, singledispatchmethod
from itertools import chain


# Hack to make data visitable ----

from siuba.siu import Call


class Data:
    func = "__data__"

    def map_subcalls(self, f, args=tuple(), kwargs=None):
        return self.args, {}

    def __call__(self, x):
        return self


# Interval --------------------------------------------------------------------


@symbolic_dispatch(cls=DuckdbColumn)
def interval(
    codata: DuckdbColumn,
    value: "str | None" = None,
    years=0,
    months=0,
    days=0,
    hours=0,
    minutes=0,
    seconds=0,
    milliseconds=0,
    microseconds=0,
):
    if value is not None:
        return SAInterval(value)

    units = {
        "years",
        "months",
        "days",
        "hours",
        "minutes",
        "seconds",
        "milliseconds",
        "microseconds",
    }
    vals = " ".join(
        chain(*[(str(v), k) for k, v in locals().items() if k in units if v != 0])
    )

    return SAInterval(vals)


# New types ----


class Varchar:
    def __init__(self, s: str):
        self._d = s

    def __array__(self, dtype=None):
        import numpy as np

        return np.array([self._d], dtype=dtype)


# ----


class Interval(Data, Call):
    def __init__(self, func, n, unit=None):
        if unit is None:
            n, unit = func, n

        self.n = n
        self.unit = unit

        self.args = (n, unit)

    def __repr__(self):
        # TODO: remove once we no longer have Call as a parent
        return super(Data).__repr__()

    def __abs__(self):
        return self.__class__(abs(self.n), self.unit)

    def __str__(self):
        return f"{self.n} {self.unit}"

    @classmethod
    def from_int(cls, period: str, x: int):
        return cls(x, period)

    @singledispatchmethod
    def convert(self, codata):
        raise NotImplementedError(f"{type(codata)}")

    @convert.register(DuckdbColumn)
    def _(self, codata):
        return interval(codata, **{self.unit: self.n})


class SAInterval(sql.expression.ColumnClause):
    type = sa_types.Interval()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def from_int(cls, period: str, x: int):
        return cls(f"{x} {period}")


class SANamedArg(sql.expression.ClauseElement):
    is_clause_element = True

    def __init__(self, name, value):
        self.name = name
        self.value = value


@compiles(SAInterval)
def _(element, compiler, **kw):
    return f"INTERVAL '{element.name}'"


@compiles(SANamedArg)
def _(element, compiler, **kw):
    compiled_val = compiler.compile(element.value)
    return f"{element.name} := {compiled_val}"


@singledispatch
def _sql_from(type_, el):
    raise NotImplementedError(f"Unsupported type: {type(type_)}")


@symbolic_dispatch(cls=DuckdbColumn)
def cast(codata: DuckdbColumn, el, type_):
    if not isinstance(type_, object):
        return _sql_from(type_(), el)

    return _sql_from(type_, el)


# @_sql_from.register
# def _(type_: DateTime, el):
#    return sql.cast(el, sa_types.DateTime())
#
#
# @_sql_from.register
# def _(type_: Date, el):
#    return sql.cast(el, sa_types.Date())
#


@_sql_from.register
def _(type_: SAInterval, el):
    return sql.cast(el, sa_types.Interval())
