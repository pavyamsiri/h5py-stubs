from typing import Final, NamedTuple

class _H5PY_VERSION_CLS(NamedTuple):
    major: int
    minor: int
    bugfix: int
    pre: str | None
    post: int | None
    dev: int | None

hdf5_built_version_tuple: tuple[int, int, int]
version_tuple: _H5PY_VERSION_CLS
version: str
hdf5_version_tuple: tuple[int, int, int]
hdf5_version: str
api_version_tuple: tuple[int, int]
api_version: Final[str]
info: Final[str]
