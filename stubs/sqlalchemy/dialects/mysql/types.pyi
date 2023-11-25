from ... import exc as exc, util as util
from ...sql import sqltypes as sqltypes
from _typeshed import Incomplete

class _NumericType:
    unsigned: Incomplete
    zerofill: Incomplete
    def __init__(self, unsigned: bool = ..., zerofill: bool = ..., **kw) -> None: ...

class _FloatType(_NumericType, sqltypes.Float):
    scale: Incomplete
    def __init__(self, precision: Incomplete | None = ..., scale: Incomplete | None = ..., asdecimal: bool = ..., **kw) -> None: ...

class _IntegerType(_NumericType, sqltypes.Integer):
    display_width: Incomplete
    def __init__(self, display_width: Incomplete | None = ..., **kw) -> None: ...

class _StringType(sqltypes.String):
    charset: Incomplete
    ascii: Incomplete
    unicode: Incomplete
    binary: Incomplete
    national: Incomplete
    def __init__(self, charset: Incomplete | None = ..., collation: Incomplete | None = ..., ascii: bool = ..., binary: bool = ..., unicode: bool = ..., national: bool = ..., **kw) -> None: ...

class _MatchType(sqltypes.Float, sqltypes.MatchType):
    def __init__(self, **kw) -> None: ...

class NUMERIC(_NumericType, sqltypes.NUMERIC):
    __visit_name__: str
    def __init__(self, precision: Incomplete | None = ..., scale: Incomplete | None = ..., asdecimal: bool = ..., **kw) -> None: ...

class DECIMAL(_NumericType, sqltypes.DECIMAL):
    __visit_name__: str
    def __init__(self, precision: Incomplete | None = ..., scale: Incomplete | None = ..., asdecimal: bool = ..., **kw) -> None: ...

class DOUBLE(_FloatType, sqltypes.DOUBLE):
    __visit_name__: str
    def __init__(self, precision: Incomplete | None = ..., scale: Incomplete | None = ..., asdecimal: bool = ..., **kw) -> None: ...

class REAL(_FloatType, sqltypes.REAL):
    __visit_name__: str
    def __init__(self, precision: Incomplete | None = ..., scale: Incomplete | None = ..., asdecimal: bool = ..., **kw) -> None: ...

class FLOAT(_FloatType, sqltypes.FLOAT):
    __visit_name__: str
    def __init__(self, precision: Incomplete | None = ..., scale: Incomplete | None = ..., asdecimal: bool = ..., **kw) -> None: ...
    def bind_processor(self, dialect) -> None: ...

class INTEGER(_IntegerType, sqltypes.INTEGER):
    __visit_name__: str
    def __init__(self, display_width: Incomplete | None = ..., **kw) -> None: ...

class BIGINT(_IntegerType, sqltypes.BIGINT):
    __visit_name__: str
    def __init__(self, display_width: Incomplete | None = ..., **kw) -> None: ...

class MEDIUMINT(_IntegerType):
    __visit_name__: str
    def __init__(self, display_width: Incomplete | None = ..., **kw) -> None: ...

class TINYINT(_IntegerType):
    __visit_name__: str
    def __init__(self, display_width: Incomplete | None = ..., **kw) -> None: ...

class SMALLINT(_IntegerType, sqltypes.SMALLINT):
    __visit_name__: str
    def __init__(self, display_width: Incomplete | None = ..., **kw) -> None: ...

class BIT(sqltypes.TypeEngine):
    __visit_name__: str
    length: Incomplete
    def __init__(self, length: Incomplete | None = ...) -> None: ...
    def result_processor(self, dialect, coltype): ...

class TIME(sqltypes.TIME):
    __visit_name__: str
    fsp: Incomplete
    def __init__(self, timezone: bool = ..., fsp: Incomplete | None = ...) -> None: ...
    def result_processor(self, dialect, coltype): ...

class TIMESTAMP(sqltypes.TIMESTAMP):
    __visit_name__: str
    fsp: Incomplete
    def __init__(self, timezone: bool = ..., fsp: Incomplete | None = ...) -> None: ...

class DATETIME(sqltypes.DATETIME):
    __visit_name__: str
    fsp: Incomplete
    def __init__(self, timezone: bool = ..., fsp: Incomplete | None = ...) -> None: ...

class YEAR(sqltypes.TypeEngine):
    __visit_name__: str
    display_width: Incomplete
    def __init__(self, display_width: Incomplete | None = ...) -> None: ...

class TEXT(_StringType, sqltypes.TEXT):
    __visit_name__: str
    def __init__(self, length: Incomplete | None = ..., **kw) -> None: ...

class TINYTEXT(_StringType):
    __visit_name__: str
    def __init__(self, **kwargs) -> None: ...

class MEDIUMTEXT(_StringType):
    __visit_name__: str
    def __init__(self, **kwargs) -> None: ...

class LONGTEXT(_StringType):
    __visit_name__: str
    def __init__(self, **kwargs) -> None: ...

class VARCHAR(_StringType, sqltypes.VARCHAR):
    __visit_name__: str
    def __init__(self, length: Incomplete | None = ..., **kwargs) -> None: ...

class CHAR(_StringType, sqltypes.CHAR):
    __visit_name__: str
    def __init__(self, length: Incomplete | None = ..., **kwargs) -> None: ...

class NVARCHAR(_StringType, sqltypes.NVARCHAR):
    __visit_name__: str
    def __init__(self, length: Incomplete | None = ..., **kwargs) -> None: ...

class NCHAR(_StringType, sqltypes.NCHAR):
    __visit_name__: str
    def __init__(self, length: Incomplete | None = ..., **kwargs) -> None: ...

class TINYBLOB(sqltypes._Binary):
    __visit_name__: str

class MEDIUMBLOB(sqltypes._Binary):
    __visit_name__: str

class LONGBLOB(sqltypes._Binary):
    __visit_name__: str
