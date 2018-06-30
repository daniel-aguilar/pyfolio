.PHONY: lint isort test clean

lint: isort
	flake8

isort:
	isort -rc --atomic .

test: clean lint
	./manage.py test --settings=pyfolio.settings.test
