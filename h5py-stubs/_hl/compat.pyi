from typing import Final

from _typeshed import StrOrBytesPath

WINDOWS_ENCODING: Final[str]

def filename_encode(filename: StrOrBytesPath) -> bytes: ...
def filename_decode(filename: StrOrBytesPath) -> str: ...
