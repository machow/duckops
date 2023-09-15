from sqlalchemy import DateTime, Date


# implement literal rendering of datetime.datetime -------
# this patch isn't needed in sqlalchemy 2.0+
def _dt_literal_processor(self, dialect):
    def process(value):
        return f"Timestamp '{str(value)}'"

    return process


def _d_literal_processor(self, dialect):
    def process(value):
        return f"DATE '{str(value)}'"

    return process


DateTime.literal_processor = _dt_literal_processor
Date.literal_processor = _d_literal_processor
