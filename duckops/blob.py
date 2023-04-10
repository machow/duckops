
from . import _core
from siuba.sql import translate as _tr
from siuba.sql.dialects.duckdb import DuckdbColumn, DuckdbColumnAgg

@_core.sql_scalar("decode")
def decode(codata: DuckdbColumn, *args):
    """Convert blob to varchar. Fails if blob is not valid utf-8.
| duckdb example | result |
| -------------- | ------ |
| decode('\xC3\xBC'::BLOB) | ü |
"""



@_core.sql_scalar("encode")
def encode(codata: DuckdbColumn, *args):
    """Convert varchar to blob. Converts utf-8 characters into literal encoding.
| duckdb example | result |
| -------------- | ------ |
| encode('my_string_with_ü') | my_string_with_\xC3\xBC |
"""



@_core.sql_scalar("octet_length")
def octet_length(codata: DuckdbColumn, *args):
    """Number of bytes in blob
| duckdb example | result |
| -------------- | ------ |
| octet_length('\xAA\xBB'::BLOB) | 2 |
"""
