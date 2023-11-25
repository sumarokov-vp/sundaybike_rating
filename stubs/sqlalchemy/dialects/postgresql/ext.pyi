from . import types as types
from ...sql import coercions as coercions, elements as elements, expression as expression, functions as functions, roles as roles, schema as schema
from ...sql.schema import ColumnCollectionConstraint as ColumnCollectionConstraint
from ...sql.sqltypes import TEXT as TEXT
from ...sql.visitors import InternalTraversal as InternalTraversal
from .array import ARRAY as ARRAY
from _typeshed import Incomplete

class aggregate_order_by(expression.ColumnElement):
    __visit_name__: str
    stringify_dialect: str
    target: Incomplete
    type: Incomplete
    order_by: Incomplete
    def __init__(self, target, *order_by) -> None: ...
    def self_group(self, against: Incomplete | None = ...): ...
    def get_children(self, **kwargs): ...

class ExcludeConstraint(ColumnCollectionConstraint):
    __visit_name__: str
    where: Incomplete
    inherit_cache: bool
    create_drop_stringify_dialect: str
    operators: Incomplete
    using: Incomplete
    ops: Incomplete
    def __init__(self, *elements, **kw) -> None: ...

def array_agg(*arg, **kw): ...

class _regconfig_fn(functions.GenericFunction[_T]):
    inherit_cache: bool
    def __init__(self, *args, **kwargs) -> None: ...

class to_tsvector(_regconfig_fn):
    inherit_cache: bool
    type = types.TSVECTOR

class to_tsquery(_regconfig_fn):
    inherit_cache: bool
    type = types.TSQUERY

class plainto_tsquery(_regconfig_fn):
    inherit_cache: bool
    type = types.TSQUERY

class phraseto_tsquery(_regconfig_fn):
    inherit_cache: bool
    type = types.TSQUERY

class websearch_to_tsquery(_regconfig_fn):
    inherit_cache: bool
    type = types.TSQUERY

class ts_headline(_regconfig_fn):
    inherit_cache: bool
    type = TEXT
    def __init__(self, *args, **kwargs) -> None: ...
