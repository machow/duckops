from abc import ABC
from typing import Any, Union
from functools import singledispatch

from siuba.siu import Symbolic, Call
from duckops._types import Interval
from duckops.core._type_backends import PdSeries, PlSeries

from datetime import datetime, timedelta


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


# Unions ----
# Date, Timestamp, Time, Timestamp with Timezone
# But also, what is Time?
DatetimeLike = Union[Interval]
StringLike = Union[str]
NumberLike = Union[int, float]


# Traits ----


class IsConcrete(ABC):
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


class ConcreteLike(ABC):
    ...


class SymbolLike(ABC):
    ...


class LiteralLike(ABC):
    ...


ConcreteLike.register(PdSeries)
ConcreteLike.register(PlSeries)
SymbolLike.register(Symbolic)
SymbolLike.register(Call)
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
def data_style(arg):
    raise NotImplementedError()


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
