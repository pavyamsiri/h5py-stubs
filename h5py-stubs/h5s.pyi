from typing import Final

import numpy as np
from optype import numpy as onp

from ._objects import ObjectID

__all__ = [
    "ALL",
    "NO_CLASS",
    "NULL",
    "SCALAR",
    "SELECT_AND",
    "SELECT_APPEND",
    "SELECT_INVALID",
    "SELECT_NOOP",
    "SELECT_NOTA",
    "SELECT_NOTB",
    "SELECT_OR",
    "SELECT_PREPEND",
    "SELECT_SET",
    "SELECT_XOR",
    "SEL_ALL",
    "SEL_ERROR",
    "SEL_HYPERSLABS",
    "SEL_NONE",
    "SEL_POINTS",
    "SIMPLE",
    "UNLIMITED",
    "SpaceID",
    "create",
    "create_simple",
    "decode",
]

type _Coords = onp.Array2D[np.unsignedinteger]

ALL: Final[SpaceID]
NO_CLASS: Final[int]
NULL: Final[int]
SCALAR: Final[int]
SELECT_AND: Final[int]
SELECT_APPEND: Final[int]
SELECT_INVALID: Final[int]
SELECT_NOOP: Final[int]
SELECT_NOTA: Final[int]
SELECT_NOTB: Final[int]
SELECT_OR: Final[int]
SELECT_PREPEND: Final[int]
SELECT_SET: Final[int]
SELECT_XOR: Final[int]
SEL_ALL: Final[int]
SEL_ERROR: Final[int]
SEL_HYPERSLABS: Final[int]
SEL_NONE: Final[int]
SEL_POINTS: Final[int]
SIMPLE: Final[int]
UNLIMITED: Final[int]

def create(class_code: int) -> SpaceID: ...
def create_simple(dims_tpl: tuple[int, ...], max_dims_tpl: tuple[int, ...] | None = None) -> SpaceID: ...
def decode(buf: bytes) -> SpaceID: ...

class SpaceID(ObjectID):
    @property
    def shape(self) -> tuple[int, ...]: ...
    def get_simple_extent_dims(self) -> tuple[int, ...]: ...
    def copy(self) -> SpaceID: ...
    def encode(self) -> bytes: ...
    def is_simple(self) -> bool: ...
    def offset_simple(self, offset: tuple[int, ...] | None = None) -> None: ...
    def get_simple_extent_ndims(self) -> int: ...
    def get_simple_extent_npoints(self) -> int: ...
    def get_simple_extent_type(self) -> int: ...
    def extent_copy(self, source: SpaceID) -> None: ...
    def set_extent_simple(self, dims_tpl: tuple[int, ...], max_dims_tpl: tuple[int, ...] | None = None) -> None: ...
    def set_extent_none(self) -> None: ...
    def get_select_type(self) -> int: ...
    def get_select_npoints(self) -> int: ...
    def get_select_bounds(self) -> tuple[tuple[int, ...], tuple[int, ...]]: ...
    def select_shape_same(self, space2: SpaceID) -> bool: ...
    def select_all(self) -> None: ...
    def select_none(self) -> None: ...
    def select_valid(self) -> bool: ...
    def get_select_elem_npoints(self) -> int: ...
    def get_select_elem_pointlist(self) -> onp.Array2D[np.uint64]: ...
    def select_elements(self, coords: _Coords, op: int = ...) -> None: ...
    def get_select_hyper_nblocks(self) -> int: ...
    def get_select_hyper_blocklist(self) -> onp.Array3D[np.uint64]: ...
    def select_hyperslab(
        self,
        start: tuple[int, ...],
        count: tuple[int, ...],
        stride: tuple[int, ...] | None = None,
        block: tuple[int, ...] | None = None,
        op: int = ...,
    ) -> None: ...
    def is_regular_hyperslab(self) -> bool: ...
    def get_regular_hyperslab(
        self,
    ) -> tuple[
        tuple[int, ...],
        tuple[int, ...],
        tuple[int, ...],
        tuple[int, ...],
    ]: ...
