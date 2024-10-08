from collections.abc import Callable
from typing import Concatenate, Final, Literal

from typing_extensions import Self  # noqa: UP035

from h5py.h5p import PropFAID

from .group import Group

mpi: Final[bool]

type _Driver = Callable[Concatenate[PropFAID, ...], None]

def register_driver(name: str, set_fapl: _Driver) -> None: ...
def unregister_driver(name: str) -> None: ...
def registered_drivers() -> frozenset[str]: ...
def make_fapl(
    driver,
    libver,
    rdcc_nslots,
    rdcc_nbytes,
    rdcc_w0,
    locking,
    page_buf_size,
    min_meta_keep,
    min_raw_keep,
    alignment_threshold,
    alignment_interval,
    meta_block_size,
    **kwds,
): ...
def make_fcpl(track_order=..., fs_strategy=..., fs_persist=..., fs_threshold=..., fs_page_size=...):  # -> None:
    ...
def make_fid(name, mode, userblock_size, fapl, fcpl=..., swmr=...): ...

class File(Group):
    @property
    def attrs(self):  # -> AttributeManager:
        ...
    @property
    def filename(self) -> str: ...
    @property
    def driver(self) -> str: ...
    @property
    def mode(self) -> Literal["r+", "r"]: ...
    @property
    def libver(self) -> tuple[str, str]: ...
    @property
    def userblock_size(self) -> int: ...
    @property
    def meta_block_size(self) -> int: ...
    @property
    def atomic(self) -> bool: ...
    @atomic.setter
    def atomic(self, value: bool) -> None: ...
    @property
    def swmr_mode(self) -> bool: ...
    @swmr_mode.setter
    def swmr_mode(self, value: bool) -> None: ...
    def __init__(
        self,
        name,
        mode=...,
        driver=...,
        libver=...,
        userblock_size=...,
        swmr=...,
        rdcc_nslots=...,
        rdcc_nbytes=...,
        rdcc_w0=...,
        track_order=...,
        fs_strategy=...,
        fs_persist=...,
        fs_threshold=...,
        fs_page_size=...,
        page_buf_size=...,
        min_meta_keep=...,
        min_raw_keep=...,
        locking=...,
        alignment_threshold=...,
        alignment_interval=...,
        meta_block_size=...,
        **kwds,
    ) -> None: ...
    def close(self) -> None: ...
    def flush(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: object) -> None: ...
