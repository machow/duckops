
from . import _core
from siuba.sql import translate as _tr
from siuba.sql.dialects.duckdb import DuckdbColumn, DuckdbColumnAgg

@_core.sql_scalar("age")
def age(codata: DuckdbColumn, *args):
    """Subtract arguments, resulting in the time difference between the two timestamps
| duckdb example | result |
| -------------- | ------ |
| age(TIMESTAMP '2001-04-10', TIMESTAMP '1992-09-20') | 8 years 6 months 20 days |
"""



@_core.sql_scalar("date_diff")
def date_diff(codata: DuckdbColumn, *args):
    """The number of partition boundaries between the dates
| duckdb example | result |
| -------------- | ------ |
| date_diff('month', DATE '1992-09-15', DATE '1992-11-14') | 2 |
"""



@_core.sql_scalar("datediff")
def datediff(codata: DuckdbColumn, *args):
    """Alias of date_diff. The number of partition boundaries between the dates
| duckdb example | result |
| -------------- | ------ |
| datediff('month', DATE '1992-09-15', DATE '1992-11-14') | 2 |
"""



@_core.sql_scalar("year")
def year(codata: DuckdbColumn, *args):
    """Year
| duckdb example | result |
| -------------- | ------ |
| year(date '1992-02-15') | 1992 |
"""



@_core.sql_scalar("month")
def month(codata: DuckdbColumn, *args):
    """Month
| duckdb example | result |
| -------------- | ------ |
| month(date '1992-02-15') | 2 |
"""



@_core.sql_scalar("day")
def day(codata: DuckdbColumn, *args):
    """Day
| duckdb example | result |
| -------------- | ------ |
| day(date '1992-02-15') | 15 |
"""



@_core.sql_scalar("decade")
def decade(codata: DuckdbColumn, *args):
    """Decade (year / 10)
| duckdb example | result |
| -------------- | ------ |
| decade(date '1992-02-15') | 199 |
"""



@_core.sql_scalar("century")
def century(codata: DuckdbColumn, *args):
    """Extracts the century of a timestamp
| duckdb example | result |
| -------------- | ------ |
| century(TIMESTAMP '1992-03-22') | 20 |
"""



@_core.sql_scalar("millennium")
def millennium(codata: DuckdbColumn, *args):
    """Millennium
| duckdb example | result |
| -------------- | ------ |
| millennium(date '1992-02-15') | 2 |
"""



@_core.sql_scalar("quarter")
def quarter(codata: DuckdbColumn, *args):
    """Quarter
| duckdb example | result |
| -------------- | ------ |
| quarter(date '1992-02-15') | 1 |
"""



@_core.sql_scalar("dayofweek")
def dayofweek(codata: DuckdbColumn, *args):
    """Numeric weekday (Sunday = 0, Saturday = 6)
| duckdb example | result |
| -------------- | ------ |
| dayofweek(date '1992-02-15') | 6 |
"""



@_core.sql_scalar("isodow")
def isodow(codata: DuckdbColumn, *args):
    """Numeric ISO weekday (Monday = 1, Sunday = 7)
| duckdb example | result |
| -------------- | ------ |
| isodow(date '1992-02-15') | 6 |
"""



@_core.sql_scalar("dayofyear")
def dayofyear(codata: DuckdbColumn, *args):
    """Numeric ISO weekday (Monday = 1, Sunday = 7)
| duckdb example | result |
| -------------- | ------ |
| isodow(date '1992-02-15') | 46 |
"""



@_core.sql_scalar("week")
def week(codata: DuckdbColumn, *args):
    """ISO Week
| duckdb example | result |
| -------------- | ------ |
| week(date '1992-02-15') | 7 |
"""



@_core.sql_scalar("isoyear")
def isoyear(codata: DuckdbColumn, *args):
    """ISO Year number (Starts on Monday of week containing Jan 4th)
| duckdb example | result |
| -------------- | ------ |
| isoyear(date '2022-01-01') | 2021 |
"""



@_core.sql_scalar("era")
def era(codata: DuckdbColumn, *args):
    """Calendar era
| duckdb example | result |
| -------------- | ------ |
| era(date '0044-03-15 (BC)') | 0 |
"""



@_core.sql_scalar("timezone")
def timezone(codata: DuckdbColumn, *args):
    """Use the date parts of the timestamp in GMT to construct a timestamp in the given time zone. Effectively, the argument is a “local” time.
| duckdb example | result |
| -------------- | ------ |
| timezone('America/Denver', TIMESTAMP '2001-02-16 20:38:40') | 2001-02-16 19:38:40-08 |
"""



@_core.sql_scalar("timezone_hour")
def timezone_hour(codata: DuckdbColumn, *args):
    """Time zone offset hour portion
| duckdb example | result |
| -------------- | ------ |
| timezone_hour(date '1992-02-15') | 0 |
"""



@_core.sql_scalar("timezone_minute")
def timezone_minute(codata: DuckdbColumn, *args):
    """Time zone offset minutes portion
| duckdb example | result |
| -------------- | ------ |
| timezone_minute(date '1992-02-15') | 0 |
"""



@_core.sql_scalar("epoch")
def epoch(codata: DuckdbColumn, *args):
    """Converts a timestamp to the seconds since the epoch
| duckdb example | result |
| -------------- | ------ |
| epoch('2022-11-07 08:43:04'::TIMESTAMP); | 1667810584 |
"""



@_core.sql_scalar("microsecond")
def microsecond(codata: DuckdbColumn, *args):
    """Sub-minute microseconds
| duckdb example | result |
| -------------- | ------ |
| microsecond(timestamp '2021-08-03 11:59:44.123456') | 44123456 |
"""



@_core.sql_scalar("millisecond")
def millisecond(codata: DuckdbColumn, *args):
    """Sub-minute milliseconds
| duckdb example | result |
| -------------- | ------ |
| millisecond(timestamp '2021-08-03 11:59:44.123456') | 44123 |
"""



@_core.sql_scalar("second")
def second(codata: DuckdbColumn, *args):
    """Seconds
| duckdb example | result |
| -------------- | ------ |
| second(timestamp '2021-08-03 11:59:44.123456') | 44 |
"""



@_core.sql_scalar("minute")
def minute(codata: DuckdbColumn, *args):
    """Minutes
| duckdb example | result |
| -------------- | ------ |
| minute(timestamp '2021-08-03 11:59:44.123456') | 59 |
"""



@_core.sql_scalar("hour")
def hour(codata: DuckdbColumn, *args):
    """Hours
| duckdb example | result |
| -------------- | ------ |
| hour(timestamp '2021-08-03 11:59:44.123456') | 11 |
"""



@_core.sql_scalar("yearweek")
def yearweek(codata: DuckdbColumn, *args):
    """BIGINT of combined ISO Year number and 2-digit version of ISO Week number
| duckdb example | result |
| -------------- | ------ |
| yearweek(date '1992-02-15') | 199207 |
"""



@_core.sql_scalar("dayofmonth")
def dayofmonth(codata: DuckdbColumn, *args):
    """Day (synonym)
| duckdb example | result |
| -------------- | ------ |
| dayofmonth(date '1992-02-15') | 15 |
"""



@_core.sql_scalar("weekday")
def weekday(codata: DuckdbColumn, *args):
    """Numeric weekday synonym (Sunday = 0, Saturday = 6)
| duckdb example | result |
| -------------- | ------ |
| weekday(date '1992-02-15') | 6 |
"""



@_core.sql_scalar("weekofyear")
def weekofyear(codata: DuckdbColumn, *args):
    """ISO Week (synonym)
| duckdb example | result |
| -------------- | ------ |
| weekofyear(date '1992-02-15') | 7 |
"""



@_core.sql_scalar("last_day")
def last_day(codata: DuckdbColumn, *args):
    """The last day of the corresponding month in the date
| duckdb example | result |
| -------------- | ------ |
| last_day(DATE '1992-09-20') | 1992-09-30 |
"""



@_core.sql_scalar("monthname")
def monthname(codata: DuckdbColumn, *args):
    """The (English) name of the month
| duckdb example | result |
| -------------- | ------ |
| monthname(DATE '1992-09-20') | September |
"""



@_core.sql_scalar("dayname")
def dayname(codata: DuckdbColumn, *args):
    """The (English) name of the weekday
| duckdb example | result |
| -------------- | ------ |
| dayname(DATE '1992-09-20') | Sunday |
"""



@_core.sql_scalar("date_part")
def date_part(codata: DuckdbColumn, *args):
    """Get the subfield (equivalent to extract)
| duckdb example | result |
| -------------- | ------ |
| date_part('year', DATE '1992-09-20') | 1992 |
"""



@_core.sql_scalar("datepart")
def datepart(codata: DuckdbColumn, *args):
    """Alias of date_part. Get the subfield (equivalent to extract)
| duckdb example | result |
| -------------- | ------ |
| datepart('year', DATE '1992-09-20') | 1992 |
"""



@_core.sql_scalar("date_sub")
def date_sub(codata: DuckdbColumn, *args):
    """The number of complete partitions between the dates
| duckdb example | result |
| -------------- | ------ |
| date_sub('month', DATE '1992-09-15', DATE '1992-11-14') | 1 |
"""



@_core.sql_scalar("datesub")
def datesub(codata: DuckdbColumn, *args):
    """Alias of date_sub. The number of complete partitions between the dates
| duckdb example | result |
| -------------- | ------ |
| datesub('month', DATE '1992-09-15', DATE '1992-11-14') | 1 |
"""



@_core.sql_scalar("date_trunc")
def date_trunc(codata: DuckdbColumn, *args):
    """Truncate to specified precision
| duckdb example | result |
| -------------- | ------ |
| date_trunc('month', DATE '1992-03-07') | 1992-03-01 |
"""



@_core.sql_scalar("datetrunc")
def datetrunc(codata: DuckdbColumn, *args):
    """Alias of date_trunc. Truncate to specified precision
| duckdb example | result |
| -------------- | ------ |
| datetrunc('month', DATE '1992-03-07') | 1992-03-01 |
"""



@_core.sql_scalar("get_current_time")
def get_current_time(codata: DuckdbColumn, *args):
    """Current time (start of current transaction)
| duckdb example | result |
| -------------- | ------ |
| nan | nan |
"""



@_core.sql_scalar("today")
def today(codata: DuckdbColumn, *args):
    """Current date (start of current transaction)
| duckdb example | result |
| -------------- | ------ |
| today() | 2022-10-08 |
"""



@_core.sql_scalar("current_date")
def current_date(codata: DuckdbColumn, *args):
    """Current date (at start of current transaction)
| duckdb example | result |
| -------------- | ------ |
| current_date | 2022-10-08 |
"""



@_core.sql_scalar("now")
def now(codata: DuckdbColumn, *args):
    """Current date and time (start of current transaction)
| duckdb example | result |
| -------------- | ------ |
| now() | 2022-10-08 12:44:46.122-07 |
"""



@_core.sql_scalar("get_current_timestamp")
def get_current_timestamp(codata: DuckdbColumn, *args):
    """Current date and time (start of current transaction)
| duckdb example | result |
| -------------- | ------ |
| get_current_timestamp() | 2022-10-08 12:44:46.122-07 |
"""



@_core.sql_scalar("transaction_timestamp")
def transaction_timestamp(codata: DuckdbColumn, *args):
    """Current date and time (start of current transaction)
| duckdb example | result |
| -------------- | ------ |
| transaction_timestamp() | 2022-10-08 12:44:46.122-07 |
"""



@_core.sql_scalar("epoch_ms")
def epoch_ms(codata: DuckdbColumn, *args):
    """Converts ms since epoch to a timestamp
| duckdb example | result |
| -------------- | ------ |
| epoch_ms(701222400000) | 1992-03-22 00:00:00 |
"""



@_core.sql_scalar("to_timestamp")
def to_timestamp(codata: DuckdbColumn, *args):
    """Converts sec since epoch to a timestamp
| duckdb example | result |
| -------------- | ------ |
| to_timestamp(701222400) | 1992-03-22 00:00:00 |
"""



@_core.sql_scalar("make_date")
def make_date(codata: DuckdbColumn, *args):
    """The date for the given parts
| duckdb example | result |
| -------------- | ------ |
| make_date(1992, 9, 20) | 1992-09-20 |
"""



@_core.sql_scalar("make_time")
def make_time(codata: DuckdbColumn, *args):
    """The time for the given parts
| duckdb example | result |
| -------------- | ------ |
| make_time(13, 34, 27.123456) | 13:34:27.123456 |
"""



@_core.sql_scalar("make_timestamp")
def make_timestamp(codata: DuckdbColumn, *args):
    """The timestamp for the given parts
| duckdb example | result |
| -------------- | ------ |
| make_timestamp(1992, 9, 20, 13, 34, 27.123456) | 1992-09-20 13:34:27.123456 |
"""



@_core.sql_scalar("strftime")
def strftime(codata: DuckdbColumn, *args):
    """Converts a date to a string according to the format string
| duckdb example | result |
| -------------- | ------ |
| strftime(date '1992-01-01', '%a, %-d %B %Y') | Wed, 1 January 1992 |
"""



@_core.sql_scalar("strptime")
def strptime(codata: DuckdbColumn, *args):
    """Converts string to timestamp according to the format string
| duckdb example | result |
| -------------- | ------ |
| strptime('Wed, 1 January 1992 - 08:38:40 PM', '%a, %-d %B %Y - %I:%M:%S %p') | 1992-01-01 20:38:40 |
"""



@_core.sql_scalar("time_bucket")
def time_bucket(codata: DuckdbColumn, *args):
    """Truncate date by the specified interval bucket_width. Buckets are aligned relative to origin date. origin defaults to 2000-01-03 for buckets that don’t include a month or year interval, and to 2000-01-01 for month and year buckets.
| duckdb example | result |
| -------------- | ------ |
| time_bucket(INTERVAL '2 weeks', DATE '1992-04-20', DATE '1992-04-01') | 1992-04-15 |
"""



@_core.sql_scalar("to_years")
def to_years(codata: DuckdbColumn, *args):
    """Construct a year interval
| duckdb example | result |
| -------------- | ------ |
| to_years(5) | INTERVAL 5 YEAR |
"""



@_core.sql_scalar("to_months")
def to_months(codata: DuckdbColumn, *args):
    """Construct a month interval
| duckdb example | result |
| -------------- | ------ |
| to_months(5) | INTERVAL 5 MONTH |
"""



@_core.sql_scalar("to_days")
def to_days(codata: DuckdbColumn, *args):
    """Construct a day interval
| duckdb example | result |
| -------------- | ------ |
| to_days(5) | INTERVAL 5 DAY |
"""



@_core.sql_scalar("to_hours")
def to_hours(codata: DuckdbColumn, *args):
    """Construct a hour interval
| duckdb example | result |
| -------------- | ------ |
| to_hours(5) | INTERVAL 5 HOUR |
"""



@_core.sql_scalar("to_minutes")
def to_minutes(codata: DuckdbColumn, *args):
    """Construct a minute interval
| duckdb example | result |
| -------------- | ------ |
| to_minutes(5) | INTERVAL 5 MINUTE |
"""



@_core.sql_scalar("to_seconds")
def to_seconds(codata: DuckdbColumn, *args):
    """Construct a second interval
| duckdb example | result |
| -------------- | ------ |
| to_seconds(5) | INTERVAL 5 SECOND |
"""



@_core.sql_scalar("to_milliseconds")
def to_milliseconds(codata: DuckdbColumn, *args):
    """Construct a millisecond interval
| duckdb example | result |
| -------------- | ------ |
| to_milliseconds(5) | INTERVAL 5 MILLISECOND |
"""



@_core.sql_scalar("to_microseconds")
def to_microseconds(codata: DuckdbColumn, *args):
    """Construct a microsecond interval
| duckdb example | result |
| -------------- | ------ |
| to_microseconds(5) | INTERVAL 5 MICROSECOND |
"""



@_core.sql_scalar("current_localtimestamp")
def current_localtimestamp(codata: DuckdbColumn, *args):
    """Returns a TIMESTAMP whose GMT bin values correspond to local date and time in the current time zone.
| duckdb example | result |
| -------------- | ------ |
| current_localtimestamp() | 2022-12-17 08:47:56.497 |
"""



@_core.sql_scalar("make_timestamptz")
def make_timestamptz(codata: DuckdbColumn, *args):
    """The timestamp with time zone for the given parts in the current time zone
| duckdb example | result |
| -------------- | ------ |
| make_timestamptz(1992, 9, 20, 13, 34, 27.123456) | 1992-09-20 13:34:27.123456-07 |
"""
