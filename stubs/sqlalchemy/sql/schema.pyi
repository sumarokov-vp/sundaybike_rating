from . import coercions as coercions, ddl as ddl, roles as roles, type_api as type_api, visitors as visitors
from .. import event as event, exc as exc, inspection as inspection, util as util
from ..engine import Connection as Connection, Engine as Engine
from ..engine.interfaces import CoreExecuteOptionsParameter as CoreExecuteOptionsParameter, ExecutionContext as ExecutionContext
from ..engine.mock import MockConnection as MockConnection
from ..sql.selectable import FromClause as FromClause
from ..util import HasMemoized as HasMemoized
from ..util.typing import Final as Final, Literal as Literal, Protocol as Protocol, Self as Self, TypeGuard as TypeGuard, TypedDict as TypedDict
from ._typing import _AutoIncrementType, _DDLColumnArgument, _InfoType, _TextCoercedExpressionArgument, _TypeEngineArgument
from .base import DedupeColumnCollection as DedupeColumnCollection, DialectKWArgs as DialectKWArgs, Executable as Executable, ReadOnlyColumnCollection as ReadOnlyColumnCollection, SchemaEventTarget as SchemaEventTarget
from .compiler import DDLCompiler as DDLCompiler
from .elements import BindParameter as BindParameter, ClauseElement as ClauseElement, ColumnClause as ColumnClause, ColumnElement as ColumnElement, TextClause as TextClause, quoted_name as quoted_name
from .functions import Function as Function
from .selectable import TableClause as TableClause
from .type_api import TypeEngine as TypeEngine, to_instance as to_instance
from .visitors import ExternallyTraversible as ExternallyTraversible, InternalTraversal as InternalTraversal, anon_map as anon_map
from _typeshed import Incomplete
from abc import ABC
from enum import Enum
from typing import Any, Callable, Collection, Dict, Iterator, List, Optional, Sequence as _typing_Sequence, Set, Tuple, Union, overload

class SchemaConst(Enum):
    RETAIN_SCHEMA: int
    BLANK_SCHEMA: int
    NULL_UNSPECIFIED: int

RETAIN_SCHEMA: Final[Literal[SchemaConst.RETAIN_SCHEMA]]
BLANK_SCHEMA: Final[Literal[SchemaConst.BLANK_SCHEMA]]
NULL_UNSPECIFIED: Final[Literal[SchemaConst.NULL_UNSPECIFIED]]

class SchemaItem(SchemaEventTarget, visitors.Visitable):
    __visit_name__: str
    create_drop_stringify_dialect: str
    def info(self) -> _InfoType: ...

class HasConditionalDDL:
    def ddl_if(self, dialect: Optional[str] = ..., callable_: Optional[ddl.DDLIfCallable] = ..., state: Optional[Any] = ...) -> Self: ...

class HasSchemaAttr(SchemaItem):
    schema: Optional[str]

class Table(DialectKWArgs, HasSchemaAttr, TableClause, inspection.Inspectable['Table']):
    __visit_name__: str
    def primary_key(self) -> PrimaryKeyConstraint: ...
    def foreign_keys(self) -> Set[ForeignKey]: ...
    constraints: Set[Constraint]
    indexes: Set[Index]
    def columns(self) -> ReadOnlyColumnCollection[str, Column[Any]]: ...
    def exported_columns(self) -> ReadOnlyColumnCollection[str, Column[Any]]: ...
    def c(self) -> ReadOnlyColumnCollection[str, Column[Any]]: ...
    metadata: Incomplete
    schema: Incomplete
    foreign_keys: Incomplete
    fullname: Incomplete
    implicit_returning: Incomplete
    comment: Incomplete
    info: Incomplete
    def __init__(self, name: str, metadata: MetaData, *args: SchemaItem, schema: Optional[Union[str, Literal[SchemaConst.BLANK_SCHEMA]]] = ..., quote: Optional[bool] = ..., quote_schema: Optional[bool] = ..., autoload_with: Optional[Union[Engine, Connection]] = ..., autoload_replace: bool = ..., keep_existing: bool = ..., extend_existing: bool = ..., resolve_fks: bool = ..., include_columns: Optional[Collection[str]] = ..., implicit_returning: bool = ..., comment: Optional[str] = ..., info: Optional[Dict[Any, Any]] = ..., listeners: Optional[_typing_Sequence[Tuple[str, Callable[..., Any]]]] = ..., prefixes: Optional[_typing_Sequence[str]] = ..., _extend_on: Optional[Set[Table]] = ..., _no_init: bool = ..., **kw: Any) -> None: ...
    @property
    def foreign_key_constraints(self) -> Set[ForeignKeyConstraint]: ...
    @property
    def autoincrement_column(self) -> Optional[Column[int]]: ...
    @property
    def key(self) -> str: ...
    def add_is_dependent_on(self, table: Table) -> None: ...
    def append_column(self, column: ColumnClause[Any], replace_existing: bool = ...) -> None: ...
    def append_constraint(self, constraint: Union[Index, Constraint]) -> None: ...
    def create(self, bind: _CreateDropBind, checkfirst: bool = ...) -> None: ...
    def drop(self, bind: _CreateDropBind, checkfirst: bool = ...) -> None: ...
    def tometadata(self, metadata: MetaData, schema: Union[str, Literal[SchemaConst.RETAIN_SCHEMA]] = ..., referred_schema_fn: Optional[Callable[[Table, Optional[str], ForeignKeyConstraint, Optional[str]], Optional[str]]] = ..., name: Optional[str] = ...) -> Table: ...
    def to_metadata(self, metadata: MetaData, schema: Union[str, Literal[SchemaConst.RETAIN_SCHEMA]] = ..., referred_schema_fn: Optional[Callable[[Table, Optional[str], ForeignKeyConstraint, Optional[str]], Optional[str]]] = ..., name: Optional[str] = ...) -> Table: ...

class Column(DialectKWArgs, SchemaItem, ColumnClause[_T]):
    __visit_name__: str
    inherit_cache: bool
    key: str
    server_default: Optional[FetchedValue]
    primary_key: Incomplete
    nullable: Incomplete
    index: Incomplete
    unique: Incomplete
    system: Incomplete
    doc: Incomplete
    autoincrement: Incomplete
    constraints: Incomplete
    foreign_keys: Incomplete
    comment: Incomplete
    computed: Incomplete
    identity: Incomplete
    default: Incomplete
    onupdate: Incomplete
    server_onupdate: Incomplete
    info: Incomplete
    def __init__(self, __name_pos: Optional[Union[str, _TypeEngineArgument[_T], SchemaEventTarget]] = ..., __type_pos: Optional[Union[_TypeEngineArgument[_T], SchemaEventTarget]] = ..., *args: SchemaEventTarget, name: Optional[str] = ..., type_: Optional[_TypeEngineArgument[_T]] = ..., autoincrement: _AutoIncrementType = ..., default: Optional[Any] = ..., doc: Optional[str] = ..., key: Optional[str] = ..., index: Optional[bool] = ..., unique: Optional[bool] = ..., info: Optional[_InfoType] = ..., nullable: Optional[Union[bool, Literal[SchemaConst.NULL_UNSPECIFIED]]] = ..., onupdate: Optional[Any] = ..., primary_key: bool = ..., server_default: Optional[_ServerDefaultArgument] = ..., server_onupdate: Optional[FetchedValue] = ..., quote: Optional[bool] = ..., system: bool = ..., comment: Optional[str] = ..., insert_sentinel: bool = ..., _omit_from_statements: bool = ..., _proxies: Optional[Any] = ..., **dialect_kwargs: Any) -> None: ...
    table: Table
    def references(self, column: Column[Any]) -> bool: ...
    def append_foreign_key(self, fk: ForeignKey) -> None: ...
    def copy(self, **kw: Any) -> Column[Any]: ...

def insert_sentinel(name: Optional[str] = ..., type_: Optional[_TypeEngineArgument[_T]] = ..., *, default: Optional[Any] = ..., omit_from_statements: bool = ...) -> Column[Any]: ...

class ForeignKey(DialectKWArgs, SchemaItem):
    __visit_name__: str
    parent: Column[Any]
    constraint: Incomplete
    use_alter: Incomplete
    name: Incomplete
    onupdate: Incomplete
    ondelete: Incomplete
    deferrable: Incomplete
    initially: Incomplete
    link_to_name: Incomplete
    match: Incomplete
    comment: Incomplete
    info: Incomplete
    def __init__(self, column: _DDLColumnArgument, _constraint: Optional[ForeignKeyConstraint] = ..., use_alter: bool = ..., name: _ConstraintNameArgument = ..., onupdate: Optional[str] = ..., ondelete: Optional[str] = ..., deferrable: Optional[bool] = ..., initially: Optional[str] = ..., link_to_name: bool = ..., match: Optional[str] = ..., info: Optional[_InfoType] = ..., comment: Optional[str] = ..., _unresolvable: bool = ..., **dialect_kw: Any) -> None: ...
    def copy(self, *, schema: Optional[str] = ..., **kw: Any) -> ForeignKey: ...
    target_fullname: Incomplete
    def references(self, table: Table) -> bool: ...
    def get_referent(self, table: FromClause) -> Optional[Column[Any]]: ...
    def column(self) -> Column[Any]: ...

def default_is_sequence(obj: Optional[DefaultGenerator]) -> TypeGuard[Sequence]: ...
def default_is_clause_element(obj: Optional[DefaultGenerator]) -> TypeGuard[ColumnElementColumnDefault]: ...
def default_is_scalar(obj: Optional[DefaultGenerator]) -> TypeGuard[ScalarElementColumnDefault]: ...

class DefaultGenerator(Executable, SchemaItem):
    __visit_name__: str
    is_sequence: bool
    is_identity: bool
    is_server_default: bool
    is_clause_element: bool
    is_callable: bool
    is_scalar: bool
    has_arg: bool
    is_sentinel: bool
    column: Optional[Column[Any]]
    for_update: Incomplete
    def __init__(self, for_update: bool = ...) -> None: ...

class ColumnDefault(DefaultGenerator, ABC):
    arg: Any
    @overload
    def __new__(cls, arg: Callable[..., Any], for_update: bool = ...) -> CallableColumnDefault: ...
    @overload
    def __new__(cls, arg: ColumnElement[Any], for_update: bool = ...) -> ColumnElementColumnDefault: ...
    @overload
    def __new__(cls, arg: object, for_update: bool = ...) -> ColumnDefault: ...

class ScalarElementColumnDefault(ColumnDefault):
    is_scalar: bool
    has_arg: bool
    for_update: Incomplete
    arg: Incomplete
    def __init__(self, arg: Any, for_update: bool = ...) -> None: ...

class _InsertSentinelColumnDefault(ColumnDefault):
    is_sentinel: bool
    for_update: bool
    arg: Incomplete
    def __new__(cls) -> _InsertSentinelColumnDefault: ...
    def __init__(self) -> None: ...

class ColumnElementColumnDefault(ColumnDefault):
    is_clause_element: bool
    has_arg: bool
    arg: _SQLExprDefault
    for_update: Incomplete
    def __init__(self, arg: _SQLExprDefault, for_update: bool = ...) -> None: ...

class _CallableColumnDefaultProtocol(Protocol):
    def __call__(self, context: ExecutionContext) -> Any: ...

class CallableColumnDefault(ColumnDefault):
    is_callable: bool
    arg: _CallableColumnDefaultProtocol
    has_arg: bool
    for_update: Incomplete
    def __init__(self, arg: Union[_CallableColumnDefaultProtocol, Callable[[], Any]], for_update: bool = ...) -> None: ...

class IdentityOptions:
    start: Incomplete
    increment: Incomplete
    minvalue: Incomplete
    maxvalue: Incomplete
    nominvalue: Incomplete
    nomaxvalue: Incomplete
    cycle: Incomplete
    cache: Incomplete
    order: Incomplete
    def __init__(self, start: Optional[int] = ..., increment: Optional[int] = ..., minvalue: Optional[int] = ..., maxvalue: Optional[int] = ..., nominvalue: Optional[bool] = ..., nomaxvalue: Optional[bool] = ..., cycle: Optional[bool] = ..., cache: Optional[int] = ..., order: Optional[bool] = ...) -> None: ...

class Sequence(HasSchemaAttr, IdentityOptions, DefaultGenerator):
    __visit_name__: str
    is_sequence: bool
    column: Optional[Column[Any]]
    data_type: Optional[TypeEngine[int]]
    name: Incomplete
    optional: Incomplete
    schema: Incomplete
    metadata: Incomplete
    def __init__(self, name: str, start: Optional[int] = ..., increment: Optional[int] = ..., minvalue: Optional[int] = ..., maxvalue: Optional[int] = ..., nominvalue: Optional[bool] = ..., nomaxvalue: Optional[bool] = ..., cycle: Optional[bool] = ..., schema: Optional[Union[str, Literal[SchemaConst.BLANK_SCHEMA]]] = ..., cache: Optional[int] = ..., order: Optional[bool] = ..., data_type: Optional[_TypeEngineArgument[int]] = ..., optional: bool = ..., quote: Optional[bool] = ..., metadata: Optional[MetaData] = ..., quote_schema: Optional[bool] = ..., for_update: bool = ...) -> None: ...
    def next_value(self) -> Function[int]: ...
    def create(self, bind: _CreateDropBind, checkfirst: bool = ...) -> None: ...
    def drop(self, bind: _CreateDropBind, checkfirst: bool = ...) -> None: ...

class FetchedValue(SchemaEventTarget):
    is_server_default: bool
    reflected: bool
    has_argument: bool
    is_clause_element: bool
    is_identity: bool
    column: Optional[Column[Any]]
    for_update: Incomplete
    def __init__(self, for_update: bool = ...) -> None: ...

class DefaultClause(FetchedValue):
    has_argument: bool
    arg: Incomplete
    reflected: Incomplete
    def __init__(self, arg: Union[str, ClauseElement, TextClause], for_update: bool = ..., _reflected: bool = ...) -> None: ...

class Constraint(DialectKWArgs, HasConditionalDDL, SchemaItem):
    __visit_name__: str
    name: Incomplete
    deferrable: Incomplete
    initially: Incomplete
    info: Incomplete
    comment: Incomplete
    def __init__(self, name: _ConstraintNameArgument = ..., deferrable: Optional[bool] = ..., initially: Optional[str] = ..., info: Optional[_InfoType] = ..., comment: Optional[str] = ..., _create_rule: Optional[Any] = ..., _type_bound: bool = ..., **dialect_kw: Any) -> None: ...
    @property
    def table(self) -> Table: ...
    def copy(self, **kw: Any) -> Self: ...

class ColumnCollectionMixin:
    def __init__(self, *columns: _DDLColumnArgument, _autoattach: bool = ..., _column_flag: bool = ..., _gather_expressions: Optional[List[Union[str, ColumnElement[Any]]]] = ...) -> None: ...
    def columns(self) -> ReadOnlyColumnCollection[str, Column[Any]]: ...
    def c(self) -> ReadOnlyColumnCollection[str, Column[Any]]: ...

class ColumnCollectionConstraint(ColumnCollectionMixin, Constraint):
    def __init__(self, *columns: _DDLColumnArgument, name: _ConstraintNameArgument = ..., deferrable: Optional[bool] = ..., initially: Optional[str] = ..., info: Optional[_InfoType] = ..., _autoattach: bool = ..., _column_flag: bool = ..., _gather_expressions: Optional[List[_DDLColumnArgument]] = ..., **dialect_kw: Any) -> None: ...
    columns: ReadOnlyColumnCollection[str, Column[Any]]
    def __contains__(self, x: Any) -> bool: ...
    def copy(self, *, target_table: Optional[Table] = ..., **kw: Any) -> ColumnCollectionConstraint: ...
    def contains_column(self, col: Column[Any]) -> bool: ...
    def __iter__(self) -> Iterator[Column[Any]]: ...
    def __len__(self) -> int: ...

class CheckConstraint(ColumnCollectionConstraint):
    __visit_name__: str
    sqltext: Incomplete
    def __init__(self, sqltext: _TextCoercedExpressionArgument[Any], name: _ConstraintNameArgument = ..., deferrable: Optional[bool] = ..., initially: Optional[str] = ..., table: Optional[Table] = ..., info: Optional[_InfoType] = ..., _create_rule: Optional[Any] = ..., _autoattach: bool = ..., _type_bound: bool = ..., **dialect_kw: Any) -> None: ...
    @property
    def is_column_level(self) -> bool: ...
    def copy(self, *, target_table: Optional[Table] = ..., **kw: Any) -> CheckConstraint: ...

class ForeignKeyConstraint(ColumnCollectionConstraint):
    __visit_name__: str
    onupdate: Incomplete
    ondelete: Incomplete
    link_to_name: Incomplete
    use_alter: Incomplete
    match: Incomplete
    elements: Incomplete
    def __init__(self, columns: _typing_Sequence[_DDLColumnArgument], refcolumns: _typing_Sequence[_DDLColumnArgument], name: _ConstraintNameArgument = ..., onupdate: Optional[str] = ..., ondelete: Optional[str] = ..., deferrable: Optional[bool] = ..., initially: Optional[str] = ..., use_alter: bool = ..., link_to_name: bool = ..., match: Optional[str] = ..., table: Optional[Table] = ..., info: Optional[_InfoType] = ..., comment: Optional[str] = ..., **dialect_kw: Any) -> None: ...
    columns: ReadOnlyColumnCollection[str, Column[Any]]
    @property
    def referred_table(self) -> Table: ...
    @property
    def column_keys(self) -> _typing_Sequence[str]: ...
    def copy(self, *, schema: Optional[str] = ..., target_table: Optional[Table] = ..., **kw: Any) -> ForeignKeyConstraint: ...

class PrimaryKeyConstraint(ColumnCollectionConstraint):
    __visit_name__: str
    def __init__(self, *columns: _DDLColumnArgument, name: Optional[str] = ..., deferrable: Optional[bool] = ..., initially: Optional[str] = ..., info: Optional[_InfoType] = ..., _implicit_generated: bool = ..., **dialect_kw: Any) -> None: ...
    @property
    def columns_autoinc_first(self) -> List[Column[Any]]: ...

class UniqueConstraint(ColumnCollectionConstraint):
    __visit_name__: str

class Index(DialectKWArgs, ColumnCollectionMixin, HasConditionalDDL, SchemaItem):
    __visit_name__: str
    table: Optional[Table]
    expressions: _typing_Sequence[Union[str, ColumnElement[Any]]]
    name: Incomplete
    unique: Incomplete
    info: Incomplete
    def __init__(self, name: Optional[str], *expressions: _DDLColumnArgument, unique: bool = ..., quote: Optional[bool] = ..., info: Optional[_InfoType] = ..., _table: Optional[Table] = ..., _column_flag: bool = ..., **dialect_kw: Any) -> None: ...
    def create(self, bind: _CreateDropBind, checkfirst: bool = ...) -> None: ...
    def drop(self, bind: _CreateDropBind, checkfirst: bool = ...) -> None: ...

class _NamingSchemaTD(TypedDict, total=False):
    fk: _NamingSchemaDirective
    pk: _NamingSchemaDirective
    ix: _NamingSchemaDirective
    ck: _NamingSchemaDirective
    uq: _NamingSchemaDirective

DEFAULT_NAMING_CONVENTION: _NamingSchemaParameter

class MetaData(HasSchemaAttr):
    __visit_name__: str
    tables: Incomplete
    schema: Incomplete
    naming_convention: Incomplete
    info: Incomplete
    def __init__(self, schema: Optional[str] = ..., quote_schema: Optional[bool] = ..., naming_convention: Optional[_NamingSchemaParameter] = ..., info: Optional[_InfoType] = ...) -> None: ...
    def __contains__(self, table_or_key: Union[str, Table]) -> bool: ...
    def clear(self) -> None: ...
    def remove(self, table: Table) -> None: ...
    @property
    def sorted_tables(self) -> List[Table]: ...
    def reflect(self, bind: Union[Engine, Connection], schema: Optional[str] = ..., views: bool = ..., only: Union[_typing_Sequence[str], Callable[[str, MetaData], bool], None] = ..., extend_existing: bool = ..., autoload_replace: bool = ..., resolve_fks: bool = ..., **dialect_kwargs: Any) -> None: ...
    def create_all(self, bind: _CreateDropBind, tables: Optional[_typing_Sequence[Table]] = ..., checkfirst: bool = ...) -> None: ...
    def drop_all(self, bind: _CreateDropBind, tables: Optional[_typing_Sequence[Table]] = ..., checkfirst: bool = ...) -> None: ...

class Computed(FetchedValue, SchemaItem):
    __visit_name__: str
    column: Optional[Column[Any]]
    sqltext: Incomplete
    persisted: Incomplete
    def __init__(self, sqltext: _DDLColumnArgument, persisted: Optional[bool] = ...) -> None: ...
    def copy(self, *, target_table: Optional[Table] = ..., **kw: Any) -> Computed: ...

class Identity(IdentityOptions, FetchedValue, SchemaItem):
    __visit_name__: str
    is_identity: bool
    always: Incomplete
    on_null: Incomplete
    column: Incomplete
    def __init__(self, always: bool = ..., on_null: Optional[bool] = ..., start: Optional[int] = ..., increment: Optional[int] = ..., minvalue: Optional[int] = ..., maxvalue: Optional[int] = ..., nominvalue: Optional[bool] = ..., nomaxvalue: Optional[bool] = ..., cycle: Optional[bool] = ..., cache: Optional[int] = ..., order: Optional[bool] = ...) -> None: ...
    def copy(self, **kw: Any) -> Identity: ...
