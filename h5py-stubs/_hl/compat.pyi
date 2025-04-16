import sys
from os import fsdecode, fsencode, fspath
from typing import Final

from _typeshed import StrOrBytesPath
from h5py.version import hdf5_built_version_tuple

__all__ = [
    "WINDOWS_ENCODING",
    "filename_decode",
    "filename_encode",
    "fsdecode",
    "fsencode",
    "fspath",
    "hdf5_built_version_tuple",
    "sys",
]

WINDOWS_ENCODING: Final[str]

def filename_encode(filename: StrOrBytesPath) -> bytes: ...
def filename_decode(filename: StrOrBytesPath) -> str: ...
