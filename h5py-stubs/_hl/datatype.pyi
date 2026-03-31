import numpy as np
from h5py.h5t import TypeID

from .base import HLObject

__all__ = ["Datatype"]

type _DType = np.dtype[np.generic]

class Datatype(HLObject):
    @property
    def dtype(self) -> _DType: ...
    def __init__(self, bind: TypeID) -> None: ...
