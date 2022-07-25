import random

from fast_haversine import haversine_vec, slow_haversine


def rand_lat() -> float:
    return random.uniform(-90.0, 90.0)


def rand_lng() -> float:
    return random.uniform(-180.0, 180.0)


def create_data() -> tuple[list[float], list[float], list[float], list[float]]:
    random.seed(0)
    return (
        [rand_lat() for _ in range(100)],
        [rand_lng() for _ in range(100)],
        [rand_lat() for _ in range(100)],
        [rand_lng() for _ in range(100)],
    )


def bench_helper(fast: bool = False):
    data = create_data()
    if fast:
        haversine_vec(*data)
    else:
        for (a, b, c, d) in zip(*data):
            slow_haversine(a, b, c, d)


def test_benchmark_fast(benchmark):
    benchmark(bench_helper, fast=True)


def test_benchmark_slow(benchmark):
    benchmark(bench_helper, fast=False)
