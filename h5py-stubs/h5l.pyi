from collections.abc import Callable
from typing import Final, Literal, TypeVar, overload

from ._objects import phil, with_phil
from .h5g import GroupID
from .h5p import PropID

__all__ = [
    "TYPE_EXTERNAL",
    "TYPE_HARD",
    "TYPE_SOFT",
    "LinkInfo",
    "LinkProxy",
    "phil",
    "with_phil",
]

_R = TypeVar("_R")

TYPE_HARD: Final[int]
TYPE_SOFT: Final[int]
TYPE_EXTERNAL: Final[int]

class LinkInfo:
    @property
    def type(self) -> int: ...
    @property
    def corder_valid(self) -> bool: ...
    @property
    def corder(self) -> int: ...
    @property
    def cset(self) -> int: ...
    @property
    def u(self) -> int: ...

class LinkProxy:
    def __init__(self, id: int) -> None: ...
    def create_hard(
        self,
        new_name: bytes,
        cur_loc: GroupID,
        cur_name: bytes,
        lcpl: PropID | None = None,
        lapl: PropID | None = None,
    ) -> None: ...
    def create_soft(
        self,
        new_name: bytes,
        target: bytes,
        lcpl: PropID | None = None,
        lapl: PropID | None = None,
    ) -> None: ...
    def create_external(
        self,
        link_name: bytes,
        file_name: bytes,
        obj_name: bytes,
        lcpl: PropID | None = None,
        lapl: PropID | None = None,
    ) -> None: ...
    def get_val(
        self,
        name: bytes,
        lapl: PropID | None = None,
    ) -> bytes | tuple[bytes, bytes]: ...
    def move(
        self,
        src_name: bytes,
        dst_loc: GroupID,
        dst_name: bytes,
        lcpl: PropID | None = None,
        lapl: PropID | None = None,
    ) -> None: ...
    def exists(self, name: bytes, lapl: PropID | None = None) -> bool: ...
    def get_info(
        self,
        name: bytes,
        index: int = -1,
        *,
        lapl: PropID | None = None,
    ) -> LinkInfo: ...

    # visit overloads
    @overload
    def visit(
        self,
        func: Callable[[bytes], _R | None | Literal[False]],
        *,
        idx_type: int = ...,
        order: int = ...,
        obj_name: bytes = b".",
        lapl: PropID | None = None,
        info: bool = False,
    ) -> _R: ...
    @overload
    def visit(
        self,
        func: Callable[[bytes, LinkInfo], _R | None | Literal[False]],
        *,
        idx_type: int = ...,
        order: int = ...,
        obj_name: bytes = b".",
        lapl: PropID | None = None,
        info: bool = True,
    ) -> _R: ...

    # iterate overloads
    @overload
    def iterate(
        self,
        func: Callable[[bytes], _R | None | Literal[False]],
        *,
        idx_type: int = ...,
        order: int = ...,
        obj_name: bytes = b".",
        lapl: PropID | None = None,
        info: bool = False,
        idx: int = 0,
    ) -> tuple[_R, int]: ...
    @overload
    def iterate(
        self,
        func: Callable[[bytes, LinkInfo], _R | None | Literal[False]],
        *,
        idx_type: int = ...,
        order: int = ...,
        obj_name: bytes = b".",
        lapl: PropID | None = None,
        info: bool = True,
        idx: int = 0,
    ) -> tuple[_R, int]: ...
