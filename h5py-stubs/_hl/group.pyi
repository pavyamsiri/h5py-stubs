from collections.abc import Callable, Generator, Iterator
from contextlib import contextmanager
from typing import TypeVar

import numpy as np
from _typeshed import StrOrBytesPath
from h5py._hl.vds import VirtualLayout
from h5py.h5g import GroupID
from h5py.h5r import Reference
from optype import CanStr
from optype import numpy as onpt

from .base import HLObject, MutableMappingHDF5
from .dataset import Dataset
from .datatype import Datatype

_R = TypeVar("_R")
type _DType = np.dtype[np.generic]
type _AnyShape = tuple[int, ...]
type _AnyArray = np.ndarray[_AnyShape, _DType]

type GroupGetResult = (
    type[Group | Dataset | Datatype | SoftLink | ExternalLink | HardLink]
    | Group
    | Dataset
    | Datatype
    | SoftLink
    | ExternalLink
    | HardLink
)

class Group(HLObject, MutableMappingHDF5):
    def __init__(self, bind: GroupID) -> None: ...
    def create_group(self, name: str | bytes, track_order: bool | None = None) -> Group: ...
    def create_dataset(
        self,
        name: str | bytes | None,
        shape: tuple[int, ...] | None = None,
        dtype: onpt.AnyDType | None = None,
        data: _AnyArray | None = None,
        **kwds: object,
    ) -> Dataset: ...
    def create_virtual_dataset(
        self, name: str | bytes | None, layout: VirtualLayout, fillvalue: object | None = None
    ) -> Dataset: ...
    @contextmanager
    def build_virtual_dataset(
        self,
        name: str,
        shape: tuple[int, ...],
        dtype: onpt.DType,
        maxshape: tuple[int, ...] | None = None,
        fillvalue: object | None = None,
    ) -> Generator[VirtualLayout, None, None]: ...
    def require_dataset(
        self, name: str | bytes, shape: tuple[int, ...], dtype: onpt.DType, exact: bool = False, **kwds: object
    ) -> Dataset: ...
    def create_dataset_like(self, name: str | bytes | None, other: Dataset, **kwupdate: object) -> Dataset: ...
    def require_group(self, name: str | bytes | Reference) -> Group: ...
    def __getitem__(self, name: str | bytes | Reference) -> Group | Dataset | Datatype: ...
    def get(
        self, name: str | bytes | Reference, default: object | None = None, getclass: bool = False, getlink: bool = False
    ) -> GroupGetResult | None: ...
    def __setitem__(self, name: str | bytes, obj: object) -> None: ...
    def __delitem__(self, name: str | bytes) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
    def __reversed__(self) -> Iterator[str]: ...
    def __contains__(self, name: object) -> bool: ...
    def copy(
        self,
        source: str | Group | Dataset | Datatype,
        dest: str | Group,
        name: str | None = None,
        shallow: bool = False,
        expand_soft: bool = False,
        expand_external: bool = False,
        expand_refs: bool = False,
        without_attrs: bool = False,
    ) -> None: ...
    def move(self, source: str | bytes, dest: str | bytes) -> None: ...
    def visit(self, func: Callable[[str], _R | None]) -> _R | None: ...
    def visititems(self, func: Callable[[str, object], _R | None]) -> _R | None: ...
    def visit_links(self, func: Callable[[str], _R | None]) -> _R | None: ...
    def visititems_links(self, func: Callable[[str, object], _R | None]) -> _R | None: ...

class HardLink: ...

class SoftLink:
    @property
    def path(self) -> str: ...
    def __init__(self, path: CanStr) -> None: ...

class ExternalLink:
    @property
    def path(self) -> str: ...
    @property
    def filename(self) -> str: ...
    def __init__(self, filename: StrOrBytesPath, path: str) -> None: ...
