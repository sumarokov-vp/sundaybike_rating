from ... import Column as Column, MetaData as MetaData, Table as Table, cast as cast
from ...ext.compiler import compiles as compiles
from ...sql import expression as expression
from ...types import Boolean as Boolean, Integer as Integer, NVARCHAR as NVARCHAR, Numeric as Numeric, String as String, TypeDecorator as TypeDecorator, Unicode as Unicode
from _typeshed import Incomplete

ischema: Incomplete

class CoerceUnicode(TypeDecorator):
    impl = Unicode
    cache_ok: bool
    def bind_expression(self, bindvalue): ...

class _cast_on_2005(expression.ColumnElement):
    bindvalue: Incomplete
    def __init__(self, bindvalue) -> None: ...

schemata: Incomplete
tables: Incomplete
columns: Incomplete
mssql_temp_table_columns: Incomplete
constraints: Incomplete
column_constraints: Incomplete
key_constraints: Incomplete
ref_constraints: Incomplete
views: Incomplete
computed_columns: Incomplete
sequences: Incomplete

class NumericSqlVariant(TypeDecorator):
    impl = Unicode
    cache_ok: bool
    def column_expression(self, colexpr): ...

identity_columns: Incomplete

class NVarcharSqlVariant(TypeDecorator):
    impl = Unicode
    cache_ok: bool
    def column_expression(self, colexpr): ...

extended_properties: Incomplete
