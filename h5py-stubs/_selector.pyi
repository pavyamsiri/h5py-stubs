from types import EllipsisType

import numpy as np
import optype as op
from optype import numpy as onp

from .h5d import DatasetID
from .h5s import SpaceID

__all__ = [
    "MultiBlockSlice",
    "Reader",
    "Selector",
    "np",
]

type _SelectorArg = EllipsisType | slice[int] | op.CanInt | MultiBlockSlice | onp.Array1D[np.integer] | onp.ToArray1D[np.integer]

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
    def read(self, args: tuple[_SelectorArg, ...]) -> np.generic | onp.AnyArray: ...
