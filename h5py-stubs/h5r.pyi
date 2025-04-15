from typing import Final

from ._objects import ObjectID, phil, with_phil
from .h5p import PropID
from .h5s import SpaceID

__all__ = [
    "DATASET_REGION",
    "OBJECT",
    "Reference",
    "RegionReference",
    "create",
    "dereference",
    "get_name",
    "get_obj_type",
    "get_region",
    "phil",
    "with_phil",
]

OBJECT: Final[int]
DATASET_REGION: Final[int]

def create(loc: ObjectID, name: str, ref_type: int, space: SpaceID | None = None) -> Reference: ...
def get_region(ref: Reference, id: ObjectID) -> SpaceID | None: ...
def get_name(ref: Reference, loc: ObjectID) -> bytes: ...
def get_obj_type(ref: Reference, id: ObjectID) -> int | None: ...
def dereference(ref: Reference, id: ObjectID, oapl: PropID | None = None) -> ObjectID | None: ...

class Reference:
    @property
    def typecode(self) -> int: ...
    @property
    def typesize(self) -> int: ...

class RegionReference(Reference): ...
