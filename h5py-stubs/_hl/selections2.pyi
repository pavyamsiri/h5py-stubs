from collections.abc import Iterator
from types import EllipsisType

import numpy as np
from h5py.h5d import DatasetID
from h5py.h5s import SpaceID

__all__ = [
    "ScalarReadSelection",
    "read_dtypes",
    "read_selections_scalar",
    "select_read",
]

type _DType = np.dtype[np.generic]

def read_dtypes(dataset_dtype: _DType, names: tuple[str, ...]) -> tuple[_DType, _DType]: ...
def read_selections_scalar(dsid: DatasetID, args: tuple[()] | EllipsisType) -> tuple[tuple[int, ...] | None, SpaceID]: ...

class ScalarReadSelection:
    def __init__(self, fspace: SpaceID, args: tuple[()] | EllipsisType) -> None: ...
    def __iter__(self) -> Iterator[tuple[tuple[int, ...], SpaceID]]: ...

def select_read(fspace: SpaceID, args: tuple[()] | EllipsisType) -> ScalarReadSelection: ...
