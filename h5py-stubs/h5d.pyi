from collections import namedtuple
from collections.abc import Callable
from typing import Any, Final, NamedTuple, TypeAlias, TypeVar

import numpy as np

from ._objects import ObjectID
from .h5p import PropDAID, PropDCID, PropDXID, PropLCID
from .h5s import SpaceID
from .h5t import TypeID

__all__ = [
    "ALLOC_TIME_DEFAULT",
    "ALLOC_TIME_EARLY",
    "ALLOC_TIME_INCR",
    "ALLOC_TIME_LATE",
    "CHUNKED",
    "COMPACT",
    "CONTIGUOUS",
    "FILL_TIME_ALLOC",
    "FILL_TIME_IFSET",
    "FILL_TIME_NEVER",
    "FILL_VALUE_DEFAULT",
    "FILL_VALUE_UNDEFINED",
    "FILL_VALUE_USER_DEFINED",
    "SPACE_STATUS_ALLOCATED",
    "SPACE_STATUS_NOT_ALLOCATED",
    "SPACE_STATUS_PART_ALLOCATED",
    "VDS_FIRST_MISSING",
    "VDS_LAST_AVAILABLE",
    "VIRTUAL",
    "DatasetID",
    "StoreInfo",
    "create",
    "namedtuple",
    "open",
]

type _AnyShape = tuple[int, ...]
type _AnyArray = np.ndarray[_AnyShape, np.dtype[Any]]
_SCT = TypeVar("_SCT", bound=np.generic, default=np.generic)
_Array1D: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[_SCT]]

_R = TypeVar("_R")

ALLOC_TIME_DEFAULT: Final[int]
ALLOC_TIME_EARLY: Final[int]
ALLOC_TIME_INCR: Final[int]
ALLOC_TIME_LATE: Final[int]
CHUNKED: Final[int]
COMPACT: Final[int]
CONTIGUOUS: Final[int]
FILL_TIME_ALLOC: Final[int]
FILL_TIME_IFSET: Final[int]
FILL_TIME_NEVER: Final[int]
FILL_VALUE_DEFAULT: Final[int]
FILL_VALUE_UNDEFINED: Final[int]
FILL_VALUE_USER_DEFINED: Final[int]
SPACE_STATUS_ALLOCATED: Final[int]
SPACE_STATUS_NOT_ALLOCATED: Final[int]
SPACE_STATUS_PART_ALLOCATED: Final[int]
VDS_FIRST_MISSING: Final[int]
VDS_LAST_AVAILABLE: Final[int]
VIRTUAL: Final[int]

def open(loc: ObjectID, name: bytes, dapl: PropDAID | None = None) -> DatasetID: ...
def create(
    loc: ObjectID,
    name: bytes | None,
    tid: TypeID,
    space: SpaceID,
    dcpl: PropDCID | None = None,
    lcpl: PropLCID | None = None,
    dapl: PropDAID | None = None,
) -> DatasetID: ...

class StoreInfo(NamedTuple):
    chunk_offset: tuple[int, ...] | None
    filter_mask: int
    byte_offset: int | None
    size: int

class DatasetID(ObjectID):
    @property
    def dtype(self) -> np.dtype[Any]: ...
    @property
    def shape(self) -> tuple[int, ...]: ...
    @property
    def rank(self) -> int: ...
    def read(
        self,
        mspace: SpaceID,
        fspace: SpaceID,
        arr_obj: _AnyArray,
        mtype: TypeID | None = None,
        dxpl: PropDXID | None = None,
    ) -> None: ...
    def write(
        self,
        mspace: SpaceID,
        fspace: SpaceID,
        arr_obj: _AnyArray,
        mtype: TypeID | None = None,
        dxpl: PropDXID | None = None,
    ) -> None: ...
    def extend(self, shape: tuple[int, ...]) -> None: ...
    def set_extent(self, shape: tuple[int, ...]) -> None: ...
    def get_space(self) -> SpaceID: ...
    def get_space_status(self) -> int: ...
    def get_type(self) -> TypeID: ...
    def get_create_plist(self) -> PropDCID: ...
    def get_access_plist(self) -> PropDAID: ...
    def get_offset(self) -> int | None: ...
    def get_storage_size(self) -> int: ...
    def flush(self) -> None: ...
    def refresh(self) -> None: ...
    def write_direct_chunk(
        self,
        offsets: tuple[int, ...],
        data: memoryview,
        filter_mask: int = ...,
        dxpl: PropDXID | None = None,
    ) -> None: ...
    def read_direct_chunk(
        self,
        offsets: tuple[int, ...],
        dxpl: PropDXID | None = None,
        out: _Array1D[np.uint8] | None = None,
    ) -> None: ...
    def get_num_chunks(self, space: SpaceID | None = None) -> int: ...
    def get_chunk_info(self, index: int, space: SpaceID | None = None) -> int: ...
    def get_chunk_info_by_coord(self, chunk_offset: tuple[int, ...]) -> StoreInfo: ...
    def chunk_iter(self, func: Callable[[StoreInfo], _R | None]) -> _R: ...
