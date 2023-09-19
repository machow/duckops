# from ._core import sql_scalar, DuckdbColumn, symbolic_dispatch, support_no_args
from siuba.siu import symbolic_dispatch
from siuba.sql.dialects.duckdb import DuckdbColumn

from sqlalchemy import sql
from sqlalchemy import types as sa_types
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.dialects.postgresql import array

from itertools import chain


# Hack to make data visitable ----

from siuba.siu import Call


class Data(Call):
    func = "__data__"

    def map_subcalls(self, f, args=tuple(), kwargs=None):
        return self.args, {}

    def __call__(self, x):
        return self.to_sqla()


# Interval --------------------------------------------------------------------


class SAInterval(sql.expression.ColumnClause):
    type = sa_types.Interval()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


@compiles(SAInterval)
def _(element, compiler, **kw):
    return f"INTERVAL '{element.name}'"


class Interval(Data):
    sa_type = sa_types.Interval

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

    def to_sqla(self):
        return interval(DuckdbColumn(), **{self.unit: self.n})


@symbolic_dispatch(cls=DuckdbColumn)
def interval(
    codata: DuckdbColumn,
    years: int = 0,
    months: int = 0,
    days: int = 0,
    hours: int = 0,
    minutes: int = 0,
    seconds: int = 0,
    milliseconds: int = 0,
    microseconds: int = 0,
):

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


# List ------------------------------------------------


class List(Data):
    sa_type = sa_types.ARRAY

    def __init__(self, func, *args):
        if isinstance(func, str) and func == "__data__":
            self.args = args

        else:
            self.args = (func, *args)

    def to_sqla(self):
        return array(self.args)
