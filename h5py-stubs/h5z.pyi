from typing import Final

from ._objects import phil, with_phil

__all__ = [
    "CLASS_T_VERS",
    "DISABLE_EDC",
    "ENABLE_EDC",
    "ERROR_EDC",
    "FILTER_ALL",
    "FILTER_CONFIG_DECODE_ENABLED",
    "FILTER_CONFIG_ENCODE_ENABLED",
    "FILTER_DEFLATE",
    "FILTER_ERROR",
    "FILTER_FLETCHER32",
    "FILTER_LZF",
    "FILTER_MAX",
    "FILTER_NBIT",
    "FILTER_NONE",
    "FILTER_RESERVED",
    "FILTER_SCALEOFFSET",
    "FILTER_SHUFFLE",
    "FILTER_SZIP",
    "FLAG_DEFMASK",
    "FLAG_INVMASK",
    "FLAG_MANDATORY",
    "FLAG_OPTIONAL",
    "FLAG_REVERSE",
    "FLAG_SKIP_EDC",
    "NO_EDC",
    "SO_FLOAT_DSCALE",
    "SO_FLOAT_ESCALE",
    "SO_INT",
    "SO_INT_MINBITS_DEFAULT",
    "SZIP_ALLOW_K13_OPTION_MASK",
    "SZIP_CHIP_OPTION_MASK",
    "SZIP_EC_OPTION_MASK",
    "SZIP_MAX_PIXELS_PER_BLOCK",
    "SZIP_NN_OPTION_MASK",
    "filter_avail",
    "get_filter_info",
    "phil",
    "register_filter",
    "unregister_filter",
    "with_phil",
]

CLASS_T_VERS: Final[int]
DISABLE_EDC: Final[int]
ENABLE_EDC: Final[int]
ERROR_EDC: Final[int]
FILTER_ALL: Final[int]
FILTER_CONFIG_DECODE_ENABLED: Final[int]
FILTER_CONFIG_ENCODE_ENABLED: Final[int]
FILTER_DEFLATE: Final[int]
FILTER_ERROR: Final[int]
FILTER_FLETCHER32: Final[int]
FILTER_LZF: Final[int]
FILTER_MAX: Final[int]
FILTER_NBIT: Final[int]
FILTER_NONE: Final[int]
FILTER_RESERVED: Final[int]
FILTER_SCALEOFFSET: Final[int]
FILTER_SHUFFLE: Final[int]
FILTER_SZIP: Final[int]
FLAG_DEFMASK: Final[int]
FLAG_INVMASK: Final[int]
FLAG_MANDATORY: Final[int]
FLAG_OPTIONAL: Final[int]
FLAG_REVERSE: Final[int]
FLAG_SKIP_EDC: Final[int]
NO_EDC: Final[int]
SO_FLOAT_DSCALE: Final[int]
SO_FLOAT_ESCALE: Final[int]
SO_INT: Final[int]
SO_INT_MINBITS_DEFAULT: Final[int]
SZIP_ALLOW_K13_OPTION_MASK: Final[int]
SZIP_CHIP_OPTION_MASK: Final[int]
SZIP_EC_OPTION_MASK: Final[int]
SZIP_MAX_PIXELS_PER_BLOCK: Final[int]
SZIP_NN_OPTION_MASK: Final[int]

def filter_avail(filter_code: int) -> bool: ...
def get_filter_info(filter_code: int) -> int: ...
def register_filter(cls_pointer_address: int) -> bool: ...
def unregister_filter(filter_code: int) -> bool: ...
def _register_lzf() -> None: ...
