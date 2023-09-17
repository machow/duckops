
from __future__ import annotations

from typing import overload
from duckops.core.dispatch import create_generic, register_agg
from duckops.core.data_style import *


__all__ = (
    "array_aggr",
    "array_aggregate",
    "array_apply",
    "array_cat",
    "array_concat",
    "array_contains",
    "array_distinct",
    "array_filter",
    "array_has",
    "array_indexof",
    "array_length",
    "array_position",
    "array_reverse_sort",
    "array_sort",
    "array_transform",
    "array_unique",
    "cardinality",
    "element_at",
    "len",
    "list_aggr",
    "list_aggregate",
    "list_apply",
    "list_cat",
    "list_concat",
    "list_contains",
    "list_distinct",
    "list_filter",
    "list_has",
    "list_indexof",
    "list_pack",
    "list_position",
    "list_reverse_sort",
    "list_slice",
    "list_sort",
    "list_transform",
    "list_unique",
    "list_value",
    "map",
    "map_extract",
    "map_from_entries",
    "row",
    "struct_extract",
    "struct_insert",
    "struct_pack",
    "union_extract",
    "union_tag",
    "union_value"
)


@create_generic
def array_aggr(col0: list[Any], col1: StringLike, *args: Any) -> Any:
    """Alias for list_aggregate.

    | duckdb example | result |
    | -------------- | ------ |
    | array_aggr([1, 2, NULL], 'min') | 1 |


    """


@create_generic
def array_aggregate(col0: list[Any], col1: StringLike, *args: Any) -> Any:
    """Alias for list_aggregate.

    | duckdb example | result |
    | -------------- | ------ |
    | array_aggregate([1, 2, NULL], 'min') | 1 |


    """


@create_generic
def array_apply(col0: list[Any], col1: LambdaLike) -> list[Any]:
    """Alias for list_transform.

    | duckdb example | result |
    | -------------- | ------ |
    | array_apply(l, x -> x + 1) | [5, 6, 7] |


    """


@create_generic
def array_cat(col0: list[Any], col1: list[Any]) -> list[Any]:
    """Alias for list_concat.

    | duckdb example | result |
    | -------------- | ------ |
    | array_cat([2, 3], [4, 5, 6]) | [2, 3, 4, 5, 6] |


    """


@create_generic
def array_concat(col0: list[Any], col1: list[Any]) -> list[Any]:
    """Alias for list_concat.

    | duckdb example | result |
    | -------------- | ------ |
    | array_concat([2, 3], [4, 5, 6]) | [2, 3, 4, 5, 6] |


    """


@create_generic
def array_contains(col0: list[Any], col1: Any) -> ABool:
    """Alias for list_contains.

    | duckdb example | result |
    | -------------- | ------ |
    | array_contains([1, 2, NULL], 1) | true |


    """


@create_generic
def array_distinct(col0: list[Any]) -> list[Any]:
    """Alias for list_distinct.

    | duckdb example | result |
    | -------------- | ------ |
    | array_distinct([1, 1, NULL, -3, 1, 5]) | [1, 5, -3] |


    """


@create_generic
def array_filter(col0: list[Any], col1: LambdaLike) -> list[Any]:
    """Alias for list_filter.

    | duckdb example | result |
    | -------------- | ------ |
    | array_filter(l, x -> x > 4) | [5, 6] |


    """


@create_generic
def array_has(col0: list[Any], col1: Any) -> ABool:
    """Alias for list_contains.

    | duckdb example | result |
    | -------------- | ------ |
    | array_has([1, 2, NULL], 1) | true |


    """


@create_generic
def array_indexof(col0: list[Any], col1: Any) -> NumberLike:
    """Alias for list_position.

    | duckdb example | result |
    | -------------- | ------ |
    | array_indexof([1, 2, NULL], 2) | 2 |


    """


@overload
def array_length(col0: list[Any], col1: NumberLike) -> NumberLike: ...

@create_generic
def array_length(col0: list[Any]) -> NumberLike:
    """Alias for len.

    | duckdb example | result |
    | -------------- | ------ |
    | array_length([1, 2, 3]) | 3 |


    """


@create_generic
def array_position(col0: list[Any], col1: Any) -> NumberLike:
    """Alias for list_position.

    | duckdb example | result |
    | -------------- | ------ |
    | array_position([1, 2, NULL], 2) | 2 |


    """


@overload
def array_reverse_sort(col0: list[Any], col1: StringLike) -> list[Any]: ...

@create_generic
def array_reverse_sort(col0: list[Any]) -> list[Any]:
    """Alias for list_reverse_sort.

    | duckdb example | result |
    | -------------- | ------ |
    | array_reverse_sort([3, 6, 1, 2]) | [6, 3, 2, 1] |


    """


@overload
def array_sort(col0: list[Any], col1: StringLike) -> list[Any]: ...

@overload
def array_sort(col0: list[Any], col1: StringLike, col2: StringLike) -> list[Any]: ...

@create_generic
def array_sort(col0: list[Any]) -> list[Any]:
    """Alias for list_sort.

    | duckdb example | result |
    | -------------- | ------ |
    | array_sort([3, 6, 1, 2]) | [1, 2, 3, 6] |


    """


@create_generic
def array_transform(col0: list[Any], col1: LambdaLike) -> list[Any]:
    """Alias for list_transform.

    | duckdb example | result |
    | -------------- | ------ |
    | array_transform(l, x -> x + 1) | [5, 6, 7] |


    """


@create_generic
def array_unique(col0: list[Any]) -> NumberLike:
    """Alias for list_unique.

    | duckdb example | result |
    | -------------- | ------ |
    | array_unique([1, 1, NULL, -3, 1, 5]) | 3 |


    """


@create_generic
def cardinality(col0: Any, *args: Any) -> NumberLike:
    """Return the size of the map (or the number of entries in the map).

    | duckdb example | result |
    | -------------- | ------ |
    | cardinality( map([4, 2], ['a', 'b']) ); | 2 |


    """


@create_generic
def element_at(col0: Any, col1: Any, *args: Any) -> Any:
    """Return a list containing the value for a given key or an empty list if the key is not contained in the map. The type of the key provided in the second parameter must match the type of the map’s keys else an error is returned.

    | duckdb example | result |
    | -------------- | ------ |
    | element_at(map([100, 5], [42, 43]),100); | [42] |


    """


@overload
def len(col0: ABit) -> NumberLike: ...

@overload
def len(col0: list[Any]) -> NumberLike: ...

@create_generic
def len(col0: StringLike) -> NumberLike:
    """Return the length of the list.

    | duckdb example | result |
    | -------------- | ------ |
    | len([1, 2, 3]) | 3 |


    """


@create_generic
def list_aggr(col0: list[Any], col1: StringLike, *args: Any) -> Any:
    """Alias for list_aggregate.

    | duckdb example | result |
    | -------------- | ------ |
    | list_aggr([1, 2, NULL], 'min') | 1 |


    """


@create_generic
def list_aggregate(col0: list[Any], col1: StringLike, *args: Any) -> Any:
    """Executes the aggregate function name on the elements of list. See the List Aggregates section for more details.

    | duckdb example | result |
    | -------------- | ------ |
    | list_aggregate([1, 2, NULL], 'min') | 1 |


    """


@create_generic
def list_apply(col0: list[Any], col1: LambdaLike) -> list[Any]:
    """Alias for list_transform.

    | duckdb example | result |
    | -------------- | ------ |
    | list_apply(l, x -> x + 1) | [5, 6, 7] |


    """


@create_generic
def list_cat(col0: list[Any], col1: list[Any]) -> list[Any]:
    """Alias for list_concat.

    | duckdb example | result |
    | -------------- | ------ |
    | list_cat([2, 3], [4, 5, 6]) | [2, 3, 4, 5, 6] |


    """


@create_generic
def list_concat(col0: list[Any], col1: list[Any]) -> list[Any]:
    """Concatenates two lists.

    | duckdb example | result |
    | -------------- | ------ |
    | list_concat([2, 3], [4, 5, 6]) | [2, 3, 4, 5, 6] |


    """


@create_generic
def list_contains(col0: list[Any], col1: Any) -> ABool:
    """Returns true if the list contains the element.

    | duckdb example | result |
    | -------------- | ------ |
    | list_contains([1, 2, NULL], 1) | true |


    """


@create_generic
def list_distinct(col0: list[Any]) -> list[Any]:
    """Removes all duplicates and NULLs from a list. Does not preserve the original order.

    | duckdb example | result |
    | -------------- | ------ |
    | list_distinct([1, 1, NULL, -3, 1, 5]) | [1, 5, -3] |


    """


@create_generic
def list_filter(col0: list[Any], col1: LambdaLike) -> list[Any]:
    """Constructs a list from those elements of the input list for which the lambda function returns true. See the Lambda Functions section for more details.

    | duckdb example | result |
    | -------------- | ------ |
    | list_filter(l, x -> x > 4) | [5, 6] |


    """


@create_generic
def list_has(col0: list[Any], col1: Any) -> ABool:
    """Alias for list_contains.

    | duckdb example | result |
    | -------------- | ------ |
    | list_has([1, 2, NULL], 1) | true |


    """


@create_generic
def list_indexof(col0: list[Any], col1: Any) -> NumberLike:
    """Alias for list_position.

    | duckdb example | result |
    | -------------- | ------ |
    | list_indexof([1, 2, NULL], 2) | 2 |


    """


@create_generic
def list_pack(*args: Any) -> AList:
    """Alias for list_value.

    | duckdb example | result |
    | -------------- | ------ |
    | list_pack(4, 5, 6) | [4, 5, 6] |


    """


@create_generic
def list_position(col0: list[Any], col1: Any) -> NumberLike:
    """Returns the index of the element if the list contains the element.

    | duckdb example | result |
    | -------------- | ------ |
    | list_contains([1, 2, NULL], 2) | 2 |


    """


@overload
def list_reverse_sort(col0: list[Any], col1: StringLike) -> list[Any]: ...

@create_generic
def list_reverse_sort(col0: list[Any]) -> list[Any]:
    """Sorts the elements of the list in reverse order. See the Sorting Lists section for more details about the null sorting order.

    | duckdb example | result |
    | -------------- | ------ |
    | list_reverse_sort([3, 6, 1, 2]) | [6, 3, 2, 1] |


    """


@create_generic
def list_slice(col0: Any, col1: NumberLike, col2: NumberLike, *args: Any) -> Any:
    """Extract a sublist using slice conventions. NULLs are interpreted as the bounds of the LIST. Negative values are accepted.

    | duckdb example | result |
    | -------------- | ------ |
    | list_slice(l, 2, NULL) | [5, 6] |


    """


@overload
def list_sort(col0: list[Any], col1: StringLike) -> list[Any]: ...

@overload
def list_sort(col0: list[Any], col1: StringLike, col2: StringLike) -> list[Any]: ...

@create_generic
def list_sort(col0: list[Any]) -> list[Any]:
    """Sorts the elements of the list. See the Sorting Lists section for more details about the sorting order and the null sorting order.

    | duckdb example | result |
    | -------------- | ------ |
    | list_sort([3, 6, 1, 2]) | [1, 2, 3, 6] |


    """


@create_generic
def list_transform(col0: list[Any], col1: LambdaLike) -> list[Any]:
    """Returns a list that is the result of applying the lambda function to each element of the input list. See the Lambda Functions section for more details.

    | duckdb example | result |
    | -------------- | ------ |
    | list_transform(l, x -> x + 1) | [5, 6, 7] |


    """


@create_generic
def list_unique(col0: list[Any]) -> NumberLike:
    """Counts the unique elements of a list.

    | duckdb example | result |
    | -------------- | ------ |
    | list_unique([1, 1, NULL, -3, 1, 5]) | 3 |


    """


@create_generic
def list_value(*args: Any) -> AList:
    """Create a LIST containing the argument values.

    | duckdb example | result |
    | -------------- | ------ |
    | list_value(4, 5, 6) | [4, 5, 6] |


    """


@create_generic
def map(*args: Any) -> AMap:
    """Returns an empty map.

    | duckdb example | result |
    | -------------- | ------ |
    | map() | {} |


    """


@create_generic
def map_extract(col0: Any, col1: Any, *args: Any) -> Any:
    """Alias of element_at. Return a list containing the value for a given key or an empty list if the key is not contained in the map. The type of the key provided in the second parameter must match the type of the map’s keys else an error is returned.

    | duckdb example | result |
    | -------------- | ------ |
    | map_extract(map([100, 5], [42, 43]),100); | [42] |


    """


@create_generic
def map_from_entries(*args: Any) -> AMap:
    """Returns a map created from the entries of the array

    | duckdb example | result |
    | -------------- | ------ |
    | map_from_entries([{k: 5, v: 'val1'}, {k: 3, v: 'val2'}]); | {5=val1, 3=val2} |


    """


@create_generic
def row(*args: Any) -> StructLike:
    """Create a STRUCT containing the argument values. If the values are column references, the entry name will be the column name; otherwise it will be the string 'vN' where N is the (1-based) position of the argument.

    | duckdb example | result |
    | -------------- | ------ |
    | row(i, i % 4, i / 4) | {'i': 3, 'v2': 3, 'v3': 0} |


    """


@create_generic
def struct_extract(col0: StructLike, col1: StringLike) -> Any:
    """Extract the named entry from the struct.

    | duckdb example | result |
    | -------------- | ------ |
    | struct_extract(s, 'i') | 4 |


    """


@create_generic
def struct_insert(*args: Any) -> StructLike:
    """Add field(s)/value(s) to an existing STRUCT with the argument values. The entry name(s) will be the bound variable name(s).

    | duckdb example | result |
    | -------------- | ------ |
    | struct_insert({'a': 1}, b := 2) | {'a': 1, 'b': 2} |


    """


@create_generic
def struct_pack(*args: Any) -> StructLike:
    """Create a STRUCT containing the argument values. The entry name will be the bound variable name.

    | duckdb example | result |
    | -------------- | ------ |
    | struct_pack(i := 4, s := 'string') | {'i': 3, 's': 'string'} |


    """


@create_generic
def union_extract(col0: AUnion, col1: StringLike) -> Any:
    """Extract the value with the named tags from the union. NULL if the tag is not currently selected

    | duckdb example | result |
    | -------------- | ------ |
    | union_extract(s, 'k') | hello |


    """


@create_generic
def union_tag(col0: AUnion) -> Any:
    """Retrieve the currently selected tag of the union as an Enum.

    | duckdb example | result |
    | -------------- | ------ |
    | union_tag(union_value(k := 'foo')) | 'k' |


    """


@create_generic
def union_value(*args: Any) -> AUnion:
    """Create a single member UNION containing the argument value. The tag of the value will be the bound variable name.

    | duckdb example | result |
    | -------------- | ------ |
    | union_value(k := 'hello') | 'hello'::UNION(k VARCHAR) |


    """