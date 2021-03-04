#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort democritus_timezones/ tests/

black democritus_timezones/ tests/

mypy democritus_timezones/ tests/

pylint --fail-under 9 democritus_timezones/*.py

flake8 democritus_timezones/ tests/

bandit -r democritus_timezones/

# we run black again at the end to undo any odd changes made by any of the linters above
black democritus_timezones/ tests/
