from typing import Any, TypeAlias

import numpy as np

_NDArray: TypeAlias = np.ndarray[Any, Any]

def check_numpy_read(arr: _NDArray, space_id: int = ...) -> int: ...
def check_numpy_write(arr: _NDArray, space_id: int = ...) -> int: ...
