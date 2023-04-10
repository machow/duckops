
from . import _core
from siuba.sql import translate as _tr
from siuba.sql.dialects.duckdb import DuckdbColumn, DuckdbColumnAgg

@_core.sql_win("cume_dist", _tr.RankOver)
def cume_dist(codata: DuckdbColumn, *args):
    """The cumulative distribution: (number of partition rows preceding or peer with current row) / total partition rows.
| duckdb example | result |
| -------------- | ------ |
| cume_dist() | nan |
"""



@_core.sql_win("dense_rank", _tr.RankOver)
def dense_rank(codata: DuckdbColumn, *args):
    """The rank of the current row without gaps; this function counts peer groups.
| duckdb example | result |
| -------------- | ------ |
| dense_rank() | nan |
"""



@_core.sql_win("first_value", _tr.CumlOver)
def first_value(codata: DuckdbColumn, *args):
    """Returns expr evaluated at the row that is the first row of the window frame.
| duckdb example | result |
| -------------- | ------ |
| first_value(column) | nan |
"""



@_core.sql_win("lag", _tr.CumlOver)
def lag(codata: DuckdbColumn, *args):
    """Returns expr evaluated at the row that is offset rows before the current row within the partition; if there is no such row, instead return default (which must be of the same type as expr). Both offset and default are evaluated with respect to the current row. If omitted, offset defaults to 1 and default to null.
| duckdb example | result |
| -------------- | ------ |
| lag(column, 3, 0) | nan |
"""



@_core.sql_win("last_value", _tr.CumlOver)
def last_value(codata: DuckdbColumn, *args):
    """Returns expr evaluated at the row that is the last row of the window frame.
| duckdb example | result |
| -------------- | ------ |
| last_value(column) | nan |
"""



@_core.sql_win("lead", _tr.CumlOver)
def lead(codata: DuckdbColumn, *args):
    """Returns expr evaluated at the row that is offset rows after the current row within the partition; if there is no such row, instead return default (which must be of the same type as expr). Both offset and default are evaluated with respect to the current row. If omitted, offset defaults to 1 and default to null.
| duckdb example | result |
| -------------- | ------ |
| lead(column, 3, 0) | nan |
"""



@_core.sql_win("nth_value", _tr.CumlOver)
def nth_value(codata: DuckdbColumn, *args):
    """Returns expr evaluated at the nth row of the window frame (counting from 1); null if no such row.
| duckdb example | result |
| -------------- | ------ |
| nth_value(column, 2) | nan |
"""



@_core.sql_win("ntile", _tr.RankOver)
def ntile(codata: DuckdbColumn, *args):
    """An integer ranging from 1 to the argument value, dividing the partition as equally as possible.
| duckdb example | result |
| -------------- | ------ |
| ntile(4) | nan |
"""



@_core.sql_win("percent_rank", _tr.RankOver)
def percent_rank(codata: DuckdbColumn, *args):
    """The relative rank of the current row: (rank() - 1) / (total partition rows - 1).
| duckdb example | result |
| -------------- | ------ |
| percent_rank() | nan |
"""



@_core.sql_win("rank", _tr.RankOver)
def rank(codata: DuckdbColumn, *args):
    """The rank of the current row with gaps; same as row_number of its first peer.
| duckdb example | result |
| -------------- | ------ |
| rank() | nan |
"""



@_core.sql_win("row_number", _core.NoArgOver)
def row_number(codata: DuckdbColumn, *args):
    """The number of the current row within the partition, counting from 1.
| duckdb example | result |
| -------------- | ------ |
| row_number() | nan |
"""
