"""Democritus functions for working with timezones."""

import pytz

from .democritus_timezones_temp_utils import deduplicate, dict_flip, map_first_arg, seconds_to_hours


def pytz_timezone_object(timezone_name: str):
    """Create a pytz timezone object for the given timezone_name."""
    return pytz.timezone(timezone_name)


def pytz_country_names():
    """Get a dictionary with countries's ISO 3166 country code as keys and the country name as the value."""
    return pytz.country_names


def pytz_country_timezones():
    """Get a dictionary with countries's names as keys and the timezones as values."""
    return pytz.country_timezones


def timezones_names():
    """Get a list of all timezones."""
    return pytz.all_timezones


def timezone_utc_offset(timezone_name: str, date):
    """Find how many hours the given timezone is off from UTC."""
    pytz_object = pytz_timezone_object(timezone_name)
    offset = pytz_object.utcoffset(date)
    offset_seconds = offset.total_seconds()
    return seconds_to_hours(offset_seconds)


@map_first_arg
def timezone_abbreviation(timezone_name: str, date):
    """Find the abbreviation for the given timezone_name."""
    pytz_object = pytz_timezone_object(timezone_name)
    return pytz_object.tzname(date)


def country_timezone_abbreviation(country_name: str, date):
    """Find the abbreviation for the given country_name."""
    timezones = country_timezones(country_name)
    return deduplicate(timezone_abbreviation(timezones, date))


def country_code_timezone_abbreviation(iso_3166_country_code: str, date):
    """Find the abbreviation for the given iso_3166_country_code."""
    timezones = country_code_timezones(iso_3166_country_code)
    return deduplicate(timezone_abbreviation(timezones, date))


def country_code_timezones(iso_3166_country_code):
    """Find the timezones for the country with the given iso_3166_country_code."""
    country_timezones_dict = pytz_country_timezones()

    if country_timezones_dict.get(iso_3166_country_code):
        return country_timezones_dict[iso_3166_country_code]
    else:
        print(
            f'Unable to find the timezones for the country with the ISO 3166 country code: "{iso_3166_country_code}". Try running `countryCodes()` to see the available ISO 3166 country codes.'
        )


def country_timezones(country_name):
    """Find the timezones for the given country."""
    country_names_dict = dict_flip(pytz_country_names(), flatten_values=True)

    if country_names_dict.get(country_name):
        country_code = country_names_dict[country_name]
        return country_code_timezones(country_code)
    else:
        print(
            f'Unable to find the timezones for the country with the name: "{country_name}". Try running `pytz_country_names()` to see the available country names.'
        )


def timezone_countries(timezone_name):
    """Find countries in the given timezone_name."""
    country_timezones_dict = pytz_country_timezones()
    country_name_data = pytz_country_names()
    matching_country_names = []

    for country_code, country_timezone_list in country_timezones_dict.items():
        if timezone_name in country_timezone_list:
            matching_country_names.append(country_name_data[country_code])

    return matching_country_names
