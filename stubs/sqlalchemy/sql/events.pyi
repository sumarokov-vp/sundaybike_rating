from .. import event as event
from ..engine.base import Connection as Connection
from ..engine.interfaces import ReflectedColumn as ReflectedColumn
from ..engine.reflection import Inspector as Inspector
from .base import SchemaEventTarget as SchemaEventTarget
from .schema import Column as Column, Constraint as Constraint, SchemaItem as SchemaItem, Table as Table
from typing import Any

class DDLEvents(event.Events[SchemaEventTarget]):
    def before_create(self, target: SchemaEventTarget, connection: Connection, **kw: Any) -> None: ...
    def after_create(self, target: SchemaEventTarget, connection: Connection, **kw: Any) -> None: ...
    def before_drop(self, target: SchemaEventTarget, connection: Connection, **kw: Any) -> None: ...
    def after_drop(self, target: SchemaEventTarget, connection: Connection, **kw: Any) -> None: ...
    def before_parent_attach(self, target: SchemaEventTarget, parent: SchemaItem) -> None: ...
    def after_parent_attach(self, target: SchemaEventTarget, parent: SchemaItem) -> None: ...
    def column_reflect(self, inspector: Inspector, table: Table, column_info: ReflectedColumn) -> None: ...
