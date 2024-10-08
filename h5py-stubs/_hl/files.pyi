from collections.abc import Callable
from typing import Concatenate, Final, Literal

from _typeshed import StrOrBytesPath
from h5py._hl.attrs import AttributeManager
from h5py.h5f import FileID
from h5py.h5p import PropFAID, PropFCID
from optype import CanInt
from typing_extensions import Self  # noqa: UP035

from .group import Group

mpi: Final[bool]

type _Driver = Callable[Concatenate[PropFAID, ...], None]
type _Libver = Literal["earliest", "latest", "v108", "v110"]

def register_driver(name: str, set_fapl: _Driver) -> None: ...
def unregister_driver(name: str) -> None: ...
def registered_drivers() -> frozenset[str]: ...
def make_fapl(
    driver: str | None,
    libver: _Libver | tuple[_Libver, _Libver] | None,
    rdcc_nslots: int | None,
    rdcc_nbytes: int | None,
    rdcc_w0: int | None,
    locking: bool | Literal["true", "false", "best-effort"],
    page_buf_size: CanInt | None,
    min_meta_keep: CanInt | None,
    min_raw_keep: CanInt | None,
    alignment_threshold: int,
    alignment_interval: int,
    meta_block_size: CanInt | None,
    **kwds: object,
) -> PropFAID: ...
def make_fcpl(
    track_order: bool = False,
    fs_strategy: Literal["fsm", "page", "aggregate", "none"] | None = None,
    fs_persist: bool = False,
    fs_threshold: int = 1,
    fs_page_size: CanInt | None = None,
) -> PropFCID | None: ...
def make_fid(
    name: str,
    mode: Literal["r", "r+", "w-", "x", "w", "a"],
    userblock_size: int | None,
    fapl: PropFAID | None,
    fcpl: PropFCID | None = None,
    swmr: bool = False,
) -> FileID: ...

class File(Group):
    @property
    def attrs(self) -> AttributeManager: ...
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
        name: StrOrBytesPath,
        mode: Literal["r", "r+", "w-", "x", "w", "a"],
        driver: str | None = None,
        libver: _Libver | tuple[_Libver, _Libver] | None = None,
        userblock_size: int | None = None,
        swmr: bool = False,
        rdcc_nslots: int | None = None,
        rdcc_nbytes: int | None = None,
        rdcc_w0: int | None = None,
        track_order: bool | None = None,
        fs_strategy: Literal["fsm", "page", "aggregate", "none"] | None = None,
        fs_persist: bool = False,
        fs_threshold: int = 1,
        fs_page_size: int | None = None,
        page_buf_size: int | None = None,
        min_meta_keep: int = 0,
        min_raw_keep: int = 0,
        locking: bool | Literal["true", "false", "best-effort"] | None = None,
        alignment_threshold: int = 1,
        alignment_interval: int = 1,
        meta_block_size: int | None = None,
        **kwds: object,
    ) -> None: ...
    def close(self) -> None: ...
    def flush(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: object) -> None: ...
