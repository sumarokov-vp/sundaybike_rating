from .engine.interfaces import Dialect as Dialect, _AnyExecuteParams
from .sql.compiler import Compiled as Compiled, TypeCompiler as TypeCompiler
from .sql.elements import ClauseElement as ClauseElement
from .util import compat as compat
from _typeshed import Incomplete
from typing import Any, Optional, Tuple, Type, Union, overload

class HasDescriptionCode:
    code: Optional[str]
    def __init__(self, *arg: Any, **kw: Any) -> None: ...

class SQLAlchemyError(HasDescriptionCode, Exception): ...
class ArgumentError(SQLAlchemyError): ...
class DuplicateColumnError(ArgumentError): ...

class ObjectNotExecutableError(ArgumentError):
    target: Incomplete
    def __init__(self, target: Any) -> None: ...
    def __reduce__(self) -> Union[str, Tuple[Any, ...]]: ...

class NoSuchModuleError(ArgumentError): ...
class NoForeignKeysError(ArgumentError): ...
class AmbiguousForeignKeysError(ArgumentError): ...
class ConstraintColumnNotFoundError(ArgumentError): ...

class CircularDependencyError(SQLAlchemyError):
    cycles: Incomplete
    edges: Incomplete
    def __init__(self, message: str, cycles: Any, edges: Any, msg: Optional[str] = ..., code: Optional[str] = ...) -> None: ...
    def __reduce__(self) -> Union[str, Tuple[Any, ...]]: ...

class CompileError(SQLAlchemyError): ...

class UnsupportedCompilationError(CompileError):
    code: str
    compiler: Incomplete
    element_type: Incomplete
    message: Incomplete
    def __init__(self, compiler: Union[Compiled, TypeCompiler], element_type: Type[ClauseElement], message: Optional[str] = ...) -> None: ...
    def __reduce__(self) -> Union[str, Tuple[Any, ...]]: ...

class IdentifierError(SQLAlchemyError): ...

class DisconnectionError(SQLAlchemyError):
    invalidate_pool: bool

class InvalidatePoolError(DisconnectionError):
    invalidate_pool: bool

class TimeoutError(SQLAlchemyError): ...
class InvalidRequestError(SQLAlchemyError): ...
class IllegalStateChangeError(InvalidRequestError): ...
class NoInspectionAvailable(InvalidRequestError): ...
class PendingRollbackError(InvalidRequestError): ...
class ResourceClosedError(InvalidRequestError): ...
class NoSuchColumnError(InvalidRequestError, KeyError): ...
class NoResultFound(InvalidRequestError): ...
class MultipleResultsFound(InvalidRequestError): ...

class NoReferenceError(InvalidRequestError):
    table_name: str

class AwaitRequired(InvalidRequestError):
    code: str

class MissingGreenlet(InvalidRequestError):
    code: str

class NoReferencedTableError(NoReferenceError):
    table_name: Incomplete
    def __init__(self, message: str, tname: str) -> None: ...
    def __reduce__(self) -> Union[str, Tuple[Any, ...]]: ...

class NoReferencedColumnError(NoReferenceError):
    table_name: Incomplete
    column_name: Incomplete
    def __init__(self, message: str, tname: str, cname: str) -> None: ...
    def __reduce__(self) -> Union[str, Tuple[Any, ...]]: ...

class NoSuchTableError(InvalidRequestError): ...
class UnreflectableTableError(InvalidRequestError): ...
class UnboundExecutionError(InvalidRequestError): ...
class DontWrapMixin: ...

class StatementError(SQLAlchemyError):
    statement: Optional[str]
    params: Optional[_AnyExecuteParams]
    orig: Optional[BaseException]
    ismulti: Optional[bool]
    connection_invalidated: bool
    hide_parameters: Incomplete
    detail: Incomplete
    def __init__(self, message: str, statement: Optional[str], params: Optional[_AnyExecuteParams], orig: Optional[BaseException], hide_parameters: bool = ..., code: Optional[str] = ..., ismulti: Optional[bool] = ...) -> None: ...
    def add_detail(self, msg: str) -> None: ...
    def __reduce__(self) -> Union[str, Tuple[Any, ...]]: ...

class DBAPIError(StatementError):
    code: str
    @overload
    @classmethod
    def instance(cls, statement: Optional[str], params: Optional[_AnyExecuteParams], orig: Exception, dbapi_base_err: Type[Exception], hide_parameters: bool = ..., connection_invalidated: bool = ..., dialect: Optional[Dialect] = ..., ismulti: Optional[bool] = ...) -> StatementError: ...
    @overload
    @classmethod
    def instance(cls, statement: Optional[str], params: Optional[_AnyExecuteParams], orig: DontWrapMixin, dbapi_base_err: Type[Exception], hide_parameters: bool = ..., connection_invalidated: bool = ..., dialect: Optional[Dialect] = ..., ismulti: Optional[bool] = ...) -> DontWrapMixin: ...
    @overload
    @classmethod
    def instance(cls, statement: Optional[str], params: Optional[_AnyExecuteParams], orig: BaseException, dbapi_base_err: Type[Exception], hide_parameters: bool = ..., connection_invalidated: bool = ..., dialect: Optional[Dialect] = ..., ismulti: Optional[bool] = ...) -> BaseException: ...
    def __reduce__(self) -> Union[str, Tuple[Any, ...]]: ...
    connection_invalidated: Incomplete
    def __init__(self, statement: Optional[str], params: Optional[_AnyExecuteParams], orig: BaseException, hide_parameters: bool = ..., connection_invalidated: bool = ..., code: Optional[str] = ..., ismulti: Optional[bool] = ...) -> None: ...

class InterfaceError(DBAPIError):
    code: str

class DatabaseError(DBAPIError):
    code: str

class DataError(DatabaseError):
    code: str

class OperationalError(DatabaseError):
    code: str

class IntegrityError(DatabaseError):
    code: str

class InternalError(DatabaseError):
    code: str

class ProgrammingError(DatabaseError):
    code: str

class NotSupportedError(DatabaseError):
    code: str

class SATestSuiteWarning(Warning): ...

class SADeprecationWarning(HasDescriptionCode, DeprecationWarning):
    deprecated_since: Optional[str]

class Base20DeprecationWarning(SADeprecationWarning):
    deprecated_since: Optional[str]

class LegacyAPIWarning(Base20DeprecationWarning): ...
class MovedIn20Warning(Base20DeprecationWarning): ...

class SAPendingDeprecationWarning(PendingDeprecationWarning):
    deprecated_since: Optional[str]

class SAWarning(HasDescriptionCode, RuntimeWarning): ...
