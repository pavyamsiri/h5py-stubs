from collections.abc import Iterator

import numpy as np
from h5py.h5a import AttrID
from optype import numpy as onpt

from .base import CommonStateObject, Empty, HLObject, MutableMappingHDF5

type _AnyShape = tuple[int, ...]
type _AnyArray = np.ndarray[_AnyShape, onpt.DType]

class AttributeManager(MutableMappingHDF5, CommonStateObject):
    def __init__(self, parent: HLObject) -> None: ...
    def __getitem__(self, name: str | bytes) -> np.generic | _AnyArray | Empty: ...
    def get_id(self, name: str | bytes) -> AttrID: ...
    def __setitem__(self, name: str | bytes, value: object) -> None: ...
    def __delitem__(self, name: str | bytes) -> None: ...
    def create(
        self, name: str | bytes, data: object, shape: tuple[int, ...] | None = None, dtype: onpt.AnyDType | None = None
    ) -> None: ...
    def modify(self, name: str | bytes, value: object) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
    def __contains__(self, name: object) -> bool: ...
