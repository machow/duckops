from . import dt
from . import str as str_
from ._core import NoArgs, _query_call, DuckdbColumn, DuckdbColumnAgg
from ._types import Interval
from . import _type_backends as be
from functools import partial

from sqlalchemy import sql
from sqlalchemy import types as sqla_types

from datetime import datetime, date


# Interval constructors ---------

dt.to_years.register(int, partial(Interval.from_int, "years"))
dt.to_months.register(int, partial(Interval.from_int, "months"))
dt.to_days.register(int, partial(Interval.from_int, "days"))
dt.to_hours.register(int, partial(Interval.from_int, "hours"))
dt.to_minutes.register(int, partial(Interval.from_int, "minutes"))
dt.to_seconds.register(int, partial(Interval.from_int, "seconds"))
dt.to_milliseconds.register(int, partial(Interval.from_int, "milliseconds"))
dt.to_microseconds.register(int, partial(Interval.from_int, "microseconds"))

def _flip1(f):
    # TODO: handle kwargs
    def wrapper(arg0, arg1, *args):
        f_dispatch = f.dispatch(type(arg1))
        return f_dispatch(arg0, arg1, *args)

    return wrapper


# date_part ----------

dt.date_part.register(str, _flip1(dt.date_part))

@dt.date_part.register(Interval)
def _(part: str, data: Interval):
    sql_interval = data.convert(DuckdbColumn())
    return _query_call(sql.func.date_part(part, sql_interval))


@dt.date_part.register(be.PdSeries)
def _(part: str, data: be.PdSeries):
    return _query_call(data, lambda co, col: dt.date_part(co, part, col))


# concat(*args) -------

@str_.concat.register(be.PdSeries)
def _(string, *args):
    import pandas as pd

    # TODO: catch inproper mixed types
    other = {f"col_{ii + 1}": v for ii, v in enumerate(args)}
    df = pd.DataFrame({"col_0": string, **other})
    return _query_call(df, str_.concat)


@str_.concat.register(be.PdFrame)
def _(string):
    # TODO: catch inproper mixed types
    return _query_call(string, str_.concat)


@str_.concat.register(str)
def _(string, *args):
    return _query_call(str_.concat(DuckdbColumn(), string, *args))


# Overloads allowing functions to be called with no arguments -----------------

@dt.now.register(NoArgs)
def _(data: NoArgs) -> datetime:
    return _query_call(sql.func.now())


@dt.now.register
def _(codata: DuckdbColumn, data: sql.ColumnCollection):
    return sql.func.now()


@dt.today.register(NoArgs)
def _(data: NoArgs) -> date:
    return _query_call(sql.func.today())


@dt.today.register
def _(codata: DuckdbColumn, data: sql.ColumnCollection):
    return sql.func.today()