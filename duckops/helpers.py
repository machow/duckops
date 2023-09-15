from siuba.sql import LazyTbl
from sqlalchemy import sql
from sqlalchemy import create_engine


def query_to_tbl(engine, query: str) -> LazyTbl:

    full_query = f"""
        SELECT * FROM (\n{query}\n) WHERE 1 = 0
    """

    q = engine.execute(sql.text(full_query))
    
    columns = [sql.column(k) for k in q.keys()]
    text_as_from = sql.text(query).columns(*columns).alias()

    return LazyTbl(engine, text_as_from)


def tbl_empty(engine = None) -> LazyTbl:
    if engine is None:
        engine = create_engine("duckdb:///:memory:")

    return LazyTbl(engine, sql.selectable.FromClause())