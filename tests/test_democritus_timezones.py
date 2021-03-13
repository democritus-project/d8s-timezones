"""Tests for `d8s_timezones` module."""

from datetime import datetime

from d8s_timezones import (
    country_code_timezone_abbreviation,
    country_code_timezones,
    country_timezone_abbreviation,
    country_timezones,
    timezone_abbreviation,
    timezone_countries,
    timezone_utc_offset,
)

EXAMPLE_DATE = EXAMPLE_DATE_EST = datetime.strptime("2021-01-01 14:00", "%Y-%m-%d %H:%M")
EXAMPLE_DATE_EDT = datetime.strptime("2021-06-13 14:00", "%Y-%m-%d %H:%M")


def test_country_code_timezone_abbreviation_docs_1():
    result = country_code_timezone_abbreviation('US', EXAMPLE_DATE)
    assert sorted(result) == ['AKST', 'CST', 'EST', 'HST', 'MST', 'PST']

    result = country_code_timezone_abbreviation('SA', EXAMPLE_DATE)
    assert sorted(result) == ['+03']


def test_timezone_countries_docs_1():
    countries = timezone_countries('Africa/Mbabane')
    assert countries == ['Eswatini (Swaziland)']


def test_country_code_timezones_docs_1():
    timezones = country_code_timezones('SZ')
    assert timezones == ['Africa/Mbabane']


def test_country_timezones_docs_1():
    timezones = country_timezones('Eswatini (Swaziland)')
    assert timezones == ['Africa/Mbabane']


def test_timezone_abbreviation_docs_1():
    timezones_abbreviation = timezone_abbreviation('Africa/Mbabane', EXAMPLE_DATE)
    assert timezones_abbreviation == 'SAST'

    timezones_abbreviation = timezone_abbreviation('America/New_York', EXAMPLE_DATE_EST)
    assert timezones_abbreviation == 'EST'

    timezones_abbreviation = timezone_abbreviation('America/New_York', EXAMPLE_DATE_EDT)
    assert timezones_abbreviation == 'EDT'


def test_country_timezone_abbreviation_docs_1():
    timezones_abbreviation = country_timezone_abbreviation('Eswatini (Swaziland)', EXAMPLE_DATE)
    assert timezones_abbreviation == ['SAST']

    timezones_abbreviation = country_timezone_abbreviation('United States', EXAMPLE_DATE)
    assert sorted(timezones_abbreviation) == ['AKST', 'CST', 'EST', 'HST', 'MST', 'PST']


def test_timezone_utc_offset_docs_1():
    utc_offset = timezone_utc_offset('America/New_York', EXAMPLE_DATE_EST)
    assert utc_offset == -5.0

    # during the summer, EST switches to EDT and becomes four hours behind UTC
    utc_offset = timezone_utc_offset('America/New_York', EXAMPLE_DATE_EDT)
    assert utc_offset == -4.0

    utc_offset = timezone_utc_offset('Africa/Mbabane', EXAMPLE_DATE)
    assert utc_offset == 2.0
