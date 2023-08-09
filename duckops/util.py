
from __future__ import annotations

from typing import overload
from duckops.proto import create_generic, register_agg
from duckops.prototypes import *


__all__ = (
    "alias",
    "current_schema",
    "current_schemas",
    "current_setting",
    "currval",
    "gen_random_uuid",
    "icu_sort_key",
    "nextval",
    "stats",
    "txid_current",
    "typeof",
    "uuid",
    "version"
)


@create_generic
def alias(col0: Any) -> StringLike:
    """Return the name of the column

    | duckdb example | result |
    | -------------- | ------ |
    | alias(column1) | 'column1' |


    """


@create_generic
def current_schema() -> StringLike:
    """Return the name of the currently active schema. Default is main.

    | duckdb example | result |
    | -------------- | ------ |
    | current_schema() | 'main' |


    """


@create_generic
def current_schemas(col0: ABool) -> list[StringLike]:
    """Return list of schemas. Pass a parameter of True to include implicit schemas.

    | duckdb example | result |
    | -------------- | ------ |
    | current_schemas(true) | ['temp', 'main', 'pg_catalog'] |


    """


@create_generic
def current_setting(col0: StringLike) -> Any:
    """Return the current value of the configuration setting

    | duckdb example | result |
    | -------------- | ------ |
    | current_setting('access_mode') | 'automatic' |


    """


@create_generic
def currval(col0: StringLike) -> NumberLike:
    """Return the current value of the sequence. Note that nextval must be called at least once prior to calling currval.

    | duckdb example | result |
    | -------------- | ------ |
    | currval('my_sequence_name') | 1 |


    """


@create_generic
def gen_random_uuid() -> UuidLike:
    """Alias of uuid. Return a random uuid similar to this: eeccb8c5-9943-b2bb-bb5e-222f4e14b687.

    | duckdb example | result |
    | -------------- | ------ |
    | gen_random_uuid() | various |


    """


@create_generic
def icu_sort_key(col0: StringLike, col1: StringLike) -> StringLike:
    """Surrogate key used to sort special characters according to the specific locale. Collator parameter is optional. Valid only when ICU extension is installed.

    | duckdb example | result |
    | -------------- | ------ |
    | icu_sort_key('ö','DE') | 460145960106 |


    """


@create_generic
def nextval(col0: StringLike) -> NumberLike:
    """Return the following value of the sequence.

    | duckdb example | result |
    | -------------- | ------ |
    | nextval('my_sequence_name') | 2 |


    """


@create_generic
def stats(col0: Any) -> StringLike:
    """Returns a string with statistics about the expression. Expression can be a column, constant, or SQL expression.

    | duckdb example | result |
    | -------------- | ------ |
    | stats(5) | '[Min: 5, Max: 5][Has Null: false]' |


    """


@create_generic
def txid_current() -> NumberLike:
    """Returns the current transaction’s ID (a BIGINT). It will assign a new one if the current transaction does not have one already.

    | duckdb example | result |
    | -------------- | ------ |
    | txid_current() | various |


    """


@create_generic
def typeof(col0: Any) -> StringLike:
    """Returns the name of the data type of the result of the expression.

    | duckdb example | result |
    | -------------- | ------ |
    | typeof('abc') | 'VARCHAR' |


    """


@create_generic
def uuid() -> UuidLike:
    """Return a random uuid similar to this: eeccb8c5-9943-b2bb-bb5e-222f4e14b687.

    | duckdb example | result |
    | -------------- | ------ |
    | uuid() | various |


    """


@overload
def version() -> None: ...

@create_generic
def version() -> StringLike:
    """Return the currently active version of DuckDB in this format: v0.3.2

    | duckdb example | result |
    | -------------- | ------ |
    | version() | various |


    """