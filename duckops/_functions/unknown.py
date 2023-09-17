
from __future__ import annotations

from typing import overload
from duckops.core.dispatch import create_generic, register_agg
from duckops.core.data_style import *


__all__ = (
    "add",
    "arbitrary",
    "argmax",
    "argmin",
    "array_agg",
    "bit_position",
    "combine",
    "constant_or_null",
    "count_star",
    "covar_samp",
    "current_database",
    "current_localtime",
    "current_query",
    "divide",
    "enum_code",
    "enum_first",
    "enum_last",
    "enum_range",
    "enum_range_boundary",
    "excel_text",
    "exp",
    "finalize",
    "flatten",
    "get_bit",
    "group_concat",
    "ilike_escape",
    "json_extract_path",
    "json_extract_path_text",
    "kahan_sum",
    "max_by",
    "md5_number",
    "md5_number_lower",
    "md5_number_upper",
    "mean",
    "min_by",
    "mod",
    "multiply",
    "not_ilike_escape",
    "quantile",
    "sem",
    "set_bit",
    "split",
    "stddev",
    "stem",
    "subtract",
    "sumKahan",
    "sum_no_overflow",
    "text",
    "translate",
    "variance"
)


@overload
def add(col0: NumberLike, col1: NumberLike) -> NumberLike: ...

@overload
def add(col0: DatetimeLike, col1: NumberLike) -> DatetimeLike: ...

@overload
def add(col0: NumberLike, col1: DatetimeLike) -> DatetimeLike: ...

@overload
def add(col0: DatetimeLike, col1: DatetimeLike) -> DatetimeLike: ...

@overload
def add(col0: list[Any], col1: list[Any]) -> list[Any]: ...

@create_generic
def add(col0: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def arbitrary(col0: Any) -> Any: ...

@create_generic
def arbitrary(col0: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def argmax(col0: NumberLike, col1: StringLike) -> NumberLike: ...

@overload
def argmax(col0: NumberLike, col1: DatetimeLike) -> NumberLike: ...

@overload
def argmax(col0: NumberLike, col1: ABlob) -> NumberLike: ...

@overload
def argmax(col0: StringLike, col1: NumberLike) -> StringLike: ...

@overload
def argmax(col0: StringLike, col1: StringLike) -> StringLike: ...

@overload
def argmax(col0: StringLike, col1: DatetimeLike) -> StringLike: ...

@overload
def argmax(col0: StringLike, col1: ABlob) -> StringLike: ...

@overload
def argmax(col0: DatetimeLike, col1: NumberLike) -> DatetimeLike: ...

@overload
def argmax(col0: DatetimeLike, col1: StringLike) -> DatetimeLike: ...

@overload
def argmax(col0: DatetimeLike, col1: DatetimeLike) -> DatetimeLike: ...

@overload
def argmax(col0: DatetimeLike, col1: ABlob) -> DatetimeLike: ...

@overload
def argmax(col0: ABlob, col1: NumberLike) -> ABlob: ...

@overload
def argmax(col0: ABlob, col1: StringLike) -> ABlob: ...

@overload
def argmax(col0: ABlob, col1: DatetimeLike) -> ABlob: ...

@overload
def argmax(col0: ABlob, col1: ABlob) -> ABlob: ...

@overload
def argmax(col0: Any, col1: NumberLike) -> Any: ...

@overload
def argmax(col0: Any, col1: StringLike) -> Any: ...

@overload
def argmax(col0: Any, col1: DatetimeLike) -> Any: ...

@overload
def argmax(col0: Any, col1: ABlob) -> Any: ...

@create_generic
def argmax(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def argmin(col0: NumberLike, col1: StringLike) -> NumberLike: ...

@overload
def argmin(col0: NumberLike, col1: DatetimeLike) -> NumberLike: ...

@overload
def argmin(col0: NumberLike, col1: ABlob) -> NumberLike: ...

@overload
def argmin(col0: StringLike, col1: NumberLike) -> StringLike: ...

@overload
def argmin(col0: StringLike, col1: StringLike) -> StringLike: ...

@overload
def argmin(col0: StringLike, col1: DatetimeLike) -> StringLike: ...

@overload
def argmin(col0: StringLike, col1: ABlob) -> StringLike: ...

@overload
def argmin(col0: DatetimeLike, col1: NumberLike) -> DatetimeLike: ...

@overload
def argmin(col0: DatetimeLike, col1: StringLike) -> DatetimeLike: ...

@overload
def argmin(col0: DatetimeLike, col1: DatetimeLike) -> DatetimeLike: ...

@overload
def argmin(col0: DatetimeLike, col1: ABlob) -> DatetimeLike: ...

@overload
def argmin(col0: ABlob, col1: NumberLike) -> ABlob: ...

@overload
def argmin(col0: ABlob, col1: StringLike) -> ABlob: ...

@overload
def argmin(col0: ABlob, col1: DatetimeLike) -> ABlob: ...

@overload
def argmin(col0: ABlob, col1: ABlob) -> ABlob: ...

@overload
def argmin(col0: Any, col1: NumberLike) -> Any: ...

@overload
def argmin(col0: Any, col1: StringLike) -> Any: ...

@overload
def argmin(col0: Any, col1: DatetimeLike) -> Any: ...

@overload
def argmin(col0: Any, col1: ABlob) -> Any: ...

@create_generic
def argmin(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def array_agg(col0: Any) -> AList:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def bit_position(col0: ABit, col1: ABit) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def combine(col0: AggregateLike, col1: Any) -> AggregateLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def constant_or_null(col0: Any, col1: Any, *args: Any) -> Any:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def count_star() -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def covar_samp(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def current_database() -> StringLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def current_localtime() -> DatetimeLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def current_query() -> StringLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def divide(col0: DatetimeLike, col1: NumberLike) -> DatetimeLike: ...

@create_generic
def divide(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def enum_code(col0: Any) -> Any:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def enum_first(col0: Any) -> StringLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def enum_last(col0: Any) -> StringLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def enum_range(col0: Any) -> list[StringLike]:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def enum_range_boundary(col0: Any, col1: Any) -> list[StringLike]:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def excel_text(col0: NumberLike, col1: StringLike) -> StringLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def exp(col0: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def finalize(col0: AggregateLike) -> AInvalid:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def flatten(col0: Any) -> list[Any]:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def get_bit(col0: ABit, col1: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def group_concat(col0: StringLike, col1: StringLike) -> StringLike: ...

@create_generic
def group_concat(col0: StringLike) -> StringLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def ilike_escape(col0: StringLike, col1: StringLike, col2: StringLike) -> ABool:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def json_extract_path(col0: StringLike, col1: list[StringLike]) -> list[AJson]: ...

@overload
def json_extract_path(col0: AJson, col1: StringLike) -> AJson: ...

@overload
def json_extract_path(col0: AJson, col1: list[StringLike]) -> list[AJson]: ...

@create_generic
def json_extract_path(col0: StringLike, col1: StringLike) -> AJson:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def json_extract_path_text(col0: StringLike, col1: list[StringLike]) -> list[StringLike]: ...

@overload
def json_extract_path_text(col0: AJson, col1: StringLike) -> StringLike: ...

@overload
def json_extract_path_text(col0: AJson, col1: list[StringLike]) -> list[StringLike]: ...

@create_generic
def json_extract_path_text(col0: StringLike, col1: StringLike) -> StringLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def kahan_sum(col0: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def max_by(col0: NumberLike, col1: StringLike) -> NumberLike: ...

@overload
def max_by(col0: NumberLike, col1: DatetimeLike) -> NumberLike: ...

@overload
def max_by(col0: NumberLike, col1: ABlob) -> NumberLike: ...

@overload
def max_by(col0: StringLike, col1: NumberLike) -> StringLike: ...

@overload
def max_by(col0: StringLike, col1: StringLike) -> StringLike: ...

@overload
def max_by(col0: StringLike, col1: DatetimeLike) -> StringLike: ...

@overload
def max_by(col0: StringLike, col1: ABlob) -> StringLike: ...

@overload
def max_by(col0: DatetimeLike, col1: NumberLike) -> DatetimeLike: ...

@overload
def max_by(col0: DatetimeLike, col1: StringLike) -> DatetimeLike: ...

@overload
def max_by(col0: DatetimeLike, col1: DatetimeLike) -> DatetimeLike: ...

@overload
def max_by(col0: DatetimeLike, col1: ABlob) -> DatetimeLike: ...

@overload
def max_by(col0: ABlob, col1: NumberLike) -> ABlob: ...

@overload
def max_by(col0: ABlob, col1: StringLike) -> ABlob: ...

@overload
def max_by(col0: ABlob, col1: DatetimeLike) -> ABlob: ...

@overload
def max_by(col0: ABlob, col1: ABlob) -> ABlob: ...

@overload
def max_by(col0: Any, col1: NumberLike) -> Any: ...

@overload
def max_by(col0: Any, col1: StringLike) -> Any: ...

@overload
def max_by(col0: Any, col1: DatetimeLike) -> Any: ...

@overload
def max_by(col0: Any, col1: ABlob) -> Any: ...

@create_generic
def max_by(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def md5_number(col0: StringLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def md5_number_lower(col0: StringLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def md5_number_upper(col0: StringLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def mean(col0: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def min_by(col0: NumberLike, col1: StringLike) -> NumberLike: ...

@overload
def min_by(col0: NumberLike, col1: DatetimeLike) -> NumberLike: ...

@overload
def min_by(col0: NumberLike, col1: ABlob) -> NumberLike: ...

@overload
def min_by(col0: StringLike, col1: NumberLike) -> StringLike: ...

@overload
def min_by(col0: StringLike, col1: StringLike) -> StringLike: ...

@overload
def min_by(col0: StringLike, col1: DatetimeLike) -> StringLike: ...

@overload
def min_by(col0: StringLike, col1: ABlob) -> StringLike: ...

@overload
def min_by(col0: DatetimeLike, col1: NumberLike) -> DatetimeLike: ...

@overload
def min_by(col0: DatetimeLike, col1: StringLike) -> DatetimeLike: ...

@overload
def min_by(col0: DatetimeLike, col1: DatetimeLike) -> DatetimeLike: ...

@overload
def min_by(col0: DatetimeLike, col1: ABlob) -> DatetimeLike: ...

@overload
def min_by(col0: ABlob, col1: NumberLike) -> ABlob: ...

@overload
def min_by(col0: ABlob, col1: StringLike) -> ABlob: ...

@overload
def min_by(col0: ABlob, col1: DatetimeLike) -> ABlob: ...

@overload
def min_by(col0: ABlob, col1: ABlob) -> ABlob: ...

@overload
def min_by(col0: Any, col1: NumberLike) -> Any: ...

@overload
def min_by(col0: Any, col1: StringLike) -> Any: ...

@overload
def min_by(col0: Any, col1: DatetimeLike) -> Any: ...

@overload
def min_by(col0: Any, col1: ABlob) -> Any: ...

@create_generic
def min_by(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def mod(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def multiply(col0: DatetimeLike, col1: NumberLike) -> DatetimeLike: ...

@overload
def multiply(col0: NumberLike, col1: DatetimeLike) -> DatetimeLike: ...

@create_generic
def multiply(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def not_ilike_escape(col0: StringLike, col1: StringLike, col2: StringLike) -> ABool:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def quantile(col0: NumberLike, col1: list[NumberLike]) -> list[NumberLike]: ...

@overload
def quantile(col0: DatetimeLike, col1: NumberLike) -> DatetimeLike: ...

@overload
def quantile(col0: DatetimeLike, col1: list[NumberLike]) -> list[DatetimeLike]: ...

@overload
def quantile(col0: StringLike, col1: NumberLike) -> StringLike: ...

@overload
def quantile(col0: StringLike, col1: list[NumberLike]) -> list[StringLike]: ...

@create_generic
def quantile(col0: NumberLike, col1: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def sem(col0: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def set_bit(col0: ABit, col1: NumberLike, col2: NumberLike) -> ABit:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def split(col0: StringLike, col1: StringLike) -> list[StringLike]:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def stddev(col0: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def stem(col0: StringLike, col1: StringLike) -> StringLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def subtract(col0: NumberLike, col1: NumberLike) -> NumberLike: ...

@overload
def subtract(col0: DatetimeLike, col1: DatetimeLike) -> NumberLike: ...

@overload
def subtract(col0: DatetimeLike, col1: NumberLike) -> DatetimeLike: ...

@overload
def subtract(col0: DatetimeLike, col1: DatetimeLike) -> DatetimeLike: ...

@overload
def subtract(col0: DatetimeLike) -> DatetimeLike: ...

@create_generic
def subtract(col0: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def sumKahan(col0: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def sum_no_overflow(col0: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def text(col0: NumberLike, col1: StringLike) -> StringLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def translate(col0: StringLike, col1: StringLike, col2: StringLike) -> StringLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def variance(col0: NumberLike) -> NumberLike:
    """

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """