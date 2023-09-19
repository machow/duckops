from abc import ABC
from typing import Any, Union
from functools import singledispatch

from siuba.siu import Symbolic, Call
from duckops._types import Interval
from duckops.core._databackends import PdSeries, PlSeries, SqlaClauseElement, SbLazy

from datetime import datetime, timedelta, date

# Types ----
# Note that these should be used only for type annotations
# TODO: only make available when TYPE_CHECKING?

AInvalid = Any
ABool = Any
ABlob = Any
StructLike = Any
ABit = Any
ABlock = Any
AJson = Any
AUnion = Any
AMap = Any
AList = Any
UnionLike = Any
LambdaLike = Any
UuidLike = Any

ColumnLike = Union[PdSeries, PlSeries, SbLazy]

# Unions ----
# Date, Timestamp, Time, Timestamp with Timezone (what is a duckdb Time type?)
# Note that ColumnLike is added to these, because we can't know the internal type
# of many column types, but also don't want the type checker to yell at us.
# Using a ColumnLike is accepting that the database will decide.
DatetimeLike = Union[Interval, datetime, timedelta, date, ColumnLike]
StringLike = Union[str, ColumnLike]
NumberLike = Union[int, float, ColumnLike]


# Traits ----


class IsConcrete(ABC):
    ...


class IsUnknown(ABC):
    ...


class IsSymbol(ABC):
    ...


class IsLiteral(ABC):
    ...


class IsConcretePandas(IsConcrete):
    ...


class IsConcretePolars(IsConcrete):
    ...


class IsSymbolSiuba(IsSymbol):
    ...


class LiteralLike(ABC):
    ...


LiteralLike.register(SqlaClauseElement)
LiteralLike.register(int)
LiteralLike.register(float)
LiteralLike.register(bool)
LiteralLike.register(str)
LiteralLike.register(Interval)
LiteralLike.register(list)
LiteralLike.register(type(None))
LiteralLike.register(datetime)
LiteralLike.register(timedelta)


@singledispatch
def data_style(arg) -> Any:
    return IsUnknown()


@data_style.register
def _(arg: LiteralLike):
    return IsLiteral()


@data_style.register
def _(arg: PdSeries):
    return IsConcretePandas()


@data_style.register
def _(arg: PlSeries):
    return IsConcretePolars()


@data_style.register(Symbolic)
@data_style.register(Call)
def _(arg):
    return IsSymbolSiuba()
