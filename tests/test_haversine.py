import numpy as np
import pytest

from fast_geodist import haversine
from fast_geodist.slow import slow_haversine


def test_unsupported_input():
    with pytest.raises(NotImplementedError):
        haversine(1.0)


def test_with_tuple():
    res = haversine((42.3521, -72.1235), (70.612, 72.1260))
    assert pytest.approx(res) == 7130580.307935911


def test_with_list_tuples():
    res = haversine(
        [
            ((42.3521, -72.1235), (70.612, 72.1260)),
            ((0.0, 0.0), (1.0, 0.0)),
        ]
    )
    expect = [7130580.307935911, 111195.0802335329]
    assert isinstance(res, list)
    assert pytest.approx(res[0]) == expect[0]
    assert pytest.approx(res[1]) == expect[1]


def test_with_tuple_with_wrong_shape():
    with pytest.raises(NotImplementedError):
        # error with less than 4 elements
        haversine((1, 1))

    with pytest.raises(NotImplementedError):
        # error more than 4 elements
        haversine((1, 1, 1, 1, 1, 1))


def test_with_nparray():
    arr = np.array(
        (
            (42.3521, -72.1235, 70.612, 72.1260),
            (0.0, 0.0, 1.0, 0.0),
        )
    )
    res = haversine(arr)
    expect = [7130580.307935911, 111195.0802335329]
    assert isinstance(res, np.ndarray)
    assert pytest.approx(res[0]) == expect[0]
    assert pytest.approx(res[1]) == expect[1]


def test_slow_haversine():
    res = slow_haversine(42.3521, -72.1235, 70.612, 72.1260)
    assert pytest.approx(res) == 7130580.307935911


def test_readme_examples():
    london = (51.51, -0.12)
    paris = (48.85, 2.35)
    new_york = (40.7, -74.2)

    # calcate one distance from coordinate pairs
    result = haversine(london, paris)
    assert pytest.approx(result) == 344073.9

    # Calculate multiple distances with lists
    result = haversine([(london, paris), (new_york, london)])
    assert isinstance(result, list)
    assert pytest.approx(result[0]) == 344073.9
    assert pytest.approx(result[1]) == 5584284.1

    # or a numpy array with shape [4, n]
    result = haversine(np.array([(*london, *paris), (*new_york, *london)]))
    assert isinstance(result, np.ndarray)
    assert pytest.approx(result[0]) == 344073.9
    assert pytest.approx(result[1]) == 5584284.1
