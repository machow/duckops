
from __future__ import annotations

from typing import overload
from duckops.core.dispatch import create_generic, register_agg
from duckops.core.data_style import *


__all__ = (
    "abs",
    "acos",
    "asin",
    "atan",
    "atan2",
    "bit_count",
    "cbrt",
    "ceil",
    "ceiling",
    "chr",
    "cos",
    "cot",
    "degrees",
    "even",
    "factorial",
    "floor",
    "gamma",
    "greatest",
    "isfinite",
    "isinf",
    "isnan",
    "least",
    "lgamma",
    "ln",
    "log",
    "log10",
    "log2",
    "nextafter",
    "pi",
    "pow",
    "power",
    "radians",
    "random",
    "round",
    "setseed",
    "sign",
    "signbit",
    "sin",
    "sqrt",
    "tan",
    "xor"
)


@create_generic
def abs(col0: NumberLike) -> NumberLike:
    """absolute value

    | duckdb example | result |
    | -------------- | ------ |
    | abs(-17.4) | 17.4 |


    """


@create_generic
def acos(col0: NumberLike) -> NumberLike:
    """computes the arccosine of x

    | duckdb example | result |
    | -------------- | ------ |
    | acos(0.5) | 1.0471975511965976 |


    """


@create_generic
def asin(col0: NumberLike) -> NumberLike:
    """computes the arcsine of x

    | duckdb example | result |
    | -------------- | ------ |
    | asin(0.5) | 0.5235987755982989 |


    """


@create_generic
def atan(col0: NumberLike) -> NumberLike:
    """computes the arctangent of x

    | duckdb example | result |
    | -------------- | ------ |
    | atan(0.5) | 0.4636476090008061 |


    """


@create_generic
def atan2(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """computes the arctangent (x, y)

    | duckdb example | result |
    | -------------- | ------ |
    | atan2(0.5, 0.5) | 0.7853981633974483 |


    """


@overload
def bit_count(col0: ABit) -> NumberLike: ...

@create_generic
def bit_count(col0: NumberLike) -> NumberLike:
    """returns the number of bits that are set

    | duckdb example | result |
    | -------------- | ------ |
    | bit_count(31) | 5 |


    """


@create_generic
def cbrt(col0: NumberLike) -> NumberLike:
    """returns the cube root of the number

    | duckdb example | result |
    | -------------- | ------ |
    | cbrt(8) | 2 |


    """


@create_generic
def ceil(col0: NumberLike) -> NumberLike:
    """rounds the number up

    | duckdb example | result |
    | -------------- | ------ |
    | ceil(17.4) | 18 |


    """


@create_generic
def ceiling(col0: NumberLike) -> NumberLike:
    """rounds the number up. Alias of ceil.

    | duckdb example | result |
    | -------------- | ------ |
    | ceiling(17.4) | 18 |


    """


@create_generic
def chr(col0: NumberLike) -> StringLike:
    """returns a character which is corresponding the ASCII code value or Unicode code point

    | duckdb example | result |
    | -------------- | ------ |
    | chr(65) | A |


    """


@create_generic
def cos(col0: NumberLike) -> NumberLike:
    """computes the cosine of x

    | duckdb example | result |
    | -------------- | ------ |
    | cos(90) | -0.4480736161291701 |


    """


@create_generic
def cot(col0: NumberLike) -> NumberLike:
    """computes the cotangent of x

    | duckdb example | result |
    | -------------- | ------ |
    | cot(0.5) | 1.830487721712452 |


    """


@create_generic
def degrees(col0: NumberLike) -> NumberLike:
    """converts radians to degrees

    | duckdb example | result |
    | -------------- | ------ |
    | degrees(pi()) | 180 |


    """


@create_generic
def even(col0: NumberLike) -> NumberLike:
    """round to next even number by rounding away from zero.

    | duckdb example | result |
    | -------------- | ------ |
    | even(2.9) | 4 |


    """


@create_generic
def factorial(col0: NumberLike) -> NumberLike:
    """See ! operator. Computes the product of the current integer and all integers below it

    | duckdb example | result |
    | -------------- | ------ |
    | factorial(4) | 24 |


    """


@create_generic
def floor(col0: NumberLike) -> NumberLike:
    """rounds the number down

    | duckdb example | result |
    | -------------- | ------ |
    | floor(17.4) | 17 |


    """


@create_generic
def gamma(col0: NumberLike) -> NumberLike:
    """interpolation of (x-1) factorial (so decimal inputs are allowed)

    | duckdb example | result |
    | -------------- | ------ |
    | gamma(5.5) | 52.34277778455352 |


    """


@overload
def greatest(col0: StringLike, *args: StringLike) -> StringLike: ...

@overload
def greatest(col0: DatetimeLike, *args: DatetimeLike) -> DatetimeLike: ...

@create_generic
def greatest(col0: NumberLike, *args: NumberLike) -> NumberLike:
    """selects the largest value

    | duckdb example | result |
    | -------------- | ------ |
    | greatest(3, 2, 4, 4) | 4 |


    """


@overload
def isfinite(col0: DatetimeLike) -> ABool: ...

@create_generic
def isfinite(col0: NumberLike) -> ABool:
    """Returns true if the floating point value is finite, false otherwise

    | duckdb example | result |
    | -------------- | ------ |
    | isfinite(5.5) | true |


    """


@overload
def isinf(col0: DatetimeLike) -> ABool: ...

@create_generic
def isinf(col0: NumberLike) -> ABool:
    """Returns true if the floating point value is infinite, false otherwise

    | duckdb example | result |
    | -------------- | ------ |
    | isinf('Infinity'::float) | true |


    """


@create_generic
def isnan(col0: NumberLike) -> ABool:
    """Returns true if the floating point value is not a number, false otherwise

    | duckdb example | result |
    | -------------- | ------ |
    | isnan('NaN'::float) | true |


    """


@overload
def least(col0: StringLike, *args: StringLike) -> StringLike: ...

@overload
def least(col0: DatetimeLike, *args: DatetimeLike) -> DatetimeLike: ...

@create_generic
def least(col0: NumberLike, *args: NumberLike) -> NumberLike:
    """selects the smallest value

    | duckdb example | result |
    | -------------- | ------ |
    | least(3, 2, 4, 4) | 2 |


    """


@create_generic
def lgamma(col0: NumberLike) -> NumberLike:
    """computes the log of the gamma function.

    | duckdb example | result |
    | -------------- | ------ |
    | lgamma(2) | 0 |


    """


@create_generic
def ln(col0: NumberLike) -> NumberLike:
    """computes the natural logarithm of x

    | duckdb example | result |
    | -------------- | ------ |
    | ln(2) | 0.693 |


    """


@create_generic
def log(col0: NumberLike) -> NumberLike:
    """computes the 10-log of x

    | duckdb example | result |
    | -------------- | ------ |
    | log(100) | 2 |


    """


@create_generic
def log10(col0: NumberLike) -> NumberLike:
    """alias of log. computes the 10-log of x

    | duckdb example | result |
    | -------------- | ------ |
    | log10(1000) | 3 |


    """


@create_generic
def log2(col0: NumberLike) -> NumberLike:
    """computes the 2-log of x

    | duckdb example | result |
    | -------------- | ------ |
    | log2(8) | 3 |


    """


@create_generic
def nextafter(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """return the next floating point value after x in the direction of y

    | duckdb example | result |
    | -------------- | ------ |
    | nextafter(1::float, 2::float) | 1.0000001 |


    """


@create_generic
def pi() -> NumberLike:
    """returns the value of pi

    | duckdb example | result |
    | -------------- | ------ |
    | pi() | 3.141592653589793 |


    """


@create_generic
def pow(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """computes x to the power of y

    | duckdb example | result |
    | -------------- | ------ |
    | pow(2, 3) | 8 |


    """


@create_generic
def power(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Alias of pow. computes x to the power of y

    | duckdb example | result |
    | -------------- | ------ |
    | power(2, 3) | 8 |


    """


@create_generic
def radians(col0: NumberLike) -> NumberLike:
    """converts degrees to radians

    | duckdb example | result |
    | -------------- | ------ |
    | radians(90) | 1.5707963267948966 |


    """


@create_generic
def random() -> NumberLike:
    """returns a random number between 0 and 1

    | duckdb example | result |
    | -------------- | ------ |
    | random() | various |


    """


@overload
def round(col0: NumberLike, col1: NumberLike) -> NumberLike: ...

@create_generic
def round(col0: NumberLike) -> NumberLike:
    """round to s decimal places

    | duckdb example | result |
    | -------------- | ------ |
    | round(42.4332, 2) | 42.43 |


    """


@create_generic
def setseed(col0: NumberLike) -> None:
    """sets the seed to be used for the random function

    | duckdb example | result |
    | -------------- | ------ |
    | setseed(0.42) | nan |


    """


@create_generic
def sign(col0: NumberLike) -> NumberLike:
    """returns the sign of x as -1, 0 or 1

    | duckdb example | result |
    | -------------- | ------ |
    | sign(-349) | -1 |


    """


@create_generic
def signbit(col0: NumberLike) -> ABool:
    """returns whether the signbit is set or not

    | duckdb example | result |
    | -------------- | ------ |
    | signbit(-0.0) | true |


    """


@create_generic
def sin(col0: NumberLike) -> NumberLike:
    """computes the sin of x

    | duckdb example | result |
    | -------------- | ------ |
    | sin(90) | 0.8939966636005579 |


    """


@create_generic
def sqrt(col0: NumberLike) -> NumberLike:
    """returns the square root of the number

    | duckdb example | result |
    | -------------- | ------ |
    | sqrt(9) | 3 |


    """


@create_generic
def tan(col0: NumberLike) -> NumberLike:
    """computes the tangent of x

    | duckdb example | result |
    | -------------- | ------ |
    | tan(90) | -1.995200412208242 |


    """


@overload
def xor(col0: ABit, col1: ABit) -> ABit: ...

@create_generic
def xor(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """bitwise XOR

    | duckdb example | result |
    | -------------- | ------ |
    | xor(17, 5) | 20 |


    """