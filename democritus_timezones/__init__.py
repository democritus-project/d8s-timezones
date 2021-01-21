try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version('democritus_timezones')
except PackageNotFoundError:
    # package is not installed
    message = 'Unable to find a version number for "democritus_timezones"; This is likely indicates the installation of this library failed. Please try re-installing it.'
    print(message)

__author__ = '''Floyd Hightower'''
__email__ = 'floyd.hightower27@gmail.com'

from .democritus_timezones import *
