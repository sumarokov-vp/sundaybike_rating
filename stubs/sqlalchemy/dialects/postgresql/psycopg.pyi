from . import ranges as ranges
from ... import pool as pool, util as util
from ...engine import AdaptedConnection as AdaptedConnection
from ...sql import sqltypes as sqltypes
from ...util.concurrency import await_fallback as await_fallback, await_only as await_only
from ._psycopg_common import _PGDialect_common_psycopg, _PGExecutionContext_common_psycopg
from .base import INTERVAL as INTERVAL, PGCompiler as PGCompiler, PGIdentifierPreparer as PGIdentifierPreparer, REGCONFIG as REGCONFIG
from .json import JSON as JSON, JSONB as JSONB, JSONPathType as JSONPathType
from .types import CITEXT as CITEXT
from _typeshed import Incomplete

logger: Incomplete

class _PGString(sqltypes.String):
    render_bind_cast: bool

class _PGREGCONFIG(REGCONFIG):
    render_bind_cast: bool

class _PGJSON(JSON):
    render_bind_cast: bool
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype) -> None: ...

class _PGJSONB(JSONB):
    render_bind_cast: bool
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype) -> None: ...

class _PGJSONIntIndexType(sqltypes.JSON.JSONIntIndexType):
    __visit_name__: str
    render_bind_cast: bool

class _PGJSONStrIndexType(sqltypes.JSON.JSONStrIndexType):
    __visit_name__: str
    render_bind_cast: bool

class _PGJSONPathType(JSONPathType): ...

class _PGInterval(INTERVAL):
    render_bind_cast: bool

class _PGTimeStamp(sqltypes.DateTime):
    render_bind_cast: bool

class _PGDate(sqltypes.Date):
    render_bind_cast: bool

class _PGTime(sqltypes.Time):
    render_bind_cast: bool

class _PGInteger(sqltypes.Integer):
    render_bind_cast: bool

class _PGSmallInteger(sqltypes.SmallInteger):
    render_bind_cast: bool

class _PGNullType(sqltypes.NullType):
    render_bind_cast: bool

class _PGBigInteger(sqltypes.BigInteger):
    render_bind_cast: bool

class _PGBoolean(sqltypes.Boolean):
    render_bind_cast: bool

class _PsycopgRange(ranges.AbstractRangeImpl):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class _PsycopgMultiRange(ranges.AbstractMultiRangeImpl):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class PGExecutionContext_psycopg(_PGExecutionContext_common_psycopg): ...
class PGCompiler_psycopg(PGCompiler): ...
class PGIdentifierPreparer_psycopg(PGIdentifierPreparer): ...

class PGDialect_psycopg(_PGDialect_common_psycopg):
    driver: str
    supports_statement_cache: bool
    supports_server_side_cursors: bool
    default_paramstyle: str
    supports_sane_multi_rowcount: bool
    execution_ctx_cls = PGExecutionContext_psycopg
    statement_compiler = PGCompiler_psycopg
    preparer = PGIdentifierPreparer_psycopg
    psycopg_version: Incomplete
    colspecs: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def create_connect_args(self, url): ...
    insert_executemany_returning: bool
    def initialize(self, connection) -> None: ...
    @classmethod
    def import_dbapi(cls): ...
    @classmethod
    def get_async_dialect_cls(cls, url): ...
    def get_isolation_level(self, dbapi_connection): ...
    def set_isolation_level(self, dbapi_connection, level) -> None: ...
    def set_readonly(self, connection, value) -> None: ...
    def get_readonly(self, connection): ...
    def on_connect(self): ...
    def is_disconnect(self, e, connection, cursor): ...
    def do_rollback_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def do_commit_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...) -> None: ...

class AsyncAdapt_psycopg_cursor:
    await_: Incomplete
    def __init__(self, cursor, await_) -> None: ...
    def __getattr__(self, name): ...
    @property
    def arraysize(self): ...
    @arraysize.setter
    def arraysize(self, value) -> None: ...
    def close(self) -> None: ...
    def execute(self, query, params: Incomplete | None = ..., **kw): ...
    def executemany(self, query, params_seq): ...
    def __iter__(self): ...
    def fetchone(self): ...
    def fetchmany(self, size: Incomplete | None = ...): ...
    def fetchall(self): ...

class AsyncAdapt_psycopg_ss_cursor(AsyncAdapt_psycopg_cursor):
    def execute(self, query, params: Incomplete | None = ..., **kw): ...
    def close(self) -> None: ...
    def fetchone(self): ...
    def fetchmany(self, size: int = ...): ...
    def fetchall(self): ...
    def __iter__(self): ...

class AsyncAdapt_psycopg_connection(AdaptedConnection):
    await_: Incomplete
    def __init__(self, connection) -> None: ...
    def __getattr__(self, name): ...
    def execute(self, query, params: Incomplete | None = ..., **kw): ...
    def cursor(self, *args, **kw): ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
    def close(self) -> None: ...
    @property
    def autocommit(self): ...
    @autocommit.setter
    def autocommit(self, value) -> None: ...
    def set_autocommit(self, value) -> None: ...
    def set_isolation_level(self, value) -> None: ...
    def set_read_only(self, value) -> None: ...
    def set_deferrable(self, value) -> None: ...

class AsyncAdaptFallback_psycopg_connection(AsyncAdapt_psycopg_connection):
    await_: Incomplete

class PsycopgAdaptDBAPI:
    psycopg: Incomplete
    def __init__(self, psycopg) -> None: ...
    def connect(self, *arg, **kw): ...

class PGDialectAsync_psycopg(PGDialect_psycopg):
    is_async: bool
    supports_statement_cache: bool
    @classmethod
    def import_dbapi(cls): ...
    @classmethod
    def get_pool_class(cls, url): ...
    def set_readonly(self, connection, value) -> None: ...
    def set_deferrable(self, connection, value) -> None: ...
    def get_driver_connection(self, connection): ...
dialect = PGDialect_psycopg
dialect_async = PGDialectAsync_psycopg
