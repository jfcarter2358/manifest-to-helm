.PHONY: help clean test build publish

help:  ## Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

clean:  ## Remove build and test artifacts
	rm -rf dist || true
	rm -rf .pytest_cache || true
	rm -rf manifest_to_helm/__pycache__ || true
	rm -rf tests/__pycache__ || true
	rm -rf tests/resources/test_dump_chart/out/test || true

test:  ## Run test suite
	pytest -q

build:  ## Build and package for distribution
	poetry build

publish:  ## Publish to PyPI
	poetry publish