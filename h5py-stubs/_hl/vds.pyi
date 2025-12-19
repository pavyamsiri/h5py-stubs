from typing import NamedTuple

import numpy as np
from h5py.h5d import DatasetID
from h5py.h5s import SpaceID

from .dataset import Dataset

__all__ = ["VDSmap", "VirtualLayout", "VirtualSource", "vds_support"]

type _DType = np.dtype[np.generic]

class VDSmap(NamedTuple):
    vspace: SpaceID
    file_name: str
    dset_name: str
    src_space: SpaceID

vds_support: bool = ...

class VirtualSource:
    def __init__(
        self,
        path_or_dataset: Dataset | str,
        name: str | None = None,
        shape: tuple[int, ...] | None = None,
        dtype: _DType | None = None,
        maxshape: tuple[int, ...] | None = None,
    ) -> None: ...
    @property
    def shape(self) -> tuple[int, ...]: ...
    def __getitem__(self, key: object) -> VirtualSource: ...

class VirtualLayout:
    def __init__(
        self,
        shape: int | tuple[int, ...],
        dtype: _DType,
        maxshape: int | tuple[int, ...] | None = None,
        filename: str | None = None,
    ) -> None: ...
    def __setitem__(self, key: object, source: VirtualSource) -> None: ...
    def make_dataset(self, parent: Dataset, name: str | None, fillvalue: object | None = None) -> DatasetID: ...
