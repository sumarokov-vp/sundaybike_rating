import datetime
import decimal
from . import annotation as annotation, coercions as coercions, operators as operators, roles as roles, schema as schema, sqltypes as sqltypes, type_api as type_api
from .. import util as util
from ..engine.base import Connection as Connection
from ..engine.cursor import CursorResult as CursorResult
from ..engine.interfaces import CoreExecuteOptionsParameter as CoreExecuteOptionsParameter
from ._typing import _TypeEngineArgument, is_table_value_type as is_table_value_type
from .base import ColumnCollection as ColumnCollection, Executable as Executable, Generative as Generative, HasMemoized as HasMemoized
from .elements import BinaryExpression as BinaryExpression, BindParameter as BindParameter, Cast as Cast, ClauseList as ClauseList, ColumnElement as ColumnElement, Extract as Extract, FunctionFilter as FunctionFilter, Grouping as Grouping, NamedColumn as NamedColumn, Over as Over, WithinGroup as WithinGroup, literal_column as literal_column
from .selectable import FromClause as FromClause, Select as Select, TableValuedAlias as TableValuedAlias
from .sqltypes import TableValueType as TableValueType
from .type_api import TypeEngine as TypeEngine
from .visitors import InternalTraversal as InternalTraversal
from _typeshed import Incomplete
from typing import Any, Optional, Tuple, Type, overload

def register_function(identifier, fn, package: str = ...) -> None: ...

class FunctionElement(Executable, ColumnElement[_T], FromClause, Generative):
    packagenames: Tuple[str, ...]
    primary_key: Any
    clause_expr: Grouping[Any]
    def __init__(self, *clauses: Any) -> None: ...
    def scalar_table_valued(self, name, type_: Incomplete | None = ...): ...
    def table_valued(self, *expr, **kw): ...
    def column_valued(self, name: Incomplete | None = ..., joins_implicitly: bool = ...): ...
    def columns(self): ...
    def c(self): ...
    @property
    def exported_columns(self): ...
    def clauses(self) -> ClauseList: ...
    def over(self, partition_by: Incomplete | None = ..., order_by: Incomplete | None = ..., rows: Incomplete | None = ..., range_: Incomplete | None = ...): ...
    def within_group(self, *order_by): ...
    def filter(self, *criterion): ...
    def as_comparison(self, left_index, right_index): ...
    def within_group_type(self, within_group) -> None: ...
    def alias(self, name: Incomplete | None = ..., joins_implicitly: bool = ...): ...
    def select(self) -> Select[Any]: ...
    def self_group(self, against: Incomplete | None = ...): ...
    @property
    def entity_namespace(self): ...

class FunctionAsBinary(BinaryExpression[Any]):
    sql_function: FunctionElement[Any]
    left_index: int
    right_index: int
    operator: Incomplete
    type: Incomplete
    negate: Incomplete
    modifiers: Incomplete
    def __init__(self, fn: FunctionElement[Any], left_index: int, right_index: int) -> None: ...
    @property
    def left_expr(self) -> ColumnElement[Any]: ...
    @left_expr.setter
    def left_expr(self, value: ColumnElement[Any]) -> None: ...
    @property
    def right_expr(self) -> ColumnElement[Any]: ...
    @right_expr.setter
    def right_expr(self, value: ColumnElement[Any]) -> None: ...

class ScalarFunctionColumn(NamedColumn[_T]):
    __visit_name__: str
    is_literal: bool
    table: Incomplete
    fn: Incomplete
    name: Incomplete
    type: Incomplete
    def __init__(self, fn: FunctionElement[_T], name: str, type_: Optional[_TypeEngineArgument[_T]] = ...) -> None: ...

class _FunctionGenerator:
    opts: Incomplete
    def __init__(self, **opts) -> None: ...
    def __getattr__(self, name: str) -> _FunctionGenerator: ...
    @overload
    def __call__(self, *c: Any, type_: _TypeEngineArgument[_T], **kwargs: Any) -> Function[_T]: ...
    @overload
    def __call__(self, *c: Any, **kwargs: Any) -> Function[Any]: ...
    @property
    def aggregate_strings(self) -> Type[aggregate_strings]: ...
    @property
    def ansifunction(self) -> Type[AnsiFunction[Any]]: ...
    @property
    def array_agg(self) -> Type[array_agg[Any]]: ...
    @property
    def cast(self) -> Type[Cast[Any]]: ...
    @property
    def char_length(self) -> Type[char_length]: ...
    @property
    def coalesce(self) -> Type[coalesce[Any]]: ...
    @property
    def concat(self) -> Type[concat]: ...
    @property
    def count(self) -> Type[count]: ...
    @property
    def cube(self) -> Type[cube[Any]]: ...
    @property
    def cume_dist(self) -> Type[cume_dist]: ...
    @property
    def current_date(self) -> Type[current_date]: ...
    @property
    def current_time(self) -> Type[current_time]: ...
    @property
    def current_timestamp(self) -> Type[current_timestamp]: ...
    @property
    def current_user(self) -> Type[current_user]: ...
    @property
    def dense_rank(self) -> Type[dense_rank]: ...
    @property
    def extract(self) -> Type[Extract]: ...
    @property
    def grouping_sets(self) -> Type[grouping_sets[Any]]: ...
    @property
    def localtime(self) -> Type[localtime]: ...
    @property
    def localtimestamp(self) -> Type[localtimestamp]: ...
    @property
    def max(self) -> Type[max[Any]]: ...
    @property
    def min(self) -> Type[min[Any]]: ...
    @property
    def mode(self) -> Type[mode[Any]]: ...
    @property
    def next_value(self) -> Type[next_value]: ...
    @property
    def now(self) -> Type[now]: ...
    @property
    def orderedsetagg(self) -> Type[OrderedSetAgg[Any]]: ...
    @property
    def percent_rank(self) -> Type[percent_rank]: ...
    @property
    def percentile_cont(self) -> Type[percentile_cont[Any]]: ...
    @property
    def percentile_disc(self) -> Type[percentile_disc[Any]]: ...
    @property
    def random(self) -> Type[random]: ...
    @property
    def rank(self) -> Type[rank]: ...
    @property
    def returntypefromargs(self) -> Type[ReturnTypeFromArgs[Any]]: ...
    @property
    def rollup(self) -> Type[rollup[Any]]: ...
    @property
    def session_user(self) -> Type[session_user]: ...
    @property
    def sum(self) -> Type[sum[Any]]: ...
    @property
    def sysdate(self) -> Type[sysdate]: ...
    @property
    def user(self) -> Type[user]: ...

func: Incomplete
modifier: Incomplete

class Function(FunctionElement[_T]):
    __visit_name__: str
    name: str
    identifier: str
    type: TypeEngine[_T]
    packagenames: Incomplete
    def __init__(self, name: str, *clauses: Any, type_: Optional[_TypeEngineArgument[_T]] = ..., packagenames: Optional[Tuple[str, ...]] = ...) -> None: ...

class GenericFunction(Function[_T]):
    coerce_arguments: bool
    inherit_cache: bool
    name: str
    def __init_subclass__(cls) -> None: ...
    packagenames: Incomplete
    clause_expr: Incomplete
    type: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class next_value(GenericFunction[int]):
    type: Incomplete
    name: str
    sequence: Incomplete
    def __init__(self, seq, **kw) -> None: ...
    def compare(self, other, **kw): ...

class AnsiFunction(GenericFunction[_T]):
    inherit_cache: bool
    def __init__(self, *args, **kwargs) -> None: ...

class ReturnTypeFromArgs(GenericFunction[_T]):
    inherit_cache: bool
    def __init__(self, *args, **kwargs) -> None: ...

class coalesce(ReturnTypeFromArgs[_T]):
    inherit_cache: bool

class max(ReturnTypeFromArgs[_T]):
    inherit_cache: bool

class min(ReturnTypeFromArgs[_T]):
    inherit_cache: bool

class sum(ReturnTypeFromArgs[_T]):
    inherit_cache: bool

class now(GenericFunction[datetime.datetime]):
    type: Incomplete
    inherit_cache: bool

class concat(GenericFunction[str]):
    type: Incomplete
    inherit_cache: bool

class char_length(GenericFunction[int]):
    type: Incomplete
    inherit_cache: bool
    def __init__(self, arg, **kw) -> None: ...

class random(GenericFunction[float]):
    inherit_cache: bool

class count(GenericFunction[int]):
    type: Incomplete
    inherit_cache: bool
    def __init__(self, expression: Incomplete | None = ..., **kwargs) -> None: ...

class current_date(AnsiFunction[datetime.date]):
    type: Incomplete
    inherit_cache: bool

class current_time(AnsiFunction[datetime.time]):
    type: Incomplete
    inherit_cache: bool

class current_timestamp(AnsiFunction[datetime.datetime]):
    type: Incomplete
    inherit_cache: bool

class current_user(AnsiFunction[str]):
    type: Incomplete
    inherit_cache: bool

class localtime(AnsiFunction[datetime.datetime]):
    type: Incomplete
    inherit_cache: bool

class localtimestamp(AnsiFunction[datetime.datetime]):
    type: Incomplete
    inherit_cache: bool

class session_user(AnsiFunction[str]):
    type: Incomplete
    inherit_cache: bool

class sysdate(AnsiFunction[datetime.datetime]):
    type: Incomplete
    inherit_cache: bool

class user(AnsiFunction[str]):
    type: Incomplete
    inherit_cache: bool

class array_agg(GenericFunction[_T]):
    inherit_cache: bool
    def __init__(self, *args, **kwargs) -> None: ...

class OrderedSetAgg(GenericFunction[_T]):
    array_for_multi_clause: bool
    inherit_cache: bool
    def within_group_type(self, within_group): ...

class mode(OrderedSetAgg[_T]):
    inherit_cache: bool

class percentile_cont(OrderedSetAgg[_T]):
    array_for_multi_clause: bool
    inherit_cache: bool

class percentile_disc(OrderedSetAgg[_T]):
    array_for_multi_clause: bool
    inherit_cache: bool

class rank(GenericFunction[int]):
    type: Incomplete
    inherit_cache: bool

class dense_rank(GenericFunction[int]):
    type: Incomplete
    inherit_cache: bool

class percent_rank(GenericFunction[decimal.Decimal]):
    type: sqltypes.Numeric[decimal.Decimal]
    inherit_cache: bool

class cume_dist(GenericFunction[decimal.Decimal]):
    type: sqltypes.Numeric[decimal.Decimal]
    inherit_cache: bool

class cube(GenericFunction[_T]):
    inherit_cache: bool

class rollup(GenericFunction[_T]):
    inherit_cache: bool

class grouping_sets(GenericFunction[_T]):
    inherit_cache: bool

class aggregate_strings(GenericFunction[str]):
    type: Incomplete
    inherit_cache: bool
    def __init__(self, clause, separator) -> None: ...
