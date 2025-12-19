from collections.abc import Callable, Generator, Iterator
from contextlib import contextmanager
from typing import override

from _typeshed import StrOrBytesPath
from h5py._hl.vds import VirtualLayout
from h5py.h5g import GroupID
from h5py.h5r import Reference
from optype import CanStr
from optype import numpy as onp

from .base import HLObject, MutableMappingHDF5
from .dataset import Dataset
from .datatype import Datatype

__all__ = ["ExternalLink", "Group", "HardLink", "SoftLink"]

type _GroupKey = str | bytes | Reference
type _GroupGetResult = (
    type[Group | Dataset | Datatype | SoftLink | ExternalLink | HardLink]
    | Group
    | Dataset
    | Datatype
    | SoftLink
    | ExternalLink
    | HardLink
)

class Group(HLObject, MutableMappingHDF5[_GroupKey, _GroupGetResult | None]):
    def __init__(self, bind: GroupID) -> None: ...
    def create_group(self, name: str | bytes, track_order: bool | None = None) -> Group: ...
    def create_dataset(
        self,
        name: str | bytes | None,
        shape: tuple[int, ...] | None = None,
        dtype: onp.AnyDType | None = None,
        data: onp.AnyArray | None = None,
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
        dtype: onp.DType,
        maxshape: tuple[int, ...] | None = None,
        fillvalue: object | None = None,
    ) -> Generator[VirtualLayout, None, None]: ...
    def require_dataset(
        self, name: str | bytes, shape: tuple[int, ...], dtype: onp.DType, exact: bool = False, **kwds: object
    ) -> Dataset: ...
    def create_dataset_like(self, name: str | bytes | None, other: Dataset, **kwupdate: object) -> Dataset: ...
    def require_group(self, name: str | bytes | Reference) -> Group: ...
    @override
    def get(
        self, name: str | bytes | Reference, default: object | None = None, getclass: bool = False, getlink: bool = False
    ) -> _GroupGetResult | None: ...
    @override
    def __getitem__(self, name: str | bytes | Reference) -> Group | Dataset | Datatype: ...
    @override
    def __setitem__(self, name: _GroupKey, obj: object) -> None: ...
    @override
    def __delitem__(self, name: _GroupKey) -> None: ...
    @override
    def __len__(self) -> int: ...
    @override
    def __iter__(self) -> Iterator[str]: ...
    def __reversed__(self) -> Iterator[str]: ...
    @override
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
    def visit[R](self, func: Callable[[str], R | None]) -> R | None: ...
    def visititems[R](self, func: Callable[[str, object], R | None]) -> R | None: ...
    def visit_links[R](self, func: Callable[[str], R | None]) -> R | None: ...
    def visititems_links[R](self, func: Callable[[str, object], R | None]) -> R | None: ...

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
