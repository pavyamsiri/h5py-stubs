import gc
from collections import namedtuple
from typing import Final, NamedTuple

from h5py.h5ac import CacheConfig
from h5py.h5g import GroupIter
from h5py.h5p import PropFAID, PropFCID

from . import h5o
from ._objects import ObjectID, phil, with_phil

ACC_EXCL: Final[int]
ACC_RDONLY: Final[int]
ACC_RDWR: Final[int]
ACC_SWMR_READ: Final[int]
ACC_SWMR_WRITE: Final[int]
ACC_TRUNC: Final[int]
CLOSE_DEFAULT: Final[int]
CLOSE_SEMI: Final[int]
CLOSE_STRONG: Final[int]
CLOSE_WEAK: Final[int]
FILE_IMAGE_OPEN_RW: Final[int]
FSPACE_STRATEGY_AGGR: Final[int]
FSPACE_STRATEGY_FSM_AGGR: Final[int]
FSPACE_STRATEGY_NONE: Final[int]
FSPACE_STRATEGY_PAGE: Final[int]
LIBVER_EARLIEST: Final[int]
LIBVER_LATEST: Final[int]
LIBVER_V110: Final[int]
LIBVER_V112: Final[int]
LIBVER_V114: Final[int]
LIBVER_V18: Final[int]
OBJ_ALL: Final[int]
OBJ_ATTR: Final[int]
OBJ_DATASET: Final[int]
OBJ_DATATYPE: Final[int]
OBJ_FILE: Final[int]
OBJ_GROUP: Final[int]
OBJ_LOCAL: Final[int]
SCOPE_GLOBAL: Final[int]
SCOPE_LOCAL: Final[int]
UNLIMITED: Final[int]

def open(name: bytes, flags: int = ..., fapl: PropFAID | None = None) -> FileID: ...
def create(
    name: bytes,
    flags: int = ...,
    fcpl: PropFCID | None = None,
    fapl: PropFAID | None = None,
) -> FileID: ...
def open_file_image(image: bytes, flags: int = 0) -> FileID: ...
def flush(obj: ObjectID, scope: int = ...) -> None: ...
def is_hdf5(name: bytes) -> bool: ...
def mount(loc: ObjectID, name: bytes, fid: FileID) -> None: ...
def unmount(loc: ObjectID, name: bytes) -> None: ...
def get_name(obj: ObjectID) -> bytes: ...
def get_obj_count(where: FileID | int = ..., types: int = ...) -> int: ...
def get_obj_ids(where: FileID | int = ..., types: int = ...) -> list[ObjectID]: ...

class PageBufStats(NamedTuple):
    meta: PageStats
    raw: PageStats

class PageStats(NamedTuple):
    accesses: int
    hits: int
    misses: int
    evictions: int
    bypasses: int

class FileID(ObjectID):
    @property
    def name(self) -> bytes: ...
    def close(self) -> None: ...
    def reopen(self) -> FileID: ...
    def get_filesize(self) -> int: ...
    def get_create_plist(self) -> PropFCID: ...
    def get_access_plist(self) -> PropFAID: ...
    def get_freespace(self) -> int: ...
    def get_intent(self) -> int: ...
    def get_vfd_handle(self, fapl: PropFAID | None = None) -> int: ...
    def get_file_image(self) -> bytes: ...
    def set_mpi_atomicity(self, atomicity: bool) -> None: ...
    def get_mpi_atomicity(self) -> bool: ...
    def get_mdc_hit_rate(self) -> float: ...
    def get_mdc_size(self) -> tuple[int, int, int, int]: ...
    def reset_mdc_hit_rate_stats(self) -> None: ...
    def get_mdc_config(self) -> CacheConfig: ...
    def set_mdc_config(self, config: CacheConfig) -> None: ...
    def start_swmr_write(self) -> None: ...
    def reset_page_buffering_stats(self) -> None: ...
    def get_page_buffering_stats(self) -> PageBufStats: ...
    def __iter__(self) -> GroupIter: ...
    def __reversed__(self) -> GroupIter: ...

__all__ = [
    "ACC_EXCL",
    "ACC_RDONLY",
    "ACC_RDWR",
    "ACC_SWMR_READ",
    "ACC_SWMR_WRITE",
    "ACC_TRUNC",
    "CLOSE_DEFAULT",
    "CLOSE_SEMI",
    "CLOSE_STRONG",
    "CLOSE_WEAK",
    "FILE_IMAGE_OPEN_RW",
    "FSPACE_STRATEGY_AGGR",
    "FSPACE_STRATEGY_FSM_AGGR",
    "FSPACE_STRATEGY_NONE",
    "FSPACE_STRATEGY_PAGE",
    "LIBVER_EARLIEST",
    "LIBVER_LATEST",
    "LIBVER_V18",
    "LIBVER_V110",
    "LIBVER_V112",
    "LIBVER_V114",
    "OBJ_ALL",
    "OBJ_ATTR",
    "OBJ_DATASET",
    "OBJ_DATATYPE",
    "OBJ_FILE",
    "OBJ_GROUP",
    "OBJ_LOCAL",
    "SCOPE_GLOBAL",
    "SCOPE_LOCAL",
    "UNLIMITED",
    "FileID",
    "PageBufStats",
    "PageStats",
    "create",
    "flush",
    "gc",
    "get_name",
    "get_obj_count",
    "get_obj_ids",
    "h5o",
    "is_hdf5",
    "mount",
    "namedtuple",
    "open",
    "open_file_image",
    "phil",
    "unmount",
    "with_phil",
]
