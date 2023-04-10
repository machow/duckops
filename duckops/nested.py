
from . import _core
from siuba.sql import translate as _tr
from siuba.sql.dialects.duckdb import DuckdbColumn, DuckdbColumnAgg

@_core.sql_scalar("cardinality")
def cardinality(codata: DuckdbColumn, *args):
    """Return the size of the map (or the number of entries in the map).
| duckdb example | result |
| -------------- | ------ |
| cardinality( map([4, 2], ['a', 'b']) ); | 2 |
"""



@_core.sql_scalar("union_tag")
def union_tag(codata: DuckdbColumn, *args):
    """Retrieve the currently selected tag of the union as an Enum.
| duckdb example | result |
| -------------- | ------ |
| union_tag(union_value(k := 'foo')) | 'k' |
"""



@_core.sql_scalar("union_extract")
def union_extract(codata: DuckdbColumn, *args):
    """Extract the value with the named tags from the union. NULL if the tag is not currently selected
| duckdb example | result |
| -------------- | ------ |
| union_extract(s, 'k') | hello |
"""



@_core.sql_scalar("union_value")
def union_value(codata: DuckdbColumn, *args):
    """Create a single member UNION containing the argument value. The tag of the value will be the bound variable name.
| duckdb example | result |
| -------------- | ------ |
| union_value(k := 'hello') | 'hello'::UNION(k VARCHAR) |
"""



@_core.sql_scalar("element_at")
def element_at(codata: DuckdbColumn, *args):
    """Return a list containing the value for a given key or an empty list if the key is not contained in the map. The type of the key provided in the second parameter must match the type of the map’s keys else an error is returned.
| duckdb example | result |
| -------------- | ------ |
| element_at(map([100, 5], [42, 43]),100); | [42] |
"""



@_core.sql_scalar("map_extract")
def map_extract(codata: DuckdbColumn, *args):
    """Alias of element_at. Return a list containing the value for a given key or an empty list if the key is not contained in the map. The type of the key provided in the second parameter must match the type of the map’s keys else an error is returned.
| duckdb example | result |
| -------------- | ------ |
| map_extract(map([100, 5], [42, 43]),100); | [42] |
"""



@_core.sql_scalar("map_from_entries")
def map_from_entries(codata: DuckdbColumn, *args):
    """Returns a map created from the entries of the array
| duckdb example | result |
| -------------- | ------ |
| map_from_entries([{k: 5, v: 'val1'}, {k: 3, v: 'val2'}]); | {5=val1, 3=val2} |
"""



@_core.sql_scalar("map")
def map(codata: DuckdbColumn, *args):
    """Returns an empty map.
| duckdb example | result |
| -------------- | ------ |
| map() | {} |
"""



@_core.sql_scalar("array_reverse_sort")
def array_reverse_sort(codata: DuckdbColumn, *args):
    """Alias for list_reverse_sort.
| duckdb example | result |
| -------------- | ------ |
| array_reverse_sort([3, 6, 1, 2]) | [6, 3, 2, 1] |
"""



@_core.sql_scalar("list_reverse_sort")
def list_reverse_sort(codata: DuckdbColumn, *args):
    """Sorts the elements of the list in reverse order. See the Sorting Lists section for more details about the null sorting order.
| duckdb example | result |
| -------------- | ------ |
| list_reverse_sort([3, 6, 1, 2]) | [6, 3, 2, 1] |
"""



@_core.sql_scalar("array_sort")
def array_sort(codata: DuckdbColumn, *args):
    """Alias for list_sort.
| duckdb example | result |
| -------------- | ------ |
| array_sort([3, 6, 1, 2]) | [1, 2, 3, 6] |
"""



@_core.sql_scalar("list_sort")
def list_sort(codata: DuckdbColumn, *args):
    """Sorts the elements of the list. See the Sorting Lists section for more details about the sorting order and the null sorting order.
| duckdb example | result |
| -------------- | ------ |
| list_sort([3, 6, 1, 2]) | [1, 2, 3, 6] |
"""



@_core.sql_scalar("list_pack")
def list_pack(codata: DuckdbColumn, *args):
    """Alias for list_value.
| duckdb example | result |
| -------------- | ------ |
| list_pack(4, 5, 6) | [4, 5, 6] |
"""



@_core.sql_scalar("list_value")
def list_value(codata: DuckdbColumn, *args):
    """Create a LIST containing the argument values.
| duckdb example | result |
| -------------- | ------ |
| list_value(4, 5, 6) | [4, 5, 6] |
"""



@_core.sql_scalar("array_unique")
def array_unique(codata: DuckdbColumn, *args):
    """Alias for list_unique.
| duckdb example | result |
| -------------- | ------ |
| array_unique([1, 1, NULL, -3, 1, 5]) | 3 |
"""



@_core.sql_scalar("list_unique")
def list_unique(codata: DuckdbColumn, *args):
    """Counts the unique elements of a list.
| duckdb example | result |
| -------------- | ------ |
| list_unique([1, 1, NULL, -3, 1, 5]) | 3 |
"""



@_core.sql_scalar("array_distinct")
def array_distinct(codata: DuckdbColumn, *args):
    """Alias for list_distinct.
| duckdb example | result |
| -------------- | ------ |
| array_distinct([1, 1, NULL, -3, 1, 5]) | [1, 5, -3] |
"""



@_core.sql_scalar("list_distinct")
def list_distinct(codata: DuckdbColumn, *args):
    """Removes all duplicates and NULLs from a list. Does not preserve the original order.
| duckdb example | result |
| -------------- | ------ |
| list_distinct([1, 1, NULL, -3, 1, 5]) | [1, 5, -3] |
"""



@_core.sql_scalar("array_aggr")
def array_aggr(codata: DuckdbColumn, *args):
    """Alias for list_aggregate.
| duckdb example | result |
| -------------- | ------ |
| array_aggr([1, 2, NULL], 'min') | 1 |
"""



@_core.sql_scalar("list_aggr")
def list_aggr(codata: DuckdbColumn, *args):
    """Alias for list_aggregate.
| duckdb example | result |
| -------------- | ------ |
| list_aggr([1, 2, NULL], 'min') | 1 |
"""



@_core.sql_scalar("array_aggregate")
def array_aggregate(codata: DuckdbColumn, *args):
    """Alias for list_aggregate.
| duckdb example | result |
| -------------- | ------ |
| array_aggregate([1, 2, NULL], 'min') | 1 |
"""



@_core.sql_scalar("list_aggregate")
def list_aggregate(codata: DuckdbColumn, *args):
    """Executes the aggregate function name on the elements of list. See the List Aggregates section for more details.
| duckdb example | result |
| -------------- | ------ |
| list_aggregate([1, 2, NULL], 'min') | 1 |
"""



@_core.sql_scalar("array_indexof")
def array_indexof(codata: DuckdbColumn, *args):
    """Alias for list_position.
| duckdb example | result |
| -------------- | ------ |
| array_indexof([1, 2, NULL], 2) | 2 |
"""



@_core.sql_scalar("array_position")
def array_position(codata: DuckdbColumn, *args):
    """Alias for list_position.
| duckdb example | result |
| -------------- | ------ |
| array_position([1, 2, NULL], 2) | 2 |
"""



@_core.sql_scalar("list_indexof")
def list_indexof(codata: DuckdbColumn, *args):
    """Alias for list_position.
| duckdb example | result |
| -------------- | ------ |
| list_indexof([1, 2, NULL], 2) | 2 |
"""



@_core.sql_scalar("list_position")
def list_position(codata: DuckdbColumn, *args):
    """Returns the index of the element if the list contains the element.
| duckdb example | result |
| -------------- | ------ |
| list_contains([1, 2, NULL], 2) | 2 |
"""



@_core.sql_scalar("array_has")
def array_has(codata: DuckdbColumn, *args):
    """Alias for list_contains.
| duckdb example | result |
| -------------- | ------ |
| array_has([1, 2, NULL], 1) | true |
"""



@_core.sql_scalar("list_has")
def list_has(codata: DuckdbColumn, *args):
    """Alias for list_contains.
| duckdb example | result |
| -------------- | ------ |
| list_has([1, 2, NULL], 1) | true |
"""



@_core.sql_scalar("array_contains")
def array_contains(codata: DuckdbColumn, *args):
    """Alias for list_contains.
| duckdb example | result |
| -------------- | ------ |
| array_contains([1, 2, NULL], 1) | true |
"""



@_core.sql_scalar("list_contains")
def list_contains(codata: DuckdbColumn, *args):
    """Returns true if the list contains the element.
| duckdb example | result |
| -------------- | ------ |
| list_contains([1, 2, NULL], 1) | true |
"""



@_core.sql_scalar("array_cat")
def array_cat(codata: DuckdbColumn, *args):
    """Alias for list_concat.
| duckdb example | result |
| -------------- | ------ |
| array_cat([2, 3], [4, 5, 6]) | [2, 3, 4, 5, 6] |
"""



@_core.sql_scalar("array_concat")
def array_concat(codata: DuckdbColumn, *args):
    """Alias for list_concat.
| duckdb example | result |
| -------------- | ------ |
| array_concat([2, 3], [4, 5, 6]) | [2, 3, 4, 5, 6] |
"""



@_core.sql_scalar("list_cat")
def list_cat(codata: DuckdbColumn, *args):
    """Alias for list_concat.
| duckdb example | result |
| -------------- | ------ |
| list_cat([2, 3], [4, 5, 6]) | [2, 3, 4, 5, 6] |
"""



@_core.sql_scalar("list_concat")
def list_concat(codata: DuckdbColumn, *args):
    """Concatenates two lists.
| duckdb example | result |
| -------------- | ------ |
| list_concat([2, 3], [4, 5, 6]) | [2, 3, 4, 5, 6] |
"""



@_core.sql_scalar("array_filter")
def array_filter(codata: DuckdbColumn, *args):
    """Alias for list_filter.
| duckdb example | result |
| -------------- | ------ |
| array_filter(l, x -> x > 4) | [5, 6] |
"""



@_core.sql_scalar("list_filter")
def list_filter(codata: DuckdbColumn, *args):
    """Constructs a list from those elements of the input list for which the lambda function returns true. See the Lambda Functions section for more details.
| duckdb example | result |
| -------------- | ------ |
| list_filter(l, x -> x > 4) | [5, 6] |
"""



@_core.sql_scalar("array_apply")
def array_apply(codata: DuckdbColumn, *args):
    """Alias for list_transform.
| duckdb example | result |
| -------------- | ------ |
| array_apply(l, x -> x + 1) | [5, 6, 7] |
"""



@_core.sql_scalar("list_apply")
def list_apply(codata: DuckdbColumn, *args):
    """Alias for list_transform.
| duckdb example | result |
| -------------- | ------ |
| list_apply(l, x -> x + 1) | [5, 6, 7] |
"""



@_core.sql_scalar("array_transform")
def array_transform(codata: DuckdbColumn, *args):
    """Alias for list_transform.
| duckdb example | result |
| -------------- | ------ |
| array_transform(l, x -> x + 1) | [5, 6, 7] |
"""



@_core.sql_scalar("list_transform")
def list_transform(codata: DuckdbColumn, *args):
    """Returns a list that is the result of applying the lambda function to each element of the input list. See the Lambda Functions section for more details.
| duckdb example | result |
| -------------- | ------ |
| list_transform(l, x -> x + 1) | [5, 6, 7] |
"""



@_core.sql_scalar("struct_insert")
def struct_insert(codata: DuckdbColumn, *args):
    """Add field(s)/value(s) to an existing STRUCT with the argument values. The entry name(s) will be the bound variable name(s).
| duckdb example | result |
| -------------- | ------ |
| struct_insert({'a': 1}, b := 2) | {'a': 1, 'b': 2} |
"""



@_core.sql_scalar("struct_extract")
def struct_extract(codata: DuckdbColumn, *args):
    """Extract the named entry from the struct.
| duckdb example | result |
| -------------- | ------ |
| struct_extract(s, 'i') | 4 |
"""



@_core.sql_scalar("row")
def row(codata: DuckdbColumn, *args):
    """Create a STRUCT containing the argument values. If the values are column references, the entry name will be the column name; otherwise it will be the string 'vN' where N is the (1-based) position of the argument.
| duckdb example | result |
| -------------- | ------ |
| row(i, i % 4, i / 4) | {'i': 3, 'v2': 3, 'v3': 0} |
"""



@_core.sql_scalar("struct_pack")
def struct_pack(codata: DuckdbColumn, *args):
    """Create a STRUCT containing the argument values. The entry name will be the bound variable name.
| duckdb example | result |
| -------------- | ------ |
| struct_pack(i := 4, s := 'string') | {'i': 3, 's': 'string'} |
"""



@_core.sql_scalar("list_slice")
def list_slice(codata: DuckdbColumn, *args):
    """Extract a sublist using slice conventions. NULLs are interpreted as the bounds of the LIST. Negative values are accepted.
| duckdb example | result |
| -------------- | ------ |
| list_slice(l, 2, NULL) | [5, 6] |
"""



@_core.sql_scalar("array_length")
def array_length(codata: DuckdbColumn, *args):
    """Alias for len.
| duckdb example | result |
| -------------- | ------ |
| array_length([1, 2, 3]) | 3 |
"""



@_core.sql_scalar("len")
def len(codata: DuckdbColumn, *args):
    """Return the length of the list.
| duckdb example | result |
| -------------- | ------ |
| len([1, 2, 3]) | 3 |
"""
