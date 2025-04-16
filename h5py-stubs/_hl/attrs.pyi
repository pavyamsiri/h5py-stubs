import uuid
from typing import TypeAlias

import numpy  # noqa: ICN001
from h5py import h5, h5a, h5p, h5s, h5t
from h5py._objects import phil, with_phil
from h5py.h5a import AttrID
from optype import numpy as onpt

from . import base
from .base import CommonStateObject, Empty, HLObject, MutableMappingHDF5, is_empty_dataspace, product
from .datatype import Datatype

__all__ = [
    "AttributeManager",
    "Datatype",
    "Empty",
    "base",
    "h5",
    "h5a",
    "h5p",
    "h5s",
    "h5t",
    "is_empty_dataspace",
    "numpy",
    "phil",
    "product",
    "uuid",
    "with_phil",
]

_AnyShape: TypeAlias = tuple[int, ...]
_AnyArray: TypeAlias = numpy.ndarray[_AnyShape, onpt.DType]
_Attribute: TypeAlias = Empty | _AnyArray | numpy.generic

class AttributeManager(MutableMappingHDF5[str | bytes, _Attribute], CommonStateObject):
    def __init__(self, parent: HLObject) -> None: ...
    def __getitem__(self, name: str | bytes) -> _Attribute: ...
    def get_id(self, name: str | bytes) -> AttrID: ...
    def __setitem__(self, name: str | bytes, value: object) -> None: ...
    def __delitem__(self, name: str | bytes) -> None: ...
    def create(
        self,
        name: str | bytes,
        data: object,
        shape: tuple[int, ...] | int | None = None,
        dtype: Datatype | onpt.AnyDType | None = None,
    ) -> None: ...
    def modify(self, name: str | bytes, value: object) -> None: ...
