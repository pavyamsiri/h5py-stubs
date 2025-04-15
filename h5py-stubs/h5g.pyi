import sys
from collections.abc import Callable
from typing import Final, TypeVar

from ._objects import ObjectID, phil, with_phil
from .h5p import CRT_ORDER_TRACKED, PropGCID, PropLCID

__all__ = [
    "CRT_ORDER_TRACKED",
    "DATASET",
    "GROUP",
    "LINK",
    "LINK_ERROR",
    "LINK_HARD",
    "LINK_SOFT",
    "TYPE",
    "UNKNOWN",
    "GroupID",
    "GroupIter",
    "GroupStat",
    "create",
    "get_objinfo",
    "iterate",
    "open",
    "phil",
    "sys",
    "with_phil",
]

_R = TypeVar("_R")

UNKNOWN: Final[int]
LINK: Final[int]
GROUP: Final[int]
DATASET: Final[int]
TYPE: Final[int]
LINK_ERROR: Final[int]
LINK_HARD: Final[int]
LINK_SOFT: Final[int]

def create(
    loc: ObjectID,
    name: bytes | None,
    lcpl: PropLCID | None = None,
    gcpl: PropGCID | None = None,
) -> GroupID: ...
def open(loc: ObjectID, name: bytes) -> GroupID: ...
def get_objinfo(
    obj: ObjectID,
    name: bytes = b".",
    follow_link: bool = True,
) -> GroupStat: ...
def iterate(
    loc: GroupID,
    func: Callable[[bytes], _R | None],
    startidx: int = 0,
    *,
    obj_name: bytes = b".",
) -> _R: ...

class GroupStat:
    @property
    def fileno(self) -> tuple[int, int]: ...
    @property
    def objno(self) -> tuple[int, int]: ...
    @property
    def nlink(self) -> int: ...
    @property
    def type(self) -> int: ...
    @property
    def mtime(self) -> int: ...
    @property
    def linklen(self) -> int: ...

class GroupIter:
    def __init__(self, grp: GroupID, reversed: bool = False) -> None: ...
    def __iter__(self) -> GroupIter: ...
    def __next__(self) -> bytes: ...

class GroupID(ObjectID):
    def __init__(self, id_: int) -> None: ...
    def link(
        self,
        current_name: bytes,
        new_name: bytes,
        link_type: int = ...,
        remote: GroupID | None = None,
    ) -> None: ...
    def unlink(self, name: bytes) -> None: ...
    def move(
        self,
        current_name: bytes,
        new_name: bytes,
        remote: GroupID | None = None,
    ) -> None: ...
    def get_num_objs(self) -> int: ...
    def get_objname_by_idx(self, idx: int) -> bytes: ...
    def get_objtype_by_idx(self, idx: int) -> int: ...
    def get_linkval(self, name: bytes) -> bytes: ...
    def get_create_plist(self) -> PropGCID: ...
    def set_comment(self, name: bytes, comment: bytes) -> None: ...
    def get_comment(self, name: bytes) -> bytes: ...
    def __contains__(self, name: bytes) -> bool: ...
    def __iter__(self) -> GroupIter: ...
    def __reversed__(self) -> GroupIter: ...
    def __len__(self) -> int: ...
