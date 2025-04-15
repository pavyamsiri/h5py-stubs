from typing import TypeAlias

import numpy as np
from optype import numpy as onpt

_AnyShape: TypeAlias = tuple[int, ...]
_AnyArray: TypeAlias = np.ndarray[_AnyShape, onpt.DType]

def check_numpy_read(arr: _AnyArray, space_id: int = ...) -> int: ...
def check_numpy_write(arr: _AnyArray, space_id: int = ...) -> int: ...
