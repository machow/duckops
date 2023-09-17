
from __future__ import annotations

from typing import overload
from duckops.core.dispatch import create_generic, register_agg
from duckops.core.data_style import *


__all__ = (
    "any_value",
    "approx_count_distinct",
    "approx_quantile",
    "arg_max",
    "arg_min",
    "avg",
    "bit_and",
    "bit_or",
    "bit_xor",
    "bool_and",
    "bool_or",
    "corr",
    "count",
    "covar_pop",
    "entropy",
    "favg",
    "first",
    "fsum",
    "histogram",
    "kurtosis",
    "last",
    "list",
    "mad",
    "max",
    "median",
    "min",
    "mode",
    "product",
    "quantile_cont",
    "quantile_disc",
    "regr_avgx",
    "regr_avgy",
    "regr_count",
    "regr_intercept",
    "regr_r2",
    "regr_slope",
    "regr_sxx",
    "regr_sxy",
    "regr_syy",
    "reservoir_quantile",
    "skewness",
    "stddev_pop",
    "stddev_samp",
    "string_agg",
    "sum",
    "var_pop",
    "var_samp"
)


@overload
def any_value(col0: Any) -> Any: ...

@register_agg
@create_generic
def any_value(col0: NumberLike) -> NumberLike:
    """Returns the first non-null value from arg.

    | duckdb example | result |
    | -------------- | ------ |
    | any_value(A) | nan |


    """


@overload
def approx_count_distinct(col0: StringLike) -> NumberLike: ...

@overload
def approx_count_distinct(col0: DatetimeLike) -> NumberLike: ...

@register_agg
@create_generic
def approx_count_distinct(col0: NumberLike) -> NumberLike:
    """Gives the approximate count of distintinct elements using HyperLogLog.

    | duckdb example | result |
    | -------------- | ------ |
    | approx_count_distinct(A) | nan |


    """


@overload
def approx_quantile(col0: NumberLike, col1: list[NumberLike]) -> list[NumberLike]: ...

@register_agg
@create_generic
def approx_quantile(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Gives the approximate quantile using T-Digest.

    | duckdb example | result |
    | -------------- | ------ |
    | approx_quantile(A,0.5) | nan |


    """


@overload
def arg_max(col0: NumberLike, col1: StringLike) -> NumberLike: ...

@overload
def arg_max(col0: NumberLike, col1: DatetimeLike) -> NumberLike: ...

@overload
def arg_max(col0: NumberLike, col1: ABlob) -> NumberLike: ...

@overload
def arg_max(col0: StringLike, col1: NumberLike) -> StringLike: ...

@overload
def arg_max(col0: StringLike, col1: StringLike) -> StringLike: ...

@overload
def arg_max(col0: StringLike, col1: DatetimeLike) -> StringLike: ...

@overload
def arg_max(col0: StringLike, col1: ABlob) -> StringLike: ...

@overload
def arg_max(col0: DatetimeLike, col1: NumberLike) -> DatetimeLike: ...

@overload
def arg_max(col0: DatetimeLike, col1: StringLike) -> DatetimeLike: ...

@overload
def arg_max(col0: DatetimeLike, col1: DatetimeLike) -> DatetimeLike: ...

@overload
def arg_max(col0: DatetimeLike, col1: ABlob) -> DatetimeLike: ...

@overload
def arg_max(col0: ABlob, col1: NumberLike) -> ABlob: ...

@overload
def arg_max(col0: ABlob, col1: StringLike) -> ABlob: ...

@overload
def arg_max(col0: ABlob, col1: DatetimeLike) -> ABlob: ...

@overload
def arg_max(col0: ABlob, col1: ABlob) -> ABlob: ...

@overload
def arg_max(col0: Any, col1: NumberLike) -> Any: ...

@overload
def arg_max(col0: Any, col1: StringLike) -> Any: ...

@overload
def arg_max(col0: Any, col1: DatetimeLike) -> Any: ...

@overload
def arg_max(col0: Any, col1: ABlob) -> Any: ...

@register_agg
@create_generic
def arg_max(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Finds the row with the maximum val. Calculates the arg expression at that row.

    | duckdb example | result |
    | -------------- | ------ |
    | arg_max(A,B) | nan |


    """


@overload
def arg_min(col0: NumberLike, col1: StringLike) -> NumberLike: ...

@overload
def arg_min(col0: NumberLike, col1: DatetimeLike) -> NumberLike: ...

@overload
def arg_min(col0: NumberLike, col1: ABlob) -> NumberLike: ...

@overload
def arg_min(col0: StringLike, col1: NumberLike) -> StringLike: ...

@overload
def arg_min(col0: StringLike, col1: StringLike) -> StringLike: ...

@overload
def arg_min(col0: StringLike, col1: DatetimeLike) -> StringLike: ...

@overload
def arg_min(col0: StringLike, col1: ABlob) -> StringLike: ...

@overload
def arg_min(col0: DatetimeLike, col1: NumberLike) -> DatetimeLike: ...

@overload
def arg_min(col0: DatetimeLike, col1: StringLike) -> DatetimeLike: ...

@overload
def arg_min(col0: DatetimeLike, col1: DatetimeLike) -> DatetimeLike: ...

@overload
def arg_min(col0: DatetimeLike, col1: ABlob) -> DatetimeLike: ...

@overload
def arg_min(col0: ABlob, col1: NumberLike) -> ABlob: ...

@overload
def arg_min(col0: ABlob, col1: StringLike) -> ABlob: ...

@overload
def arg_min(col0: ABlob, col1: DatetimeLike) -> ABlob: ...

@overload
def arg_min(col0: ABlob, col1: ABlob) -> ABlob: ...

@overload
def arg_min(col0: Any, col1: NumberLike) -> Any: ...

@overload
def arg_min(col0: Any, col1: StringLike) -> Any: ...

@overload
def arg_min(col0: Any, col1: DatetimeLike) -> Any: ...

@overload
def arg_min(col0: Any, col1: ABlob) -> Any: ...

@register_agg
@create_generic
def arg_min(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Finds the row with the minimum val. Calculates the arg expression at that row.

    | duckdb example | result |
    | -------------- | ------ |
    | arg_min(A,B) | nan |


    """


@register_agg
@create_generic
def avg(col0: NumberLike) -> NumberLike:
    """Calculates the average value for all tuples in arg.

    | duckdb example | result |
    | -------------- | ------ |
    | avg(A) | nan |


    """


@register_agg
@create_generic
def bit_and(col0: NumberLike) -> NumberLike:
    """Returns the bitwise AND of all bits in a given expression .

    | duckdb example | result |
    | -------------- | ------ |
    | bit_and(A) | nan |


    """


@register_agg
@create_generic
def bit_or(col0: NumberLike) -> NumberLike:
    """Returns the bitwise OR of all bits in a given expression.

    | duckdb example | result |
    | -------------- | ------ |
    | bit_or(A) | nan |


    """


@register_agg
@create_generic
def bit_xor(col0: NumberLike) -> NumberLike:
    """Returns the bitwise XOR of all bits in a given expression.

    | duckdb example | result |
    | -------------- | ------ |
    | bit_xor(A) | nan |


    """


@register_agg
@create_generic
def bool_and(col0: ABool) -> ABool:
    """Returns TRUE if every input value is TRUE, otherwise FALSE.

    | duckdb example | result |
    | -------------- | ------ |
    | bool_and(A) | nan |


    """


@register_agg
@create_generic
def bool_or(col0: ABool) -> ABool:
    """Returns TRUE if any input value is TRUE, otherwise FALSE.

    | duckdb example | result |
    | -------------- | ------ |
    | bool_or(A) | nan |


    """


@register_agg
@create_generic
def corr(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Returns the correlation coefficient for non-null pairs in a group.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def count() -> NumberLike: ...

@register_agg
@create_generic
def count(col0: Any) -> NumberLike:
    """Calculates the number of tuples tuples in arg.

    | duckdb example | result |
    | -------------- | ------ |
    | count(A) | nan |


    """


@register_agg
@create_generic
def covar_pop(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Returns the population covariance of input values.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def entropy(col0: StringLike) -> NumberLike: ...

@overload
def entropy(col0: DatetimeLike) -> NumberLike: ...

@register_agg
@create_generic
def entropy(col0: NumberLike) -> NumberLike:
    """Returns the log-2 entropy of count input-values.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@register_agg
@create_generic
def favg(col0: NumberLike) -> NumberLike:
    """Calculates the average using a more accurate floating point summation (Kahan Sum).

    | duckdb example | result |
    | -------------- | ------ |
    | favg(A) | nan |


    """


@overload
def first(col0: Any) -> Any: ...

@register_agg
@create_generic
def first(col0: NumberLike) -> NumberLike:
    """Returns the first value of a column.

    | duckdb example | result |
    | -------------- | ------ |
    | first(A) | nan |


    """


@register_agg
@create_generic
def fsum(col0: NumberLike) -> NumberLike:
    """Calculates the sum using a more accurate floating point summation (Kahan Sum).

    | duckdb example | result |
    | -------------- | ------ |
    | fsum(A) | nan |


    """


@overload
def histogram(col0: NumberLike) -> AMap: ...

@overload
def histogram(col0: StringLike) -> AMap: ...

@overload
def histogram(col0: DatetimeLike) -> AMap: ...

@register_agg
@create_generic
def histogram(col0: ABool) -> AMap:
    """Returns a LIST of STRUCTs with the fields bucket and count.

    | duckdb example | result |
    | -------------- | ------ |
    | histogram(A) | nan |


    """


@register_agg
@create_generic
def kurtosis(col0: NumberLike) -> NumberLike:
    """Returns the excess kurtosis of all input values.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def last(col0: Any) -> Any: ...

@register_agg
@create_generic
def last(col0: NumberLike) -> NumberLike:
    """Returns the last value of a column.

    | duckdb example | result |
    | -------------- | ------ |
    | last(A) | nan |


    """


@register_agg
@create_generic
def list(col0: Any) -> AList:
    """Returns a LIST containing all the values of a column.

    | duckdb example | result |
    | -------------- | ------ |
    | list(A) | nan |


    """


@overload
def mad(col0: DatetimeLike) -> DatetimeLike: ...

@register_agg
@create_generic
def mad(col0: NumberLike) -> NumberLike:
    """Returns the median absolute deviation for the values within x. NULL values are ignored. Temporal types return a positive INTERVAL.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def max(col0: Any) -> Any: ...

@register_agg
@create_generic
def max(col0: NumberLike) -> NumberLike:
    """Returns the maximum value present in arg.

    | duckdb example | result |
    | -------------- | ------ |
    | max(A) | nan |


    """


@overload
def median(col0: DatetimeLike) -> DatetimeLike: ...

@overload
def median(col0: StringLike) -> StringLike: ...

@register_agg
@create_generic
def median(col0: NumberLike) -> NumberLike:
    """Returns the middle value of the set. NULL values are ignored. For even value counts, quantitiative values are averaged and ordinal values return the lower value.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def min(col0: Any) -> Any: ...

@register_agg
@create_generic
def min(col0: NumberLike) -> NumberLike:
    """Returns the minumum value present in arg.

    | duckdb example | result |
    | -------------- | ------ |
    | min(A) | nan |


    """


@overload
def mode(col0: DatetimeLike) -> DatetimeLike: ...

@overload
def mode(col0: StringLike) -> StringLike: ...

@register_agg
@create_generic
def mode(col0: NumberLike) -> NumberLike:
    """Returns the most frequent value for the values within x. NULL values are ignored.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@register_agg
@create_generic
def product(col0: NumberLike) -> NumberLike:
    """Calculates the product of all tuples in arg

    | duckdb example | result |
    | -------------- | ------ |
    | product(A) | nan |


    """


@overload
def quantile_cont(col0: NumberLike, col1: list[NumberLike]) -> list[NumberLike]: ...

@overload
def quantile_cont(col0: DatetimeLike, col1: NumberLike) -> DatetimeLike: ...

@overload
def quantile_cont(col0: DatetimeLike, col1: list[NumberLike]) -> list[DatetimeLike]: ...

@register_agg
@create_generic
def quantile_cont(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Returns the intepolated quantile number between 0 and 1 . If pos is a LIST of FLOATs, then the result is a LIST of the corresponding intepolated quantiles.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def quantile_disc(col0: NumberLike, col1: list[NumberLike]) -> list[NumberLike]: ...

@overload
def quantile_disc(col0: DatetimeLike, col1: NumberLike) -> DatetimeLike: ...

@overload
def quantile_disc(col0: DatetimeLike, col1: list[NumberLike]) -> list[DatetimeLike]: ...

@overload
def quantile_disc(col0: StringLike, col1: NumberLike) -> StringLike: ...

@overload
def quantile_disc(col0: StringLike, col1: list[NumberLike]) -> list[StringLike]: ...

@register_agg
@create_generic
def quantile_disc(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Returns the exact quantile number between 0 and 1 . If pos is a LIST of FLOATs, then the result is a LIST of the corresponding exact quantiles.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@register_agg
@create_generic
def regr_avgx(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Returns the average of the independent variable for non-null pairs in a group, where x is the independent variable and y is the dependent variable.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@register_agg
@create_generic
def regr_avgy(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Returns the average of the dependent variable for non-null pairs in a group, where x is the independent variable and y is the dependent variable.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@register_agg
@create_generic
def regr_count(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Returns the number of non-null number pairs in a group.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@register_agg
@create_generic
def regr_intercept(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Returns the intercept of the univariate linear regression line for non-null pairs in a group.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@register_agg
@create_generic
def regr_r2(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Returns the coefficient of determination for non-null pairs in a group.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@register_agg
@create_generic
def regr_slope(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Returns the slope of the linear regression line for non-null pairs in a group.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@register_agg
@create_generic
def regr_sxx(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """-

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@register_agg
@create_generic
def regr_sxy(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Returns the population covariance of input values.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@register_agg
@create_generic
def regr_syy(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """-

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def reservoir_quantile(col0: NumberLike, col1: NumberLike, col2: NumberLike) -> NumberLike: ...

@overload
def reservoir_quantile(col0: NumberLike, col1: list[NumberLike]) -> list[NumberLike]: ...

@overload
def reservoir_quantile(col0: NumberLike, col1: list[NumberLike], col2: NumberLike) -> list[NumberLike]: ...

@register_agg
@create_generic
def reservoir_quantile(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """Gives the approximate quantile using reservoir sampling, the sample size is optional and uses 8192 as a default size.

    | duckdb example | result |
    | -------------- | ------ |
    | reservoir_quantile(A,0.5,1024) | nan |


    """


@register_agg
@create_generic
def skewness(col0: NumberLike) -> NumberLike:
    """Returns the skewness of all input values.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@register_agg
@create_generic
def stddev_pop(col0: NumberLike) -> NumberLike:
    """Returns the population standard deviation.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@register_agg
@create_generic
def stddev_samp(col0: NumberLike) -> NumberLike:
    """Returns the sample standard deviation.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def string_agg(col0: StringLike, col1: StringLike) -> StringLike: ...

@register_agg
@create_generic
def string_agg(col0: StringLike) -> StringLike:
    """Concatenates the column string values with a separator

    | duckdb example | result |
    | -------------- | ------ |
    | string_agg(S, ',') | nan |


    """


@register_agg
@create_generic
def sum(col0: NumberLike) -> NumberLike:
    """Calculates the sum value for all tuples in arg.

    | duckdb example | result |
    | -------------- | ------ |
    | sum(A) | nan |


    """


@register_agg
@create_generic
def var_pop(col0: NumberLike) -> NumberLike:
    """Returns the population variance.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@register_agg
@create_generic
def var_samp(col0: NumberLike) -> NumberLike:
    """Returns the sample variance of all input values.

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """