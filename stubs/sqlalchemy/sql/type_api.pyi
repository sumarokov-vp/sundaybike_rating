from .. import exc as exc, util as util
from ..engine.interfaces import Dialect as Dialect
from ..util.typing import GenericProtocol as GenericProtocol, Protocol as Protocol, Self as Self, TypeGuard as TypeGuard, TypedDict as TypedDict
from ._typing import _TypeEngineArgument
from .base import SchemaEventTarget as SchemaEventTarget
from .cache_key import CacheConst as CacheConst, NO_CACHE as NO_CACHE
from .elements import BindParameter as BindParameter, ColumnElement as ColumnElement
from .operators import ColumnOperators as ColumnOperators, OperatorType as OperatorType
from .visitors import Visitable as Visitable
from enum import Enum
from types import ModuleType
from typing import Any, Callable, Dict, Generic, Mapping, Optional, Sequence, Type, Union, overload

class _NoValueInList(Enum):
    NO_VALUE_IN_LIST: int

class _LiteralProcessorType(Protocol[_T_co]):
    def __call__(self, value: Any) -> str: ...

class _BindProcessorType(Protocol[_T_con]):
    def __call__(self, value: Optional[_T_con]) -> Any: ...

class _ResultProcessorType(Protocol[_T_co]):
    def __call__(self, value: Any) -> Optional[_T_co]: ...

class _SentinelProcessorType(Protocol[_T_co]):
    def __call__(self, value: Any) -> Optional[_T_co]: ...

class _BaseTypeMemoDict(TypedDict):
    impl: TypeEngine[Any]
    result: Dict[Any, Optional[_ResultProcessorType[Any]]]

class _TypeMemoDict(_BaseTypeMemoDict, total=False):
    literal: Optional[_LiteralProcessorType[Any]]
    bind: Optional[_BindProcessorType[Any]]
    sentinel: Optional[_SentinelProcessorType[Any]]
    custom: Dict[Any, object]

class _ComparatorFactory(Protocol[_T]):
    def __call__(self, expr: ColumnElement[_T]) -> TypeEngine.Comparator[_T]: ...

class TypeEngine(Visitable, Generic[_T]):
    render_bind_cast: bool
    render_literal_cast: bool
    class Comparator(ColumnOperators, Generic[_CT]):
        expr: ColumnElement[_CT]
        type: TypeEngine[_CT]
        def __clause_element__(self) -> ColumnElement[_CT]: ...
        def __init__(self, expr: ColumnElement[_CT]) -> None: ...
        def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> ColumnElement[_CT]: ...
        def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> ColumnElement[_CT]: ...
    hashable: bool
    comparator_factory: _ComparatorFactory[Any]
    sort_key_function: Optional[Callable[[Any], Any]]
    should_evaluate_none: bool
    def evaluates_none(self) -> Self: ...
    def copy(self, **kw: Any) -> Self: ...
    def copy_value(self, value: Any) -> Any: ...
    def literal_processor(self, dialect: Dialect) -> Optional[_LiteralProcessorType[_T]]: ...
    def bind_processor(self, dialect: Dialect) -> Optional[_BindProcessorType[_T]]: ...
    def result_processor(self, dialect: Dialect, coltype: object) -> Optional[_ResultProcessorType[_T]]: ...
    def column_expression(self, colexpr: ColumnElement[_T]) -> Optional[ColumnElement[_T]]: ...
    def bind_expression(self, bindvalue: BindParameter[_T]) -> Optional[ColumnElement[_T]]: ...
    def compare_values(self, x: Any, y: Any) -> bool: ...
    def get_dbapi_type(self, dbapi: ModuleType) -> Optional[Any]: ...
    @property
    def python_type(self) -> Type[Any]: ...
    def with_variant(self, type_: _TypeEngineArgument[Any], *dialect_names: str) -> Self: ...
    def as_generic(self, allow_nulltype: bool = ...) -> TypeEngine[_T]: ...
    def dialect_impl(self, dialect: Dialect) -> TypeEngine[_T]: ...
    @overload
    def adapt(self, cls: Type[_TE], **kw: Any) -> _TE: ...
    @overload
    def adapt(self, cls: Type[TypeEngineMixin], **kw: Any) -> TypeEngine[Any]: ...
    def coerce_compared_value(self, op: Optional[OperatorType], value: Any) -> TypeEngine[Any]: ...
    def compile(self, dialect: Optional[Dialect] = ...) -> str: ...

class TypeEngineMixin:
    @overload
    def adapt(self, cls: Type[_TE], **kw: Any) -> _TE: ...
    @overload
    def adapt(self, cls: Type[TypeEngineMixin], **kw: Any) -> TypeEngine[Any]: ...
    def dialect_impl(self, dialect: Dialect) -> TypeEngine[Any]: ...

class ExternalType(TypeEngineMixin):
    cache_ok: Optional[bool]

class UserDefinedType(ExternalType, TypeEngineMixin, TypeEngine[_T], util.EnsureKWArg):
    __visit_name__: str
    ensure_kwarg: str
    def coerce_compared_value(self, op: Optional[OperatorType], value: Any) -> TypeEngine[Any]: ...

class Emulated(TypeEngineMixin):
    native: bool
    def adapt_to_emulated(self, impltype: Type[Union[TypeEngine[Any], TypeEngineMixin]], **kw: Any) -> TypeEngine[Any]: ...
    @overload
    def adapt(self, cls: Type[_TE], **kw: Any) -> _TE: ...
    @overload
    def adapt(self, cls: Type[TypeEngineMixin], **kw: Any) -> TypeEngine[Any]: ...

class NativeForEmulated(TypeEngineMixin):
    @classmethod
    def adapt_native_to_emulated(cls, impl: Union[TypeEngine[Any], TypeEngineMixin], **kw: Any) -> TypeEngine[Any]: ...
    @classmethod
    def adapt_emulated_to_native(cls, impl: Union[TypeEngine[Any], TypeEngineMixin], **kw: Any) -> TypeEngine[Any]: ...

class TypeDecorator(SchemaEventTarget, ExternalType, TypeEngine[_T]):
    __visit_name__: str
    impl: Union[TypeEngine[Any], Type[TypeEngine[Any]]]
    def impl_instance(self) -> TypeEngine[Any]: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    coerce_to_is_types: Sequence[Type[Any]]
    class Comparator(TypeEngine.Comparator[_CT]):
        def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> ColumnElement[_CT]: ...
        def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> ColumnElement[_CT]: ...
    @property
    def comparator_factory(self) -> _ComparatorFactory[Any]: ...
    def type_engine(self, dialect: Dialect) -> TypeEngine[Any]: ...
    def load_dialect_impl(self, dialect: Dialect) -> TypeEngine[Any]: ...
    def __getattr__(self, key: str) -> Any: ...
    def process_literal_param(self, value: Optional[_T], dialect: Dialect) -> str: ...
    def process_bind_param(self, value: Optional[_T], dialect: Dialect) -> Any: ...
    def process_result_value(self, value: Optional[Any], dialect: Dialect) -> Optional[_T]: ...
    def literal_processor(self, dialect: Dialect) -> Optional[_LiteralProcessorType[_T]]: ...
    def bind_processor(self, dialect: Dialect) -> Optional[_BindProcessorType[_T]]: ...
    def result_processor(self, dialect: Dialect, coltype: Any) -> Optional[_ResultProcessorType[_T]]: ...
    def bind_expression(self, bindparam: BindParameter[_T]) -> Optional[ColumnElement[_T]]: ...
    def column_expression(self, column: ColumnElement[_T]) -> Optional[ColumnElement[_T]]: ...
    def coerce_compared_value(self, op: Optional[OperatorType], value: Any) -> Any: ...
    def copy(self, **kw: Any) -> Self: ...
    def get_dbapi_type(self, dbapi: ModuleType) -> Optional[Any]: ...
    def compare_values(self, x: Any, y: Any) -> bool: ...
    @property
    def sort_key_function(self) -> Optional[Callable[[Any], Any]]: ...

class Variant(TypeDecorator[_T]):
    def __init__(self, *arg: Any, **kw: Any) -> None: ...

@overload
def to_instance(typeobj: Union[Type[_TE], _TE], *arg: Any, **kw: Any) -> _TE: ...
@overload
def to_instance(typeobj: None, *arg: Any, **kw: Any) -> TypeEngine[None]: ...
def adapt_type(typeobj: TypeEngine[Any], colspecs: Mapping[Type[Any], Type[TypeEngine[Any]]]) -> TypeEngine[Any]: ...