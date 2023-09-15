
from __future__ import annotations

from typing import overload, TYPE_CHECKING
from duckops.proto import create_generic, register_agg
from duckops.prototypes import *

if TYPE_CHECKING:
    from typing import overload as create_generic



__all__ = (
    "age",
    "century",
    "current_date",
    "current_localtimestamp",
    "date_diff",
    "date_part",
    "date_sub",
    "date_trunc",
    "datediff",
    "datepart",
    "datesub",
    "datetrunc",
    "day",
    "dayname",
    "dayofmonth",
    "dayofweek",
    "dayofyear",
    "decade",
    "epoch",
    "epoch_ms",
    "era",
    "generate_series",
    "get_current_time",
    "get_current_timestamp",
    "hour",
    "isodow",
    "isoyear",
    "last_day",
    "make_date",
    "make_time",
    "make_timestamp",
    "make_timestamptz",
    "microsecond",
    "millennium",
    "millisecond",
    "minute",
    "month",
    "monthname",
    "now",
    "quarter",
    "range",
    "second",
    "strftime",
    "strptime",
    "time_bucket",
    "timezone",
    "timezone_hour",
    "timezone_minute",
    "to_days",
    "to_hours",
    "to_microseconds",
    "to_milliseconds",
    "to_minutes",
    "to_months",
    "to_seconds",
    "to_timestamp",
    "to_years",
    "today",
    "transaction_timestamp",
    "week",
    "weekday",
    "weekofyear",
    "year",
    "yearweek"
)


@overload
def age(col0: DatetimeLike, col1: DatetimeLike) -> DatetimeLike: ...

@create_generic
def age(col0: DatetimeLike) -> DatetimeLike:
    """Subtract arguments, resulting in the time difference between the two timestamps

    | duckdb example | result |
    | -------------- | ------ |
    | age(TIMESTAMP '2001-04-10', TIMESTAMP '1992-09-20') | 8 years 6 months 20 days |


    """


@create_generic
def century(col0: DatetimeLike) -> NumberLike:
    """Extracts the century of a timestamp

    | duckdb example | result |
    | -------------- | ------ |
    | century(TIMESTAMP '1992-03-22') | 20 |


    """


@create_generic
def current_date() -> DatetimeLike:
    """Current date (at start of current transaction)

    | duckdb example | result |
    | -------------- | ------ |
    | current_date | 2022-10-08 |


    """


@create_generic
def current_localtimestamp() -> DatetimeLike:
    """Returns a TIMESTAMP whose GMT bin values correspond to local date and time in the current time zone.

    | duckdb example | result |
    | -------------- | ------ |
    | current_localtimestamp() | 2022-12-17 08:47:56.497 |


    """


@create_generic
def date_diff(col0: StringLike, col1: DatetimeLike, col2: DatetimeLike) -> NumberLike:
    """The number of partition boundaries between the dates

    | duckdb example | result |
    | -------------- | ------ |
    | date_diff('month', DATE '1992-09-15', DATE '1992-11-14') | 2 |


    """


@overload
def date_part(col0: list[StringLike], col1: DatetimeLike) -> StructLike: ...

@create_generic
def date_part(col0: StringLike, col1: DatetimeLike) -> NumberLike:
    """Get the subfield (equivalent to extract)

    | duckdb example | result |
    | -------------- | ------ |
    | date_part('year', DATE '1992-09-20') | 1992 |


    """


@create_generic
def date_sub(col0: StringLike, col1: DatetimeLike, col2: DatetimeLike) -> NumberLike:
    """The number of complete partitions between the dates

    | duckdb example | result |
    | -------------- | ------ |
    | date_sub('month', DATE '1992-09-15', DATE '1992-11-14') | 1 |


    """


@create_generic
def date_trunc(col0: StringLike, col1: DatetimeLike) -> DatetimeLike:
    """Truncate to specified precision

    | duckdb example | result |
    | -------------- | ------ |
    | date_trunc('month', DATE '1992-03-07') | 1992-03-01 |


    """


@create_generic
def datediff(col0: StringLike, col1: DatetimeLike, col2: DatetimeLike) -> NumberLike:
    """Alias of date_diff. The number of partition boundaries between the dates

    | duckdb example | result |
    | -------------- | ------ |
    | datediff('month', DATE '1992-09-15', DATE '1992-11-14') | 2 |


    """


@overload
def datepart(col0: list[StringLike], col1: DatetimeLike) -> StructLike: ...

@create_generic
def datepart(col0: StringLike, col1: DatetimeLike) -> NumberLike:
    """Alias of date_part. Get the subfield (equivalent to extract)

    | duckdb example | result |
    | -------------- | ------ |
    | datepart('year', DATE '1992-09-20') | 1992 |


    """


@create_generic
def datesub(col0: StringLike, col1: DatetimeLike, col2: DatetimeLike) -> NumberLike:
    """Alias of date_sub. The number of complete partitions between the dates

    | duckdb example | result |
    | -------------- | ------ |
    | datesub('month', DATE '1992-09-15', DATE '1992-11-14') | 1 |


    """


@create_generic
def datetrunc(col0: StringLike, col1: DatetimeLike) -> DatetimeLike:
    """Alias of date_trunc. Truncate to specified precision

    | duckdb example | result |
    | -------------- | ------ |
    | datetrunc('month', DATE '1992-03-07') | 1992-03-01 |


    """


@create_generic
def day(col0: DatetimeLike) -> NumberLike:
    """Day

    | duckdb example | result |
    | -------------- | ------ |
    | day(date '1992-02-15') | 15 |


    """


@create_generic
def dayname(col0: DatetimeLike) -> StringLike:
    """The (English) name of the weekday

    | duckdb example | result |
    | -------------- | ------ |
    | dayname(DATE '1992-09-20') | Sunday |


    """


@create_generic
def dayofmonth(col0: DatetimeLike) -> NumberLike:
    """Day (synonym)

    | duckdb example | result |
    | -------------- | ------ |
    | dayofmonth(date '1992-02-15') | 15 |


    """


@create_generic
def dayofweek(col0: DatetimeLike) -> NumberLike:
    """Numeric weekday (Sunday = 0, Saturday = 6)

    | duckdb example | result |
    | -------------- | ------ |
    | dayofweek(date '1992-02-15') | 6 |


    """


@create_generic
def dayofyear(col0: DatetimeLike) -> NumberLike:
    """Numeric ISO weekday (Monday = 1, Sunday = 7)

    | duckdb example | result |
    | -------------- | ------ |
    | isodow(date '1992-02-15') | 46 |


    """


@create_generic
def decade(col0: DatetimeLike) -> NumberLike:
    """Decade (year / 10)

    | duckdb example | result |
    | -------------- | ------ |
    | decade(date '1992-02-15') | 199 |


    """


@create_generic
def epoch(col0: DatetimeLike) -> NumberLike:
    """Converts a timestamp to the seconds since the epoch

    | duckdb example | result |
    | -------------- | ------ |
    | epoch('2022-11-07 08:43:04'::TIMESTAMP); | 1667810584 |


    """


@create_generic
def epoch_ms(col0: NumberLike) -> DatetimeLike:
    """Converts ms since epoch to a timestamp

    | duckdb example | result |
    | -------------- | ------ |
    | epoch_ms(701222400000) | 1992-03-22 00:00:00 |


    """


@create_generic
def era(col0: DatetimeLike) -> NumberLike:
    """Calendar era

    | duckdb example | result |
    | -------------- | ------ |
    | era(date '0044-03-15 (BC)') | 0 |


    """


@overload
def generate_series(col0: NumberLike, col1: NumberLike) -> list[NumberLike]: ...

@overload
def generate_series(col0: NumberLike, col1: NumberLike, col2: NumberLike) -> list[NumberLike]: ...

@overload
def generate_series(col0: DatetimeLike, col1: DatetimeLike, col2: DatetimeLike) -> list[DatetimeLike]: ...

@create_generic
def generate_series(col0: NumberLike) -> list[NumberLike]:
    """Generate a table of timestamps in the closed range, stepping by the interval

    | duckdb example | result |
    | -------------- | ------ |
    | generate_series(TIMESTAMP '2001-04-10', TIMESTAMP '2001-04-11', INTERVAL 30 MINUTE) | nan |


    """


@create_generic
def get_current_time() -> DatetimeLike:
    """Current time (start of current transaction)

    | duckdb example | result |
    | -------------- | ------ |
    | nan | nan |


    """


@create_generic
def get_current_timestamp() -> DatetimeLike:
    """Current date and time (start of current transaction)

    | duckdb example | result |
    | -------------- | ------ |
    | get_current_timestamp() | 2022-10-08 12:44:46.122-07 |


    """


@create_generic
def hour(col0: DatetimeLike) -> NumberLike:
    """Hours

    | duckdb example | result |
    | -------------- | ------ |
    | hour(timestamp '2021-08-03 11:59:44.123456') | 11 |


    """


@create_generic
def isodow(col0: DatetimeLike) -> NumberLike:
    """Numeric ISO weekday (Monday = 1, Sunday = 7)

    | duckdb example | result |
    | -------------- | ------ |
    | isodow(date '1992-02-15') | 6 |


    """


@create_generic
def isoyear(col0: DatetimeLike) -> NumberLike:
    """ISO Year number (Starts on Monday of week containing Jan 4th)

    | duckdb example | result |
    | -------------- | ------ |
    | isoyear(date '2022-01-01') | 2021 |


    """


@create_generic
def last_day(col0: DatetimeLike) -> DatetimeLike:
    """The last day of the corresponding month in the date

    | duckdb example | result |
    | -------------- | ------ |
    | last_day(DATE '1992-09-20') | 1992-09-30 |


    """


@overload
def make_date(col0: Any) -> DatetimeLike: ...

@create_generic
def make_date(col0: NumberLike, col1: NumberLike, col2: NumberLike) -> DatetimeLike:
    """The date for the given parts

    | duckdb example | result |
    | -------------- | ------ |
    | make_date(1992, 9, 20) | 1992-09-20 |


    """


@create_generic
def make_time(col0: NumberLike, col1: NumberLike, col2: NumberLike) -> DatetimeLike:
    """The time for the given parts

    | duckdb example | result |
    | -------------- | ------ |
    | make_time(13, 34, 27.123456) | 13:34:27.123456 |


    """


@create_generic
def make_timestamp(col0: NumberLike, col1: NumberLike, col2: NumberLike, col3: NumberLike, col4: NumberLike, col5: NumberLike) -> DatetimeLike:
    """The timestamp for the given parts

    | duckdb example | result |
    | -------------- | ------ |
    | make_timestamp(1992, 9, 20, 13, 34, 27.123456) | 1992-09-20 13:34:27.123456 |


    """


@overload
def make_timestamptz(col0: NumberLike, col1: NumberLike, col2: NumberLike, col3: NumberLike, col4: NumberLike, col5: NumberLike, col6: StringLike) -> DatetimeLike: ...

@create_generic
def make_timestamptz(col0: NumberLike, col1: NumberLike, col2: NumberLike, col3: NumberLike, col4: NumberLike, col5: NumberLike) -> DatetimeLike:
    """The timestamp with time zone for the given parts in the current time zone

    | duckdb example | result |
    | -------------- | ------ |
    | make_timestamptz(1992, 9, 20, 13, 34, 27.123456) | 1992-09-20 13:34:27.123456-07 |


    """


@create_generic
def microsecond(col0: DatetimeLike) -> NumberLike:
    """Sub-minute microseconds

    | duckdb example | result |
    | -------------- | ------ |
    | microsecond(timestamp '2021-08-03 11:59:44.123456') | 44123456 |


    """


@create_generic
def millennium(col0: DatetimeLike) -> NumberLike:
    """Millennium

    | duckdb example | result |
    | -------------- | ------ |
    | millennium(date '1992-02-15') | 2 |


    """


@create_generic
def millisecond(col0: DatetimeLike) -> NumberLike:
    """Sub-minute milliseconds

    | duckdb example | result |
    | -------------- | ------ |
    | millisecond(timestamp '2021-08-03 11:59:44.123456') | 44123 |


    """


@create_generic
def minute(col0: DatetimeLike) -> NumberLike:
    """Minutes

    | duckdb example | result |
    | -------------- | ------ |
    | minute(timestamp '2021-08-03 11:59:44.123456') | 59 |


    """


@create_generic
def month(col0: DatetimeLike) -> NumberLike:
    """Month

    | duckdb example | result |
    | -------------- | ------ |
    | month(date '1992-02-15') | 2 |


    """


@create_generic
def monthname(col0: DatetimeLike) -> StringLike:
    """The (English) name of the month

    | duckdb example | result |
    | -------------- | ------ |
    | monthname(DATE '1992-09-20') | September |


    """


@create_generic
def now() -> DatetimeLike:
    """Current date and time (start of current transaction)

    | duckdb example | result |
    | -------------- | ------ |
    | now() | 2022-10-08 12:44:46.122-07 |


    """


@create_generic
def quarter(col0: DatetimeLike) -> NumberLike:
    """Quarter

    | duckdb example | result |
    | -------------- | ------ |
    | quarter(date '1992-02-15') | 1 |


    """


@overload
def range(col0: NumberLike, col1: NumberLike) -> list[NumberLike]: ...

@overload
def range(col0: NumberLike, col1: NumberLike, col2: NumberLike) -> list[NumberLike]: ...

@overload
def range(col0: DatetimeLike, col1: DatetimeLike, col2: DatetimeLike) -> list[DatetimeLike]: ...

@create_generic
def range(col0: NumberLike) -> list[NumberLike]:
    """Generate a table of timestamps in the half open range, stepping by the interval

    | duckdb example | result |
    | -------------- | ------ |
    | range(TIMESTAMP '2001-04-10', TIMESTAMP '2001-04-11', INTERVAL 30 MINUTE) | nan |


    """


@create_generic
def second(col0: DatetimeLike) -> NumberLike:
    """Seconds

    | duckdb example | result |
    | -------------- | ------ |
    | second(timestamp '2021-08-03 11:59:44.123456') | 44 |


    """


@overload
def strftime(col0: StringLike, col1: DatetimeLike) -> StringLike: ...

@create_generic
def strftime(col0: DatetimeLike, col1: StringLike) -> StringLike:
    """Converts a date to a string according to the format string

    | duckdb example | result |
    | -------------- | ------ |
    | strftime(date '1992-01-01', '%a, %-d %B %Y') | Wed, 1 January 1992 |


    """


@create_generic
def strptime(col0: StringLike, col1: StringLike) -> DatetimeLike:
    """Converts string to timestamp according to the format string

    | duckdb example | result |
    | -------------- | ------ |
    | strptime('Wed, 1 January 1992 - 08:38:40 PM', '%a, %-d %B %Y - %I:%M:%S %p') | 1992-01-01 20:38:40 |


    """


@overload
def time_bucket(col0: DatetimeLike, col1: DatetimeLike, col2: DatetimeLike) -> DatetimeLike: ...

@overload
def time_bucket(col0: DatetimeLike, col1: DatetimeLike, col2: StringLike) -> DatetimeLike: ...

@create_generic
def time_bucket(col0: DatetimeLike, col1: DatetimeLike) -> DatetimeLike:
    """Truncate date by the specified interval bucket_width. Buckets are aligned relative to origin date. origin defaults to 2000-01-03 for buckets that don’t include a month or year interval, and to 2000-01-01 for month and year buckets.

    | duckdb example | result |
    | -------------- | ------ |
    | time_bucket(INTERVAL '2 weeks', DATE '1992-04-20', DATE '1992-04-01') | 1992-04-15 |


    """


@overload
def timezone(col0: StringLike, col1: DatetimeLike) -> DatetimeLike: ...

@create_generic
def timezone(col0: DatetimeLike) -> NumberLike:
    """Use the date parts of the timestamp in GMT to construct a timestamp in the given time zone. Effectively, the argument is a “local” time.

    | duckdb example | result |
    | -------------- | ------ |
    | timezone('America/Denver', TIMESTAMP '2001-02-16 20:38:40') | 2001-02-16 19:38:40-08 |


    """


@create_generic
def timezone_hour(col0: DatetimeLike) -> NumberLike:
    """Time zone offset hour portion

    | duckdb example | result |
    | -------------- | ------ |
    | timezone_hour(date '1992-02-15') | 0 |


    """


@create_generic
def timezone_minute(col0: DatetimeLike) -> NumberLike:
    """Time zone offset minutes portion

    | duckdb example | result |
    | -------------- | ------ |
    | timezone_minute(date '1992-02-15') | 0 |


    """


@create_generic
def to_days(col0: NumberLike) -> DatetimeLike:
    """Construct a day interval

    | duckdb example | result |
    | -------------- | ------ |
    | to_days(5) | INTERVAL 5 DAY |


    """


@create_generic
def to_hours(col0: NumberLike) -> DatetimeLike:
    """Construct a hour interval

    | duckdb example | result |
    | -------------- | ------ |
    | to_hours(5) | INTERVAL 5 HOUR |


    """


@create_generic
def to_microseconds(col0: NumberLike) -> DatetimeLike:
    """Construct a microsecond interval

    | duckdb example | result |
    | -------------- | ------ |
    | to_microseconds(5) | INTERVAL 5 MICROSECOND |


    """


@create_generic
def to_milliseconds(col0: NumberLike) -> DatetimeLike:
    """Construct a millisecond interval

    | duckdb example | result |
    | -------------- | ------ |
    | to_milliseconds(5) | INTERVAL 5 MILLISECOND |


    """


@create_generic
def to_minutes(col0: NumberLike) -> DatetimeLike:
    """Construct a minute interval

    | duckdb example | result |
    | -------------- | ------ |
    | to_minutes(5) | INTERVAL 5 MINUTE |


    """


@create_generic
def to_months(col0: NumberLike) -> DatetimeLike:
    """Construct a month interval

    | duckdb example | result |
    | -------------- | ------ |
    | to_months(5) | INTERVAL 5 MONTH |


    """


@create_generic
def to_seconds(col0: NumberLike) -> DatetimeLike:
    """Construct a second interval

    | duckdb example | result |
    | -------------- | ------ |
    | to_seconds(5) | INTERVAL 5 SECOND |


    """


@create_generic
def to_timestamp(col0: NumberLike) -> DatetimeLike:
    """Converts sec since epoch to a timestamp

    | duckdb example | result |
    | -------------- | ------ |
    | to_timestamp(701222400) | 1992-03-22 00:00:00 |


    """


@create_generic
def to_years(col0: NumberLike) -> DatetimeLike:
    """Construct a year interval

    | duckdb example | result |
    | -------------- | ------ |
    | to_years(5) | INTERVAL 5 YEAR |


    """


@create_generic
def today() -> DatetimeLike:
    """Current date (start of current transaction)

    | duckdb example | result |
    | -------------- | ------ |
    | today() | 2022-10-08 |


    """


@create_generic
def transaction_timestamp() -> DatetimeLike:
    """Current date and time (start of current transaction)

    | duckdb example | result |
    | -------------- | ------ |
    | transaction_timestamp() | 2022-10-08 12:44:46.122-07 |


    """


@create_generic
def week(col0: DatetimeLike) -> NumberLike:
    """ISO Week

    | duckdb example | result |
    | -------------- | ------ |
    | week(date '1992-02-15') | 7 |


    """


@create_generic
def weekday(col0: DatetimeLike) -> NumberLike:
    """Numeric weekday synonym (Sunday = 0, Saturday = 6)

    | duckdb example | result |
    | -------------- | ------ |
    | weekday(date '1992-02-15') | 6 |


    """


@create_generic
def weekofyear(col0: DatetimeLike) -> NumberLike:
    """ISO Week (synonym)

    | duckdb example | result |
    | -------------- | ------ |
    | weekofyear(date '1992-02-15') | 7 |


    """


@create_generic
def year(col0: DatetimeLike) -> NumberLike:
    """Year

    | duckdb example | result |
    | -------------- | ------ |
    | year(date '1992-02-15') | 1992 |


    """


@create_generic
def yearweek(col0: DatetimeLike) -> NumberLike:
    """BIGINT of combined ISO Year number and 2-digit version of ISO Week number

    | duckdb example | result |
    | -------------- | ------ |
    | yearweek(date '1992-02-15') | 199207 |


    """