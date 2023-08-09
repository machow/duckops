
from __future__ import annotations

from typing import overload
from duckops.proto import create_generic, register_agg
from duckops.prototypes import *


__all__ = (
    "array_to_json",
    "from_json",
    "from_json_strict",
    "json_array",
    "json_array_length",
    "json_contains",
    "json_extract",
    "json_extract_string",
    "json_keys",
    "json_merge_patch",
    "json_object",
    "json_quote",
    "json_structure",
    "json_transform",
    "json_transform_strict",
    "json_type",
    "json_valid",
    "row_to_json",
    "to_json"
)


@create_generic
def array_to_json(*args: Any) -> AJson:
    """Alias for to_json that only accepts LIST

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def from_json(col0: AJson, col1: StringLike) -> Any: ...

@create_generic
def from_json(col0: StringLike, col1: StringLike) -> Any:
    """Alias for json_transform

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def from_json_strict(col0: AJson, col1: StringLike) -> Any: ...

@create_generic
def from_json_strict(col0: StringLike, col1: StringLike) -> Any:
    """Alias for json_transform_strict

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def json_array(*args: Any) -> AJson:
    """Create a JSON array from any number of values

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def json_array_length(col0: StringLike, col1: StringLike) -> NumberLike: ...

@overload
def json_array_length(col0: StringLike, col1: list[StringLike]) -> list[NumberLike]: ...

@overload
def json_array_length(col0: AJson) -> NumberLike: ...

@overload
def json_array_length(col0: AJson, col1: StringLike) -> NumberLike: ...

@overload
def json_array_length(col0: AJson, col1: list[StringLike]) -> list[NumberLike]: ...

@create_generic
def json_array_length(col0: StringLike) -> NumberLike:
    """Return the number of elements in the JSON array json, or 0 if it is not a JSON array. If path is specified, return the number of elements in the JSON array at the given path. If path is a LIST, the result will be LIST of array lengths

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def json_contains(col0: StringLike, col1: AJson) -> ABool: ...

@overload
def json_contains(col0: AJson, col1: StringLike) -> ABool: ...

@overload
def json_contains(col0: AJson, col1: AJson) -> ABool: ...

@create_generic
def json_contains(col0: StringLike, col1: StringLike) -> ABool:
    """Returns true if json_needle is contained in json_haystack. Both parameters are of JSON type, but json_needle can also be a numeric value or a string, however the string must be wrapped in double quotes

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def json_extract(col0: StringLike, col1: list[StringLike]) -> list[AJson]: ...

@overload
def json_extract(col0: AJson, col1: StringLike) -> AJson: ...

@overload
def json_extract(col0: AJson, col1: list[StringLike]) -> list[AJson]: ...

@create_generic
def json_extract(col0: StringLike, col1: StringLike) -> AJson:
    """Extract JSON from json at the given path. If path is a LIST, the result will be a LIST of JSON

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def json_extract_string(col0: StringLike, col1: list[StringLike]) -> list[StringLike]: ...

@overload
def json_extract_string(col0: AJson, col1: StringLike) -> StringLike: ...

@overload
def json_extract_string(col0: AJson, col1: list[StringLike]) -> list[StringLike]: ...

@create_generic
def json_extract_string(col0: StringLike, col1: StringLike) -> StringLike:
    """Extract VARCHAR from json at the given path. If path is a LIST, the result will be a LIST of VARCHAR

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def json_keys(col0: StringLike, col1: StringLike) -> list[StringLike]: ...

@overload
def json_keys(col0: StringLike, col1: list[StringLike]) -> Any: ...

@overload
def json_keys(col0: AJson) -> list[StringLike]: ...

@overload
def json_keys(col0: AJson, col1: StringLike) -> list[StringLike]: ...

@overload
def json_keys(col0: AJson, col1: list[StringLike]) -> Any: ...

@create_generic
def json_keys(col0: StringLike) -> list[StringLike]:
    """Returns the keys of json as a LIST of VARCHAR, if json is a JSON object. If path is specified, return the keys of the JSON object at the given path. If path is a LIST, the result will be LIST of LIST of VARCHAR

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def json_merge_patch(*args: Any) -> AJson:
    """Merge two json documents together

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def json_object(*args: Any) -> AJson:
    """Create a JSON object from any number of key, value pairs

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def json_quote(*args: Any) -> AJson:
    """Alias for to_json

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def json_structure(col0: AJson) -> AJson: ...

@create_generic
def json_structure(col0: StringLike) -> AJson:
    """Return the structure of json. Throws an error if the structure is inconsistent (incompatible types in an array)

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def json_transform(col0: AJson, col1: StringLike) -> Any: ...

@create_generic
def json_transform(col0: StringLike, col1: StringLike) -> Any:
    """Transform json according to the specified structure

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def json_transform_strict(col0: AJson, col1: StringLike) -> Any: ...

@create_generic
def json_transform_strict(col0: StringLike, col1: StringLike) -> Any:
    """Same as json_transform, but throws an error when type casting fails

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def json_type(col0: StringLike, col1: StringLike) -> StringLike: ...

@overload
def json_type(col0: StringLike, col1: list[StringLike]) -> list[StringLike]: ...

@overload
def json_type(col0: AJson) -> StringLike: ...

@overload
def json_type(col0: AJson, col1: StringLike) -> StringLike: ...

@overload
def json_type(col0: AJson, col1: list[StringLike]) -> list[StringLike]: ...

@create_generic
def json_type(col0: StringLike) -> StringLike:
    """Return the type of the supplied json, which is one of OBJECT, ARRAY, BIGINT, UBIGINT, VARCHAR, BOOLEAN, NULL. If path is specified, return the type of the element at the given path. If path is a LIST, the result will be LIST of types

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@overload
def json_valid(col0: AJson) -> ABool: ...

@create_generic
def json_valid(col0: StringLike) -> ABool:
    """Return whether json is valid JSON

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def row_to_json(*args: Any) -> AJson:
    """Alias for to_json that only accepts STRUCT

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def to_json(*args: Any) -> AJson:
    """Create JSON from a value of any type. Our LIST is converted to a JSON array, and our STRUCT and MAP are converted to a JSON object

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """