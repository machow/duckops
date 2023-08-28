from siuba.sql import LazyTbl
from sqlalchemy import sql


def query_to_tbl(engine, query: str) -> LazyTbl:

    full_query = f"""
        SELECT * FROM (\n{query}\n) WHERE 1 = 0
    """

    q = engine.execute(sql.text(full_query))
    
    columns = [sql.column(k) for k in q.keys()]
    text_as_from = sql.text(query).columns(*columns).alias()

    return LazyTbl(engine, text_as_from)