from ...sql._typing import _DMLTableArgument
from ...sql.base import ReadOnlyColumnCollection
from ...sql.dml import Insert as StandardInsert
from ...sql.elements import ClauseElement, KeyedColumnElement
from ...sql.selectable import NamedFromClause
from ...util.typing import Self
from _typeshed import Incomplete
from typing import Any

def insert(table: _DMLTableArgument) -> Insert: ...

class Insert(StandardInsert):
    stringify_dialect: str
    inherit_cache: bool
    @property
    def inserted(self) -> ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]: ...
    def inserted_alias(self) -> NamedFromClause: ...
    def on_duplicate_key_update(self, *args: _UpdateArg, **kw: Any) -> Self: ...

class OnDuplicateClause(ClauseElement):
    __visit_name__: str
    stringify_dialect: str
    inserted_alias: Incomplete
    update: Incomplete
    def __init__(self, inserted_alias: NamedFromClause, update: _UpdateArg) -> None: ...
