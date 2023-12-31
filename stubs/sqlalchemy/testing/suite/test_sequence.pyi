from .. import config as config, fixtures as fixtures
from ... import Integer as Integer, MetaData as MetaData, Sequence as Sequence, String as String, inspect as inspect, testing as testing
from ..assertions import eq_ as eq_, is_true as is_true
from ..config import requirements as requirements
from ..provision import normalize_sequence as normalize_sequence
from ..schema import Column as Column, Table as Table
from _typeshed import Incomplete

class SequenceTest(fixtures.TablesTest):
    __requires__: Incomplete
    __backend__: bool
    run_create_tables: str
    @classmethod
    def define_tables(cls, metadata) -> None: ...
    def test_insert_roundtrip(self, connection) -> None: ...
    def test_insert_lastrowid(self, connection) -> None: ...
    def test_nextval_direct(self, connection) -> None: ...
    def test_optional_seq(self, connection) -> None: ...
    def test_insert_roundtrip_no_implicit_returning(self, connection) -> None: ...
    def test_insert_roundtrip_translate(self, connection, implicit_returning) -> None: ...
    def test_nextval_direct_schema_translate(self, connection) -> None: ...

class SequenceCompilerTest(testing.AssertsCompiledSQL, fixtures.TestBase):
    __requires__: Incomplete
    __backend__: bool
    def test_literal_binds_inline_compile(self, connection) -> None: ...

class HasSequenceTest(fixtures.TablesTest):
    run_deletes: Incomplete
    __requires__: Incomplete
    __backend__: bool
    @classmethod
    def define_tables(cls, metadata) -> None: ...
    def test_has_sequence(self, connection) -> None: ...
    def test_has_sequence_cache(self, connection, metadata) -> None: ...
    def test_has_sequence_other_object(self, connection) -> None: ...
    def test_has_sequence_schema(self, connection) -> None: ...
    def test_has_sequence_neg(self, connection) -> None: ...
    def test_has_sequence_schemas_neg(self, connection) -> None: ...
    def test_has_sequence_default_not_in_remote(self, connection) -> None: ...
    def test_has_sequence_remote_not_in_default(self, connection) -> None: ...
    def test_get_sequence_names(self, connection) -> None: ...
    def test_get_sequence_names_no_sequence_schema(self, connection) -> None: ...
    def test_get_sequence_names_sequences_schema(self, connection) -> None: ...

class HasSequenceTestEmpty(fixtures.TestBase):
    __requires__: Incomplete
    __backend__: bool
    def test_get_sequence_names_no_sequence(self, connection) -> None: ...
