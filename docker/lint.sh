#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort d8s_timezones/ tests/

black d8s_timezones/ tests/

mypy d8s_timezones/ tests/

pylint --fail-under 9 d8s_timezones/*.py

flake8 d8s_timezones/ tests/

bandit -r d8s_timezones/

# we run black again at the end to undo any odd changes made by any of the linters above
black d8s_timezones/ tests/
