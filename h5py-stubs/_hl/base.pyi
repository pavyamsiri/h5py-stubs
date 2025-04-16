import abc
import os
import posixpath
from collections.abc import Callable, ItemsView, Iterable, KeysView, Mapping, MutableMapping, ValuesView
from typing import Any, Generic, TypeAlias, TypeVar, overload

import numpy as np
from _typeshed import StrOrBytesPath
from h5py import h5d, h5f, h5i, h5p, h5r, h5s, h5t
from h5py._hl.attrs import AttributeManager
from h5py._hl.files import File
from h5py._hl.group import Group
from h5py._objects import ObjectID, phil, with_phil
from h5py.h5a import AttrID
from h5py.h5p import PropLAID, PropLCID
from h5py.h5r import Reference
from optype import numpy as onpt
from typing_extensions import Self  # noqa: UP035

from .compat import filename_encode, fspath

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
    "filename_encode",
    "find_item_type",
    "fspath",
    "guess_dtype",
    "h5d",
    "h5f",
    "h5i",
    "h5p",
    "h5r",
    "h5s",
    "h5t",
    "is_empty_dataspace",
    "is_float16_dtype",
    "is_hdf5",
    "np",
    "os",
    "phil",
    "posixpath",
    "product",
    "with_phil",
]

_K = TypeVar("_K")
_V = TypeVar("_V")
_T = TypeVar("_T")

_SCT = TypeVar("_SCT", bound=np.generic, default=np.generic)
_AnyShape: TypeAlias = tuple[int, ...]
_AnyArray: TypeAlias = np.ndarray[_AnyShape, np.dtype[_SCT]]

dlapl: PropLAID | None
dlcpl: PropLCID | None

def is_hdf5(fname: StrOrBytesPath) -> bool: ...
def find_item_type(data: object) -> type | None: ...
def guess_dtype(data: object) -> onpt.DType | None: ...
def is_float16_dtype(dt: onpt.AnyDType | None) -> bool: ...
def default_lapl() -> PropLAID | None: ...
def default_lcpl() -> PropLCID | None: ...
def is_empty_dataspace(obj: AttrID | h5d.DatasetID) -> bool: ...
def product(nums: Iterable[int]) -> int: ...

# array_for_new_object overloads
# Case 1: Specified dtype is float16
@overload
def array_for_new_object(
    data: object,
    specified_dtype: type[np.dtype[np.float16]],
) -> _AnyArray[np.float16]: ...

# Case 2: data is an array; specified dtype is ignored
@overload
def array_for_new_object(
    data: _AnyArray[_SCT],
    specified_dtype: type[np.dtype[Any]] | None = None,
) -> _AnyArray[_SCT]: ...

# Case 3: data is an array-like (not array) and specified dtype is given
@overload
def array_for_new_object(
    data: object,
    specified_dtype: type[np.dtype[_SCT]],
) -> _AnyArray[_SCT]: ...

# Case 4: data is an array-like (not array) and specified dtype is not given
@overload
def array_for_new_object(
    data: object,
    specified_dtype: None = None,
) -> _AnyArray: ...

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

class KeysViewHDF5(KeysView[_K]): ...
class ValuesViewHDF5(ValuesView[_V]): ...
class ItemsViewHDF5(ItemsView[_K, _V]): ...

class MappingHDF5(Mapping[_K, _V], metaclass=abc.ABCMeta):
    def keys(self) -> KeysViewHDF5[_K]: ...
    def values(self) -> ValuesViewHDF5[_V]: ...
    def items(self) -> ItemsViewHDF5[_K, _V]: ...

class MutableMappingHDF5(MappingHDF5[_K, _V], MutableMapping[_K, _V], metaclass=abc.ABCMeta): ...

class Empty:
    shape: None = None
    size: None = None
    def __init__(self, dtype: onpt.AnyDType) -> None: ...

class cached_property(Generic[_T]):
    def __init__(self, func: Callable[..., _T]) -> None: ...
    def __get__(self, obj: object, cls: type) -> Self | _T: ...
