import gc
import warnings
import weakref
from collections.abc import Callable
from typing import Final

from ._locks import BogoLock, FastRLock

__all__ = [
    "BogoLock",
    "FastRLock",
    "ObjectID",
    "gc",
    "nonlocal_close",
    "phil",
    "print_reg",
    "warnings",
    "weakref",
    "with_phil",
]

phil: Final[FastRLock]

def nonlocal_close() -> None: ...
def print_reg() -> None: ...
def with_phil[R](func: Callable[..., R]) -> Callable[..., R]: ...

class ObjectID:
    @property
    def fileno(self) -> tuple[int, int]: ...
    @property
    def valid(self) -> bool: ...
    @property
    def id(self) -> int: ...
    @property
    def locked(self) -> int: ...
    def close(self) -> None: ...
