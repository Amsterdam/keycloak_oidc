.PHONY: release dist build test coverage clean distclean

PYTHON = python3

help:                           ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

release: clean test dist              ## Test, create a distribution and upload it to pypi
	twine upload dist/*

dist:                           ## Create a distribution
	$(PYTHON) setup.py sdist bdist_wheel

build:                          ## Build the package
	$(PYTHON) setup.py build

test:                           ## Run the tests
	tox
	
clean:                          ## Delete everything in dist/*
	rm -rf dist/*
