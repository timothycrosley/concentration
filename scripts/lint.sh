#!/bin/bash
set -euxo pipefail

poetry run cruft check
poetry run mypy --ignore-missing-imports concentration/
poetry run isort --check --diff concentration/ tests/
poetry run black --check concentration/ tests/
poetry run flake8 concentration/ tests/
poetry run safety check -i 39462
poetry run bandit -r concentration/
