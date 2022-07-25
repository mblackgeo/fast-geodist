from fast_haversine import haversine, slow_haversine
from pytest import approx


def test_fast_haversine():
    res = haversine(42.3521, -72.1235, 70.612, 72.1260)
    expect = 7130580.307935911
    assert res == approx(expect)


def test_slow_haversine():
    res = slow_haversine(42.3521, -72.1235, 70.612, 72.1260)
    expect = 7130580.307935911
    assert res == approx(expect)
