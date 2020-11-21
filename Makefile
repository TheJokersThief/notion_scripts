.PHONY: lint clean dev install help

help:
	@echo
	@echo "  lint       check style"
	@echo "  clean      remove build and python file artifacts"
	@echo "  dev        install in development mode"
	@echo "  install"
	@echo "  help       print this message"
	@echo

ensure-poetry:
	@if ! [ -x $(command -v poetry) ]; then \
		echo "Please install poetry (e.g. pip install poetry)"; \
		exit 1; \
	fi

lint: ensure-poetry
	poetry check
	poetry run flake8 --ignore F821,W504 scripts

clean:
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete
	rm -rf .coverage dist build htmlcov *.egg-info

dev: ensure-poetry clean
	poetry install

install: ensure-poetry clean
	poetry install --no-dev

gen-config: ensure-poetry install
	rm -f config.toml.example
	poetry run notion_scripts --config config.toml.example
