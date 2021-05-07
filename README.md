# Democritus Timezones

[![PyPI](https://img.shields.io/pypi/v/d8s-timezones.svg)](https://pypi.python.org/pypi/d8s-timezones)
[![CI](https://github.com/democritus-project/d8s-timezones/workflows/CI/badge.svg)](https://github.com/democritus-project/d8s-timezones/actions)
[![Lint](https://github.com/democritus-project/d8s-timezones/workflows/Lint/badge.svg)](https://github.com/democritus-project/d8s-timezones/actions)
[![codecov](https://codecov.io/gh/democritus-project/d8s-timezones/branch/main/graph/badge.svg?token=V0WOIXRGMM)](https://codecov.io/gh/democritus-project/d8s-timezones)
[![The Democritus Project uses semver version 2.0.0](https://img.shields.io/badge/-semver%20v2.0.0-22bfda)](https://semver.org/spec/v2.0.0.html)
[![The Democritus Project uses black to format code](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://choosealicense.com/licenses/lgpl-3.0/)

Democritus functions<sup>[1]</sup> for working with timezones.

[1] Democritus functions are <i>simple, effective, modular, well-tested, and well-documented</i> Python functions.

We use `d8s` (pronounced "dee-eights") as an abbreviation for `democritus` (you can read more about this [here](https://github.com/democritus-project/roadmap#what-is-d8s)).

## Usage

You import the library like:

```python
from d8s_timezones import *
```

Once imported, you can use any of the functions listed below.

## Functions

  - ```python
    def pytz_timezone_object(timezone_name: str):
        """Create a pytz timezone object for the given timezone_name."""
    ```
  - ```python
    def pytz_country_names():
        """Get a dictionary with countries's ISO 3166 country code as keys and the country name as the value."""
    ```
  - ```python
    def pytz_country_timezones():
        """Get a dictionary with countries's names as keys and the timezones as values."""
    ```
  - ```python
    def timezones_names():
        """Get a list of all timezones."""
    ```
  - ```python
    def timezone_utc_offset(timezone_name: str, date):
        """Find how many hours the given timezone is off from UTC."""
    ```
  - ```python
    def timezone_abbreviation(timezone_name: str, date):
        """Find the abbreviation for the given timezone_name."""
    ```
  - ```python
    def country_timezone_abbreviation(country_name: str, date):
        """Find the abbreviation for the given country_name."""
    ```
  - ```python
    def country_code_timezone_abbreviation(iso_3166_country_code: str, date):
        """Find the abbreviation for the given iso_3166_country_code."""
    ```
  - ```python
    def country_code_timezones(iso_3166_country_code):
        """Find the timezones for the country with the given iso_3166_country_code."""
    ```
  - ```python
    def country_timezones(country_name):
        """Find the timezones for the given country."""
    ```
  - ```python
    def timezone_countries(timezone_name):
        """Find countries in the given timezone_name."""
    ```

## Development

👋 &nbsp;If you want to get involved in this project, we have some short, helpful guides below:

- [contribute to this project 🥇][contributing]
- [test it 🧪][local-dev]
- [lint it 🧹][local-dev]
- [explore it 🔭][local-dev]

If you have any questions or there is anything we did not cover, please raise an issue and we'll be happy to help.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and Floyd Hightower's [Python project template](https://github.com/fhightower-templates/python-project-template).

[contributing]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#contributing-a-pr-
[local-dev]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#local-development-
