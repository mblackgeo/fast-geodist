import numpy as np
from pytest import approx

from fast_haversine import haversine, haversine_array, slow_haversine


def test_fast_haversine():
    res = haversine(42.3521, -72.1235, 70.612, 72.1260)
    expect = 7130580.307935911
    assert res == approx(expect)


def test_fast_haversine_vec():
    arr = np.array([[42.3521, -72.1235, 70.612, 72.1260], [0.0, 0.0, 1.0, 0.0]])
    res = haversine_array(arr)
    expect = [7130580.307935911, 111195.0802335329]
    assert res[0] == approx(expect[0])
    assert res[1] == approx(expect[1])


def test_slow_haversine():
    res = slow_haversine(42.3521, -72.1235, 70.612, 72.1260)
    expect = 7130580.307935911
    assert res == approx(expect)
