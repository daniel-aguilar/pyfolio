.PHONY: lint isort test

test: lint
	coverage run manage.py test --settings=pyfolio.settings.test

lint: isort
	flake8

isort:
	isort -c .
