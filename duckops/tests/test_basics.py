import pytest

import duckops as dop
from duckops import _types
from duckops._core import _query_call

from siuba import _
from siuba.siu import Call

import datetime
import pandas as pd

# op kind (scalar, ...) x eager
# custom data x eager
# op varieties:
#   - lazy arg is second
#   - no args
#   - TODO: dispatch any: pandas Series anywhere, Call anywhere
# op data inputs:
#   - lazy (Calls, Symbolics)
#   - external (e.g. pandas Series)
#   - built-in types
#   - duckops types
# op misuses:
#   - TODO: mix of lazy and external data
#   - TODO: mix of duckops types and external data
def test_op_no_args():
    res = dop.dt.now()
    assert isinstance(res, datetime.datetime)


def test_op_no_args_lazy():
    res = dop.dt.now(_)
    assert isinstance(res, Call)
    assert isinstance(_query_call(res), datetime.datetime)


def test_op_arg_flipped():
    res = dop.dt.date_part("year", _types.Interval(3, "years"))
    assert res == 3


def test_op_ext_data():
    col = pd.Series([pd.Timestamp("2021-01-01")])
    res = dop.dt.date_part("year", col)

    assert isinstance(res, pd.Series)