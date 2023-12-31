from .. import util as util
from ..orm import InspectionAttrExtensionType as InspectionAttrExtensionType, ORMDescriptor as ORMDescriptor, attributes as attributes, interfaces as interfaces
from ..orm.attributes import QueryableAttribute as QueryableAttribute
from ..orm.interfaces import MapperProperty as MapperProperty
from ..orm.util import AliasedInsp as AliasedInsp
from ..sql import SQLColumnExpression as SQLColumnExpression, roles as roles
from ..sql._typing import _ColumnExpressionArgument, _DMLColumnArgument, _HasClauseElement, _InfoType, is_has_clause_element as is_has_clause_element
from ..sql.elements import ColumnElement as ColumnElement, SQLCoreOperations as SQLCoreOperations
from ..sql.operators import OperatorType as OperatorType
from ..util.typing import Concatenate as Concatenate, Literal as Literal, ParamSpec as ParamSpec, Protocol as Protocol, Self as Self
from _typeshed import Incomplete
from typing import Any, Callable, Generic, List, Optional, Tuple, Type, Union, overload

class HybridExtensionType(InspectionAttrExtensionType):
    HYBRID_METHOD: str
    HYBRID_PROPERTY: str

class _HybridGetterType(Protocol[_T_co]):
    def __call__(s, self: Any) -> _T_co: ...

class _HybridSetterType(Protocol[_T_con]):
    def __call__(s, self: Any, value: _T_con) -> None: ...

class _HybridUpdaterType(Protocol[_T_con]):
    def __call__(s, cls: Any, value: Union[_T_con, _ColumnExpressionArgument[_T_con]]) -> List[Tuple[_DMLColumnArgument, Any]]: ...

class _HybridDeleterType(Protocol[_T_co]):
    def __call__(s, self: Any) -> None: ...

class _HybridExprCallableType(Protocol[_T_co]):
    def __call__(s, cls: Any) -> Union[_HasClauseElement, SQLColumnExpression[_T_co]]: ...

class _HybridComparatorCallableType(Protocol[_T]):
    def __call__(self, cls: Any) -> Comparator[_T]: ...

class _HybridClassLevelAccessor(QueryableAttribute[_T]):
    def getter(self, fget: _HybridGetterType[_T]) -> hybrid_property[_T]: ...
    def setter(self, fset: _HybridSetterType[_T]) -> hybrid_property[_T]: ...
    def deleter(self, fdel: _HybridDeleterType[_T]) -> hybrid_property[_T]: ...
    @property
    def overrides(self) -> hybrid_property[_T]: ...
    def update_expression(self, meth: _HybridUpdaterType[_T]) -> hybrid_property[_T]: ...

class hybrid_method(interfaces.InspectionAttrInfo, Generic[_P, _R]):
    is_attribute: bool
    extension_type: Incomplete
    func: Incomplete
    def __init__(self, func: Callable[Concatenate[Any, _P], _R], expr: Optional[Callable[Concatenate[Any, _P], SQLCoreOperations[_R]]] = ...) -> None: ...
    @property
    def inplace(self) -> Self: ...
    @overload
    def __get__(self, instance: Literal[None], owner: Type[object]) -> Callable[_P, SQLCoreOperations[_R]]: ...
    @overload
    def __get__(self, instance: object, owner: Type[object]) -> Callable[_P, _R]: ...
    expr: Incomplete
    def expression(self, expr: Callable[Concatenate[Any, _P], SQLCoreOperations[_R]]) -> hybrid_method[_P, _R]: ...

class hybrid_property(interfaces.InspectionAttrInfo, ORMDescriptor[_T]):
    is_attribute: bool
    extension_type: Incomplete
    fget: Incomplete
    fset: Incomplete
    fdel: Incomplete
    expr: Incomplete
    custom_comparator: Incomplete
    update_expr: Incomplete
    def __init__(self, fget: _HybridGetterType[_T], fset: Optional[_HybridSetterType[_T]] = ..., fdel: Optional[_HybridDeleterType[_T]] = ..., expr: Optional[_HybridExprCallableType[_T]] = ..., custom_comparator: Optional[Comparator[_T]] = ..., update_expr: Optional[_HybridUpdaterType[_T]] = ...) -> None: ...
    @overload
    def __get__(self, instance: Any, owner: Literal[None]) -> Self: ...
    @overload
    def __get__(self, instance: Literal[None], owner: Type[object]) -> _HybridClassLevelAccessor[_T]: ...
    @overload
    def __get__(self, instance: object, owner: Type[object]) -> _T: ...
    def __set__(self, instance: object, value: Any) -> None: ...
    def __delete__(self, instance: object) -> None: ...
    @property
    def overrides(self) -> Self: ...
    class _InPlace(Generic[_TE]):
        attr: Incomplete
        def __init__(self, attr: hybrid_property[_TE]) -> None: ...
        def getter(self, fget: _HybridGetterType[_TE]) -> hybrid_property[_TE]: ...
        def setter(self, fset: _HybridSetterType[_TE]) -> hybrid_property[_TE]: ...
        def deleter(self, fdel: _HybridDeleterType[_TE]) -> hybrid_property[_TE]: ...
        def expression(self, expr: _HybridExprCallableType[_TE]) -> hybrid_property[_TE]: ...
        def comparator(self, comparator: _HybridComparatorCallableType[_TE]) -> hybrid_property[_TE]: ...
        def update_expression(self, meth: _HybridUpdaterType[_TE]) -> hybrid_property[_TE]: ...
    @property
    def inplace(self) -> _InPlace[_T]: ...
    def getter(self, fget: _HybridGetterType[_T]) -> hybrid_property[_T]: ...
    def setter(self, fset: _HybridSetterType[_T]) -> hybrid_property[_T]: ...
    def deleter(self, fdel: _HybridDeleterType[_T]) -> hybrid_property[_T]: ...
    def expression(self, expr: _HybridExprCallableType[_T]) -> hybrid_property[_T]: ...
    def comparator(self, comparator: _HybridComparatorCallableType[_T]) -> hybrid_property[_T]: ...
    def update_expression(self, meth: _HybridUpdaterType[_T]) -> hybrid_property[_T]: ...

class Comparator(interfaces.PropComparator[_T]):
    expression: Incomplete
    def __init__(self, expression: Union[_HasClauseElement, SQLColumnExpression[_T]]) -> None: ...
    def __clause_element__(self) -> roles.ColumnsClauseRole: ...
    def property(self) -> interfaces.MapperProperty[_T]: ...
    def adapt_to_entity(self, adapt_to_entity: AliasedInsp[Any]) -> Comparator[_T]: ...

class ExprComparator(Comparator[_T]):
    cls: Incomplete
    expression: Incomplete
    hybrid: Incomplete
    def __init__(self, cls: Type[Any], expression: Union[_HasClauseElement, SQLColumnExpression[_T]], hybrid: hybrid_property[_T]) -> None: ...
    def __getattr__(self, key: str) -> Any: ...
    def info(self) -> _InfoType: ...
    def property(self) -> MapperProperty[_T]: ...
    def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
