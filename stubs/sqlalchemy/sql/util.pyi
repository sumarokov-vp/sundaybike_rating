from . import coercions as coercions, operators as operators, roles as roles, visitors as visitors
from .. import exc as exc, util as util
from ..engine.interfaces import _AnyExecuteParams
from ..engine.row import Row as Row
from ..util.typing import Literal as Literal, Protocol as Protocol
from ._typing import _EquivalentColumnMap, is_text_clause as is_text_clause
from .elements import BinaryExpression as BinaryExpression, BindParameter as BindParameter, ClauseElement as ClauseElement, ColumnClause as ColumnClause, ColumnElement as ColumnElement, Grouping as Grouping, KeyedColumnElement as KeyedColumnElement, Label as Label, NamedColumn as NamedColumn, Null as Null, TextClause as TextClause, UnaryExpression as UnaryExpression
from .schema import Column as Column
from .selectable import Alias as Alias, FromClause as FromClause, FromGrouping as FromGrouping, Join as Join, ScalarSelect as ScalarSelect, SelectBase as SelectBase, Selectable as Selectable, TableClause as TableClause, _JoinTargetElement, _SelectIterable
from .visitors import ExternalTraversal as ExternalTraversal, ExternallyTraversible as ExternallyTraversible, _ET
from _typeshed import Incomplete
from collections.abc import Generator
from typing import AbstractSet, Any, Callable, Collection, Iterable, Iterator, List, Optional, Sequence, Union, overload

def join_condition(a: FromClause, b: FromClause, a_subset: Optional[FromClause] = ..., consider_as_foreign_keys: Optional[AbstractSet[ColumnClause[Any]]] = ...) -> ColumnElement[bool]: ...
def find_join_source(clauses: List[FromClause], join_to: FromClause) -> List[int]: ...
def find_left_clause_that_matches_given(clauses: Sequence[FromClause], join_from: FromClause) -> List[int]: ...
def find_left_clause_to_join_from(clauses: Sequence[FromClause], join_to: _JoinTargetElement, onclause: Optional[ColumnElement[Any]]) -> List[int]: ...
def visit_binary_product(fn: Callable[[BinaryExpression[Any], ColumnElement[Any], ColumnElement[Any]], None], expr: ColumnElement[Any]) -> None: ...
def find_tables(clause: ClauseElement, *, check_columns: bool = ..., include_aliases: bool = ..., include_joins: bool = ..., include_selects: bool = ..., include_crud: bool = ...) -> List[TableClause]: ...
def unwrap_order_by(clause): ...
def unwrap_label_reference(element): ...
def expand_column_list_from_order_by(collist, order_by): ...
def clause_is_present(clause, search): ...
def tables_from_leftmost(clause: FromClause) -> Iterator[FromClause]: ...
def surface_selectables(clause) -> Generator[Incomplete, None, None]: ...
def surface_selectables_only(clause) -> Generator[Incomplete, None, None]: ...
def extract_first_column_annotation(column, annotation_name): ...
def selectables_overlap(left: FromClause, right: FromClause) -> bool: ...
def bind_values(clause): ...

class _repr_base:
    max_chars: int
    def trunc(self, value: Any) -> str: ...

class _repr_row(_repr_base):
    row: Incomplete
    max_chars: Incomplete
    def __init__(self, row: Row[Any], max_chars: int = ...) -> None: ...

class _long_statement(str): ...

class _repr_params(_repr_base):
    params: Incomplete
    ismulti: Incomplete
    batches: Incomplete
    max_chars: Incomplete
    max_params: Incomplete
    def __init__(self, params: Optional[_AnyExecuteParams], batches: int, max_params: int = ..., max_chars: int = ..., ismulti: Optional[bool] = ...) -> None: ...

def adapt_criterion_to_null(crit: _CE, nulls: Collection[Any]) -> _CE: ...
def splice_joins(left: Optional[FromClause], right: Optional[FromClause], stop_on: Optional[FromClause] = ...) -> Optional[FromClause]: ...
@overload
def reduce_columns(columns: Iterable[ColumnElement[Any]], *clauses: Optional[ClauseElement], **kw: bool) -> Sequence[ColumnElement[Any]]: ...
@overload
def reduce_columns(columns: _SelectIterable, *clauses: Optional[ClauseElement], **kw: bool) -> Sequence[Union[ColumnElement[Any], TextClause]]: ...
def criterion_as_pairs(expression, consider_as_foreign_keys: Incomplete | None = ..., consider_as_referenced_keys: Incomplete | None = ..., any_operator: bool = ...): ...

class ClauseAdapter(visitors.ReplacingExternalTraversal):
    __traverse_options__: Incomplete
    selectable: Incomplete
    include_fn: Incomplete
    exclude_fn: Incomplete
    equivalents: Incomplete
    adapt_on_names: Incomplete
    adapt_from_selectables: Incomplete
    def __init__(self, selectable: Selectable, equivalents: Optional[_EquivalentColumnMap] = ..., include_fn: Optional[Callable[[ClauseElement], bool]] = ..., exclude_fn: Optional[Callable[[ClauseElement], bool]] = ..., adapt_on_names: bool = ..., anonymize_labels: bool = ..., adapt_from_selectables: Optional[AbstractSet[FromClause]] = ...) -> None: ...
    @overload
    def traverse(self, obj: Literal[None]) -> None: ...
    @overload
    def traverse(self, obj: _ET) -> _ET: ...
    def replace(self, col: _ET, _include_singleton_constants: bool = ...) -> Optional[_ET]: ...

class _ColumnLookup(Protocol):
    @overload
    def __getitem__(self, key: None) -> None: ...
    @overload
    def __getitem__(self, key: ColumnClause[Any]) -> ColumnClause[Any]: ...
    @overload
    def __getitem__(self, key: ColumnElement[Any]) -> ColumnElement[Any]: ...
    @overload
    def __getitem__(self, key: _ET) -> _ET: ...

class ColumnAdapter(ClauseAdapter):
    columns: _ColumnLookup
    adapt_required: Incomplete
    allow_label_resolve: Incomplete
    def __init__(self, selectable: Selectable, equivalents: Optional[_EquivalentColumnMap] = ..., adapt_required: bool = ..., include_fn: Optional[Callable[[ClauseElement], bool]] = ..., exclude_fn: Optional[Callable[[ClauseElement], bool]] = ..., adapt_on_names: bool = ..., allow_label_resolve: bool = ..., anonymize_labels: bool = ..., adapt_from_selectables: Optional[AbstractSet[FromClause]] = ...) -> None: ...
    class _IncludeExcludeMapping:
        parent: Incomplete
        columns: Incomplete
        def __init__(self, parent, columns) -> None: ...
        def __getitem__(self, key): ...
    def wrap(self, adapter): ...
    @overload
    def traverse(self, obj: Literal[None]) -> None: ...
    @overload
    def traverse(self, obj: _ET) -> _ET: ...
    def chain(self, visitor: ExternalTraversal) -> ColumnAdapter: ...
    @property
    def visitor_iterator(self) -> Iterator[ColumnAdapter]: ...
    adapt_clause = traverse
    adapt_list: Incomplete
    def adapt_check_present(self, col: ColumnElement[Any]) -> Optional[ColumnElement[Any]]: ...
