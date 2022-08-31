import random
from typing import List, Tuple

from fast_haversine import haversine_vec, slow_haversine


def rand_lat() -> float:
    return random.uniform(-90.0, 90.0)


def rand_lng() -> float:
    return random.uniform(-180.0, 180.0)


def create_data() -> Tuple[List[float], List[float], List[float], List[float]]:
    random.seed(0)
    return (
        [rand_lat() for _ in range(100_000)],
        [rand_lng() for _ in range(100_000)],
        [rand_lat() for _ in range(100_000)],
        [rand_lng() for _ in range(100_000)],
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
