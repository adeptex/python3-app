install:
	pip3 install -e .

install-dev:
	pip3 install -e ".[dev]"

flake8-lint:
	flake8 "{{ cookiecutter.project_slug }}/" tests/

isort-lint:
	isort --check-only "{{ cookiecutter.project_slug }}/" tests/

black-lint:
	black --check "{{ cookiecutter.project_slug }}/" tests/

lint: isort-lint black-lint flake8-lint

format:
	autoflake --in-place --recursive --remove-all-unused-imports "{{ cookiecutter.project_slug }}/" tests/ setup.py
	autopep8 --in-place --recursive --aggressive --aggressive "{{ cookiecutter.project_slug }}/" tests/ setup.py
	isort "{{ cookiecutter.project_slug }}/" tests/
	black "{{ cookiecutter.project_slug }}/" tests/

unit:
	pytest --show-capture=all -v tests/

coverage:
	coverage run --source="{{ cookiecutter.project_slug }}/" --branch -m pytest tests/ --junitxml=build/test.xml -v
	coverage xml -i -o build/coverage.xml
	coverage report

test: 
	make lint coverage

freeze:
	CUSTOM_COMPILE_COMMAND="make freeze" \
	pip-compile \
		--no-emit-index-url \
		--output-file requirements.txt \
		--no-annotate \
		--strip-extras \
		--no-allow-unsafe \
		setup.py

freeze-upgrade:
	CUSTOM_COMPILE_COMMAND="make freeze-upgrade" \
	pip-compile \
		--no-emit-index-url \
		--output-file requirements.txt \
		--no-annotate \
		--strip-extras \
		--no-allow-unsafe \
		--upgrade \
		setup.py

.PHONY: install install-dev isort-lint black-lint flake8-lint format lint unit coverage test freeze freeze-upgrade
