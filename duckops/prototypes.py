from abc import ABC
from typing import Any

from siuba.siu import Symbolic, Call
from duckops._types import Interval

import pandas as pd
import polars as pl

AInvalid = Any
ABool = Any
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


# Traits ----

class IsConcrete(ABC): ...
class IsSymbol(ABC): ...
class IsLiteral(ABC): ...


class IsConcretePandas(IsConcrete): ...
class IsConcretePolars(IsConcrete): ...


class ConcreteLike(ABC): ...
class SymbolLike(ABC): ...
class LiteralLike(ABC): ...


ConcreteLike.register(pd.Series)
ConcreteLike.register(pl.Series)
SymbolLike.register(Symbolic)
SymbolLike.register(Call)
LiteralLike.register(int)
LiteralLike.register(float)
LiteralLike.register(bool)
LiteralLike.register(str)
LiteralLike.register(Interval)

