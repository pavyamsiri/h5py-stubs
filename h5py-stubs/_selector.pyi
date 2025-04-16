from types import EllipsisType
from typing import TypeAlias, TypeVar

import numpy as np
import optype as op
from numpy.typing import NBitBase
from optype import numpy as onpt

from .h5d import DatasetID
from .h5s import SpaceID

__all__ = [
    "MultiBlockSlice",
    "Reader",
    "Selector",
    "np",
]

_AnyShape: TypeAlias = tuple[int, ...]
_SCT = TypeVar("_SCT", bound=np.generic, default=np.generic)
_AnyArray: TypeAlias = np.ndarray[_AnyShape, np.dtype[_SCT]]
_Array1D: TypeAlias = np.ndarray[tuple[int], np.dtype[_SCT]]
_SelectorArg: TypeAlias = (
    EllipsisType
    | slice[int]
    | op.CanInt[int]
    | MultiBlockSlice
    | _Array1D[np.integer[NBitBase]]
    | onpt.ToArray1D[np.integer[NBitBase]]
)

class MultiBlockSlice:
    start: int
    stride: int
    count: int | None
    block: int

    def __init__(
        self,
        start: int = 0,
        stride: int = 1,
        count: int | None = None,
        block: int = 1,
    ) -> None: ...
    def indices(self, length: int) -> tuple[int, int, int, int]: ...

class Selector:
    def __init__(self, space: SpaceID) -> None: ...
    def make_selection(self, args: tuple[_SelectorArg, ...]) -> None: ...

class Reader:
    def __init__(self, dsid: DatasetID) -> None: ...
    def read(self, args: tuple[_SelectorArg, ...]) -> np.generic | _AnyArray: ...
