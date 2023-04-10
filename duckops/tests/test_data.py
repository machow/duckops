import pytest

from duckops._types import Interval

@pytest.mark.parametrize("n, unit", [
    (1, "years"),
])
def test_interval_construct(n, unit):
    interval = Interval(n, unit)