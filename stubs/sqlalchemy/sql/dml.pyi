from . import coercions as coercions, roles as roles
from .. import exc as exc, util as util
from ..util.typing import Self as Self, TypeGuard as TypeGuard
from ._typing import _ColumnExpressionArgument, _ColumnsClauseArgument, _DMLColumnArgument, _DMLColumnKeyMapping, _DMLTableArgument, _T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _TP, _TypedColumnClauseArgument as _TCCA, is_column_element as is_column_element, is_named_from_clause as is_named_from_clause
from .base import ColumnCollection as ColumnCollection, CompileState as CompileState, DialectKWArgs as DialectKWArgs, Executable as Executable, Generative as Generative, HasCompileState as HasCompileState, ReadOnlyColumnCollection as ReadOnlyColumnCollection
from .compiler import SQLCompiler as SQLCompiler
from .elements import BooleanClauseList as BooleanClauseList, ClauseElement as ClauseElement, ColumnClause as ColumnClause, ColumnElement as ColumnElement, KeyedColumnElement as KeyedColumnElement, Null as Null
from .selectable import Alias as Alias, ExecutableReturnsRows as ExecutableReturnsRows, FromClause as FromClause, HasCTE as HasCTE, HasPrefixes as HasPrefixes, Join as Join, Select as Select, SelectLabelStyle as SelectLabelStyle, Selectable as Selectable, TableClause as TableClause, TypedReturnsRows as TypedReturnsRows
from .sqltypes import NullType as NullType
from .visitors import InternalTraversal as InternalTraversal
from _typeshed import Incomplete
from typing import Any, Dict, Iterable, List, NoReturn, Optional, Sequence, Tuple, Type, Union, overload

def isupdate(dml: DMLState) -> TypeGuard[UpdateDMLState]: ...
def isdelete(dml: DMLState) -> TypeGuard[DeleteDMLState]: ...
def isinsert(dml: DMLState) -> TypeGuard[InsertDMLState]: ...

class DMLState(CompileState):
    isupdate: bool
    isdelete: bool
    isinsert: bool
    statement: UpdateBase
    def __init__(self, statement: UpdateBase, compiler: SQLCompiler, **kw: Any) -> None: ...
    @classmethod
    def get_entity_description(cls, statement: UpdateBase) -> Dict[str, Any]: ...
    @classmethod
    def get_returning_column_descriptions(cls, statement: UpdateBase) -> List[Dict[str, Any]]: ...
    @property
    def dml_table(self) -> _DMLTableElement: ...
    @classmethod
    def get_plugin_class(cls, statement: Executable) -> Type[DMLState]: ...

class InsertDMLState(DMLState):
    isinsert: bool
    include_table_with_column_exprs: bool
    statement: Incomplete
    def __init__(self, statement: Insert, compiler: SQLCompiler, disable_implicit_returning: bool = ..., **kw: Any) -> None: ...

class UpdateDMLState(DMLState):
    isupdate: bool
    include_table_with_column_exprs: bool
    statement: Incomplete
    is_multitable: Incomplete
    def __init__(self, statement: Update, compiler: SQLCompiler, **kw: Any) -> None: ...

class DeleteDMLState(DMLState):
    isdelete: bool
    statement: Incomplete
    is_multitable: Incomplete
    def __init__(self, statement: Delete, compiler: SQLCompiler, **kw: Any) -> None: ...

class UpdateBase(roles.DMLRole, HasCTE, HasCompileState, DialectKWArgs, HasPrefixes, Generative, ExecutableReturnsRows, ClauseElement):
    __visit_name__: str
    named_with_column: bool
    table: _DMLTableElement
    is_dml: bool
    def params(self, *arg: Any, **kw: Any) -> NoReturn: ...
    def with_dialect_options(self, **opt: Any) -> Self: ...
    def return_defaults(self, *cols: _DMLColumnArgument, supplemental_cols: Optional[Iterable[_DMLColumnArgument]] = ..., sort_by_parameter_order: bool = ...) -> Self: ...
    def returning(self, *cols: _ColumnsClauseArgument[Any], sort_by_parameter_order: bool = ..., **__kw: Any) -> UpdateBase: ...
    def corresponding_column(self, column: KeyedColumnElement[Any], require_embedded: bool = ...) -> Optional[ColumnElement[Any]]: ...
    def exported_columns(self) -> ReadOnlyColumnCollection[Optional[str], ColumnElement[Any]]: ...
    def with_hint(self, text: str, selectable: Optional[_DMLTableArgument] = ..., dialect_name: str = ...) -> Self: ...
    @property
    def entity_description(self) -> Dict[str, Any]: ...
    @property
    def returning_column_descriptions(self) -> List[Dict[str, Any]]: ...

class ValuesBase(UpdateBase):
    __visit_name__: str
    select: Optional[Select[Any]]
    table: Incomplete
    def __init__(self, table: _DMLTableArgument) -> None: ...
    def values(self, *args: Union[_DMLColumnKeyMapping[Any], Sequence[Any]], **kwargs: Any) -> Self: ...

class Insert(ValuesBase):
    __visit_name__: str
    select: Incomplete
    include_insert_from_select_defaults: bool
    is_insert: bool
    table: TableClause
    def __init__(self, table: _DMLTableArgument) -> None: ...
    def inline(self) -> Self: ...
    def from_select(self, names: Sequence[_DMLColumnArgument], select: Selectable, include_defaults: bool = ...) -> Self: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], *, sort_by_parameter_order: bool = ...) -> ReturningInsert[Tuple[_T0]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], *, sort_by_parameter_order: bool = ...) -> ReturningInsert[Tuple[_T0, _T1]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], *, sort_by_parameter_order: bool = ...) -> ReturningInsert[Tuple[_T0, _T1, _T2]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], *, sort_by_parameter_order: bool = ...) -> ReturningInsert[Tuple[_T0, _T1, _T2, _T3]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], *, sort_by_parameter_order: bool = ...) -> ReturningInsert[Tuple[_T0, _T1, _T2, _T3, _T4]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5], *, sort_by_parameter_order: bool = ...) -> ReturningInsert[Tuple[_T0, _T1, _T2, _T3, _T4, _T5]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5], __ent6: _TCCA[_T6], *, sort_by_parameter_order: bool = ...) -> ReturningInsert[Tuple[_T0, _T1, _T2, _T3, _T4, _T5, _T6]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5], __ent6: _TCCA[_T6], __ent7: _TCCA[_T7], *, sort_by_parameter_order: bool = ...) -> ReturningInsert[Tuple[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7]]: ...
    @overload
    def returning(self, *cols: _ColumnsClauseArgument[Any], sort_by_parameter_order: bool = ..., **__kw: Any) -> ReturningInsert[Any]: ...

class ReturningInsert(Insert, TypedReturnsRows[_TP]): ...

class DMLWhereBase:
    table: _DMLTableElement
    def where(self, *whereclause: _ColumnExpressionArgument[bool]) -> Self: ...
    def filter(self, *criteria: roles.ExpressionElementRole[Any]) -> Self: ...
    def filter_by(self, **kwargs: Any) -> Self: ...
    @property
    def whereclause(self) -> Optional[ColumnElement[Any]]: ...

class Update(DMLWhereBase, ValuesBase):
    __visit_name__: str
    is_update: bool
    def __init__(self, table: _DMLTableArgument) -> None: ...
    def ordered_values(self, *args: Tuple[_DMLColumnArgument, Any]) -> Self: ...
    def inline(self) -> Self: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0]) -> ReturningUpdate[Tuple[_T0]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1]) -> ReturningUpdate[Tuple[_T0, _T1]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2]) -> ReturningUpdate[Tuple[_T0, _T1, _T2]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3]) -> ReturningUpdate[Tuple[_T0, _T1, _T2, _T3]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4]) -> ReturningUpdate[Tuple[_T0, _T1, _T2, _T3, _T4]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5]) -> ReturningUpdate[Tuple[_T0, _T1, _T2, _T3, _T4, _T5]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5], __ent6: _TCCA[_T6]) -> ReturningUpdate[Tuple[_T0, _T1, _T2, _T3, _T4, _T5, _T6]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5], __ent6: _TCCA[_T6], __ent7: _TCCA[_T7]) -> ReturningUpdate[Tuple[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7]]: ...
    @overload
    def returning(self, *cols: _ColumnsClauseArgument[Any], **__kw: Any) -> ReturningUpdate[Any]: ...

class ReturningUpdate(Update, TypedReturnsRows[_TP]): ...

class Delete(DMLWhereBase, UpdateBase):
    __visit_name__: str
    is_delete: bool
    table: Incomplete
    def __init__(self, table: _DMLTableArgument) -> None: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0]) -> ReturningDelete[Tuple[_T0]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1]) -> ReturningDelete[Tuple[_T0, _T1]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2]) -> ReturningDelete[Tuple[_T0, _T1, _T2]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3]) -> ReturningDelete[Tuple[_T0, _T1, _T2, _T3]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4]) -> ReturningDelete[Tuple[_T0, _T1, _T2, _T3, _T4]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5]) -> ReturningDelete[Tuple[_T0, _T1, _T2, _T3, _T4, _T5]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5], __ent6: _TCCA[_T6]) -> ReturningDelete[Tuple[_T0, _T1, _T2, _T3, _T4, _T5, _T6]]: ...
    @overload
    def returning(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5], __ent6: _TCCA[_T6], __ent7: _TCCA[_T7]) -> ReturningDelete[Tuple[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7]]: ...
    @overload
    def returning(self, *cols: _ColumnsClauseArgument[Any], **__kw: Any) -> ReturningDelete[Any]: ...

class ReturningDelete(Update, TypedReturnsRows[_TP]): ...
