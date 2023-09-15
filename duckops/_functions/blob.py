
from __future__ import annotations

from typing import overload
from duckops.proto import create_generic, register_agg
from duckops.prototypes import *


__all__ = (
    "decode",
    "encode",
    "octet_length"
)


@create_generic
def decode(col0: ABlob) -> StringLike:
    """Convert blob to varchar. Fails if blob is not valid utf-8.

    | duckdb example | result |
    | -------------- | ------ |
    | decode('\xC3\xBC'::BLOB) | ü |


    """


@create_generic
def encode(col0: StringLike) -> ABlob:
    """Convert varchar to blob. Converts utf-8 characters into literal encoding.

    | duckdb example | result |
    | -------------- | ------ |
    | encode('my_string_with_ü') | my_string_with_\xC3\xBC |


    """


@overload
def octet_length(col0: ABit) -> NumberLike: ...

@create_generic
def octet_length(col0: ABlob) -> NumberLike:
    """Number of bytes in blob

    | duckdb example | result |
    | -------------- | ------ |
    | octet_length('\xAA\xBB'::BLOB) | 2 |


    """