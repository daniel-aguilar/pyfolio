.PHONY: install install-dev format format-check lint test lock export

install:
	uv sync

install-dev:
	uv sync --extra dev

format:
	uv run ruff format

format-check:
	uv run ruff format --check

lint: format-check
	uv run ruff check

test: lint
	uv run coverage run manage.py test --settings=pyfolio.settings.test
	uv run coverage report

lock:
	uv lock

export:
	uv export --no-dev --no-emit-project -o requirements.txt
