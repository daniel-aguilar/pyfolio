.PHONY: lint isort test clean

lint: isort
	flake8

isort:
	isort -rc --atomic .

test: clean lint
	./manage.py test --settings=pyfolio.settings.test

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -rf staticfiles
