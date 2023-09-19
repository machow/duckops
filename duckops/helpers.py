from __future__ import annotations

from siuba import tbl
from siuba.sql import LazyTbl
from sqlalchemy import sql
from sqlalchemy import create_engine


def to_duckdb(data, name: str | None = None, engine=None):
    if engine is None:
        engine = create_engine("duckdb:///:memory:")

    if name is not None:
        return tbl(engine, name, data)

    return tbl(engine, data)


def query_to_tbl(engine, query: str) -> LazyTbl:
    """Create a lazy table from a query string."""

    full_query = f"""
        SELECT * FROM (\n{query}\n) WHERE 1 = 0
    """

    with engine.begin() as conn:
        q = conn.execute(sql.text(full_query))

        columns = [sql.column(k) for k in q.keys()]
        text_as_from = sql.text(query).columns(*columns).alias()

        return LazyTbl(engine, text_as_from)


def tbl_empty(engine=None) -> LazyTbl:
    """Create a lazy table with no FROM clause.

    This is useful for quick test queries and examples.
    """

    if engine is None:
        engine = create_engine("duckdb:///:memory:")

    return LazyTbl(engine, sql.selectable.FromClause())
