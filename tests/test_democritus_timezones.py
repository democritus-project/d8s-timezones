"""Tests for `democritus_timezones` module."""

from democritus_timezones import (
    timezone_countries,
    country_code_timezones,
    country_timezones,
    timezone_abbreviation,
    country_timezone_abbreviation,
    timezone_utc_offset,
)


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
    timezones_abbreviation = timezone_abbreviation('Africa/Mbabane')
    assert timezones_abbreviation == 'SAST'

    # the results of this test will change based on when in the year this test is run
    timezones_abbreviation = timezone_abbreviation('America/New_York')
    assert timezones_abbreviation in ['EDT', 'EST']

    timezones_abbreviation = timezone_abbreviation('America/New_York', date='2019-01-01')
    assert timezones_abbreviation == 'EST'

    timezones_abbreviation = timezone_abbreviation('America/New_York', date='2019-06-13')
    assert timezones_abbreviation == 'EDT'


def test_country_timezone_abbreviation_docs_1():
    timezones_abbreviation = country_timezone_abbreviation('Eswatini (Swaziland)')
    assert timezones_abbreviation == ['SAST']

    timezones_abbreviation = country_timezone_abbreviation('United States')
    assert sorted(timezones_abbreviation) == ['AKST', 'CST', 'EST', 'HST', 'MST', 'PST']


def test_timezone_utc_offset_docs_1():
    utc_offset = timezone_utc_offset('America/New_York')
    assert utc_offset == -5.0

    utc_offset = timezone_utc_offset('America/New_York', date='2019-01-01')
    assert utc_offset == -5.0

    # during the summer, EST switches to EDT and becomes four hours behind UTC
    utc_offset = timezone_utc_offset('America/New_York', date='2019-06-13')
    assert utc_offset == -4.0

    utc_offset = timezone_utc_offset('Africa/Mbabane')
    assert utc_offset == 2.0
