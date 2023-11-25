import typing
from . import roles as roles
from .. import exc as exc, util as util
from ..engine.base import Connection as Connection
from ..engine.interfaces import CacheStats as CacheStats, CompiledCacheType as CompiledCacheType, Dialect as Dialect, SchemaTranslateMapType as SchemaTranslateMapType
from ..util import topological as topological
from ..util.typing import Protocol as Protocol, Self as Self
from .base import Executable as Executable, SchemaVisitor as SchemaVisitor
from .compiler import Compiled as Compiled, DDLCompiler as DDLCompiler
from .elements import BindParameter as BindParameter, ClauseElement as ClauseElement
from .schema import Constraint as Constraint, ForeignKeyConstraint as ForeignKeyConstraint, SchemaItem as SchemaItem, Sequence as Sequence, Table as Table
from .selectable import TableClause as TableClause
from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, Callable, Iterable, List, Optional, Sequence as typing_Sequence, Tuple

class BaseDDLElement(ClauseElement): ...

class DDLIfCallable(Protocol):
    def __call__(self, ddl: BaseDDLElement, target: SchemaItem, bind: Optional[Connection], tables: Optional[List[Table]] = ..., state: Optional[Any] = ..., *, dialect: Dialect, compiler: Optional[DDLCompiler] = ..., checkfirst: bool) -> bool: ...

class DDLIf(typing.NamedTuple):
    dialect: Optional[str]
    callable_: Optional[DDLIfCallable]
    state: Optional[Any]

class ExecutableDDLElement(roles.DDLRole, Executable, BaseDDLElement):
    target: Optional[SchemaItem]
    def against(self, target: SchemaItem) -> Self: ...
    def execute_if(self, dialect: Optional[str] = ..., callable_: Optional[DDLIfCallable] = ..., state: Optional[Any] = ...) -> Self: ...
    def __call__(self, target, bind, **kw) -> None: ...
DDLElement = ExecutableDDLElement

class DDL(ExecutableDDLElement):
    __visit_name__: str
    statement: Incomplete
    context: Incomplete
    def __init__(self, statement, context: Incomplete | None = ...) -> None: ...

class _CreateDropBase(ExecutableDDLElement):
    element: Incomplete
    def __init__(self, element) -> None: ...
    @property
    def stringify_dialect(self): ...

class _CreateBase(_CreateDropBase):
    if_not_exists: Incomplete
    def __init__(self, element, if_not_exists: bool = ...) -> None: ...

class _DropBase(_CreateDropBase):
    if_exists: Incomplete
    def __init__(self, element, if_exists: bool = ...) -> None: ...

class CreateSchema(_CreateBase):
    __visit_name__: str
    stringify_dialect: str
    def __init__(self, name, if_not_exists: bool = ...) -> None: ...

class DropSchema(_DropBase):
    __visit_name__: str
    stringify_dialect: str
    cascade: Incomplete
    def __init__(self, name, cascade: bool = ..., if_exists: bool = ...) -> None: ...

class CreateTable(_CreateBase):
    __visit_name__: str
    columns: Incomplete
    include_foreign_key_constraints: Incomplete
    def __init__(self, element: Table, include_foreign_key_constraints: Optional[typing_Sequence[ForeignKeyConstraint]] = ..., if_not_exists: bool = ...) -> None: ...

class _DropView(_DropBase):
    __visit_name__: str

class CreateConstraint(BaseDDLElement):
    element: Incomplete
    def __init__(self, element: Constraint) -> None: ...

class CreateColumn(BaseDDLElement):
    __visit_name__: str
    element: Incomplete
    def __init__(self, element) -> None: ...

class DropTable(_DropBase):
    __visit_name__: str
    def __init__(self, element: Table, if_exists: bool = ...) -> None: ...

class CreateSequence(_CreateBase):
    __visit_name__: str
    def __init__(self, element: Sequence, if_not_exists: bool = ...) -> None: ...

class DropSequence(_DropBase):
    __visit_name__: str
    def __init__(self, element: Sequence, if_exists: bool = ...) -> None: ...

class CreateIndex(_CreateBase):
    __visit_name__: str
    def __init__(self, element, if_not_exists: bool = ...) -> None: ...

class DropIndex(_DropBase):
    __visit_name__: str
    def __init__(self, element, if_exists: bool = ...) -> None: ...

class AddConstraint(_CreateBase):
    __visit_name__: str
    def __init__(self, element) -> None: ...

class DropConstraint(_DropBase):
    __visit_name__: str
    cascade: Incomplete
    def __init__(self, element, cascade: bool = ..., if_exists: bool = ..., **kw) -> None: ...

class SetTableComment(_CreateDropBase):
    __visit_name__: str

class DropTableComment(_CreateDropBase):
    __visit_name__: str

class SetColumnComment(_CreateDropBase):
    __visit_name__: str

class DropColumnComment(_CreateDropBase):
    __visit_name__: str

class SetConstraintComment(_CreateDropBase):
    __visit_name__: str

class DropConstraintComment(_CreateDropBase):
    __visit_name__: str

class InvokeDDLBase(SchemaVisitor):
    connection: Incomplete
    def __init__(self, connection) -> None: ...
    def with_ddl_events(self, target, **kw) -> None: ...

class InvokeCreateDDLBase(InvokeDDLBase):
    def with_ddl_events(self, target, **kw) -> Generator[None, None, None]: ...

class InvokeDropDDLBase(InvokeDDLBase):
    def with_ddl_events(self, target, **kw) -> Generator[None, None, None]: ...

class SchemaGenerator(InvokeCreateDDLBase):
    checkfirst: Incomplete
    tables: Incomplete
    preparer: Incomplete
    dialect: Incomplete
    memo: Incomplete
    def __init__(self, dialect, connection, checkfirst: bool = ..., tables: Incomplete | None = ..., **kwargs) -> None: ...
    def visit_metadata(self, metadata) -> None: ...
    def visit_table(self, table, create_ok: bool = ..., include_foreign_key_constraints: Incomplete | None = ..., _is_metadata_operation: bool = ...) -> None: ...
    def visit_foreign_key_constraint(self, constraint) -> None: ...
    def visit_sequence(self, sequence, create_ok: bool = ...) -> None: ...
    def visit_index(self, index, create_ok: bool = ...) -> None: ...

class SchemaDropper(InvokeDropDDLBase):
    checkfirst: Incomplete
    tables: Incomplete
    preparer: Incomplete
    dialect: Incomplete
    memo: Incomplete
    def __init__(self, dialect, connection, checkfirst: bool = ..., tables: Incomplete | None = ..., **kwargs) -> None: ...
    def visit_metadata(self, metadata): ...
    def visit_index(self, index, drop_ok: bool = ...) -> None: ...
    def visit_table(self, table, drop_ok: bool = ..., _is_metadata_operation: bool = ..., _ignore_sequences=...) -> None: ...
    def visit_foreign_key_constraint(self, constraint) -> None: ...
    def visit_sequence(self, sequence, drop_ok: bool = ...) -> None: ...

def sort_tables(tables: Iterable[TableClause], skip_fn: Optional[Callable[[ForeignKeyConstraint], bool]] = ..., extra_dependencies: Optional[typing_Sequence[Tuple[TableClause, TableClause]]] = ...) -> List[Table]: ...
def sort_tables_and_constraints(tables, filter_fn: Incomplete | None = ..., extra_dependencies: Incomplete | None = ..., _warn_for_cycles: bool = ...): ...
