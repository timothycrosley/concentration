#!/bin/bash
set -euxo pipefail

poetry run isort concentration/ tests/
poetry run black concentration/ tests/
