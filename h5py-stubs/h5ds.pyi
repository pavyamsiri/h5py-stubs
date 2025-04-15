from collections.abc import Callable
from typing import TypeVar

from ._objects import phil, with_phil
from .h5d import DatasetID

__all__ = [
    "attach_scale",
    "detach_scale",
    "get_label",
    "get_num_scales",
    "get_scale_name",
    "is_attached",
    "is_scale",
    "iterate",
    "phil",
    "set_label",
    "set_scale",
    "with_phil",
]

_R = TypeVar("_R")

def set_scale(dset: DatasetID, dimname: bytes = b"") -> None: ...
def is_scale(dset: DatasetID) -> bool: ...
def attach_scale(dset: DatasetID, dscale: DatasetID, idx: int) -> None: ...
def is_attached(dset: DatasetID, dscale: DatasetID, idx: int) -> bool: ...
def detach_scale(dset: DatasetID, dscale: DatasetID, idx: int) -> None: ...
def get_num_scales(dset: DatasetID, dim: int) -> int: ...
def set_label(dset: DatasetID, idx: int, label: bytes) -> None: ...
def get_label(dset: DatasetID, idx: int) -> bytes: ...
def get_scale_name(dscale: DatasetID) -> bytes: ...
def iterate(
    dset: DatasetID,
    dim: int,
    func: Callable[[bytes], _R | None],
    startidx: int = 0,
) -> _R: ...
