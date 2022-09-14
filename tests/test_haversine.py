import numpy as np
import pytest

from fast_haversine import haversine
from fast_haversine.slow import slow_haversine


def test_unsupported_input():
    with pytest.raises(NotImplementedError):
        haversine(1.0)


def test_with_tuple():
    res = haversine((42.3521, -72.1235, 70.612, 72.1260))
    expect = 7130580.307935911
    assert res == pytest.approx(expect)


def test_with_tuple_with_wrong_shape():
    with pytest.raises(ValueError):
        # error with less than 4 elements
        res = haversine((1, 1))

    with pytest.raises(ValueError):
        # error more than 4 elements
        res = haversine((1, 1, 1, 1, 1, 1))


def test_with_nparray():
    arr = np.array(
        (
            (42.3521, -72.1235, 70.612, 72.1260),
            (0.0, 0.0, 1.0, 0.0),
        )
    )
    res = haversine(arr)
    expect = [7130580.307935911, 111195.0802335329]
    assert res[0] == pytest.approx(expect[0])
    assert res[1] == pytest.approx(expect[1])


@pytest.mark.skip
def test_slow_haversine():
    res = slow_haversine(42.3521, -72.1235, 70.612, 72.1260)
    expect = 7130580.307935911
    assert res == pytest.approx(expect)
