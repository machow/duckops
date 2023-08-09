import sqlglot as sg

from ._core import sql_scalar, DuckdbColumn, symbolic_dispatch, support_no_args

from sqlalchemy import sql
from sqlalchemy import types as sa_types
from sqlalchemy.ext.compiler import compiles

from datetime import date, datetime, timedelta
from functools import singledispatch, singledispatchmethod
from itertools import chain

from . import _type_backends as be


# Hack to make data visitable ----

from siuba.siu import Call, Lazy

class Data:
    func = "__data__"
    
    def map_subcalls(self, f, args = tuple(), kwargs = None):
        return self.args, {}
    
    def __call__(self, x):
        return self

@singledispatch
def convert(src, dst):
    raise NotImplementedError(f"Unsupported type: {type(src)}")

# Interval --------------------------------------------------------------------

@symbolic_dispatch(cls=DuckdbColumn)
def interval(codata: DuckdbColumn, value: "str | None" = None, years=0, months=0, days=0, seconds=0, milliseconds=0, microseconds=0):
    if value is not None:
        return SAInterval(value)
    
    units = {"years", "months", "days", "seconds", "milliseconds", "microseconds"}
    vals = " ".join(chain(*[(str(v), k) for k, v in locals().items() if k in units if v != 0 ]))

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
    
    def __neg__(self):
        return self.__class__(-self.n, self.unit)
    
    def __add__(self, x):
        if isinstance(x, be.PdArray):
            return self.to_pandas() + x
        elif isinstance(x, be.PlObject):
            pl_by = self.to_polars()
            return x.dt.offset_by(pl_by)
        
        raise NotImplementedError()
    
    def __radd__(self, x):
        return self.__add__(x)

    def __sub__(self, x):
        raise NotImplementedError()

    def __rsub__(self, x):
        # TODO: note there this is currently no way to support this in polars
        # except by pretending to be a timedelta (which we do not do.)

        if isinstance(x, be.PdArray):
            return x - self.to_pandas()
        elif isinstance(x, be.PlObject):
            pl_by = (-self).to_polars()
            return x.dt.offset_by(pl_by)
        
        raise NotImplementedError()

    @classmethod
    def from_int(cls, period: str, x: int):
        return cls(x, period)
    
    def to_polars(self):
        unit_map = {
            "years": "y",
            "day": "d",
            "month": "m"
        }

        try:
            pl_unit = unit_map[self.unit]
        except KeyError:
            raise NotImplementedError(f"TODO: convert unit {self.unit} to polars.")

        return f"{self.n}{pl_unit}"
    
    def to_pandas(self):
        import pandas as pd

        # sqlglot errors for negative values of n, so we
        # convert the absolute, then add the sign back in.
        interval = sg.exp.to_interval(str(abs(self)))
        n, unit = int(interval.name), interval.text("unit")

        if self.n < 0:
            n = -n

        # TODO: make more robust
        return pd.DateOffset(**{unit: n})
    
    @singledispatchmethod
    def convert(self, codata):
        raise NotImplementedError(f"{type(codata)}")
    
    @convert.register(DuckdbColumn)
    def _(self, codata):
        print("CONVERTING")
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


#@_sql_from.register
#def _(type_: DateTime, el):
#    return sql.cast(el, sa_types.DateTime())
#
#
#@_sql_from.register
#def _(type_: Date, el):
#    return sql.cast(el, sa_types.Date())
#

@_sql_from.register
def _(type_: SAInterval, el):
    return sql.cast(el, sa_types.Interval())