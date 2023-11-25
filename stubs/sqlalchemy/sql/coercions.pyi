from . import elements as elements, lambdas as lambdas, operators as operators, roles as roles, schema as schema, selectable as selectable, visitors as visitors
from .. import exc as exc, inspection as inspection, util as util
from ..util.typing import Literal as Literal
from ._typing import _ColumnExpressionArgument, _ColumnsClauseArgument, _DDLColumnArgument, _DMLTableArgument, _FromClauseArgument, is_from_clause as is_from_clause
from .base import ExecutableOption as ExecutableOption, Options as Options
from .cache_key import HasCacheKey as HasCacheKey
from .dml import _DMLTableElement
from .elements import BindParameter as BindParameter, ClauseElement as ClauseElement, ColumnClause as ColumnClause, ColumnElement as ColumnElement, DQLDMLClauseElement as DQLDMLClauseElement, NamedColumn as NamedColumn, SQLCoreOperations as SQLCoreOperations
from .schema import Column as Column
from .selectable import FromClause as FromClause, HasCTE as HasCTE, SelectBase as SelectBase, Subquery as Subquery, _ColumnsClauseElement, _JoinTargetProtocol
from .visitors import Visitable as Visitable
from _typeshed import Incomplete
from typing import Any, Iterable, Iterator, Optional, Tuple, Type, Union, overload

@overload
def expect(role: Type[roles.TruncatedLabelRole], element: Any, **kw: Any) -> str: ...
@overload
def expect(role: Type[roles.DMLColumnRole], element: Any, *, as_key: Literal[True] = ..., **kw: Any) -> str: ...
@overload
def expect(role: Type[roles.LiteralValueRole], element: Any, **kw: Any) -> BindParameter[Any]: ...
@overload
def expect(role: Type[roles.DDLReferredColumnRole], element: Any, **kw: Any) -> Column[Any]: ...
@overload
def expect(role: Type[roles.DDLConstraintColumnRole], element: Any, **kw: Any) -> Union[Column[Any], str]: ...
@overload
def expect(role: Type[roles.StatementOptionRole], element: Any, **kw: Any) -> DQLDMLClauseElement: ...
@overload
def expect(role: Type[roles.LabeledColumnExprRole[Any]], element: _ColumnExpressionArgument[_T], **kw: Any) -> NamedColumn[_T]: ...
@overload
def expect(role: Union[Type[roles.ExpressionElementRole[Any]], Type[roles.LimitOffsetRole], Type[roles.WhereHavingRole]], element: _ColumnExpressionArgument[_T], **kw: Any) -> ColumnElement[_T]: ...
@overload
def expect(role: Union[Type[roles.ExpressionElementRole[Any]], Type[roles.LimitOffsetRole], Type[roles.WhereHavingRole], Type[roles.OnClauseRole], Type[roles.ColumnArgumentRole]], element: Any, **kw: Any) -> ColumnElement[Any]: ...
@overload
def expect(role: Type[roles.DMLTableRole], element: _DMLTableArgument, **kw: Any) -> _DMLTableElement: ...
@overload
def expect(role: Type[roles.HasCTERole], element: HasCTE, **kw: Any) -> HasCTE: ...
@overload
def expect(role: Type[roles.SelectStatementRole], element: SelectBase, **kw: Any) -> SelectBase: ...
@overload
def expect(role: Type[roles.FromClauseRole], element: _FromClauseArgument, **kw: Any) -> FromClause: ...
@overload
def expect(role: Type[roles.FromClauseRole], element: SelectBase, *, explicit_subquery: Literal[True] = ..., **kw: Any) -> Subquery: ...
@overload
def expect(role: Type[roles.ColumnsClauseRole], element: _ColumnsClauseArgument[Any], **kw: Any) -> _ColumnsClauseElement: ...
@overload
def expect(role: Type[roles.JoinTargetRole], element: _JoinTargetProtocol, **kw: Any) -> _JoinTargetProtocol: ...
@overload
def expect(role: Type[_SR], element: Any, **kw: Any) -> Any: ...
def expect_as_key(role: Type[roles.DMLColumnRole], element: Any, **kw: Any) -> str: ...
def expect_col_expression_collection(role: Type[roles.DDLConstraintColumnRole], expressions: Iterable[_DDLColumnArgument]) -> Iterator[Tuple[Union[str, Column[Any]], Optional[ColumnClause[Any]], Optional[str], Optional[Union[Column[Any], str]]]]: ...

class RoleImpl:
    name: Incomplete
    def __init__(self, role_class) -> None: ...

class _Deannotate: ...
class _StringOnly: ...
class _ReturnsStringKey(RoleImpl): ...
class _ColumnCoercions(RoleImpl): ...
class _NoTextCoercion(RoleImpl): ...
class _CoerceLiterals(RoleImpl): ...
class LiteralValueImpl(RoleImpl): ...
class _SelectIsNotFrom(RoleImpl): ...
class HasCacheKeyImpl(RoleImpl): ...
class ExecutableOptionImpl(RoleImpl): ...
class ExpressionElementImpl(_ColumnCoercions, RoleImpl): ...
class BinaryElementImpl(ExpressionElementImpl, RoleImpl): ...
class InElementImpl(RoleImpl): ...
class OnClauseImpl(_ColumnCoercions, RoleImpl): ...
class WhereHavingImpl(_CoerceLiterals, _ColumnCoercions, RoleImpl): ...
class StatementOptionImpl(_CoerceLiterals, RoleImpl): ...
class ColumnArgumentImpl(_NoTextCoercion, RoleImpl): ...
class ColumnArgumentOrKeyImpl(_ReturnsStringKey, RoleImpl): ...
class StrAsPlainColumnImpl(_CoerceLiterals, RoleImpl): ...
class ByOfImpl(_CoerceLiterals, _ColumnCoercions, RoleImpl, roles.ByOfRole): ...
class OrderByImpl(ByOfImpl, RoleImpl): ...
class GroupByImpl(ByOfImpl, RoleImpl): ...
class DMLColumnImpl(_ReturnsStringKey, RoleImpl): ...
class ConstExprImpl(RoleImpl): ...
class TruncatedLabelImpl(_StringOnly, RoleImpl): ...
class DDLExpressionImpl(_Deannotate, _CoerceLiterals, RoleImpl): ...
class DDLConstraintColumnImpl(_Deannotate, _ReturnsStringKey, RoleImpl): ...
class DDLReferredColumnImpl(DDLConstraintColumnImpl): ...
class LimitOffsetImpl(RoleImpl): ...
class LabeledColumnExprImpl(ExpressionElementImpl): ...
class ColumnsClauseImpl(_SelectIsNotFrom, _CoerceLiterals, RoleImpl): ...
class ReturnsRowsImpl(RoleImpl): ...
class StatementImpl(_CoerceLiterals, RoleImpl): ...
class SelectStatementImpl(_NoTextCoercion, RoleImpl): ...
class HasCTEImpl(ReturnsRowsImpl): ...
class IsCTEImpl(RoleImpl): ...
class JoinTargetImpl(RoleImpl): ...
class FromClauseImpl(_SelectIsNotFrom, _NoTextCoercion, RoleImpl): ...
class StrictFromClauseImpl(FromClauseImpl): ...
class AnonymizedFromClauseImpl(StrictFromClauseImpl): ...
class DMLTableImpl(_SelectIsNotFrom, _NoTextCoercion, RoleImpl): ...
class DMLSelectImpl(_NoTextCoercion, RoleImpl): ...
class CompoundElementImpl(_NoTextCoercion, RoleImpl): ...

cls: Incomplete
name: Incomplete
impl: Incomplete
