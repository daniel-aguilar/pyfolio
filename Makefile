.PHONY: test lint format

test: lint
	coverage run manage.py test --settings=pyfolio.settings.test

lint: format
	ruff check

format:
	ruff format --check
