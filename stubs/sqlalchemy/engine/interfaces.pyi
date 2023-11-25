from .. import util as util
from ..event import EventTarget as EventTarget, dispatcher as dispatcher
from ..exc import StatementError as StatementError
from ..pool import Pool as Pool, PoolProxiedConnection as PoolProxiedConnection
from ..sql import Executable as Executable
from ..sql.compiler import Compiled as Compiled, DDLCompiler as DDLCompiler, IdentifierPreparer as IdentifierPreparer, InsertmanyvaluesSentinelOpts as InsertmanyvaluesSentinelOpts, Linting as Linting, SQLCompiler as SQLCompiler, TypeCompiler as TypeCompiler
from ..sql.elements import BindParameter as BindParameter, ClauseElement as ClauseElement
from ..sql.schema import Column as Column, DefaultGenerator as DefaultGenerator, SchemaItem as SchemaItem, Sequence as Sequence_SchemaItem
from ..sql.sqltypes import Integer as Integer
from ..sql.type_api import TypeEngine as TypeEngine
from ..util import immutabledict as immutabledict
from ..util.concurrency import await_only as await_only
from ..util.typing import Literal as Literal, NotRequired as NotRequired, Protocol as Protocol, TypedDict as TypedDict
from .base import Connection as Connection, Engine as Engine
from .cursor import CursorResult as CursorResult
from .url import URL as URL
from _typeshed import Incomplete
from enum import Enum
from types import ModuleType
from typing import Any, Awaitable, Callable, ClassVar, Collection, Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Set, Tuple, Type, Union

ConnectArgsType = Tuple[Sequence[str], MutableMapping[str, Any]]

class CacheStats(Enum):
    CACHE_HIT: int
    CACHE_MISS: int
    CACHING_DISABLED: int
    NO_CACHE_KEY: int
    NO_DIALECT_SUPPORT: int

class ExecuteStyle(Enum):
    EXECUTE: int
    EXECUTEMANY: int
    INSERTMANYVALUES: int

class DBAPIConnection(Protocol):
    def close(self) -> None: ...
    def commit(self) -> None: ...
    def cursor(self) -> DBAPICursor: ...
    def rollback(self) -> None: ...
    autocommit: bool

class DBAPIType(Protocol): ...

class DBAPICursor(Protocol):
    @property
    def description(self) -> _DBAPICursorDescription: ...
    @property
    def rowcount(self) -> int: ...
    arraysize: int
    lastrowid: int
    def close(self) -> None: ...
    def execute(self, operation: Any, parameters: Optional[_DBAPISingleExecuteParams] = ...) -> Any: ...
    def executemany(self, operation: Any, parameters: Sequence[_DBAPIMultiExecuteParams]) -> Any: ...
    def fetchone(self) -> Optional[Any]: ...
    def fetchmany(self, size: int = ...) -> Sequence[Any]: ...
    def fetchall(self) -> Sequence[Any]: ...
    def setinputsizes(self, sizes: Sequence[Any]) -> None: ...
    def setoutputsize(self, size: Any, column: Any) -> None: ...
    def callproc(self, procname: str, parameters: Sequence[Any] = ...) -> Any: ...
    def nextset(self) -> Optional[bool]: ...
    def __getattr__(self, key: str) -> Any: ...

CompiledCacheType: Incomplete
SchemaTranslateMapType = Mapping[Optional[str], Optional[str]]
IsolationLevel: Incomplete

class _CoreKnownExecutionOptions(TypedDict, total=False):
    compiled_cache: Optional[CompiledCacheType]
    logging_token: str
    isolation_level: IsolationLevel
    no_parameters: bool
    stream_results: bool
    max_row_buffer: int
    yield_per: int
    insertmanyvalues_page_size: int
    schema_translate_map: Optional[SchemaTranslateMapType]

CoreExecuteOptionsParameter: Incomplete

class ReflectedIdentity(TypedDict):
    always: bool
    on_null: bool
    start: int
    increment: int
    minvalue: int
    maxvalue: int
    nominvalue: bool
    nomaxvalue: bool
    cycle: bool
    cache: Optional[int]
    order: bool

class ReflectedComputed(TypedDict):
    sqltext: str
    persisted: NotRequired[bool]

class ReflectedColumn(TypedDict):
    name: str
    type: TypeEngine[Any]
    nullable: bool
    default: Optional[str]
    autoincrement: NotRequired[bool]
    comment: NotRequired[Optional[str]]
    computed: NotRequired[ReflectedComputed]
    identity: NotRequired[ReflectedIdentity]
    dialect_options: NotRequired[Dict[str, Any]]

class ReflectedConstraint(TypedDict):
    name: Optional[str]
    comment: NotRequired[Optional[str]]

class ReflectedCheckConstraint(ReflectedConstraint):
    sqltext: str
    dialect_options: NotRequired[Dict[str, Any]]

class ReflectedUniqueConstraint(ReflectedConstraint):
    column_names: List[str]
    duplicates_index: NotRequired[Optional[str]]
    dialect_options: NotRequired[Dict[str, Any]]

class ReflectedPrimaryKeyConstraint(ReflectedConstraint):
    constrained_columns: List[str]
    dialect_options: NotRequired[Dict[str, Any]]

class ReflectedForeignKeyConstraint(ReflectedConstraint):
    constrained_columns: List[str]
    referred_schema: Optional[str]
    referred_table: str
    referred_columns: List[str]
    options: NotRequired[Dict[str, Any]]

class ReflectedIndex(TypedDict):
    name: Optional[str]
    column_names: List[Optional[str]]
    expressions: NotRequired[List[str]]
    unique: bool
    duplicates_constraint: NotRequired[Optional[str]]
    include_columns: NotRequired[List[str]]
    column_sorting: NotRequired[Dict[str, Tuple[str]]]
    dialect_options: NotRequired[Dict[str, Any]]

class ReflectedTableComment(TypedDict):
    text: Optional[str]

class BindTyping(Enum):
    NONE: int
    SETINPUTSIZES: int
    RENDER_CASTS: int
VersionInfoType = Tuple[Union[int, str], ...]
TableKey = Tuple[Optional[str], str]

class Dialect(EventTarget):
    CACHE_HIT: Incomplete
    CACHE_MISS: Incomplete
    CACHING_DISABLED: Incomplete
    NO_CACHE_KEY: Incomplete
    NO_DIALECT_SUPPORT: Incomplete
    dispatch: dispatcher[Dialect]
    name: str
    driver: str
    dialect_description: str
    dbapi: Optional[ModuleType]
    def loaded_dbapi(self) -> ModuleType: ...
    positional: bool
    paramstyle: str
    compiler_linting: Linting
    statement_compiler: Type[SQLCompiler]
    ddl_compiler: Type[DDLCompiler]
    type_compiler_cls: ClassVar[Type[TypeCompiler]]
    type_compiler_instance: TypeCompiler
    type_compiler: Any
    preparer: Type[IdentifierPreparer]
    identifier_preparer: IdentifierPreparer
    server_version_info: Optional[Tuple[Any, ...]]
    default_schema_name: Optional[str]
    default_isolation_level: Optional[IsolationLevel]
    execution_ctx_cls: Type[ExecutionContext]
    execute_sequence_format: Union[Type[Tuple[Any, ...]], Type[Tuple[List[Any]]]]
    supports_alter: bool
    max_identifier_length: int
    supports_server_side_cursors: bool
    server_side_cursors: bool
    supports_sane_rowcount: bool
    supports_sane_multi_rowcount: bool
    supports_empty_insert: bool
    supports_default_values: bool
    supports_default_metavalue: bool
    default_metavalue_token: str
    supports_multivalues_insert: bool
    insert_executemany_returning: bool
    insert_executemany_returning_sort_by_parameter_order: bool
    update_executemany_returning: bool
    delete_executemany_returning: bool
    use_insertmanyvalues: bool
    use_insertmanyvalues_wo_returning: bool
    insertmanyvalues_implicit_sentinel: InsertmanyvaluesSentinelOpts
    insertmanyvalues_page_size: int
    insertmanyvalues_max_parameters: int
    preexecute_autoincrement_sequences: bool
    insert_returning: bool
    update_returning: bool
    update_returning_multifrom: bool
    delete_returning: bool
    delete_returning_multifrom: bool
    favor_returning_over_lastrowid: bool
    supports_identity_columns: bool
    cte_follows_insert: bool
    colspecs: MutableMapping[Type[TypeEngine[Any]], Type[TypeEngine[Any]]]
    supports_sequences: bool
    sequences_optional: bool
    default_sequence_base: int
    supports_native_enum: bool
    supports_native_boolean: bool
    supports_native_decimal: bool
    supports_native_uuid: bool
    returns_native_bytes: bool
    construct_arguments: Optional[List[Tuple[Type[Union[SchemaItem, ClauseElement]], Mapping[str, Any]]]]
    reflection_options: Sequence[str]
    dbapi_exception_translation_map: Mapping[str, str]
    supports_comments: bool
    inline_comments: bool
    supports_constraint_comments: bool
    supports_statement_cache: bool
    bind_typing: Incomplete
    is_async: bool
    has_terminate: bool
    engine_config_types: Mapping[str, Any]
    label_length: Optional[int]
    include_set_input_sizes: Optional[Set[Any]]
    exclude_set_input_sizes: Optional[Set[Any]]
    supports_simple_order_by_label: bool
    div_is_floordiv: bool
    tuple_in_values: bool
    def create_connect_args(self, url: URL) -> ConnectArgsType: ...
    @classmethod
    def import_dbapi(cls) -> ModuleType: ...
    @classmethod
    def type_descriptor(cls, typeobj: TypeEngine[_T]) -> TypeEngine[_T]: ...
    def initialize(self, connection: Connection) -> None: ...
    def get_columns(self, connection: Connection, table_name: str, schema: Optional[str] = ..., **kw: Any) -> List[ReflectedColumn]: ...
    def get_multi_columns(self, connection: Connection, schema: Optional[str] = ..., filter_names: Optional[Collection[str]] = ..., **kw: Any) -> Iterable[Tuple[TableKey, List[ReflectedColumn]]]: ...
    def get_pk_constraint(self, connection: Connection, table_name: str, schema: Optional[str] = ..., **kw: Any) -> ReflectedPrimaryKeyConstraint: ...
    def get_multi_pk_constraint(self, connection: Connection, schema: Optional[str] = ..., filter_names: Optional[Collection[str]] = ..., **kw: Any) -> Iterable[Tuple[TableKey, ReflectedPrimaryKeyConstraint]]: ...
    def get_foreign_keys(self, connection: Connection, table_name: str, schema: Optional[str] = ..., **kw: Any) -> List[ReflectedForeignKeyConstraint]: ...
    def get_multi_foreign_keys(self, connection: Connection, schema: Optional[str] = ..., filter_names: Optional[Collection[str]] = ..., **kw: Any) -> Iterable[Tuple[TableKey, List[ReflectedForeignKeyConstraint]]]: ...
    def get_table_names(self, connection: Connection, schema: Optional[str] = ..., **kw: Any) -> List[str]: ...
    def get_temp_table_names(self, connection: Connection, schema: Optional[str] = ..., **kw: Any) -> List[str]: ...
    def get_view_names(self, connection: Connection, schema: Optional[str] = ..., **kw: Any) -> List[str]: ...
    def get_materialized_view_names(self, connection: Connection, schema: Optional[str] = ..., **kw: Any) -> List[str]: ...
    def get_sequence_names(self, connection: Connection, schema: Optional[str] = ..., **kw: Any) -> List[str]: ...
    def get_temp_view_names(self, connection: Connection, schema: Optional[str] = ..., **kw: Any) -> List[str]: ...
    def get_schema_names(self, connection: Connection, **kw: Any) -> List[str]: ...
    def get_view_definition(self, connection: Connection, view_name: str, schema: Optional[str] = ..., **kw: Any) -> str: ...
    def get_indexes(self, connection: Connection, table_name: str, schema: Optional[str] = ..., **kw: Any) -> List[ReflectedIndex]: ...
    def get_multi_indexes(self, connection: Connection, schema: Optional[str] = ..., filter_names: Optional[Collection[str]] = ..., **kw: Any) -> Iterable[Tuple[TableKey, List[ReflectedIndex]]]: ...
    def get_unique_constraints(self, connection: Connection, table_name: str, schema: Optional[str] = ..., **kw: Any) -> List[ReflectedUniqueConstraint]: ...
    def get_multi_unique_constraints(self, connection: Connection, schema: Optional[str] = ..., filter_names: Optional[Collection[str]] = ..., **kw: Any) -> Iterable[Tuple[TableKey, List[ReflectedUniqueConstraint]]]: ...
    def get_check_constraints(self, connection: Connection, table_name: str, schema: Optional[str] = ..., **kw: Any) -> List[ReflectedCheckConstraint]: ...
    def get_multi_check_constraints(self, connection: Connection, schema: Optional[str] = ..., filter_names: Optional[Collection[str]] = ..., **kw: Any) -> Iterable[Tuple[TableKey, List[ReflectedCheckConstraint]]]: ...
    def get_table_options(self, connection: Connection, table_name: str, schema: Optional[str] = ..., **kw: Any) -> Dict[str, Any]: ...
    def get_multi_table_options(self, connection: Connection, schema: Optional[str] = ..., filter_names: Optional[Collection[str]] = ..., **kw: Any) -> Iterable[Tuple[TableKey, Dict[str, Any]]]: ...
    def get_table_comment(self, connection: Connection, table_name: str, schema: Optional[str] = ..., **kw: Any) -> ReflectedTableComment: ...
    def get_multi_table_comment(self, connection: Connection, schema: Optional[str] = ..., filter_names: Optional[Collection[str]] = ..., **kw: Any) -> Iterable[Tuple[TableKey, ReflectedTableComment]]: ...
    def normalize_name(self, name: str) -> str: ...
    def denormalize_name(self, name: str) -> str: ...
    def has_table(self, connection: Connection, table_name: str, schema: Optional[str] = ..., **kw: Any) -> bool: ...
    def has_index(self, connection: Connection, table_name: str, index_name: str, schema: Optional[str] = ..., **kw: Any) -> bool: ...
    def has_sequence(self, connection: Connection, sequence_name: str, schema: Optional[str] = ..., **kw: Any) -> bool: ...
    def has_schema(self, connection: Connection, schema_name: str, **kw: Any) -> bool: ...
    def do_begin(self, dbapi_connection: PoolProxiedConnection) -> None: ...
    def do_rollback(self, dbapi_connection: PoolProxiedConnection) -> None: ...
    def do_commit(self, dbapi_connection: PoolProxiedConnection) -> None: ...
    def do_terminate(self, dbapi_connection: DBAPIConnection) -> None: ...
    def do_close(self, dbapi_connection: DBAPIConnection) -> None: ...
    def do_ping(self, dbapi_connection: DBAPIConnection) -> bool: ...
    def do_set_input_sizes(self, cursor: DBAPICursor, list_of_tuples: _GenericSetInputSizesType, context: ExecutionContext) -> Any: ...
    def create_xid(self) -> Any: ...
    def do_savepoint(self, connection: Connection, name: str) -> None: ...
    def do_rollback_to_savepoint(self, connection: Connection, name: str) -> None: ...
    def do_release_savepoint(self, connection: Connection, name: str) -> None: ...
    def do_begin_twophase(self, connection: Connection, xid: Any) -> None: ...
    def do_prepare_twophase(self, connection: Connection, xid: Any) -> None: ...
    def do_rollback_twophase(self, connection: Connection, xid: Any, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def do_commit_twophase(self, connection: Connection, xid: Any, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def do_recover_twophase(self, connection: Connection) -> List[Any]: ...
    def do_executemany(self, cursor: DBAPICursor, statement: str, parameters: _DBAPIMultiExecuteParams, context: Optional[ExecutionContext] = ...) -> None: ...
    def do_execute(self, cursor: DBAPICursor, statement: str, parameters: Optional[_DBAPISingleExecuteParams], context: Optional[ExecutionContext] = ...) -> None: ...
    def do_execute_no_params(self, cursor: DBAPICursor, statement: str, context: Optional[ExecutionContext] = ...) -> None: ...
    def is_disconnect(self, e: Exception, connection: Optional[Union[PoolProxiedConnection, DBAPIConnection]], cursor: Optional[DBAPICursor]) -> bool: ...
    def connect(self, *cargs: Any, **cparams: Any) -> DBAPIConnection: ...
    def on_connect_url(self, url: URL) -> Optional[Callable[[Any], Any]]: ...
    def on_connect(self) -> Optional[Callable[[Any], Any]]: ...
    def reset_isolation_level(self, dbapi_connection: DBAPIConnection) -> None: ...
    def set_isolation_level(self, dbapi_connection: DBAPIConnection, level: IsolationLevel) -> None: ...
    def get_isolation_level(self, dbapi_connection: DBAPIConnection) -> IsolationLevel: ...
    def get_default_isolation_level(self, dbapi_conn: DBAPIConnection) -> IsolationLevel: ...
    def get_isolation_level_values(self, dbapi_conn: DBAPIConnection) -> List[IsolationLevel]: ...
    @classmethod
    def get_dialect_cls(cls, url: URL) -> Type[Dialect]: ...
    @classmethod
    def get_async_dialect_cls(cls, url: URL) -> Type[Dialect]: ...
    @classmethod
    def load_provisioning(cls) -> None: ...
    @classmethod
    def engine_created(cls, engine: Engine) -> None: ...
    def get_driver_connection(self, connection: DBAPIConnection) -> Any: ...
    def set_engine_execution_options(self, engine: Engine, opts: CoreExecuteOptionsParameter) -> None: ...
    def set_connection_execution_options(self, connection: Connection, opts: CoreExecuteOptionsParameter) -> None: ...
    def get_dialect_pool_class(self, url: URL) -> Type[Pool]: ...

class CreateEnginePlugin:
    url: Incomplete
    def __init__(self, url: URL, kwargs: Dict[str, Any]) -> None: ...
    def update_url(self, url: URL) -> URL: ...
    def handle_dialect_kwargs(self, dialect_cls: Type[Dialect], dialect_args: Dict[str, Any]) -> None: ...
    def handle_pool_kwargs(self, pool_cls: Type[Pool], pool_args: Dict[str, Any]) -> None: ...
    def engine_created(self, engine: Engine) -> None: ...

class ExecutionContext:
    engine: Engine
    connection: Connection
    root_connection: Connection
    dialect: Dialect
    cursor: DBAPICursor
    compiled: Optional[Compiled]
    statement: str
    invoked_statement: Optional[Executable]
    parameters: _AnyMultiExecuteParams
    no_parameters: bool
    isinsert: bool
    isupdate: bool
    execute_style: ExecuteStyle
    executemany: bool
    prefetch_cols: util.generic_fn_descriptor[Optional[Sequence[Column[Any]]]]
    postfetch_cols: util.generic_fn_descriptor[Optional[Sequence[Column[Any]]]]
    def fire_sequence(self, seq: Sequence_SchemaItem, type_: Integer) -> int: ...
    def create_cursor(self) -> DBAPICursor: ...
    def pre_exec(self) -> None: ...
    def get_out_parameter_values(self, out_param_names: Sequence[str]) -> Sequence[Any]: ...
    def post_exec(self) -> None: ...
    def handle_dbapi_exception(self, e: BaseException) -> None: ...
    def lastrow_has_defaults(self) -> bool: ...
    def get_rowcount(self) -> Optional[int]: ...
    def fetchall_for_returning(self, cursor: DBAPICursor) -> Sequence[Any]: ...

class ConnectionEventsTarget(EventTarget):
    dispatch: dispatcher[ConnectionEventsTarget]
Connectable = ConnectionEventsTarget

class ExceptionContext:
    dialect: Dialect
    connection: Optional[Connection]
    engine: Optional[Engine]
    cursor: Optional[DBAPICursor]
    statement: Optional[str]
    parameters: Optional[_DBAPIAnyExecuteParams]
    original_exception: BaseException
    sqlalchemy_exception: Optional[StatementError]
    chained_exception: Optional[BaseException]
    execution_context: Optional[ExecutionContext]
    is_disconnect: bool
    invalidate_pool_on_disconnect: bool
    is_pre_ping: bool

class AdaptedConnection:
    @property
    def driver_connection(self) -> Any: ...
    def run_async(self, fn: Callable[[Any], Awaitable[_T]]) -> _T: ...
