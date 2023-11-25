from .. import engines as engines, fixtures as fixtures
from ... import DateTime as DateTime, Integer as Integer, String as String, func as func, select as select, sql as sql, testing as testing, text as text
from ..assertions import eq_ as eq_
from ..config import requirements as requirements
from ..schema import Column as Column, Table as Table
from _typeshed import Incomplete

class RowFetchTest(fixtures.TablesTest):
    __backend__: bool
    @classmethod
    def define_tables(cls, metadata) -> None: ...
    @classmethod
    def insert_data(cls, connection) -> None: ...
    def test_via_attr(self, connection) -> None: ...
    def test_via_string(self, connection) -> None: ...
    def test_via_int(self, connection) -> None: ...
    def test_via_col_object(self, connection) -> None: ...
    def test_row_with_dupe_names(self, connection) -> None: ...
    def test_row_w_scalar_select(self, connection) -> None: ...

class PercentSchemaNamesTest(fixtures.TablesTest):
    __requires__: Incomplete
    __backend__: bool
    @classmethod
    def define_tables(cls, metadata) -> None: ...
    def test_single_roundtrip(self, connection) -> None: ...
    def test_executemany_roundtrip(self, connection) -> None: ...
    def test_executemany_returning_roundtrip(self, connection) -> None: ...

class ServerSideCursorsTest(fixtures.TestBase, testing.AssertsExecutionResults):
    __requires__: Incomplete
    __backend__: bool
    def test_ss_cursor_status(self, engine_ss_arg, statement, cursor_ss_status) -> None: ...
    def test_conn_option(self) -> None: ...
    def test_stmt_enabled_conn_option_disabled(self) -> None: ...
    def test_aliases_and_ss(self) -> None: ...
    def test_roundtrip_fetchall(self, metadata) -> None: ...
    def test_roundtrip_fetchmany(self, metadata) -> None: ...