import typing
from . import exc as exc
from .. import inspection as inspection, util as util
from ..sql import roles as roles
from ..sql._typing import _ColumnExpressionArgument, _InfoType
from ..sql.elements import ColumnElement as ColumnElement, SQLColumnExpression as SQLColumnExpression, SQLCoreOperations as SQLCoreOperations
from ..sql.operators import OperatorType as OperatorType
from ..util import FastIntFlag as FastIntFlag
from ..util.langhelpers import TypingOnly as TypingOnly
from ..util.typing import Literal as Literal
from ._typing import _EntityType, insp_is_mapper as insp_is_mapper
from .attributes import InstrumentedAttribute as InstrumentedAttribute
from .dynamic import AppenderQuery as AppenderQuery
from .instrumentation import ClassManager as ClassManager
from .interfaces import PropComparator as PropComparator
from .mapper import Mapper as Mapper
from .state import InstanceState as InstanceState
from .util import AliasedClass as AliasedClass
from .writeonly import WriteOnlyCollection as WriteOnlyCollection
from _typeshed import Incomplete
from enum import Enum
from typing import Any, Dict, Generic, Optional, Type, Union, overload

class LoaderCallableStatus(Enum):
    PASSIVE_NO_RESULT: int
    PASSIVE_CLASS_MISMATCH: int
    ATTR_WAS_SET: int
    ATTR_EMPTY: int
    NO_VALUE: int
    NEVER_SET = NO_VALUE

PASSIVE_NO_RESULT: Incomplete
PASSIVE_CLASS_MISMATCH: Incomplete
ATTR_WAS_SET: Incomplete
ATTR_EMPTY: Incomplete
NO_VALUE: Incomplete
NEVER_SET = NO_VALUE

class PassiveFlag(FastIntFlag):
    NO_CHANGE: int
    CALLABLES_OK: int
    SQL_OK: int
    RELATED_OBJECT_OK: int
    INIT_OK: int
    NON_PERSISTENT_OK: int
    LOAD_AGAINST_COMMITTED: int
    NO_AUTOFLUSH: int
    NO_RAISE: int
    DEFERRED_HISTORY_LOAD: int
    INCLUDE_PENDING_MUTATIONS: int
    PASSIVE_OFF: Incomplete
    PASSIVE_RETURN_NO_VALUE: Incomplete
    PASSIVE_NO_INITIALIZE: Incomplete
    PASSIVE_NO_FETCH: Incomplete
    PASSIVE_NO_FETCH_RELATED: Incomplete
    PASSIVE_ONLY_PERSISTENT: Incomplete
    PASSIVE_MERGE: Incomplete

NO_CHANGE: Incomplete
CALLABLES_OK: Incomplete
SQL_OK: Incomplete
RELATED_OBJECT_OK: Incomplete
INIT_OK: Incomplete
NON_PERSISTENT_OK: Incomplete
LOAD_AGAINST_COMMITTED: Incomplete
NO_AUTOFLUSH: Incomplete
NO_RAISE: Incomplete
DEFERRED_HISTORY_LOAD: Incomplete
INCLUDE_PENDING_MUTATIONS: Incomplete
PASSIVE_OFF: Incomplete
PASSIVE_RETURN_NO_VALUE: Incomplete
PASSIVE_NO_INITIALIZE: Incomplete
PASSIVE_NO_FETCH: Incomplete
PASSIVE_NO_FETCH_RELATED: Incomplete
PASSIVE_ONLY_PERSISTENT: Incomplete
PASSIVE_MERGE: Incomplete
DEFAULT_MANAGER_ATTR: str
DEFAULT_STATE_ATTR: str

class EventConstants(Enum):
    EXT_CONTINUE: int
    EXT_STOP: int
    EXT_SKIP: int
    NO_KEY: int

EXT_CONTINUE: Incomplete
EXT_STOP: Incomplete
EXT_SKIP: Incomplete
NO_KEY: Incomplete

class RelationshipDirection(Enum):
    ONETOMANY: int
    MANYTOONE: int
    MANYTOMANY: int

ONETOMANY: Incomplete
MANYTOONE: Incomplete
MANYTOMANY: Incomplete

class InspectionAttrExtensionType(Enum): ...

class NotExtension(InspectionAttrExtensionType):
    NOT_EXTENSION: str

def manager_of_class(cls) -> ClassManager[_O]: ...
@overload
def opt_manager_of_class(cls) -> None: ...
@overload
def opt_manager_of_class(cls) -> Optional[ClassManager[_O]]: ...
def instance_state(instance: _O) -> InstanceState[_O]: ...
def instance_dict(instance: object) -> Dict[str, Any]: ...
def instance_str(instance: object) -> str: ...
def state_str(state: InstanceState[Any]) -> str: ...
def state_class_str(state: InstanceState[Any]) -> str: ...
def attribute_str(instance: object, attribute: str) -> str: ...
def state_attribute_str(state: InstanceState[Any], attribute: str) -> str: ...
def object_mapper(instance: _T) -> Mapper[_T]: ...
def object_state(instance: _T) -> InstanceState[_T]: ...
def class_mapper(class_: Type[_O], configure: bool = ...) -> Mapper[_O]: ...

class InspectionAttr:
    is_selectable: bool
    is_aliased_class: bool
    is_instance: bool
    is_mapper: bool
    is_bundle: bool
    is_property: bool
    is_attribute: bool
    is_clause_element: bool
    extension_type: InspectionAttrExtensionType

class InspectionAttrInfo(InspectionAttr):
    def info(self) -> _InfoType: ...

class SQLORMOperations(SQLCoreOperations[_T_co], TypingOnly):
    def of_type(self, class_: _EntityType[Any]) -> PropComparator[_T_co]: ...
    def and_(self, *criteria: _ColumnExpressionArgument[bool]) -> PropComparator[bool]: ...
    def any(self, criterion: Optional[_ColumnExpressionArgument[bool]] = ..., **kwargs: Any) -> ColumnElement[bool]: ...
    def has(self, criterion: Optional[_ColumnExpressionArgument[bool]] = ..., **kwargs: Any) -> ColumnElement[bool]: ...

class ORMDescriptor(TypingOnly, Generic[_T_co]):
    @overload
    def __get__(self, instance: Any, owner: Literal[None]) -> ORMDescriptor[_T_co]: ...
    @overload
    def __get__(self, instance: Literal[None], owner: Any) -> SQLCoreOperations[_T_co]: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> _T_co: ...

class _MappedAnnotationBase(TypingOnly, Generic[_T_co]): ...
class SQLORMExpression(SQLORMOperations[_T_co], SQLColumnExpression[_T_co], TypingOnly): ...

class Mapped(SQLORMExpression[_T_co], ORMDescriptor[_T_co], _MappedAnnotationBase[_T_co], roles.DDLConstraintColumnRole):
    @overload
    def __get__(self, instance: None, owner: Any) -> InstrumentedAttribute[_T_co]: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> _T_co: ...
    def __set__(self, instance: Any, value: Union[SQLCoreOperations[_T_co], _T_co]) -> None: ...
    def __delete__(self, instance: Any) -> None: ...

class _MappedAttribute(TypingOnly, Generic[_T_co]): ...

class _DeclarativeMapped(Mapped[_T_co], _MappedAttribute[_T_co]):
    def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> Any: ...
    __sa_operate__ = operate
    def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> Any: ...

class DynamicMapped(_MappedAnnotationBase[_T_co]):
    @overload
    def __get__(self, instance: None, owner: Any) -> InstrumentedAttribute[_T_co]: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> AppenderQuery[_T_co]: ...
    def __set__(self, instance: Any, value: typing.Collection[_T_co]) -> None: ...

class WriteOnlyMapped(_MappedAnnotationBase[_T_co]):
    @overload
    def __get__(self, instance: None, owner: Any) -> InstrumentedAttribute[_T_co]: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> WriteOnlyCollection[_T_co]: ...
    def __set__(self, instance: Any, value: typing.Collection[_T_co]) -> None: ...
