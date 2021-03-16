try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:
    from importlib_metadata import PackageNotFoundError, version  # type: ignore

from .democritus_timezones import *

try:
    __version__ = version('d8s_timezones')
except PackageNotFoundError:
    message = (
        'Unable to find a version number for "d8s_timezones".'
        + 'This likely means the library was not installed properly.'
        + 'Please try re-installing it.'
    )
    print(message)

__author__ = '''Floyd Hightower'''
__email__ = 'floyd.hightower27@gmail.com'
