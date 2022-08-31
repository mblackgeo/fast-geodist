.DEFAULT_GOAL := help

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY: install
install:  ## Install dev requirements into the current python environment
	pip install -r requirements-dev.txt
	pip install -e .

# TODO build

.PHONY: lint
lint:  ## Run linting checks with cargo, flake8, isort, and black
	cargo fmt --check
	flake8 .
	black --check .
	isort -c .

.PHONY: test
test:  ## Run the test suite using cargo and pytest
	cargo test
	pytest tests

.PHONY: bench
bench:  ## Run the Rust and Python benchmarks
	pytest tests/bench.py