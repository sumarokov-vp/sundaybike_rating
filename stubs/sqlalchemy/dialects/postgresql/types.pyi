import datetime as dt
from ...engine.interfaces import Dialect as Dialect
from ...sql import sqltypes as sqltypes, type_api as type_api
from ...sql.operators import OperatorType as OperatorType
from ...sql.type_api import TypeEngine as TypeEngine, _LiteralProcessorType
from ...util.typing import Literal as Literal
from _typeshed import Incomplete
from typing import Any, Optional, Type, overload

class PGUuid(sqltypes.UUID[sqltypes._UUID_RETURN]):
    render_bind_cast: bool
    render_literal_cast: bool
    @overload
    def __init__(self, as_uuid: Literal[True] = ...) -> None: ...
    @overload
    def __init__(self, as_uuid: Literal[False] = ...) -> None: ...

class BYTEA(sqltypes.LargeBinary):
    __visit_name__: str

class INET(sqltypes.TypeEngine[str]):
    __visit_name__: str
PGInet = INET

class CIDR(sqltypes.TypeEngine[str]):
    __visit_name__: str
PGCidr = CIDR

class MACADDR(sqltypes.TypeEngine[str]):
    __visit_name__: str
PGMacAddr = MACADDR

class MACADDR8(sqltypes.TypeEngine[str]):
    __visit_name__: str
PGMacAddr8 = MACADDR8

class MONEY(sqltypes.TypeEngine[str]):
    __visit_name__: str

class OID(sqltypes.TypeEngine[int]):
    __visit_name__: str

class REGCONFIG(sqltypes.TypeEngine[str]):
    __visit_name__: str

class TSQUERY(sqltypes.TypeEngine[str]):
    __visit_name__: str

class REGCLASS(sqltypes.TypeEngine[str]):
    __visit_name__: str

class TIMESTAMP(sqltypes.TIMESTAMP):
    __visit_name__: str
    precision: Incomplete
    def __init__(self, timezone: bool = ..., precision: Optional[int] = ...) -> None: ...

class TIME(sqltypes.TIME):
    __visit_name__: str
    precision: Incomplete
    def __init__(self, timezone: bool = ..., precision: Optional[int] = ...) -> None: ...

class INTERVAL(type_api.NativeForEmulated, sqltypes._AbstractInterval):
    __visit_name__: str
    native: bool
    precision: Incomplete
    fields: Incomplete
    def __init__(self, precision: Optional[int] = ..., fields: Optional[str] = ...) -> None: ...
    @classmethod
    def adapt_emulated_to_native(cls, interval: sqltypes.Interval, **kw: Any) -> INTERVAL: ...
    def as_generic(self, allow_nulltype: bool = ...) -> sqltypes.Interval: ...
    @property
    def python_type(self) -> Type[dt.timedelta]: ...
    def literal_processor(self, dialect: Dialect) -> Optional[_LiteralProcessorType[dt.timedelta]]: ...
PGInterval = INTERVAL

class BIT(sqltypes.TypeEngine[int]):
    __visit_name__: str
    length: Incomplete
    varying: Incomplete
    def __init__(self, length: Optional[int] = ..., varying: bool = ...) -> None: ...
PGBit = BIT

class TSVECTOR(sqltypes.TypeEngine[str]):
    __visit_name__: str

class CITEXT(sqltypes.TEXT):
    __visit_name__: str
    def coerce_compared_value(self, op: Optional[OperatorType], value: Any) -> TypeEngine[Any]: ...
