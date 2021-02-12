try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version('democritus_timezones')
except PackageNotFoundError:
    message = 'Unable to find a version number for "democritus_timezones". This likely means the library was not installed properly. Please try re-installing it.'
    print(message)

__author__ = '''Floyd Hightower'''
__email__ = 'floyd.hightower27@gmail.com'

from .democritus_timezones import *
