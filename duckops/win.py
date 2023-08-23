
#from . import _core
from .proto import create_generic, sql_win, NoArgOver
from siuba.sql import translate as _tr


@sql_win(_tr.RankOver)
@create_generic
def cume_dist(*args):
    """The cumulative distribution: (number of partition rows preceding or peer with current row) / total partition rows.
| duckdb example | result |
| -------------- | ------ |
| cume_dist() | nan |
"""



@sql_win(_tr.RankOver)
@create_generic
def dense_rank(*args):
    """The rank of the current row without gaps; this function counts peer groups.
| duckdb example | result |
| -------------- | ------ |
| dense_rank() | nan |
"""


@sql_win(_tr.RankOver)
@create_generic
def first_value(*args):
    """Returns expr evaluated at the row that is the first row of the window frame.
| duckdb example | result |
| -------------- | ------ |
| first_value(column) | nan |
"""



@sql_win(_tr.CumlOver)
@create_generic
def lag(*args):
    """Returns expr evaluated at the row that is offset rows before the current row within the partition; if there is no such row, instead return default (which must be of the same type as expr). Both offset and default are evaluated with respect to the current row. If omitted, offset defaults to 1 and default to null.
| duckdb example | result |
| -------------- | ------ |
| lag(column, 3, 0) | nan |
"""



@sql_win(_tr.CumlOver)
@create_generic
def last_value(*args):
    """Returns expr evaluated at the row that is the last row of the window frame.
| duckdb example | result |
| -------------- | ------ |
| last_value(column) | nan |
"""


@sql_win(_tr.CumlOver)
@create_generic
def lead(*args):
    """Returns expr evaluated at the row that is offset rows after the current row within the partition; if there is no such row, instead return default (which must be of the same type as expr). Both offset and default are evaluated with respect to the current row. If omitted, offset defaults to 1 and default to null.
| duckdb example | result |
| -------------- | ------ |
| lead(column, 3, 0) | nan |
"""


@sql_win(_tr.CumlOver)
@create_generic
def nth_value(*args):
    """Returns expr evaluated at the nth row of the window frame (counting from 1); null if no such row.
| duckdb example | result |
| -------------- | ------ |
| nth_value(column, 2) | nan |
"""


@sql_win(_tr.RankOver)
@create_generic
def ntile(*args):
    """An integer ranging from 1 to the argument value, dividing the partition as equally as possible.
| duckdb example | result |
| -------------- | ------ |
| ntile(4) | nan |
"""


@sql_win(_tr.RankOver)
@create_generic
def percent_rank(*args):
    """The relative rank of the current row: (rank() - 1) / (total partition rows - 1).
| duckdb example | result |
| -------------- | ------ |
| percent_rank() | nan |
"""


@sql_win(_tr.RankOver)
@create_generic
def rank(*args):
    """The rank of the current row with gaps; same as row_number of its first peer.
| duckdb example | result |
| -------------- | ------ |
| rank() | nan |
"""


@sql_win(NoArgOver)
@create_generic
def row_number(*args):
    """The number of the current row within the partition, counting from 1.
| duckdb example | result |
| -------------- | ------ |
| row_number() | nan |
"""
