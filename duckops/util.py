
from . import _core
from siuba.sql import translate as _tr
from siuba.sql.dialects.duckdb import DuckdbColumn, DuckdbColumnAgg

@_core.sql_scalar("txid_current")
def txid_current(codata: DuckdbColumn, *args):
    """Returns the current transaction’s ID (a BIGINT). It will assign a new one if the current transaction does not have one already.
| duckdb example | result |
| -------------- | ------ |
| txid_current() | various |
"""



@_core.sql_scalar("alias")
def alias(codata: DuckdbColumn, *args):
    """Return the name of the column
| duckdb example | result |
| -------------- | ------ |
| alias(column1) | 'column1' |
"""



@_core.sql_scalar("stats")
def stats(codata: DuckdbColumn, *args):
    """Returns a string with statistics about the expression. Expression can be a column, constant, or SQL expression.
| duckdb example | result |
| -------------- | ------ |
| stats(5) | '[Min: 5, Max: 5][Has Null: false]' |
"""



@_core.sql_scalar("typeof")
def typeof(codata: DuckdbColumn, *args):
    """Returns the name of the data type of the result of the expression.
| duckdb example | result |
| -------------- | ------ |
| typeof('abc') | 'VARCHAR' |
"""



@_core.sql_scalar("current_setting")
def current_setting(codata: DuckdbColumn, *args):
    """Return the current value of the configuration setting
| duckdb example | result |
| -------------- | ------ |
| current_setting('access_mode') | 'automatic' |
"""



@_core.sql_scalar("current_schema")
def current_schema(codata: DuckdbColumn, *args):
    """Return the name of the currently active schema. Default is main.
| duckdb example | result |
| -------------- | ------ |
| current_schema() | 'main' |
"""



@_core.sql_scalar("icu_sort_key")
def icu_sort_key(codata: DuckdbColumn, *args):
    """Surrogate key used to sort special characters according to the specific locale. Collator parameter is optional. Valid only when ICU extension is installed.
| duckdb example | result |
| -------------- | ------ |
| icu_sort_key('ö','DE') | 460145960106 |
"""



@_core.sql_scalar("current_schemas")
def current_schemas(codata: DuckdbColumn, *args):
    """Return list of schemas. Pass a parameter of True to include implicit schemas.
| duckdb example | result |
| -------------- | ------ |
| current_schemas(true) | ['temp', 'main', 'pg_catalog'] |
"""



@_core.sql_scalar("version")
def version(codata: DuckdbColumn, *args):
    """Return the currently active version of DuckDB in this format: v0.3.2
| duckdb example | result |
| -------------- | ------ |
| version() | various |
"""



@_core.sql_scalar("gen_random_uuid")
def gen_random_uuid(codata: DuckdbColumn, *args):
    """Alias of uuid. Return a random uuid similar to this: eeccb8c5-9943-b2bb-bb5e-222f4e14b687.
| duckdb example | result |
| -------------- | ------ |
| gen_random_uuid() | various |
"""



@_core.sql_scalar("uuid")
def uuid(codata: DuckdbColumn, *args):
    """Return a random uuid similar to this: eeccb8c5-9943-b2bb-bb5e-222f4e14b687.
| duckdb example | result |
| -------------- | ------ |
| uuid() | various |
"""



@_core.sql_scalar("currval")
def currval(codata: DuckdbColumn, *args):
    """Return the current value of the sequence. Note that nextval must be called at least once prior to calling currval.
| duckdb example | result |
| -------------- | ------ |
| currval('my_sequence_name') | 1 |
"""



@_core.sql_scalar("nextval")
def nextval(codata: DuckdbColumn, *args):
    """Return the following value of the sequence.
| duckdb example | result |
| -------------- | ------ |
| nextval('my_sequence_name') | 2 |
"""
