import posixpath as pp
from typing import TypeVar

import numpy as np
from h5py._objects import with_phil
from h5py.h5t import TypeID

from .base import HLObject

__all__ = [
    "Datatype",
    "HLObject",
    "TypeID",
    "pp",
    "with_phil",
]

_SCT = TypeVar("_SCT", bound=np.generic, default=np.generic)

class Datatype(HLObject):
    @property
    def dtype(self) -> np.dtype[_SCT]: ...
    def __init__(self, bind: TypeID) -> None: ...
