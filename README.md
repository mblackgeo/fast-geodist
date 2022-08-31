# fast-haversine

An implementation of the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula) for calculating [Great Circle distance](https://en.wikipedia.org/wiki/Great-circle_distance) using Rust and [PyO3](https://github.com/PyO3/PyO3).

This package was started as an experiement for learning how implement functions in Rust and wrap them for use in python. The Haversine Formula is implemented following [georust](https://github.com/georust/geo/blob/main/geo/src/algorithm/haversine_distance.rs), with an array-wise implementation written using [`ndarray::parallel`](https://docs.rs/ndarray/latest/ndarray/parallel/index.html). It is wrapped for python using [`setuptools-rust`](https://github.com/PyO3/setuptools-rust) and integrates [`rust-numpy`](https://github.com/PyO3/rust-numpy) for array operations.

## Installation

Coming soon (for now see Development below to install from source).

## Quick start

The package provides two main entry points:

```python
import numpy as np
from fast_haversine import haversine

# input either a tuple of lat/lon pairs
result = haversine((1, 1, 0, 0))

# or a numpy array of coordinates pairs
# useful if loads of distances need to be calculated, handled in parallel
result = haversine(np.array([(1,1,0,0), (2,2,0,0)]))
```

## Developement

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
* The [Github Actions pipeline](.github/workflows/cicd.yml) runs these checks and tests
* (Soon) [Semantic-release](https://python-semantic-release.readthedocs.io/en/latest/) is used with [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for automated releasing to PyPI

## Roadmap

- [ ] Rust benchmarks
- [ ] Packaging using [Maturin](https://github.com/PyO3/maturin)
- [ ] CD pipeline with semantic release integration

## References

As well as the excellent PyO3 documentation, the following posts helped with creation of this package:

- https://blog.yossarian.net/2020/08/02/Writing-and-publishing-a-python-module-in-rust
- https://depth-first.com/articles/2020/08/10/python-extensions-in-pure-rust-with-pyo3/
- http://saidvandeklundert.net/learn/2021-11-18-calling-rust-from-python-using-pyo3/
- https://itnext.io/how-to-bind-python-numpy-with-rust-ndarray-2efa5717ed21
