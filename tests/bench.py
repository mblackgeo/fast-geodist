import random

import numpy as np

from fast_haversine import haversine_array, slow_haversine


def rand_lat() -> float:
    return random.uniform(-90.0, 90.0)


def rand_lng() -> float:
    return random.uniform(-180.0, 180.0)


def create_data() -> np.ndarray:
    random.seed(0)
    return np.array(
        [(rand_lat(), rand_lng(), rand_lat(), rand_lng()) for _ in range(500_000)],
    )


def bench_helper(fast: bool = False):
    data = create_data()
    if fast:
        haversine_array(data)
    else:
        for row in data:
            slow_haversine(*row)


def test_benchmark_fast(benchmark):
    benchmark(bench_helper, fast=True)


def test_benchmark_slow(benchmark):
    benchmark(bench_helper, fast=False)
