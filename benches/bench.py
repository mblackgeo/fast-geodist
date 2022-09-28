import random

import numpy as np

from fast_geodist import haversine_array
from fast_geodist.slow import slow_haversine


def rand_lat() -> float:
    return random.uniform(-90.0, 90.0)


def rand_lng() -> float:
    return random.uniform(-180.0, 180.0)


def create_data() -> np.ndarray:
    random.seed(0)
    return np.array(
        [(rand_lat(), rand_lng(), rand_lat(), rand_lng()) for _ in range(1_000_000)],
    )


def bench_helper(data: np.ndarray, fast: bool = False):
    if fast:
        haversine_array(data)
    else:
        for row in data:
            slow_haversine(*row)


def test_benchmark_fast(benchmark):
    data = create_data()
    benchmark(bench_helper, data=data, fast=True)


def test_benchmark_slow(benchmark):
    data = create_data()
    benchmark(bench_helper, data=data, fast=False)
