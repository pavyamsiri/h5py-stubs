from typing import Final

from _typeshed import StrOrBytesPath

__all__ = ["WINDOWS_ENCODING", "filename_decode", "filename_encode"]

WINDOWS_ENCODING: Final[str]

def filename_encode(filename: StrOrBytesPath) -> bytes: ...
def filename_decode(filename: StrOrBytesPath) -> str: ...
