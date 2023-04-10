
from . import _core
from siuba.sql import translate as _tr
from siuba.sql.dialects.duckdb import DuckdbColumn, DuckdbColumnAgg

@_core.sql_scalar("least")
def least(codata: DuckdbColumn, *args):
    """selects the smallest value
| duckdb example | result |
| -------------- | ------ |
| least(3, 2, 4, 4) | 2 |
"""



@_core.sql_scalar("greatest")
def greatest(codata: DuckdbColumn, *args):
    """selects the largest value
| duckdb example | result |
| -------------- | ------ |
| greatest(3, 2, 4, 4) | 4 |
"""



@_core.sql_scalar("atan2")
def atan2(codata: DuckdbColumn, *args):
    """computes the arctangent (x, y)
| duckdb example | result |
| -------------- | ------ |
| atan2(0.5, 0.5) | 0.7853981633974483 |
"""



@_core.sql_scalar("cot")
def cot(codata: DuckdbColumn, *args):
    """computes the cotangent of x
| duckdb example | result |
| -------------- | ------ |
| cot(0.5) | 1.830487721712452 |
"""



@_core.sql_scalar("atan")
def atan(codata: DuckdbColumn, *args):
    """computes the arctangent of x
| duckdb example | result |
| -------------- | ------ |
| atan(0.5) | 0.4636476090008061 |
"""



@_core.sql_scalar("acos")
def acos(codata: DuckdbColumn, *args):
    """computes the arccosine of x
| duckdb example | result |
| -------------- | ------ |
| acos(0.5) | 1.0471975511965976 |
"""



@_core.sql_scalar("asin")
def asin(codata: DuckdbColumn, *args):
    """computes the arcsine of x
| duckdb example | result |
| -------------- | ------ |
| asin(0.5) | 0.5235987755982989 |
"""



@_core.sql_scalar("tan")
def tan(codata: DuckdbColumn, *args):
    """computes the tangent of x
| duckdb example | result |
| -------------- | ------ |
| tan(90) | -1.995200412208242 |
"""



@_core.sql_scalar("cos")
def cos(codata: DuckdbColumn, *args):
    """computes the cosine of x
| duckdb example | result |
| -------------- | ------ |
| cos(90) | -0.4480736161291701 |
"""



@_core.sql_scalar("sin")
def sin(codata: DuckdbColumn, *args):
    """computes the sin of x
| duckdb example | result |
| -------------- | ------ |
| sin(90) | 0.8939966636005579 |
"""



@_core.sql_scalar("abs")
def abs(codata: DuckdbColumn, *args):
    """absolute value
| duckdb example | result |
| -------------- | ------ |
| abs(-17.4) | 17.4 |
"""



@_core.sql_scalar("chr")
def chr(codata: DuckdbColumn, *args):
    """returns a character which is corresponding the ASCII code value or Unicode code point
| duckdb example | result |
| -------------- | ------ |
| chr(65) | A |
"""



@_core.sql_scalar("xor")
def xor(codata: DuckdbColumn, *args):
    """bitwise XOR
| duckdb example | result |
| -------------- | ------ |
| xor(17, 5) | 20 |
"""



@_core.sql_scalar("isfinite")
def isfinite(codata: DuckdbColumn, *args):
    """Returns true if the floating point value is finite, false otherwise
| duckdb example | result |
| -------------- | ------ |
| isfinite(5.5) | true |
"""



@_core.sql_scalar("isinf")
def isinf(codata: DuckdbColumn, *args):
    """Returns true if the floating point value is infinite, false otherwise
| duckdb example | result |
| -------------- | ------ |
| isinf('Infinity'::float) | true |
"""



@_core.sql_scalar("signbit")
def signbit(codata: DuckdbColumn, *args):
    """returns whether the signbit is set or not
| duckdb example | result |
| -------------- | ------ |
| signbit(-0.0) | true |
"""



@_core.sql_scalar("isnan")
def isnan(codata: DuckdbColumn, *args):
    """Returns true if the floating point value is not a number, false otherwise
| duckdb example | result |
| -------------- | ------ |
| isnan('NaN'::float) | true |
"""



@_core.sql_scalar("even")
def even(codata: DuckdbColumn, *args):
    """round to next even number by rounding away from zero.
| duckdb example | result |
| -------------- | ------ |
| even(2.9) | 4 |
"""



@_core.sql_scalar("nextafter")
def nextafter(codata: DuckdbColumn, *args):
    """return the next floating point value after x in the direction of y
| duckdb example | result |
| -------------- | ------ |
| nextafter(1::float, 2::float) | 1.0000001 |
"""



@_core.sql_scalar("factorial")
def factorial(codata: DuckdbColumn, *args):
    """See ! operator. Computes the product of the current integer and all integers below it
| duckdb example | result |
| -------------- | ------ |
| factorial(4) | 24 |
"""



@_core.sql_scalar("lgamma")
def lgamma(codata: DuckdbColumn, *args):
    """computes the log of the gamma function.
| duckdb example | result |
| -------------- | ------ |
| lgamma(2) | 0 |
"""



@_core.sql_scalar("gamma")
def gamma(codata: DuckdbColumn, *args):
    """interpolation of (x-1) factorial (so decimal inputs are allowed)
| duckdb example | result |
| -------------- | ------ |
| gamma(5.5) | 52.34277778455352 |
"""



@_core.sql_scalar("bit_count")
def bit_count(codata: DuckdbColumn, *args):
    """returns the number of bits that are set
| duckdb example | result |
| -------------- | ------ |
| bit_count(31) | 5 |
"""



@_core.sql_scalar("pi")
def pi(codata: DuckdbColumn, *args):
    """returns the value of pi
| duckdb example | result |
| -------------- | ------ |
| pi() | 3.141592653589793 |
"""



@_core.sql_scalar("sqrt")
def sqrt(codata: DuckdbColumn, *args):
    """returns the square root of the number
| duckdb example | result |
| -------------- | ------ |
| sqrt(9) | 3 |
"""



@_core.sql_scalar("setseed")
def setseed(codata: DuckdbColumn, *args):
    """sets the seed to be used for the random function
| duckdb example | result |
| -------------- | ------ |
| setseed(0.42) | nan |
"""



@_core.sql_scalar("random")
def random(codata: DuckdbColumn, *args):
    """returns a random number between 0 and 1
| duckdb example | result |
| -------------- | ------ |
| random() | various |
"""



@_core.sql_scalar("power")
def power(codata: DuckdbColumn, *args):
    """Alias of pow. computes x to the power of y
| duckdb example | result |
| -------------- | ------ |
| power(2, 3) | 8 |
"""



@_core.sql_scalar("pow")
def pow(codata: DuckdbColumn, *args):
    """computes x to the power of y
| duckdb example | result |
| -------------- | ------ |
| pow(2, 3) | 8 |
"""



@_core.sql_scalar("ln")
def ln(codata: DuckdbColumn, *args):
    """computes the natural logarithm of x
| duckdb example | result |
| -------------- | ------ |
| ln(2) | 0.693 |
"""



@_core.sql_scalar("log")
def log(codata: DuckdbColumn, *args):
    """computes the 10-log of x
| duckdb example | result |
| -------------- | ------ |
| log(100) | 2 |
"""



@_core.sql_scalar("log10")
def log10(codata: DuckdbColumn, *args):
    """alias of log. computes the 10-log of x
| duckdb example | result |
| -------------- | ------ |
| log10(1000) | 3 |
"""



@_core.sql_scalar("log2")
def log2(codata: DuckdbColumn, *args):
    """computes the 2-log of x
| duckdb example | result |
| -------------- | ------ |
| log2(8) | 3 |
"""



@_core.sql_scalar("cbrt")
def cbrt(codata: DuckdbColumn, *args):
    """returns the cube root of the number
| duckdb example | result |
| -------------- | ------ |
| cbrt(8) | 2 |
"""



@_core.sql_scalar("radians")
def radians(codata: DuckdbColumn, *args):
    """converts degrees to radians
| duckdb example | result |
| -------------- | ------ |
| radians(90) | 1.5707963267948966 |
"""



@_core.sql_scalar("degrees")
def degrees(codata: DuckdbColumn, *args):
    """converts radians to degrees
| duckdb example | result |
| -------------- | ------ |
| degrees(pi()) | 180 |
"""



@_core.sql_scalar("round")
def round(codata: DuckdbColumn, *args):
    """round to s decimal places
| duckdb example | result |
| -------------- | ------ |
| round(42.4332, 2) | 42.43 |
"""



@_core.sql_scalar("floor")
def floor(codata: DuckdbColumn, *args):
    """rounds the number down
| duckdb example | result |
| -------------- | ------ |
| floor(17.4) | 17 |
"""



@_core.sql_scalar("ceiling")
def ceiling(codata: DuckdbColumn, *args):
    """rounds the number up. Alias of ceil.
| duckdb example | result |
| -------------- | ------ |
| ceiling(17.4) | 18 |
"""



@_core.sql_scalar("ceil")
def ceil(codata: DuckdbColumn, *args):
    """rounds the number up
| duckdb example | result |
| -------------- | ------ |
| ceil(17.4) | 18 |
"""



@_core.sql_scalar("sign")
def sign(codata: DuckdbColumn, *args):
    """returns the sign of x as -1, 0 or 1
| duckdb example | result |
| -------------- | ------ |
| sign(-349) | -1 |
"""
