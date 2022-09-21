# fast-geodist

[![PyPI](https://img.shields.io/pypi/v/fast-geodist?style=for-the-badge)](https://pypi.org/project/fast-geodist/)
[![CI](https://img.shields.io/github/workflow/status/mblackgeo/fast-geodist/ci?label=CI&style=for-the-badge)](https://github.com/mblackgeo/fast-geodist/actions)
[![Release](https://img.shields.io/github/workflow/status/mblackgeo/fast-geodist/release?label=RELEASE&style=for-the-badge)](https://github.com/mblackgeo/fast-geodist/actions)
[![Code Style](https://img.shields.io/static/v1?label=code%20style&message=black&color=blue&style=for-the-badge)](https://github.com/psf/black)

An implementation of the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula) for calculating [Great Circle distance](https://en.wikipedia.org/wiki/Great-circle_distance) using Rust and [PyO3](https://github.com/PyO3/PyO3).

This package was started as an experiement for learning how to implement functions in Rust and wrap them for use in python. The Haversine Formula is implemented following [georust](https://github.com/georust/geo/blob/main/geo/src/algorithm/haversine_distance.rs), with an array-wise implementation written using [`ndarray::parallel`](https://docs.rs/ndarray/latest/ndarray/parallel/index.html). It is wrapped for python using [Maturin](https://github.com/PyO3/maturin) and integrates [`rust-numpy`](https://github.com/PyO3/rust-numpy) for array operations.

## Installation

```
pip install fast-geodist
```

## Quick start

The package provides two main entry points:

```python
import numpy as np
from fast_geodist import haversine

# input either a tuple of (lat/lon, lat/lon)
result = haversine((1, 1, 0, 0))

# or a numpy array of coordinates pairs
# useful if lots of distances need to be calculated
# will be computed in parallel
result = haversine(np.array([(1, 1, 0, 0), (2, 2, 0, 0)]))
```

## Benchmarks

The results of benchmarking show the rust implementation is **2.5x to 2.7x faster** than the python implementation. This benchmark computes distances on an array containing 250,000 pairs on coordinates (see [`bench.py`](/tests/bench.py)):

```
--------------------------------------------------- benchmark: 2 tests --------------------------------------------------
Name (time in ms)            Min                 Max                Mean             StdDev              Median
-------------------------------------------------------------------------------------------------------------------------
test_benchmark_fast     260.0692 (1.0)      265.6916 (1.0)      262.6179 (1.0)       2.0324 (1.0)      262.5162 (1.0)
test_benchmark_slow     655.8816 (2.52)     845.2172 (3.18)     709.3914 (2.70)     80.1352 (39.43)    667.0456 (2.54)
-------------------------------------------------------------------------------------------------------------------------
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

## Roadmap

- [ ] Rust benchmarks

## References

As well as the excellent PyO3 documentation, the following posts helped with creation of this package:

- https://blog.yossarian.net/2020/08/02/Writing-and-publishing-a-python-module-in-rust
- https://depth-first.com/articles/2020/08/10/python-extensions-in-pure-rust-with-pyo3/
- http://saidvandeklundert.net/learn/2021-11-18-calling-rust-from-python-using-pyo3/
- https://itnext.io/how-to-bind-python-numpy-with-rust-ndarray-2efa5717ed21
