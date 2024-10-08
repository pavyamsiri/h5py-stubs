from h5py._objects import ObjectID
from h5py.h5p import PropID

class AttrID(ObjectID): ...

def open(
    loc: ObjectID,
    name: bytes = b"",
    index: int = -1,
    *,
    obj_name: bytes = b".",
    index_type: int = ...,
    order: int = ...,
    lapl: PropID | None = None,
) -> AttrID: ...
