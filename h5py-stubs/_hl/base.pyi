import abc
from collections.abc import Callable, ItemsView, Iterable, Iterator, KeysView, Mapping, MutableMapping, ValuesView
from typing import overload, override

import numpy as np
from _typeshed import StrOrBytesPath
from h5py._hl.attrs import AttributeManager
from h5py._hl.files import File
from h5py._hl.group import Group
from h5py._objects import ObjectID
from h5py.h5p import PropLAID, PropLCID
from h5py.h5r import Reference
from optype import numpy as onp
from typing_extensions import Self  # noqa: UP035

__all__ = [
    "CommonStateObject",
    "Empty",
    "HLObject",
    "ItemsView",
    "ItemsViewHDF5",
    "KeysView",
    "KeysViewHDF5",
    "Mapping",
    "MappingHDF5",
    "MutableMapping",
    "MutableMappingHDF5",
    "ValuesView",
    "ValuesViewHDF5",
    "array_for_new_object",
    "cached_property",
    "default_lapl",
    "default_lcpl",
    "dlapl",
    "dlcpl",
    "find_item_type",
    "guess_dtype",
    "is_float16_dtype",
    "is_hdf5",
    "product",
]

dlapl: PropLAID | None
dlcpl: PropLCID | None

def is_hdf5(fname: StrOrBytesPath) -> bool: ...
def find_item_type(data: object) -> type | None: ...
def guess_dtype(data: object) -> onp.DType | None: ...
def is_float16_dtype(dt: onp.AnyDType | None) -> bool: ...
def default_lapl() -> PropLAID | None: ...
def default_lcpl() -> PropLCID | None: ...

# array_for_new_object overloads
# Case 1: Specified dtype is float16
@overload
def array_for_new_object(
    data: object,
    specified_dtype: type[np.dtype[np.float16]],
) -> onp.AnyArray[np.float16]: ...

# Case 2: data is an array; specified dtype is ignored
@overload
def array_for_new_object[SCT: np.generic](
    data: onp.AnyArray[SCT],
    specified_dtype: type[onp.DType] | None = None,
) -> onp.AnyArray[SCT]: ...

# Case 3: data is an array-like (not array) and specified dtype is given
@overload
def array_for_new_object[SCT: np.generic](
    data: object,
    specified_dtype: type[np.dtype[SCT]],
) -> onp.AnyArray[SCT]: ...

# Case 4: data is an array-like (not array) and specified dtype is not given
@overload
def array_for_new_object(
    data: object,
    specified_dtype: None = None,
) -> onp.AnyArray: ...

# end array_for_new_object overloads

class CommonStateObject: ...

class _RegionProxy:
    def __init__(self, obj: ObjectID) -> None: ...
    def __getitem__(self, args: object) -> Reference: ...
    def shape(self, ref: Reference) -> tuple[int, ...]: ...
    def selection(self, ref: Reference) -> tuple[int, ...]: ...

class HLObject(CommonStateObject):
    @property
    def file(self) -> File: ...
    @property
    def name(self) -> str | None: ...
    @property
    def parent(self) -> Group: ...
    @property
    def id(self) -> ObjectID: ...
    @property
    def ref(self) -> Reference: ...
    @property
    def regionref(self) -> _RegionProxy: ...
    @property
    def attrs(self) -> AttributeManager: ...
    def __init__(self, oid: ObjectID) -> None: ...

class KeysViewHDF5[K](KeysView[K]):
    @override
    def __iter__(self) -> Iterator[K]: ...
    def __reversed__(self) -> Iterator[K]: ...

class ValuesViewHDF5[V](ValuesView[V]):
    @override
    def __contains__(self, value: object) -> bool: ...
    @override
    def __iter__(self) -> Iterator[V]: ...
    def __reversed__(self) -> Iterator[V]: ...

class ItemsViewHDF5[K, V](ItemsView[K, V]):
    @override
    def __contains__(self, item: object) -> bool: ...
    @override
    def __iter__(self) -> Iterator[tuple[K, V]]: ...
    def __reversed__(self) -> Iterator[tuple[K, V]]: ...

class MappingHDF5[K, V](Mapping[K, V], metaclass=abc.ABCMeta):
    @override
    def keys(self) -> KeysViewHDF5[K]: ...
    @override
    def values(self) -> ValuesViewHDF5[V]: ...
    @override
    def items(self) -> ItemsViewHDF5[K, V]: ...

class MutableMappingHDF5[K, V](MappingHDF5[K, V], MutableMapping[K, V], metaclass=abc.ABCMeta): ...

class Empty:
    shape: None = None
    size: None = None
    def __init__(self, dtype: onp.AnyDType) -> None: ...
    @override
    def __eq__(self, other: object) -> bool: ...

def product(nums: Iterable[int]) -> int: ...

class cached_property[T]:
    def __init__(self, func: Callable[..., T]) -> None: ...
    def __get__(self, obj: object, cls: type) -> Self | T: ...
