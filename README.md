# fast-geodist

[![PyPI](https://img.shields.io/pypi/v/fast-geodist?style=for-the-badge)](https://pypi.org/project/fast-geodist/)
[![CI](https://img.shields.io/github/workflow/status/mblackgeo/fast-geodist/ci?label=CI&style=for-the-badge)](https://github.com/mblackgeo/fast-geodist/actions)
[![Release](https://img.shields.io/github/workflow/status/mblackgeo/fast-geodist/release?label=RELEASE&style=for-the-badge)](https://github.com/mblackgeo/fast-geodist/actions)
[![Code Style](https://img.shields.io/static/v1?label=code%20style&message=black&color=blue&style=for-the-badge)](https://github.com/psf/black)

An implementation of the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula) for calculating [Great Circle distance](https://en.wikipedia.org/wiki/Great-circle_distance) using Rust and [PyO3](https://github.com/PyO3/PyO3).

This package was started as an experiment for learning how to implement functions in Rust and wrap them for use in python. The Haversine Formula is implemented following [georust](https://github.com/georust/geo/blob/main/geo/src/algorithm/haversine_distance.rs), with an array-wise implementation written using [`ndarray::parallel`](https://docs.rs/ndarray/latest/ndarray/parallel/index.html). It is wrapped for python using [Maturin](https://github.com/PyO3/maturin) and integrates [`rust-numpy`](https://github.com/PyO3/rust-numpy) for array operations.

## Installation

```
pip install fast-geodist
```

## Quick start

The package provides two main entry points:

```python
import numpy as np
from fast_geodist import haversine

# Calculate a single distance
# input either a pair of coordinate tuples: (lat1/lon1), (lat2/lon2)
london = (51.51, -0.12)
paris = (48.85, 2.35)
new_york = (40.7, -74.2)

result = haversine(london, paris)

# Calculate multiple distances with lists
result = haversine([(london, paris), (new_york, london)])

# or a numpy array with shape [4, n]
result = haversine(np.array([(*london, *paris), (*new_york, *london)]))
```

## Benchmarks

The results of benchmarking show the rust implementation is **14x faster** than the python implementation. This benchmark computes distances on an array containing 1,000,000 pairs of coordinates (see [`bench.py`](/tests/bench.py)):

```
--------------------------------------------- benchmark: 2 tests ---------------------------------------------
Name (time in ms)              Min                   Max                  Mean                Median
--------------------------------------------------------------------------------------------------------------
test_benchmark_fast       164.0635 (1.0)        171.7663 (1.0)        168.0218 (1.0)        168.4129 (1.0)
test_benchmark_slow     2,335.4281 (14.23)    2,439.7850 (14.20)    2,395.6077 (14.26)    2,406.6356 (14.29)
--------------------------------------------------------------------------------------------------------------
```
Computed on an Intel i7-1165G7.

## Development

Prequisites:

* Python (>=3.7) and make
* [Rust toolchain](https://rustup.rs/)

After cloning the repository, the Makefile includes helpful commands for setting up a development environment, linting, formatting, testing, and benchmarking. Get started as follows:

```shell
# setup a new virtual environment
python -m venv .venv
source .venv/bin/activate

# install the development dependencies
make install

# check other available commands
make help
```

Tooling:

* Cargo and [Pytest](https://docs.pytest.org/en/6.2.x/) are used for testing the Rust and Python code respectively (see [`/tests`](/tests/)).
* Python code is linted using [flake8](https://flake8.pycqa.org/en/latest/) and formatted using [Black](https://github.com/psf/black); rust code with `cargo fmt` and `cargo clippy`.
* [pre-commit](https://pre-commit.com/) is used to run these checks locally before files are pushed to git
* The [Github Actions pipeline](.github/workflows/ci.yml) runs these checks and tests
* [Semantic-release](https://python-semantic-release.readthedocs.io/en/latest/) is used with [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for automated releasing to PyPI

## References

As well as the excellent PyO3 documentation, the following posts helped with creation of this package:

- https://blog.yossarian.net/2020/08/02/Writing-and-publishing-a-python-module-in-rust
- https://depth-first.com/articles/2020/08/10/python-extensions-in-pure-rust-with-pyo3/
- http://saidvandeklundert.net/learn/2021-11-18-calling-rust-from-python-using-pyo3/
- https://itnext.io/how-to-bind-python-numpy-with-rust-ndarray-2efa5717ed21
