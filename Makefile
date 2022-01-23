install:
	pip3 install -r requirements.txt

test:
	rm -rf ./cookie || true
	cookiecutter . --no-input
	cd ./cookie && make test

.PHONY: install test
