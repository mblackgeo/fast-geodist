import random

from fast_haversine import haversine, slow_haversine


def rand_lat() -> float:
    return random.uniform(-90.0, 90.0)


def rand_lng() -> float:
    return random.uniform(-180.0, 180.0)


def bench_helper(fast: bool = False):
    fn = haversine if fast else slow_haversine
    fn(rand_lat(), rand_lng(), rand_lat(), rand_lng())


def test_benchmark_fast(benchmark):
    benchmark(bench_helper, fast=True)


def test_benchmark_slow(benchmark):
    benchmark(bench_helper, fast=False)
