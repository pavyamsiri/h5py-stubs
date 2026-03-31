from collections.abc import Callable
from typing import overload

import numpy as np
from optype import numpy as onp

from ._objects import ObjectID, phil, with_phil
from .h5p import PropLAID
from .h5s import SpaceID
from .h5t import TypeID

__all__ = [
    "AttrID",
    "AttrInfo",
    "create",
    "delete",
    "exists",
    "get_info",
    "get_num_attrs",
    "iterate",
    "open",
    "phil",
    "rename",
    "with_phil",
]

def open(
    loc: ObjectID,
    name: bytes = b"",
    index: int = -1,
    *,
    obj_name: bytes = b".",
    index_type: int = ...,
    order: int = ...,
    lapl: PropLAID | None = None,
) -> AttrID: ...
def exists(loc: ObjectID, name: bytes, *, obj_name: bytes = b"", lapl: PropLAID | None = None) -> bool: ...
def rename(loc: ObjectID, name: bytes, new_name: bytes, *, obj_name: bytes = b".", lapl: PropLAID | None = None) -> None: ...
def create(
    loc: ObjectID, name: bytes, tid: TypeID, space: SpaceID, *, obj_name: bytes = b".", lapl: PropLAID | None = None
) -> AttrID: ...
def delete(
    loc: ObjectID,
    name: bytes = b"",
    index: int = -1,
    *,
    obj_name: bytes = b".",
    index_type: int = ...,
    order: int = ...,
    lapl: PropLAID | None = None,
) -> None: ...
def get_info(
    loc: ObjectID,
    name: bytes = b"",
    index: int = -1,
    *,
    obj_name: bytes = b".",
    lapl: PropLAID | None = None,
    index_type: int = ...,
    order: int = ...,
) -> AttrInfo: ...
def get_num_attrs(loc: ObjectID) -> int: ...

# iterate overloads
# Case 1: info = False
@overload
def iterate[R](
    loc: ObjectID,
    func: Callable[[bytes], R],
    index: int = 0,
    *,
    index_type: int = ...,
    order: int = ...,
    info: bool = False,
) -> R: ...

# Case 1: info = True
@overload
def iterate[R](
    loc: ObjectID,
    func: Callable[[bytes, AttrInfo], R],
    index: int = 0,
    *,
    index_type: int = ...,
    order: int = ...,
    info: bool = True,
) -> R: ...

class AttrInfo:
    @property
    def corder_valid(self) -> bool: ...
    @property
    def corder(self) -> int: ...
    @property
    def cset(self) -> int: ...
    @property
    def data_size(self) -> int: ...

class AttrID(ObjectID):
    @property
    def name(self) -> bytes: ...
    @property
    def shape(self) -> tuple[int, ...] | None: ...
    @property
    def dtype(self) -> np.dtype[np.generic]: ...
    def read(self, arr: onp.Array, mtype: TypeID | None = None) -> None: ...
    def write(self, arr: onp.Array, mtype: TypeID | None = None) -> None: ...
    def get_name(self) -> bytes: ...
    def get_shape(self) -> SpaceID: ...
    def get_dtype(self) -> TypeID: ...
    def get_storage_size(self) -> int: ...
