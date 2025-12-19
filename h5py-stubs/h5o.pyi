from collections.abc import Callable
from typing import Final, overload

from ._objects import ObjectID, phil, with_phil
from .h5g import GroupID
from .h5p import PropCopyID, PropLAID, PropLCID

__all__ = [
    "COPY_EXPAND_EXT_LINK_FLAG",
    "COPY_EXPAND_REFERENCE_FLAG",
    "COPY_EXPAND_SOFT_LINK_FLAG",
    "COPY_PRESERVE_NULL_FLAG",
    "COPY_SHALLOW_HIERARCHY_FLAG",
    "COPY_WITHOUT_ATTR_FLAG",
    "TYPE_DATASET",
    "TYPE_GROUP",
    "TYPE_NAMED_DATATYPE",
    "ObjInfo",
    "copy",
    "exists_by_name",
    "get_comment",
    "get_info",
    "link",
    "open",
    "phil",
    "set_comment",
    "visit",
    "with_phil",
]

TYPE_GROUP: Final[int]
TYPE_DATASET: Final[int]
TYPE_NAMED_DATATYPE: Final[int]

COPY_SHALLOW_HIERARCHY_FLAG: Final[int]
COPY_EXPAND_SOFT_LINK_FLAG: Final[int]
COPY_EXPAND_EXT_LINK_FLAG: Final[int]
COPY_EXPAND_REFERENCE_FLAG: Final[int]
COPY_WITHOUT_ATTR_FLAG: Final[int]
COPY_PRESERVE_NULL_FLAG: Final[int]

def copy(
    src_loc: ObjectID,
    src_name: bytes,
    dst_loc: GroupID,
    dst_name: bytes,
    copypl: PropCopyID | None = None,
    lcpl: PropLCID | None = None,
) -> None: ...
def exists_by_name(loc: ObjectID, name: bytes, lapl: PropLAID | None = None) -> bool: ...
def get_comment(loc: ObjectID, comment: bytes, *, obj_name: bytes = b".", lapl: PropLAID | None = None) -> bytes: ...
def set_comment(loc: ObjectID, comment: bytes, *, obj_name: bytes = b".", lapl: PropLAID | None = None) -> None: ...
def get_info(
    loc: ObjectID,
    name: bytes = b"",
    index: int = -1,
    *,
    obj_name: bytes = b".",
    index_type: int = ...,
    order: int = ...,
    lapl: PropLAID | None = None,
) -> ObjInfo: ...
def link(obj: ObjectID, loc: GroupID, name: bytes, lcpl: PropLCID | None = None, lapl: PropLAID | None = None) -> None: ...
def open(loc: ObjectID, name: bytes, lapl: PropLAID | None = None) -> ObjectID: ...

# visit overloads
# Case 1: info = False
@overload
def visit[R](
    loc: ObjectID,
    func: Callable[[bytes], R | None],
    *,
    idx_type: int = ...,
    order: int = ...,
    obj_name: bytes = b".",
    lapl: PropLAID | None = None,
    info: bool = False,
) -> R: ...

# Case 2: info = True
@overload
def visit[R](
    loc: ObjectID,
    func: Callable[[bytes, ObjInfo], R | None],
    *,
    idx_type: int = ...,
    order: int = ...,
    obj_name: bytes = b".",
    lapl: PropLAID | None = None,
    info: bool = False,
) -> R: ...

class _OHdrMesg:
    @property
    def present(self) -> int: ...
    @property
    def shared(self) -> int: ...

class _ObjMetaInfo:
    @property
    def index_size(self) -> int: ...
    @property
    def heap_size(self) -> int: ...

class _OMetaSize:
    def __init__(self) -> None: ...
    @property
    def obj(self) -> _ObjMetaInfo: ...
    @property
    def attr(self) -> _ObjMetaInfo: ...

class _OHdrSpace:
    @property
    def total(self) -> int: ...
    @property
    def meta(self) -> int: ...
    @property
    def mesg(self) -> int: ...
    @property
    def free(self) -> int: ...

class _OHdr:
    @property
    def flags(self) -> int: ...
    @property
    def nchunks(self) -> int: ...
    @property
    def nmesgs(self) -> int: ...
    @property
    def version(self) -> int: ...
    @property
    def space(self) -> _OHdrSpace: ...
    @property
    def mesg(self) -> _OHdrMesg: ...

class ObjInfo:
    def __init__(self) -> None: ...
    @property
    def fileno(self) -> int: ...
    @property
    def addr(self) -> int: ...
    @property
    def type(self) -> int: ...
    @property
    def rc(self) -> int: ...
    @property
    def atime(self) -> int: ...
    @property
    def mtime(self) -> int: ...
    @property
    def ctime(self) -> int: ...
    @property
    def btime(self) -> int: ...
    @property
    def num_attrs(self) -> int: ...
    @property
    def hdr(self) -> _OHdr: ...
    @property
    def meta_size(self) -> _OMetaSize: ...
