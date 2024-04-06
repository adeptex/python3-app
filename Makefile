install:
	pip3 install -r requirements.txt

test:
	rm -rf /tmp/cookie || true
	cookiecutter --no-input -o /tmp .
	cd /tmp/cookie && make test

.PHONY: install test
