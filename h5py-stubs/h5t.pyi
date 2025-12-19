import codecs
import platform
from typing import Any, Final, Literal, NamedTuple, overload

import numpy as np
from numpy.dtypes import BytesDType, ObjectDType
from optype import numpy as onp

from ._objects import ObjectID
from .h5 import H5PYConfig, get_config
from .h5f import FileID
from .h5g import GroupID
from .h5p import PropDXID, PropLCID, PropTCID
from .h5r import Reference, RegionReference

type _Encoding = Literal["ascii", "utf-8"]

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
def special_dtype[Int: np.int64](*, enum: tuple[onp.DType[Int], dict[str, int]]) -> onp.DType[Int]: ...

# Case 3: ref = Reference | RegionReference
@overload
def special_dtype(*, ref: type[Reference | RegionReference]) -> ObjectDType: ...

# end special_dtype overloads

# enum_dtype overloads
# Case 1: basetype is given
@overload
def enum_dtype[Int: np.int64](values_dict: dict[str, int], basetype: onp.DType[Int]) -> onp.DType[Int]: ...

# Case 2: basetype is defaulted
@overload
def enum_dtype(values_dict: dict[str, int], basetype: onp.DType[np.integer] = ...) -> onp.DType[np.integer]: ...

# end enum_dtype overloads
# string_dtype overloads
# Case 1: length is given
@overload
def string_dtype(encoding: _Encoding, length: int) -> BytesDType[Any]: ...

# Case 2: length is defaulted
@overload
def string_dtype(encoding: _Encoding = "utf-8", length: None = None) -> ObjectDType: ...

# end string_dtype overloads
def check_enum_dtype(dt: np.dtype[Any]) -> dict[str, int] | None: ...
def check_opaque_dtype(dt: np.dtype[Any]) -> bool: ...
def check_ref_dtype(dt: np.dtype[Any]) -> type[Reference | RegionReference] | None: ...
def check_string_dtype(dt: np.dtype[Any]) -> string_info: ...
def check_vlen_dtype(dt: np.dtype[Any]) -> np.dtype[Any] | None: ...
def opaque_dtype[G: np.generic](np_dtype: np.dtype[G]) -> np.dtype[G]: ...
def vlen_dtype(basetype: ObjectDType) -> ObjectDType: ...
def convert(
    src: TypeID,
    dst: TypeID,
    n: int,
    buf: onp.Array,
    bkg: onp.Array | None = None,
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

class TypeID(ObjectID):
    @property
    def dtype(self) -> np.dtype[Any]: ...
    def commit(self, group: FileID | GroupID, name: bytes, lcpl: PropLCID | None = None) -> None: ...
    def committed(self) -> bool: ...
    def copy(self) -> TypeID: ...
    def equal(self, typeid: TypeID) -> bool: ...
    def lock(self) -> None: ...
    def get_class(self) -> int: ...
    def get_size(self) -> int: ...
    def set_size(self, size: int) -> None: ...
    def get_super(self) -> TypeID: ...
    def detect_class(self, classtype: int) -> bool: ...
    def encode(self) -> bytes: ...
    def get_create_plist(self) -> PropTCID: ...

# --- Top-level classes ---

class TypeArrayID(TypeID):
    def get_array_ndims(self) -> int: ...
    def get_array_dims(self) -> tuple[int, ...]: ...

class TypeOpaqueID(TypeID):
    def set_tag(self, tag: bytes) -> None: ...
    def get_tag(self) -> bytes: ...

# Both vlen and fixed-len strings
class TypeStringID(TypeID):
    def is_variable_str(self) -> bool: ...
    def get_cset(self) -> int: ...
    def set_cset(self, cset: int) -> None: ...
    def get_strpad(self) -> int: ...
    def set_strpad(self, pad: int) -> None: ...

# Non-string vlens
class TypeVlenID(TypeID): ...
class TypeTimeID(TypeID): ...

class TypeBitfieldID(TypeID):
    def get_order(self) -> int: ...

class TypeReferenceID(TypeID): ...

# --- Numeric atomic types ---

class TypeAtomicID(TypeID):
    def get_order(self) -> int: ...
    def set_order(self, order: int) -> None: ...
    def get_precision(self) -> int: ...
    def set_precision(self, precision: int) -> None: ...
    def get_offset(self) -> int: ...
    def set_offset(self, offset: int) -> None: ...
    def get_pad(self) -> tuple[int, int]: ...
    def set_pad(self, lsb: int, msb: int) -> None: ...

class TypeIntegerID(TypeAtomicID):
    def get_sign(self) -> int: ...
    def set_sign(self, sign: int) -> None: ...

class TypeFloatID(TypeAtomicID):
    def get_fields(self) -> tuple[int, int, int, int, int]: ...
    def set_fields(self, spos: int, epos: int, esize: int, mpos: int, msize: int) -> None: ...
    def get_ebias(self) -> int: ...
    def set_ebias(self, ebias: int) -> None: ...
    def get_norm(self) -> int: ...
    def set_norm(self, norm: int) -> None: ...
    def get_inpad(self) -> int: ...
    def set_inpad(self, pad_code: int) -> None: ...

# --- Enums & compound types ---

class TypeCompositeID(TypeID):
    def get_nmembers(self) -> int: ...
    def get_member_name(self, member: int) -> bytes: ...
    def get_member_index(self, name: bytes) -> int: ...

class TypeCompoundID(TypeCompositeID):
    def get_member_class(self, member: int) -> int: ...
    def get_member_offset(self, member: int) -> int: ...
    def get_member_type(self, member: int) -> TypeID: ...
    def insert(self, name: bytes, offset: int, field: TypeID) -> None: ...
    def pack(self) -> None: ...

class TypeEnumID(TypeCompositeID):
    def enum_insert(self, name: bytes, value: int) -> None: ...
    def enum_nameof(self, value: int) -> bytes: ...
    def enum_valueof(self, name: bytes) -> int: ...
    def get_member_value(self, idx: int) -> int: ...

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
    "opaque_dtype",
    "open",
    "platform",
    "py_create",
    "ref_dtype",
    "regionref_dtype",
    "special_dtype",
    "string_dtype",
    "string_info",
    "typewrap",
    "vlen_create",
    "vlen_dtype",
]
