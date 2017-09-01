.PHONY: lint isort test clean

lint: isort
	pycodestyle --show-source --show-pep8 .

isort:
	isort -rc --atomic .

test: clean lint
	./manage.py test --settings=pyfolio.test_settings

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
