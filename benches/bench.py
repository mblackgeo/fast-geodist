import numpy as np

from fast_geodist import haversine_array
from fast_geodist.slow import slow_haversine


def create_data() -> np.ndarray:
    return np.random.uniform(low=-90.0, high=90.0, size=(1_000_000, 4))


def bench_helper(data: np.ndarray):
    for row in data:
        slow_haversine(*row)


def test_benchmark_fast(benchmark):
    data = create_data()
    benchmark(haversine_array, data)


def test_benchmark_slow(benchmark):
    data = create_data()
    benchmark(bench_helper, data)
