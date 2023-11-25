from ... import schema as schema, util as util
from ...sql import coercions as coercions, elements as elements, roles as roles, sqltypes as sqltypes, type_api as type_api
from ...sql._typing import _TypeEngineArgument
from ...sql.base import _NoArg
from ...sql.ddl import InvokeCreateDDLBase as InvokeCreateDDLBase, InvokeDropDDLBase as InvokeDropDDLBase
from _typeshed import Incomplete
from typing import Any, Optional, Type, Union

class NamedType(sqltypes.TypeEngine):
    __abstract__: bool
    DDLGenerator: Type[NamedTypeGenerator]
    DDLDropper: Type[NamedTypeDropper]
    create_type: bool
    def create(self, bind, checkfirst: bool = ..., **kw) -> None: ...
    def drop(self, bind, checkfirst: bool = ..., **kw) -> None: ...

class NamedTypeGenerator(InvokeCreateDDLBase):
    checkfirst: Incomplete
    def __init__(self, dialect, connection, checkfirst: bool = ..., **kwargs) -> None: ...

class NamedTypeDropper(InvokeDropDDLBase):
    checkfirst: Incomplete
    def __init__(self, dialect, connection, checkfirst: bool = ..., **kwargs) -> None: ...

class EnumGenerator(NamedTypeGenerator):
    def visit_enum(self, enum) -> None: ...

class EnumDropper(NamedTypeDropper):
    def visit_enum(self, enum) -> None: ...

class ENUM(NamedType, type_api.NativeForEmulated, sqltypes.Enum):
    native_enum: bool
    DDLGenerator = EnumGenerator
    DDLDropper = EnumDropper
    create_type: Incomplete
    def __init__(self, *enums, name: Union[str, _NoArg, None] = ..., create_type: bool = ..., **kw) -> None: ...
    def coerce_compared_value(self, op, value): ...
    @classmethod
    def __test_init__(cls): ...
    @classmethod
    def adapt_emulated_to_native(cls, impl, **kw): ...
    def create(self, bind: Incomplete | None = ..., checkfirst: bool = ...) -> None: ...
    def drop(self, bind: Incomplete | None = ..., checkfirst: bool = ...) -> None: ...
    def get_dbapi_type(self, dbapi) -> None: ...

class DomainGenerator(NamedTypeGenerator):
    def visit_DOMAIN(self, domain) -> None: ...

class DomainDropper(NamedTypeDropper):
    def visit_DOMAIN(self, domain) -> None: ...

class DOMAIN(NamedType, sqltypes.SchemaType):
    DDLGenerator = DomainGenerator
    DDLDropper = DomainDropper
    __visit_name__: str
    data_type: Incomplete
    default: Incomplete
    collation: Incomplete
    constraint_name: Incomplete
    not_null: Incomplete
    check: Incomplete
    create_type: Incomplete
    def __init__(self, name: str, data_type: _TypeEngineArgument[Any], *, collation: Optional[str] = ..., default: Optional[Union[str, elements.TextClause]] = ..., constraint_name: Optional[str] = ..., not_null: Optional[bool] = ..., check: Optional[str] = ..., create_type: bool = ..., **kw: Any) -> None: ...
    @classmethod
    def __test_init__(cls): ...

class CreateEnumType(schema._CreateDropBase):
    __visit_name__: str

class DropEnumType(schema._CreateDropBase):
    __visit_name__: str

class CreateDomainType(schema._CreateDropBase):
    __visit_name__: str

class DropDomainType(schema._CreateDropBase):
    __visit_name__: str
