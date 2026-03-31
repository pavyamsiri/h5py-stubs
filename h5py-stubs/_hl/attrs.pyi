from collections.abc import Iterator
from typing import override

from h5py.h5a import AttrID
from optype import numpy as onp

from .base import CommonStateObject, Empty, HLObject, MutableMappingHDF5
from .datatype import Datatype

__all__ = ["AttributeManager"]

type _Attribute = object | onp.AnyArray | Empty

class AttributeManager(MutableMappingHDF5[str | bytes, _Attribute], CommonStateObject):
    def __init__(self, parent: HLObject) -> None: ...
    def get_id(self, name: str | bytes) -> AttrID: ...
    def create(
        self,
        name: str | bytes,
        data: object,
        shape: tuple[int, ...] | int | None = None,
        dtype: Datatype | onp.AnyDType | None = None,
    ) -> None: ...
    def modify(self, name: str | bytes, value: object) -> None: ...
    @override
    def __getitem__(self, name: str | bytes) -> _Attribute: ...
    @override
    def __setitem__(self, name: str | bytes, value: object) -> None: ...
    @override
    def __delitem__(self, name: str | bytes) -> None: ...
    @override
    def __len__(self) -> int: ...
    @override
    def __iter__(self) -> Iterator[str]: ...
    @override
    def __contains__(self, name: object) -> bool: ...
