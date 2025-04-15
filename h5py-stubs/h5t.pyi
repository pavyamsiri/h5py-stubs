import codecs
import platform
import sys
from collections import namedtuple
from typing import Any, Final, Literal, NamedTuple, TypeAlias, TypeVar, overload

import numpy as np
from h5py.h5p import PropDXID
from numpy.dtypes import BytesDType, ObjectDType
from numpy.typing import NBitBase

from ._objects import ObjectID, phil, with_phil
from .h5 import H5PYConfig, get_config
from .h5r import Reference, RegionReference

_Encoding: TypeAlias = Literal["ascii", "utf-8"]
_GT = TypeVar("_GT", bound=Any, default=Any)
_IT = TypeVar("_IT", bound=np.integer[NBitBase], default=np.integer[NBitBase])
_GenericIntDType: TypeAlias = np.dtype[_IT]
_GenericArray: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[Any]]

cfg: Final[H5PYConfig]
ref_dtype: Final[ObjectDType]
regionref_dtype: Final[ObjectDType]

# check_dtype overloads
# Case 1: vlen = dtype
@overload
def check_dtype(*, vlen: np.dtype[Any]) -> np.dtype[Any] | None: ...

# Case 2: enum = dtype
@overload
def check_dtype(*, enum: np.dtype[Any]) -> dict[str, int] | None: ...

# Case 3: ref = dtype
@overload
def check_dtype(*, ref: np.dtype[Any]) -> type[Reference | RegionReference] | None: ...

# end check_dtype overloads

# special_dtype overloads
# Case 1: vlen = basetype
@overload
def special_dtype(*, vlen: type[str] | np.dtype[Any]) -> ObjectDType: ...

# Case 2: enum = (basetype, value_dict)
@overload
def special_dtype(*, enum: tuple[_GenericIntDType[_IT], dict[str, int]]) -> _GenericIntDType[_IT]: ...

# Case 3: ref = Reference | RegionReference
@overload
def special_dtype(*, ref: type[Reference | RegionReference]) -> ObjectDType: ...

# end special_dtype overloads

# enum_dtype overloads
# Case 1: basetype is given
@overload
def enum_dtype(values_dict: dict[str, int], basetype: _GenericIntDType[_IT]) -> _GenericIntDType[_IT]: ...

# Case 2: basetype is defaulted
@overload
def enum_dtype(values_dict: dict[str, int], basetype: _GenericIntDType = ...) -> _GenericIntDType: ...

# end enum_dtype overloads
# string_dtype overloads
# Case 1: length is given
@overload
def string_dtype(encoding: _Encoding, length: int) -> BytesDType[Any]: ...

# Case 2: length is defaulted
@overload
def string_dtype(encoding: _Encoding = "utf-8", length: Literal[None] = None) -> ObjectDType: ...

# end string_dtype overloads
def check_enum_dtype(dt: np.dtype[Any]) -> dict[str, int] | None: ...
def check_opaque_dtype(dt: np.dtype[Any]) -> bool: ...
def check_ref_dtype(dt: np.dtype[Any]) -> type[Reference | RegionReference] | None: ...
def check_string_dtype(dt: np.dtype[Any]) -> string_info: ...
def check_vlen_dtype(dt: np.dtype[Any]) -> np.dtype[Any] | None: ...
def opaque_dtype(np_dtype: np.dtype[_GT]) -> np.dtype[_GT]: ...
def vlen_dtype(basetype: ObjectDType) -> ObjectDType: ...
def convert(
    src: TypeID,
    dst: TypeID,
    n: int,
    buf: _GenericArray,
    bkg: _GenericArray | None = None,
    dxpl: PropDXID | None = None,
) -> None: ...
def find(src: TypeID, dst: TypeID) -> tuple[int, ...] | None: ...
def open(group: ObjectID, name: bytes, tapl: ObjectID | None = None) -> TypeID: ...
def create(classtype: int, size: int) -> TypeID: ...
def decode(buf: bytes) -> TypeID: ...
def typewrap(id_: int) -> TypeID: ...
def array_create(base: TypeID, dims_tpl: tuple[int, ...]) -> TypeArrayID: ...
def py_create(dtype_in: np.dtype[Any] | str, logical: bool = False, aligned: bool = False) -> TypeID: ...
def vlen_create(base: TypeID) -> TypeID: ...
def enum_create(base: TypeID) -> TypeID: ...

class string_info(NamedTuple):
    encoding: _Encoding
    length: int | None

class TypeID(ObjectID): ...

# --- Top-level classes ---

class TypeArrayID(TypeID): ...
class TypeOpaqueID(TypeID): ...

class TypeStringID(TypeID):
    # Both vlen and fixed-len strings
    ...

class TypeVlenID(TypeID):
    # Non-string vlens
    ...

class TypeTimeID(TypeID): ...
class TypeBitfieldID(TypeID): ...
class TypeReferenceID(TypeID): ...

# --- Numeric atomic types ---

class TypeAtomicID(TypeID): ...
class TypeIntegerID(TypeAtomicID): ...
class TypeFloatID(TypeAtomicID): ...

# --- Enums & compound types ---

class TypeCompositeID(TypeID): ...
class TypeEnumID(TypeCompositeID): ...
class TypeCompoundID(TypeCompositeID): ...

ARRAY: Final[int]
BITFIELD: Final[int]
BKG_NO: Final[int]
BKG_TEMP: Final[int]
BKG_YES: Final[int]
COMPOUND: Final[int]
CSET_ASCII: Final[int]
CSET_UTF8: Final[int]
C_S1: Final[TypeStringID]
DIR_ASCEND: Final[int]
DIR_DEFAULT: Final[int]
DIR_DESCEND: Final[int]
ENUM: Final[int]
FLOAT: Final[int]
FORTRAN_S1: Final[TypeStringID]
IEEE_F128BE: Final[TypeFloatID]
IEEE_F128LE: Final[TypeFloatID]
IEEE_F16BE: Final[TypeFloatID]
IEEE_F16LE: Final[TypeFloatID]
IEEE_F32BE: Final[TypeFloatID]
IEEE_F32LE: Final[TypeFloatID]
IEEE_F64BE: Final[TypeFloatID]
IEEE_F64LE: Final[TypeFloatID]
INTEGER: Final[int]
LDOUBLE_BE: Final[TypeFloatID]
LDOUBLE_LE: Final[TypeFloatID]
NATIVE_B16: Final[TypeBitfieldID]
NATIVE_B32: Final[TypeBitfieldID]
NATIVE_B64: Final[TypeBitfieldID]
NATIVE_B8: Final[TypeBitfieldID]
NATIVE_DOUBLE: Final[TypeFloatID]
NATIVE_FLOAT: Final[TypeFloatID]
NATIVE_FLOAT16: Final[TypeFloatID]
NATIVE_INT16: Final[TypeIntegerID]
NATIVE_INT32: Final[TypeIntegerID]
NATIVE_INT64: Final[TypeIntegerID]
NATIVE_INT8: Final[TypeIntegerID]
NATIVE_LDOUBLE: Final[TypeFloatID]
NATIVE_UINT16: Final[TypeIntegerID]
NATIVE_UINT32: Final[TypeIntegerID]
NATIVE_UINT64: Final[TypeIntegerID]
NATIVE_UINT8: Final[TypeIntegerID]
NORM_IMPLIED: Final[int]
NORM_MSBSET: Final[int]
NORM_NONE: Final[int]
NO_CLASS: Final[int]
OPAQUE: Final[int]
ORDER_BE: Final[int]
ORDER_LE: Final[int]
ORDER_NATIVE: Final[int]
ORDER_NONE: Final[int]
ORDER_VAX: Final[int]
PAD_BACKGROUND: Final[int]
PAD_ONE: Final[int]
PAD_ZERO: Final[int]
PYTHON_OBJECT: Final[TypeOpaqueID]
REFERENCE: Final[int]
SGN_2: Final[int]
SGN_NONE: Final[int]
STD_B16BE: Final[TypeBitfieldID]
STD_B16LE: Final[TypeBitfieldID]
STD_B32BE: Final[TypeBitfieldID]
STD_B32LE: Final[TypeBitfieldID]
STD_B64BE: Final[TypeBitfieldID]
STD_B64LE: Final[TypeBitfieldID]
STD_B8BE: Final[TypeBitfieldID]
STD_B8LE: Final[TypeBitfieldID]
STD_I16BE: Final[TypeIntegerID]
STD_I16LE: Final[TypeIntegerID]
STD_I32BE: Final[TypeIntegerID]
STD_I32LE: Final[TypeIntegerID]
STD_I64BE: Final[TypeIntegerID]
STD_I64LE: Final[TypeIntegerID]
STD_I8BE: Final[TypeIntegerID]
STD_I8LE: Final[TypeIntegerID]
STD_REF_DSETREG: Final[TypeReferenceID]
STD_REF_OBJ: Final[TypeReferenceID]
STD_U16BE: Final[TypeIntegerID]
STD_U16LE: Final[TypeIntegerID]
STD_U32BE: Final[TypeIntegerID]
STD_U32LE: Final[TypeIntegerID]
STD_U64BE: Final[TypeIntegerID]
STD_U64LE: Final[TypeIntegerID]
STD_U8BE: Final[TypeIntegerID]
STD_U8LE: Final[TypeIntegerID]
STRING: Final[int]
STR_NULLPAD: Final[int]
STR_NULLTERM: Final[int]
STR_SPACEPAD: Final[int]
TIME: Final[int]
UNIX_D32BE: Final[TypeTimeID]
UNIX_D32LE: Final[TypeTimeID]
UNIX_D64BE: Final[TypeTimeID]
UNIX_D64LE: Final[TypeTimeID]
VARIABLE: Final[int]
VLEN: Final[int]

__all__ = [
    "ARRAY",
    "BITFIELD",
    "BKG_NO",
    "BKG_TEMP",
    "BKG_YES",
    "COMPOUND",
    "CSET_ASCII",
    "CSET_UTF8",
    "C_S1",
    "DIR_ASCEND",
    "DIR_DEFAULT",
    "DIR_DESCEND",
    "ENUM",
    "FLOAT",
    "FORTRAN_S1",
    "IEEE_F16BE",
    "IEEE_F16LE",
    "IEEE_F32BE",
    "IEEE_F32LE",
    "IEEE_F64BE",
    "IEEE_F64LE",
    "IEEE_F128BE",
    "IEEE_F128LE",
    "INTEGER",
    "LDOUBLE_BE",
    "LDOUBLE_LE",
    "NATIVE_B8",
    "NATIVE_B16",
    "NATIVE_B32",
    "NATIVE_B64",
    "NATIVE_DOUBLE",
    "NATIVE_FLOAT",
    "NATIVE_FLOAT16",
    "NATIVE_INT8",
    "NATIVE_INT16",
    "NATIVE_INT32",
    "NATIVE_INT64",
    "NATIVE_LDOUBLE",
    "NATIVE_UINT8",
    "NATIVE_UINT16",
    "NATIVE_UINT32",
    "NATIVE_UINT64",
    "NORM_IMPLIED",
    "NORM_MSBSET",
    "NORM_NONE",
    "NO_CLASS",
    "OPAQUE",
    "ORDER_BE",
    "ORDER_LE",
    "ORDER_NATIVE",
    "ORDER_NONE",
    "ORDER_VAX",
    "PAD_BACKGROUND",
    "PAD_ONE",
    "PAD_ZERO",
    "PYTHON_OBJECT",
    "REFERENCE",
    "SGN_2",
    "SGN_NONE",
    "STD_B8BE",
    "STD_B8LE",
    "STD_B16BE",
    "STD_B16LE",
    "STD_B32BE",
    "STD_B32LE",
    "STD_B64BE",
    "STD_B64LE",
    "STD_I8BE",
    "STD_I8LE",
    "STD_I16BE",
    "STD_I16LE",
    "STD_I32BE",
    "STD_I32LE",
    "STD_I64BE",
    "STD_I64LE",
    "STD_REF_DSETREG",
    "STD_REF_OBJ",
    "STD_U8BE",
    "STD_U8LE",
    "STD_U16BE",
    "STD_U16LE",
    "STD_U32BE",
    "STD_U32LE",
    "STD_U64BE",
    "STD_U64LE",
    "STRING",
    "STR_NULLPAD",
    "STR_NULLTERM",
    "STR_SPACEPAD",
    "TIME",
    "UNIX_D32BE",
    "UNIX_D32LE",
    "UNIX_D64BE",
    "UNIX_D64LE",
    "VARIABLE",
    "VLEN",
    "TypeArrayID",
    "TypeAtomicID",
    "TypeBitfieldID",
    "TypeCompositeID",
    "TypeCompoundID",
    "TypeEnumID",
    "TypeFloatID",
    "TypeID",
    "TypeIntegerID",
    "TypeOpaqueID",
    "TypeReferenceID",
    "TypeStringID",
    "TypeTimeID",
    "TypeVlenID",
    "array_create",
    "cfg",
    "check_dtype",
    "check_enum_dtype",
    "check_opaque_dtype",
    "check_ref_dtype",
    "check_string_dtype",
    "check_vlen_dtype",
    "codecs",
    "convert",
    "create",
    "decode",
    "enum_create",
    "enum_dtype",
    "find",
    "get_config",
    "namedtuple",
    "np",
    "opaque_dtype",
    "open",
    "phil",
    "platform",
    "py_create",
    "ref_dtype",
    "regionref_dtype",
    "special_dtype",
    "string_dtype",
    "string_info",
    "sys",
    "typewrap",
    "vlen_create",
    "vlen_dtype",
    "with_phil",
]
