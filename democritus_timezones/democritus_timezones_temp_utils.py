"""Utility functions temporarily provided until the rest of the democritus functions get uploaded."""

import copy
import functools
from typing import Any, Dict, Iterable, List


def seconds_to_hours(seconds: int) -> float:
    """Convert seconds to hours."""
    return seconds / 60 / 60


def map_first_arg(func):
    """If the first argument is a list or tuple, iterate through each item in the list and send it to the function."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        iterable_arg = args[0]
        other_args = args[1:]

        # TODO: define these types elsewhere
        if isinstance(iterable_arg, (list, set, tuple)):
            results = []
            # iterate through the list argument sending each item into the function (along with the other arguments/kwargs)
            for item in iterable_arg:
                results.append(func(item, *other_args, **kwargs))
            return results
        else:
            return func(*args, **kwargs)

    return wrapper


def deduplicate(iterable: Iterable) -> list:
    """Deduplicate the iterable."""
    # TODO: will this work for every type except for dicts???
    deduplicated_list = list(set(iterable))
    return deduplicated_list


python_types_not_allowed_as_dict_keys = (dict, list, set)


def is_valid_dict_key(key: Any) -> bool:
    """Return whether or not a dictionary could have the given key."""
    type_is_invalid_key = type(key) in python_types_not_allowed_as_dict_keys
    return not type_is_invalid_key


@map_first_arg
def dict_delistify_values(dictionary: dict) -> dict:
    """For all values in the given dictionary that are lists whose lengths are one, replace the list of length one with the value in the list."""
    # TODO: it would be nice to be able to do this iteratively throughout a dict... currently it only goes through the first level of values - adding a recursive option would be nice... would this principle apply to other functions in this library?
    for k, v in dictionary.items():
        if isinstance(v, list) and len(v) == 1:
            dictionary[k] = v[0]
    return dictionary


@map_first_arg
def dict_flip(dictionary: dict, *, flatten_values: bool = False, flip_lists_and_sets: bool = False) -> dict:
    """Flip the dictionary's keys and values; all of the values become keys and keys become values."""
    new_dict: Dict[Any, Any] = {}

    for key, value in dictionary.items():
        if not is_valid_dict_key(value):
            if flip_lists_and_sets and isinstance(value, (list, set)):
                temp_dict = copy.deepcopy(new_dict)
                for i in value:
                    try:
                        temp_dict = dict_add(temp_dict, i, key)
                    except TypeError as e:
                        message = f'Unable to flip <<{value}>> because it contains items of a type which cannot be the keys for dictionaries.'
                        raise TypeError(message) from e
                    else:
                        new_dict.update(temp_dict)
        else:
            new_dict = dict_add(new_dict, value, key)

    if flatten_values:
        new_dict = dict_delistify_values(new_dict)

    return new_dict


def dict_add(dictionary: Dict[Any, List[Any]], key: Any, value: Any) -> Dict[Any, List[Any]]:
    """Add the given value to the dictionary at the given key. This function expects that all values of the dictionary parameter are lists."""
    if key in dictionary:
        if not isinstance(dictionary[key], list):
            message = f'The value at the "{key}" key in the dictionary is not a list and the dict_add function requires all values to be a list.'
            raise TypeError(message)
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]
    return dictionary
