import datetime as dt
from ... import exc as exc
from ...engine.interfaces import Dialect as Dialect
from ...sql import sqltypes as sqltypes
from ...sql.type_api import _LiteralProcessorType
from ...types import NVARCHAR as NVARCHAR, VARCHAR as VARCHAR
from _typeshed import Incomplete
from typing import Optional, Type

class RAW(sqltypes._Binary):
    __visit_name__: str
OracleRaw = RAW

class NCLOB(sqltypes.Text):
    __visit_name__: str

class VARCHAR2(VARCHAR):
    __visit_name__: str
NVARCHAR2 = NVARCHAR

class NUMBER(sqltypes.Numeric, sqltypes.Integer):
    __visit_name__: str
    def __init__(self, precision: Incomplete | None = ..., scale: Incomplete | None = ..., asdecimal: Incomplete | None = ...) -> None: ...
    def adapt(self, impltype): ...

class FLOAT(sqltypes.FLOAT):
    __visit_name__: str
    binary_precision: Incomplete
    def __init__(self, binary_precision: Incomplete | None = ..., asdecimal: bool = ..., decimal_return_scale: Incomplete | None = ...) -> None: ...

class BINARY_DOUBLE(sqltypes.Double):
    __visit_name__: str

class BINARY_FLOAT(sqltypes.Float):
    __visit_name__: str

class BFILE(sqltypes.LargeBinary):
    __visit_name__: str

class LONG(sqltypes.Text):
    __visit_name__: str

class _OracleDateLiteralRender: ...

class DATE(_OracleDateLiteralRender, sqltypes.DateTime):
    __visit_name__: str
    def literal_processor(self, dialect): ...

class _OracleDate(_OracleDateLiteralRender, sqltypes.Date):
    def literal_processor(self, dialect): ...

class INTERVAL(sqltypes.NativeForEmulated, sqltypes._AbstractInterval):
    __visit_name__: str
    day_precision: Incomplete
    second_precision: Incomplete
    def __init__(self, day_precision: Incomplete | None = ..., second_precision: Incomplete | None = ...) -> None: ...
    @classmethod
    def adapt_emulated_to_native(cls, interval: sqltypes.Interval, **kw): ...
    def as_generic(self, allow_nulltype: bool = ...): ...
    @property
    def python_type(self) -> Type[dt.timedelta]: ...
    def literal_processor(self, dialect: Dialect) -> Optional[_LiteralProcessorType[dt.timedelta]]: ...

class TIMESTAMP(sqltypes.TIMESTAMP):
    local_timezone: Incomplete
    def __init__(self, timezone: bool = ..., local_timezone: bool = ...) -> None: ...

class ROWID(sqltypes.TypeEngine):
    __visit_name__: str

class _OracleBoolean(sqltypes.Boolean):
    def get_dbapi_type(self, dbapi): ...
