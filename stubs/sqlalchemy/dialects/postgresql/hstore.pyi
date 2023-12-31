from ... import types as sqltypes
from ...sql import functions as sqlfunc
from _typeshed import Incomplete

class HSTORE(sqltypes.Indexable, sqltypes.Concatenable, sqltypes.TypeEngine):
    __visit_name__: str
    hashable: bool
    text_type: Incomplete
    def __init__(self, text_type: Incomplete | None = ...) -> None: ...
    class Comparator(sqltypes.Indexable.Comparator, sqltypes.Concatenable.Comparator):
        def has_key(self, other): ...
        def has_all(self, other): ...
        def has_any(self, other): ...
        def contains(self, other, **kwargs): ...
        def contained_by(self, other): ...
        def defined(self, key): ...
        def delete(self, key): ...
        def slice(self, array): ...
        def keys(self): ...
        def vals(self): ...
        def array(self): ...
        def matrix(self): ...
    comparator_factory = Comparator
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class hstore(sqlfunc.GenericFunction):
    type = HSTORE
    name: str
    inherit_cache: bool

class _HStoreDefinedFunction(sqlfunc.GenericFunction):
    type = sqltypes.Boolean
    name: str
    inherit_cache: bool

class _HStoreDeleteFunction(sqlfunc.GenericFunction):
    type = HSTORE
    name: str
    inherit_cache: bool

class _HStoreSliceFunction(sqlfunc.GenericFunction):
    type = HSTORE
    name: str
    inherit_cache: bool

class _HStoreKeysFunction(sqlfunc.GenericFunction):
    type: Incomplete
    name: str
    inherit_cache: bool

class _HStoreValsFunction(sqlfunc.GenericFunction):
    type: Incomplete
    name: str
    inherit_cache: bool

class _HStoreArrayFunction(sqlfunc.GenericFunction):
    type: Incomplete
    name: str
    inherit_cache: bool

class _HStoreMatrixFunction(sqlfunc.GenericFunction):
    type: Incomplete
    name: str
    inherit_cache: bool
