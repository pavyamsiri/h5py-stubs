import atexit
from warnings import warn as _warn

from . import _errors, h5a, h5d, h5ds, h5f, h5fd, h5g, h5p, h5pl, h5r, h5s, h5t, h5z, utils, version
from ._conv import register_converters as _register_converters
from ._conv import unregister_converters as _unregister_converters
from ._hl import filters
from ._hl.attrs import AttributeManager
from ._hl.base import Empty, HLObject, is_hdf5
from ._hl.dataset import Dataset
from ._hl.datatype import Datatype
from ._hl.files import File, register_driver, registered_drivers, unregister_driver
from ._hl.group import ExternalLink, Group, HardLink, SoftLink
from ._hl.vds import VirtualLayout, VirtualSource
from ._selector import MultiBlockSlice
from .h5 import get_config
from .h5r import Reference, RegionReference
from .h5s import UNLIMITED
from .h5t import (
    check_dtype,
    check_enum_dtype,
    check_opaque_dtype,
    check_ref_dtype,
    check_string_dtype,
    check_vlen_dtype,
    enum_dtype,
    opaque_dtype,
    ref_dtype,
    regionref_dtype,
    special_dtype,
    string_dtype,
    vlen_dtype,
)
from .h5z import _register_lzf
from .version import version as __version__

def run_tests(args: str = ...) -> int: ...
def enable_ipython_completer() -> None: ...

__all__ = [
    "AttributeManager",
    "Dataset",
    "Datatype",
    "Empty",
    "ExternalLink",
    "File",
    "Group",
    "HLObject",
    "HardLink",
    "MultiBlockSlice",
    "Reference",
    "RegionReference",
    "SoftLink",
    "UNLIMITED",
    "VirtualLayout",
    "VirtualSource",
    "atexit",
    "check_dtype",
    "check_enum_dtype",
    "check_opaque_dtype",
    "check_ref_dtype",
    "check_string_dtype",
    "check_vlen_dtype",
    "defs",
    "enable_ipython_completer",
    "enum_dtype",
    "filters",
    "get_config",
    "h5",
    "h5a",
    "h5ac",
    "h5d",
    "h5ds",
    "h5f",
    "h5fd",
    "h5g",
    "h5i",
    "h5l",
    "h5o",
    "h5p",
    "h5pl",
    "h5py_warnings",
    "h5r",
    "h5s",
    "h5t",
    "h5z",
    "is_hdf5",
    "opaque_dtype",
    "ref_dtype",
    "regionref_dtype",
    "register_driver",
    "registered_drivers",
    "run_tests",
    "special_dtype",
    "string_dtype",
    "unregister_driver",
    "utils",
    "version",
    "vlen_dtype",
]
