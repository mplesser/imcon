"""
imcon is a python application used to control scientific imaging systems.
"""

from importlib import metadata

from azcam.database import AzcamDatabase

__version__ = metadata.version(__package__)
__version_info__ = tuple(int(i) for i in __version__.split(".") if i.isdigit())
