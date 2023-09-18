# -*- coding: utf-8 -*-

"""Top-level package for bioio_imageio."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("bioio-imageio")
except PackageNotFoundError:
    __version__ = "uninstalled"

__author__ = "Sean Meharry"
__email__ = "seanm@alleninstitute.org"

from .reader import Reader
from .reader_metadata import ReaderMetadata

__all__ = ["Reader", "ReaderMetadata"]
