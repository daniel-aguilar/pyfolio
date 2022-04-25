.PHONY: lint isort test clean

test: lint
	coverage run manage.py test --settings=pyfolio.settings.test

lint: isort
	flake8

isort:
	isort --atomic .

