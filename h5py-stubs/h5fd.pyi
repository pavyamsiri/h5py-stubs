from typing import Final, Literal

__all__ = [
    "CORE",
    "DIRECT",
    "FAMILY",
    "LOG",
    "LOG_ALL",
    "LOG_ALLOC",
    "LOG_FILE_IO",
    "LOG_FILE_READ",
    "LOG_FILE_WRITE",
    "LOG_FLAVOR",
    "LOG_LOC_IO",
    "LOG_LOC_READ",
    "LOG_LOC_SEEK",
    "LOG_LOC_WRITE",
    "LOG_NUM_IO",
    "LOG_NUM_READ",
    "LOG_NUM_SEEK",
    "LOG_NUM_WRITE",
    "LOG_TIME_CLOSE",
    "LOG_TIME_IO",
    "LOG_TIME_OPEN",
    "LOG_TIME_READ",
    "LOG_TIME_SEEK",
    "LOG_TIME_WRITE",
    "MEM_BTREE",
    "MEM_DEFAULT",
    "MEM_DRAW",
    "MEM_GHEAP",
    "MEM_LHEAP",
    "MEM_NTYPES",
    "MEM_OHDR",
    "MEM_SUPER",
    "MPIO",
    "MPIO_COLLECTIVE",
    "MPIO_INDEPENDENT",
    "MPIPOSIX",
    "MULTI",
    "ROS3D",
    "SEC2",
    "STDIO",
    "WINDOWS",
    "fileobj_driver",
]

MEM_DEFAULT: Final[int]
MEM_SUPER: Final[int]
MEM_BTREE: Final[int]
MEM_DRAW: Final[int]
MEM_GHEAP: Final[int]
MEM_LHEAP: Final[int]
MEM_OHDR: Final[int]
MEM_NTYPES: Final[int]

MPIO_INDEPENDENT: Final[int]
MPIO_COLLECTIVE: Final[int]

CORE: Final[int]
FAMILY: Final[int]
LOG: Final[int]
MPIO: Final[int]
MPIPOSIX: Literal[-1]
MULTI: Final[int]
SEC2: Final[int]
DIRECT: Final[int]
STDIO: Final[int]
ROS3D: Final[int]
WINDOWS: Final[int]

LOG_LOC_READ: Literal[0x0001]
LOG_LOC_WRITE: Literal[0x0002]
LOG_LOC_SEEK: Literal[0x0004]
LOG_LOC_IO: Literal[0x0007]

LOG_FILE_READ: Literal[0x0008]
LOG_FILE_WRITE: Literal[0x0010]
LOG_FILE_IO: Literal[0x0018]

LOG_FLAVOR: Literal[0x0020]

LOG_NUM_READ: Literal[0x0040]
LOG_NUM_WRITE: Literal[0x0080]
LOG_NUM_SEEK: Literal[0x0100]
LOG_NUM_IO: Literal[0x01C0]

LOG_TIME_OPEN: Literal[0x0200]
LOG_TIME_READ: Literal[0x0400]
LOG_TIME_WRITE: Literal[0x0800]
LOG_TIME_SEEK: Literal[0x1000]

LOG_TIME_CLOSE: Literal[0x2000]
LOG_TIME_IO: Literal[0x3E00]

LOG_ALLOC: Literal[0x4000]
LOG_ALL: Literal[0x7FFF]

fileobj_driver: Final[int]
