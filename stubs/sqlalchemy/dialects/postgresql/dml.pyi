from ...sql._typing import _DMLTableArgument
from ...sql.base import ReadOnlyColumnCollection
from ...sql.dml import Insert as StandardInsert
from ...sql.elements import ClauseElement, KeyedColumnElement
from ...util.typing import Self
from .._typing import _OnConflictConstraintT, _OnConflictIndexElementsT, _OnConflictIndexWhereT, _OnConflictSetT, _OnConflictWhereT
from _typeshed import Incomplete
from typing import Any, Optional

def insert(table: _DMLTableArgument) -> Insert: ...

class Insert(StandardInsert):
    stringify_dialect: str
    inherit_cache: bool
    def excluded(self) -> ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]: ...
    def on_conflict_do_update(self, constraint: _OnConflictConstraintT = ..., index_elements: _OnConflictIndexElementsT = ..., index_where: _OnConflictIndexWhereT = ..., set_: _OnConflictSetT = ..., where: _OnConflictWhereT = ...) -> Self: ...
    def on_conflict_do_nothing(self, constraint: _OnConflictConstraintT = ..., index_elements: _OnConflictIndexElementsT = ..., index_where: _OnConflictIndexWhereT = ...) -> Self: ...

class OnConflictClause(ClauseElement):
    stringify_dialect: str
    constraint_target: Optional[str]
    inferred_target_elements: _OnConflictIndexElementsT
    inferred_target_whereclause: _OnConflictIndexWhereT
    def __init__(self, constraint: _OnConflictConstraintT = ..., index_elements: _OnConflictIndexElementsT = ..., index_where: _OnConflictIndexWhereT = ...) -> None: ...

class OnConflictDoNothing(OnConflictClause):
    __visit_name__: str

class OnConflictDoUpdate(OnConflictClause):
    __visit_name__: str
    update_values_to_set: Incomplete
    update_whereclause: Incomplete
    def __init__(self, constraint: _OnConflictConstraintT = ..., index_elements: _OnConflictIndexElementsT = ..., index_where: _OnConflictIndexWhereT = ..., set_: _OnConflictSetT = ..., where: _OnConflictWhereT = ...) -> None: ...
