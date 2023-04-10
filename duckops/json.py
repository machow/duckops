
from . import _core
from siuba.sql import translate as _tr
from siuba.sql.dialects.duckdb import DuckdbColumn, DuckdbColumnAgg

@_core.sql_scalar("json_valid")
def json_valid(codata: DuckdbColumn, *args):
    """Return whether json is valid JSON
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("json_type")
def json_type(codata: DuckdbColumn, *args):
    """Return the type of the supplied json, which is one of OBJECT, ARRAY, BIGINT, UBIGINT, VARCHAR, BOOLEAN, NULL. If path is specified, return the type of the element at the given path. If path is a LIST, the result will be LIST of types
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("json_keys")
def json_keys(codata: DuckdbColumn, *args):
    """Returns the keys of json as a LIST of VARCHAR, if json is a JSON object. If path is specified, return the keys of the JSON object at the given path. If path is a LIST, the result will be LIST of LIST of VARCHAR
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("json_contains")
def json_contains(codata: DuckdbColumn, *args):
    """Returns true if json_needle is contained in json_haystack. Both parameters are of JSON type, but json_needle can also be a numeric value or a string, however the string must be wrapped in double quotes
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("json_array_length")
def json_array_length(codata: DuckdbColumn, *args):
    """Return the number of elements in the JSON array json, or 0 if it is not a JSON array. If path is specified, return the number of elements in the JSON array at the given path. If path is a LIST, the result will be LIST of array lengths
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("from_json_strict")
def from_json_strict(codata: DuckdbColumn, *args):
    """Alias for json_transform_strict
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("json_transform_strict")
def json_transform_strict(codata: DuckdbColumn, *args):
    """Same as json_transform, but throws an error when type casting fails
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("from_json")
def from_json(codata: DuckdbColumn, *args):
    """Alias for json_transform
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("json_transform")
def json_transform(codata: DuckdbColumn, *args):
    """Transform json according to the specified structure
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("json_structure")
def json_structure(codata: DuckdbColumn, *args):
    """Return the structure of json. Throws an error if the structure is inconsistent (incompatible types in an array)
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("json_merge_patch")
def json_merge_patch(codata: DuckdbColumn, *args):
    """Merge two json documents together
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("row_to_json")
def row_to_json(codata: DuckdbColumn, *args):
    """Alias for to_json that only accepts STRUCT
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("array_to_json")
def array_to_json(codata: DuckdbColumn, *args):
    """Alias for to_json that only accepts LIST
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("json_quote")
def json_quote(codata: DuckdbColumn, *args):
    """Alias for to_json
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("to_json")
def to_json(codata: DuckdbColumn, *args):
    """Create JSON from a value of any type. Our LIST is converted to a JSON array, and our STRUCT and MAP are converted to a JSON object
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("json_object")
def json_object(codata: DuckdbColumn, *args):
    """Create a JSON object from any number of key, value pairs
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("json_array")
def json_array(codata: DuckdbColumn, *args):
    """Create a JSON array from any number of values
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("json_extract_string")
def json_extract_string(codata: DuckdbColumn, *args):
    """Extract VARCHAR from json at the given path. If path is a LIST, the result will be a LIST of VARCHAR
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("json_extract")
def json_extract(codata: DuckdbColumn, *args):
    """Extract JSON from json at the given path. If path is a LIST, the result will be a LIST of JSON
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""
