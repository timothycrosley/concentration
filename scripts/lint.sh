#!/bin/bash
set -euxo pipefail

poetry run cruft check
poetry run mypy --ignore-missing-imports concentration/
poetry run black --check concentration/ tests/
poetry run ruff concentration/ tests/
poetry run safety check -i 39462 -i 40291
poetry run bandit -r concentration/
