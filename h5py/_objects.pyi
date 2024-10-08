from collections.abc import Callable
from typing import TypeVar

_R = TypeVar("_R")

def with_phil(func: Callable[..., _R]) -> Callable[..., _R]: ...
