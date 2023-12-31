from ... import types as sqltypes
from _typeshed import Incomplete

class JSONPathType(sqltypes.JSON.JSONPathType):
    def bind_processor(self, dialect): ...
    def literal_processor(self, dialect): ...

class JSONPATH(JSONPathType):
    __visit_name__: str

class JSON(sqltypes.JSON):
    astext_type: Incomplete
    def __init__(self, none_as_null: bool = ..., astext_type: Incomplete | None = ...) -> None: ...
    class Comparator(sqltypes.JSON.Comparator):
        @property
        def astext(self): ...
    comparator_factory = Comparator

class JSONB(JSON):
    __visit_name__: str
    class Comparator(JSON.Comparator):
        def has_key(self, other): ...
        def has_all(self, other): ...
        def has_any(self, other): ...
        def contains(self, other, **kwargs): ...
        def contained_by(self, other): ...
        def delete_path(self, array): ...
        def path_exists(self, other): ...
        def path_match(self, other): ...
    comparator_factory = Comparator
