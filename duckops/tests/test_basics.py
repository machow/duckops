import datetime
import pandas as pd
from pandas.testing import assert_series_equal, assert_frame_equal
import duckdb
import pytest

from duckops.prototypes import Interval
from duckops.str import concat
from duckops.dt import date_part, today
from duckops.nested import struct_pack
from duckops.win import row_number

from siuba import _, tbl, mutate, collect
from siuba.siu import strip_symbolic, Symbolic
from sqlalchemy import create_engine


con = duckdb.connect()

engine = create_engine("duckdb:///:memory:")

df = pd.DataFrame({
    "part": ["year", "month"],
    "date": pd.to_datetime(["2022-01-01", "2023-02-03"]),
    "x": ["a", "b"],
    "y": ["c", "d"]
})
tbl_df = tbl(engine, "df", df)


def assert_is_equal(res, dst):
    if isinstance(dst, pd.Series):
        assert_series_equal(res, dst)
    elif isinstance(dst, pd.DataFrame):
        assert_frame_equal(res, dst)
    else:
        assert res == dst


@pytest.mark.parametrize("x, y, dst", [
    (df["part"], df["date"], pd.Series([2022, 2])),
    (df["part"], Interval(3, "years"), pd.Series([3, 0])),
    ("year", df["date"], pd.Series([2022, 2023])),
    ("year", Interval(3, "years"), 3)
])
def test_date_part(x, y, dst):
    res = date_part(x, y)

    assert isinstance(res, type(dst))
    assert_is_equal(res, dst)


@pytest.mark.parametrize("x, dst", [
    ("a", "a"),
    (pd.Series(["a", "x"]), pd.Series(["a", "x"]))
])
def test_func_varargs_1(x, dst):
    res = concat(x)

    assert isinstance(res, type(dst))
    assert_is_equal(x, dst)


@pytest.mark.parametrize("x,y,z,dst", [
    ("a", "-", "b", "a-b"),
    (pd.Series(["a", "x"]), "-", pd.Series(["b", "c"]), pd.Series(["a-b", "x-c"])),
    ("-", pd.Series(["a", "x"]), pd.Series(["b", "c"]), pd.Series(["-ab", "-xc"])),
])
def test_func_varargs_3(x, y, z, dst):
    res = concat(x, y, z)

    assert isinstance(res, type(dst))
    assert_is_equal(res, dst)


def test_assign_equal_syntax():
    res = struct_pack(a = 1, b = "x", c = Interval(2, "days"))

    assert res == {'a': 1, 'b': 'x', 'c': datetime.timedelta(days=2)}


def test_func_argless():
    res = today()
    isinstance(res, datetime.datetime)


def test_func_argless_lazy():
    res = today(_)
    assert isinstance(res, Symbolic)

    # TODO call it


def test_func_win():
    res = row_number(df["x"])
    assert res.tolist() == [1, 2]


def test_func_siuba_lazy():
    res1 = tbl_df >> mutate(res = date_part(_.part, _.date)) >> collect()
    res2 = df >> mutate(res = date_part(_.part, _.date))

    assert_is_equal(res1, res2)