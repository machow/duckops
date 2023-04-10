
from . import _core
from siuba.sql import translate as _tr
from siuba.sql.dialects.duckdb import DuckdbColumn, DuckdbColumnAgg

@_core.sql_agg("arg_max", _tr.AggOver)
def arg_max(codata: DuckdbColumnAgg, *args):
    """Finds the row with the maximum val. Calculates the arg expression at that row.
| duckdb example | result |
| -------------- | ------ |
| arg_max(A,B) | nan |
"""



@_core.sql_agg("arg_min", _tr.AggOver)
def arg_min(codata: DuckdbColumnAgg, *args):
    """Finds the row with the minimum val. Calculates the arg expression at that row.
| duckdb example | result |
| -------------- | ------ |
| arg_min(A,B) | nan |
"""



@_core.sql_agg("bool_and", _tr.AggOver)
def bool_and(codata: DuckdbColumnAgg, *args):
    """Returns TRUE if every input value is TRUE, otherwise FALSE.
| duckdb example | result |
| -------------- | ------ |
| bool_and(A) | nan |
"""



@_core.sql_agg("bool_or", _tr.AggOver)
def bool_or(codata: DuckdbColumnAgg, *args):
    """Returns TRUE if any input value is TRUE, otherwise FALSE.
| duckdb example | result |
| -------------- | ------ |
| bool_or(A) | nan |
"""



@_core.sql_agg("product", _tr.AggOver)
def product(codata: DuckdbColumnAgg, *args):
    """Calculates the product of all tuples in arg
| duckdb example | result |
| -------------- | ------ |
| product(A) | nan |
"""



@_core.sql_agg("approx_count_distinct", _tr.AggOver)
def approx_count_distinct(codata: DuckdbColumnAgg, *args):
    """Gives the approximate count of distintinct elements using HyperLogLog.
| duckdb example | result |
| -------------- | ------ |
| approx_count_distinct(A) | nan |
"""



@_core.sql_agg("string_agg", _tr.AggOver)
def string_agg(codata: DuckdbColumnAgg, *args):
    """Concatenates the column string values with a separator
| duckdb example | result |
| -------------- | ------ |
| string_agg(S, ',') | nan |
"""



@_core.sql_agg("fsum", _tr.AggOver)
def fsum(codata: DuckdbColumnAgg, *args):
    """Calculates the sum using a more accurate floating point summation (Kahan Sum).
| duckdb example | result |
| -------------- | ------ |
| fsum(A) | nan |
"""



@_core.sql_agg("sum", _tr.AggOver)
def sum(codata: DuckdbColumnAgg, *args):
    """Calculates the sum value for all tuples in arg.
| duckdb example | result |
| -------------- | ------ |
| sum(A) | nan |
"""



@_core.sql_agg("min", _tr.AggOver)
def min(codata: DuckdbColumnAgg, *args):
    """Returns the minumum value present in arg.
| duckdb example | result |
| -------------- | ------ |
| min(A) | nan |
"""



@_core.sql_agg("max", _tr.AggOver)
def max(codata: DuckdbColumnAgg, *args):
    """Returns the maximum value present in arg.
| duckdb example | result |
| -------------- | ------ |
| max(A) | nan |
"""



@_core.sql_agg("any_value", _tr.AggOver)
def any_value(codata: DuckdbColumnAgg, *args):
    """Returns the first non-null value from arg.
| duckdb example | result |
| -------------- | ------ |
| any_value(A) | nan |
"""



@_core.sql_agg("last", _tr.AggOver)
def last(codata: DuckdbColumnAgg, *args):
    """Returns the last value of a column.
| duckdb example | result |
| -------------- | ------ |
| last(A) | nan |
"""



@_core.sql_agg("first", _tr.AggOver)
def first(codata: DuckdbColumnAgg, *args):
    """Returns the first value of a column.
| duckdb example | result |
| -------------- | ------ |
| first(A) | nan |
"""



@_core.sql_agg("count", _tr.AggOver)
def count(codata: DuckdbColumnAgg, *args):
    """Calculates the number of tuples tuples in arg.
| duckdb example | result |
| -------------- | ------ |
| count(A) | nan |
"""



@_core.sql_agg("bit_xor", _tr.AggOver)
def bit_xor(codata: DuckdbColumnAgg, *args):
    """Returns the bitwise XOR of all bits in a given expression.
| duckdb example | result |
| -------------- | ------ |
| bit_xor(A) | nan |
"""



@_core.sql_agg("bit_or", _tr.AggOver)
def bit_or(codata: DuckdbColumnAgg, *args):
    """Returns the bitwise OR of all bits in a given expression.
| duckdb example | result |
| -------------- | ------ |
| bit_or(A) | nan |
"""



@_core.sql_agg("bit_and", _tr.AggOver)
def bit_and(codata: DuckdbColumnAgg, *args):
    """Returns the bitwise AND of all bits in a given expression .
| duckdb example | result |
| -------------- | ------ |
| bit_and(A) | nan |
"""



@_core.sql_agg("corr", _tr.AggOver)
def corr(codata: DuckdbColumnAgg, *args):
    """Returns the correlation coefficient for non-null pairs in a group.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("var_samp", _tr.AggOver)
def var_samp(codata: DuckdbColumnAgg, *args):
    """Returns the sample variance of all input values.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("var_pop", _tr.AggOver)
def var_pop(codata: DuckdbColumnAgg, *args):
    """Returns the population variance.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("stddev_pop", _tr.AggOver)
def stddev_pop(codata: DuckdbColumnAgg, *args):
    """Returns the population standard deviation.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("stddev_samp", _tr.AggOver)
def stddev_samp(codata: DuckdbColumnAgg, *args):
    """Returns the sample standard deviation.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("covar_pop", _tr.AggOver)
def covar_pop(codata: DuckdbColumnAgg, *args):
    """Returns the population covariance of input values.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("favg", _tr.AggOver)
def favg(codata: DuckdbColumnAgg, *args):
    """Calculates the average using a more accurate floating point summation (Kahan Sum).
| duckdb example | result |
| -------------- | ------ |
| favg(A) | nan |
"""



@_core.sql_agg("avg", _tr.AggOver)
def avg(codata: DuckdbColumnAgg, *args):
    """Calculates the average value for all tuples in arg.
| duckdb example | result |
| -------------- | ------ |
| avg(A) | nan |
"""



@_core.sql_agg("skewness", _tr.AggOver)
def skewness(codata: DuckdbColumnAgg, *args):
    """Returns the skewness of all input values.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("kurtosis", _tr.AggOver)
def kurtosis(codata: DuckdbColumnAgg, *args):
    """Returns the excess kurtosis of all input values.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("entropy", _tr.AggOver)
def entropy(codata: DuckdbColumnAgg, *args):
    """Returns the log-2 entropy of count input-values.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("list", _tr.AggOver)
def list(codata: DuckdbColumnAgg, *args):
    """Returns a LIST containing all the values of a column.
| duckdb example | result |
| -------------- | ------ |
| list(A) | nan |
"""



@_core.sql_agg("histogram", _tr.AggOver)
def histogram(codata: DuckdbColumnAgg, *args):
    """Returns a LIST of STRUCTs with the fields bucket and count.
| duckdb example | result |
| -------------- | ------ |
| histogram(A) | nan |
"""



@_core.sql_agg("median", _tr.AggOver)
def median(codata: DuckdbColumnAgg, *args):
    """Returns the middle value of the set. NULL values are ignored. For even value counts, quantitiative values are averaged and ordinal values return the lower value.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("quantile_disc", _tr.AggOver)
def quantile_disc(codata: DuckdbColumnAgg, *args):
    """Returns the exact quantile number between 0 and 1 . If pos is a LIST of FLOATs, then the result is a LIST of the corresponding exact quantiles.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("quantile_cont", _tr.AggOver)
def quantile_cont(codata: DuckdbColumnAgg, *args):
    """Returns the intepolated quantile number between 0 and 1 . If pos is a LIST of FLOATs, then the result is a LIST of the corresponding intepolated quantiles.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("mad", _tr.AggOver)
def mad(codata: DuckdbColumnAgg, *args):
    """Returns the median absolute deviation for the values within x. NULL values are ignored. Temporal types return a positive INTERVAL.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("mode", _tr.AggOver)
def mode(codata: DuckdbColumnAgg, *args):
    """Returns the most frequent value for the values within x. NULL values are ignored.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("approx_quantile", _tr.AggOver)
def approx_quantile(codata: DuckdbColumnAgg, *args):
    """Gives the approximate quantile using T-Digest.
| duckdb example | result |
| -------------- | ------ |
| approx_quantile(A,0.5) | nan |
"""



@_core.sql_agg("reservoir_quantile", _tr.AggOver)
def reservoir_quantile(codata: DuckdbColumnAgg, *args):
    """Gives the approximate quantile using reservoir sampling, the sample size is optional and uses 8192 as a default size.
| duckdb example | result |
| -------------- | ------ |
| reservoir_quantile(A,0.5,1024) | nan |
"""



@_core.sql_agg("regr_avgx", _tr.AggOver)
def regr_avgx(codata: DuckdbColumnAgg, *args):
    """Returns the average of the independent variable for non-null pairs in a group, where x is the independent variable and y is the dependent variable.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("regr_avgy", _tr.AggOver)
def regr_avgy(codata: DuckdbColumnAgg, *args):
    """Returns the average of the dependent variable for non-null pairs in a group, where x is the independent variable and y is the dependent variable.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("regr_count", _tr.AggOver)
def regr_count(codata: DuckdbColumnAgg, *args):
    """Returns the number of non-null number pairs in a group.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("regr_slope", _tr.AggOver)
def regr_slope(codata: DuckdbColumnAgg, *args):
    """Returns the slope of the linear regression line for non-null pairs in a group.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("regr_r2", _tr.AggOver)
def regr_r2(codata: DuckdbColumnAgg, *args):
    """Returns the coefficient of determination for non-null pairs in a group.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("regr_syy", _tr.AggOver)
def regr_syy(codata: DuckdbColumnAgg, *args):
    """-
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("regr_sxx", _tr.AggOver)
def regr_sxx(codata: DuckdbColumnAgg, *args):
    """-
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("regr_sxy", _tr.AggOver)
def regr_sxy(codata: DuckdbColumnAgg, *args):
    """Returns the population covariance of input values.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_agg("regr_intercept", _tr.AggOver)
def regr_intercept(codata: DuckdbColumnAgg, *args):
    """Returns the intercept of the univariate linear regression line for non-null pairs in a group.
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""
