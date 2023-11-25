from ..engine import AdaptedConnection as AdaptedConnection
from ..util.concurrency import asyncio as asyncio, await_fallback as await_fallback, await_only as await_only
from _typeshed import Incomplete

class AsyncAdapt_dbapi_cursor:
    server_side: bool
    await_: Incomplete
    def __init__(self, adapt_connection) -> None: ...
    @property
    def description(self): ...
    @property
    def rowcount(self): ...
    @property
    def arraysize(self): ...
    @arraysize.setter
    def arraysize(self, value) -> None: ...
    @property
    def lastrowid(self): ...
    def close(self) -> None: ...
    def execute(self, operation, parameters: Incomplete | None = ...): ...
    def executemany(self, operation, seq_of_parameters): ...
    def nextset(self) -> None: ...
    def setinputsizes(self, *inputsizes): ...
    def __iter__(self): ...
    def fetchone(self): ...
    def fetchmany(self, size: Incomplete | None = ...): ...
    def fetchall(self): ...

class AsyncAdapt_dbapi_ss_cursor(AsyncAdapt_dbapi_cursor):
    server_side: bool
    await_: Incomplete
    def __init__(self, adapt_connection) -> None: ...
    def close(self) -> None: ...
    def fetchone(self): ...
    def fetchmany(self, size: Incomplete | None = ...): ...
    def fetchall(self): ...

class AsyncAdapt_dbapi_connection(AdaptedConnection):
    await_: Incomplete
    dbapi: Incomplete
    def __init__(self, dbapi, connection) -> None: ...
    def ping(self, reconnect): ...
    def add_output_converter(self, *arg, **kw) -> None: ...
    def character_set_name(self): ...
    @property
    def autocommit(self): ...
    @autocommit.setter
    def autocommit(self, value) -> None: ...
    def cursor(self, server_side: bool = ...): ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def close(self) -> None: ...

class AsyncAdaptFallback_dbapi_connection(AsyncAdapt_dbapi_connection):
    await_: Incomplete
