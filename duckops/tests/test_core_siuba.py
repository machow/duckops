# across
# some aggregates
# tbl creation

import pandas as pd

from duckops.all import string_agg, string_split, contains, list_pack, list_transform
from duckops.syntax import lam, extract, list_comp
from duckops.helpers import tbl_empty

from siuba import tbl, mutate, summarize, _, across, Fx, collect
from sqlalchemy import create_engine


engine = create_engine("duckdb:///:memory:")
df = pd.DataFrame({"x": ["a", "b"], "y": ["c", "d"]})
tbl_df = tbl(engine, "df", df)


def test_list_comp():
    res = (
        tbl_empty()
        >> mutate(
            # TODO: should we be eager by default? wrapping in Lazy seems annoying
            ships=list_pack("a b c", "d e f"),
            split=list_comp(_.ships, string_split(Fx, " "), contains(Fx, "a")),
        )
        >> collect(_)
    )

    assert res["split"][0] == [["a", "b", "c"]]


def test_lam():
    res = (
        tbl_empty()
        >> mutate(
            name=list_pack("a b c", "d e f"),
            short_name=list_transform(_["name"], lam(string_split(Fx, " "))),
        )
        >> collect(_)
    )

    assert res["short_name"][0] == [["a", "b", "c"], ["d", "e", "f"]]


def test_extract():
    res = (
        tbl_empty()
        >> mutate(
            name=list_pack("one", "two", "three"),
            first=extract(_["name"], 1),
        )
        >> collect()
    )

    assert res["first"][0] == "one"


def test_aggregate():
    res = tbl_df >> summarize(agged=string_agg(_.x, ",")) >> collect(_)

    assert res["agged"][0] == "a,b"


def test_aggregate_across():
    res = tbl_df >> summarize(across(_.contains(""), string_agg(Fx, ","))) >> collect(_)

    assert res["x"][0] == "a,b"
    assert res["y"][0] == "c,d"
