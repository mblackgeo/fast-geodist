.DEFAULT_GOAL := help

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY: install
install:  ## Install dev requirements into the current python environment
	pre-commit install
	pre-commit install --hook-type commit-msg
	pip install -r requirements-dev.txt

.PHONY: build-dev
build-dev:  ## Build the development (debug candidate)
	python setup.py develop

.PHONY: build
build:  ## Build the optimised release binaries
	python setup.py install

.PHONY: lint
lint:  ## Run linting checks with cargo, flake8, isort, and black
	cargo fmt --check
	cargo clippy -- -D warnings
	flake8 .
	black --check .
	isort -c .

.PHONY: test
test: build  ## Run the test suite using cargo and pytest
	cargo test
	pytest tests

.PHONY: bench
bench: build ## Run the Rust and Python benchmarks
	pytest tests/bench.py