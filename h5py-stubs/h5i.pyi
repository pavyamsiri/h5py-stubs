from typing import Final

from ._objects import ObjectID, phil, with_phil
from .h5f import FileID

__all__ = [
    "ATTR",
    "BADID",
    "DATASET",
    "DATASPACE",
    "DATATYPE",
    "FILE",
    "GENPROP_CLS",
    "GENPROP_LST",
    "GROUP",
    "INVALID_HID",
    "dec_ref",
    "get_file_id",
    "get_name",
    "get_ref",
    "get_type",
    "inc_ref",
    "phil",
    "with_phil",
    "wrap_identifier",
]

INVALID_HID: Final[int]
BADID: Final[int]
FILE: Final[int]
GROUP: Final[int]
DATASPACE: Final[int]
DATASET: Final[int]
ATTR: Final[int]
GENPROP_CLS: Final[int]
GENPROP_LST: Final[int]
DATATYPE: Final[int]

def wrap_identifier(ident: int) -> ObjectID: ...
def get_name(obj: ObjectID) -> bytes | None: ...
def get_file_id(obj: ObjectID) -> FileID: ...
def inc_ref(obj: ObjectID) -> None: ...
def dec_ref(obj: ObjectID) -> None: ...
def get_ref(obj: ObjectID) -> int: ...
def get_type(obj: ObjectID) -> int: ...
