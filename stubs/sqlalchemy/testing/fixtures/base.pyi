from .. import assertions as assertions, config as config
from ... import Column as Column, Integer as Integer, Table as Table, func as func, select as select
from ...orm import DeclarativeBase as DeclarativeBase, MappedAsDataclass as MappedAsDataclass, registry as registry
from ..assertions import eq_ as eq_
from ..util import drop_all_tables_from_metadata as drop_all_tables_from_metadata
from _typeshed import Incomplete
from collections.abc import Generator

class TestBase:
    __requires__: Incomplete
    __unsupported_on__: Incomplete
    __only_on__: Incomplete
    __skip_if__: Incomplete
    __leave_connections_for_teardown__: bool
    def assert_(self, val, msg: Incomplete | None = ...) -> None: ...
    def nocache(self) -> Generator[None, None, None]: ...
    def connection_no_trans(self) -> Generator[Incomplete, None, None]: ...
    def connection(self) -> Generator[Incomplete, None, None]: ...
    def close_result_when_finished(self) -> Generator[Incomplete, None, None]: ...
    def registry(self, metadata) -> Generator[Incomplete, None, None]: ...
    def decl_base(self, metadata) -> Generator[Incomplete, None, None]: ...
    def dc_decl_base(self, metadata) -> Generator[Incomplete, None, None]: ...
    def future_connection(self, future_engine, connection) -> Generator[Incomplete, None, None]: ...
    def future_engine(self) -> Generator[None, None, None]: ...
    def testing_engine(self) -> Generator[Incomplete, None, Incomplete]: ...
    def async_testing_engine(self, testing_engine): ...
    def metadata(self, request) -> Generator[Incomplete, None, None]: ...
    def trans_ctx_manager_fixture(self, request, metadata): ...

class FutureEngineMixin: ...
