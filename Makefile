lint:
	poetry run flake8 gendiff

gen-diff:
	poetry run gendiff

build:lint
	poetry build

publish:
	poetry publish --dry-run

uninstall-hexlet:
	pip uninstall hexlet_code -y

package-install: # python3 -m pip install --user dist/*.whl
	python3 -m pip install dist/*.whl

check:
	pytest -v

tests-coverage:
	poetry run pytest --cov -v

install:
	poetry install
