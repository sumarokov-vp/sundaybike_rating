from .. import exc as exc, inspection as inspection, sql as sql, util as util
from ..sql import operators as operators, schema as sa_schema
from ..sql.elements import TextClause as TextClause
from ..sql.type_api import TypeEngine as TypeEngine
from ..sql.visitors import InternalTraversal as InternalTraversal
from ..util import topological as topological
from ..util.typing import final as final
from .base import Connection as Connection, Engine as Engine
from .interfaces import Dialect as Dialect, ReflectedCheckConstraint as ReflectedCheckConstraint, ReflectedColumn as ReflectedColumn, ReflectedForeignKeyConstraint as ReflectedForeignKeyConstraint, ReflectedIndex as ReflectedIndex, ReflectedPrimaryKeyConstraint as ReflectedPrimaryKeyConstraint, ReflectedTableComment as ReflectedTableComment, ReflectedUniqueConstraint as ReflectedUniqueConstraint, TableKey as TableKey
from _typeshed import Incomplete
from dataclasses import dataclass
from enum import Flag
from typing import Any, Callable, Collection, Dict, List, Optional, Sequence, Set, Tuple, Union

def cache(fn: Callable[..., _R], self: Dialect, con: Connection, *args: Any, **kw: Any) -> _R: ...
def flexi_cache(*traverse_args: Tuple[str, InternalTraversal]) -> Callable[[Callable[..., _R]], Callable[..., _R]]: ...

class ObjectKind(Flag):
    TABLE: Incomplete
    VIEW: Incomplete
    MATERIALIZED_VIEW: Incomplete
    ANY_VIEW: Incomplete
    ANY: Incomplete

class ObjectScope(Flag):
    DEFAULT: Incomplete
    TEMPORARY: Incomplete
    ANY: Incomplete

class Inspector(inspection.Inspectable['Inspector']):
    bind: Union[Engine, Connection]
    engine: Engine
    dialect: Dialect
    info_cache: Dict[Any, Any]
    def __init__(self, bind: Union[Engine, Connection]) -> None: ...
    def clear_cache(self) -> None: ...
    @classmethod
    def from_engine(cls, bind: Engine) -> Inspector: ...
    @property
    def default_schema_name(self) -> Optional[str]: ...
    def get_schema_names(self, **kw: Any) -> List[str]: ...
    def get_table_names(self, schema: Optional[str] = ..., **kw: Any) -> List[str]: ...
    def has_table(self, table_name: str, schema: Optional[str] = ..., **kw: Any) -> bool: ...
    def has_sequence(self, sequence_name: str, schema: Optional[str] = ..., **kw: Any) -> bool: ...
    def has_index(self, table_name: str, index_name: str, schema: Optional[str] = ..., **kw: Any) -> bool: ...
    def has_schema(self, schema_name: str, **kw: Any) -> bool: ...
    def get_sorted_table_and_fkc_names(self, schema: Optional[str] = ..., **kw: Any) -> List[Tuple[Optional[str], List[Tuple[str, Optional[str]]]]]: ...
    def sort_tables_on_foreign_key_dependency(self, consider_schemas: Collection[Optional[str]] = ..., **kw: Any) -> List[Tuple[Optional[Tuple[Optional[str], str]], List[Tuple[Tuple[Optional[str], str], Optional[str]]]]]: ...
    def get_temp_table_names(self, **kw: Any) -> List[str]: ...
    def get_temp_view_names(self, **kw: Any) -> List[str]: ...
    def get_table_options(self, table_name: str, schema: Optional[str] = ..., **kw: Any) -> Dict[str, Any]: ...
    def get_multi_table_options(self, schema: Optional[str] = ..., filter_names: Optional[Sequence[str]] = ..., kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, Dict[str, Any]]: ...
    def get_view_names(self, schema: Optional[str] = ..., **kw: Any) -> List[str]: ...
    def get_materialized_view_names(self, schema: Optional[str] = ..., **kw: Any) -> List[str]: ...
    def get_sequence_names(self, schema: Optional[str] = ..., **kw: Any) -> List[str]: ...
    def get_view_definition(self, view_name: str, schema: Optional[str] = ..., **kw: Any) -> str: ...
    def get_columns(self, table_name: str, schema: Optional[str] = ..., **kw: Any) -> List[ReflectedColumn]: ...
    def get_multi_columns(self, schema: Optional[str] = ..., filter_names: Optional[Sequence[str]] = ..., kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, List[ReflectedColumn]]: ...
    def get_pk_constraint(self, table_name: str, schema: Optional[str] = ..., **kw: Any) -> ReflectedPrimaryKeyConstraint: ...
    def get_multi_pk_constraint(self, schema: Optional[str] = ..., filter_names: Optional[Sequence[str]] = ..., kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, ReflectedPrimaryKeyConstraint]: ...
    def get_foreign_keys(self, table_name: str, schema: Optional[str] = ..., **kw: Any) -> List[ReflectedForeignKeyConstraint]: ...
    def get_multi_foreign_keys(self, schema: Optional[str] = ..., filter_names: Optional[Sequence[str]] = ..., kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, List[ReflectedForeignKeyConstraint]]: ...
    def get_indexes(self, table_name: str, schema: Optional[str] = ..., **kw: Any) -> List[ReflectedIndex]: ...
    def get_multi_indexes(self, schema: Optional[str] = ..., filter_names: Optional[Sequence[str]] = ..., kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, List[ReflectedIndex]]: ...
    def get_unique_constraints(self, table_name: str, schema: Optional[str] = ..., **kw: Any) -> List[ReflectedUniqueConstraint]: ...
    def get_multi_unique_constraints(self, schema: Optional[str] = ..., filter_names: Optional[Sequence[str]] = ..., kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, List[ReflectedUniqueConstraint]]: ...
    def get_table_comment(self, table_name: str, schema: Optional[str] = ..., **kw: Any) -> ReflectedTableComment: ...
    def get_multi_table_comment(self, schema: Optional[str] = ..., filter_names: Optional[Sequence[str]] = ..., kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, ReflectedTableComment]: ...
    def get_check_constraints(self, table_name: str, schema: Optional[str] = ..., **kw: Any) -> List[ReflectedCheckConstraint]: ...
    def get_multi_check_constraints(self, schema: Optional[str] = ..., filter_names: Optional[Sequence[str]] = ..., kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, List[ReflectedCheckConstraint]]: ...
    def reflect_table(self, table: sa_schema.Table, include_columns: Optional[Collection[str]], exclude_columns: Collection[str] = ..., resolve_fks: bool = ..., _extend_on: Optional[Set[sa_schema.Table]] = ..., _reflect_info: Optional[_ReflectionInfo] = ...) -> None: ...

class ReflectionDefaults:
    @classmethod
    def columns(cls) -> List[ReflectedColumn]: ...
    @classmethod
    def pk_constraint(cls) -> ReflectedPrimaryKeyConstraint: ...
    @classmethod
    def foreign_keys(cls) -> List[ReflectedForeignKeyConstraint]: ...
    @classmethod
    def indexes(cls) -> List[ReflectedIndex]: ...
    @classmethod
    def unique_constraints(cls) -> List[ReflectedUniqueConstraint]: ...
    @classmethod
    def check_constraints(cls) -> List[ReflectedCheckConstraint]: ...
    @classmethod
    def table_options(cls) -> Dict[str, Any]: ...
    @classmethod
    def table_comment(cls) -> ReflectedTableComment: ...

@dataclass
class _ReflectionInfo:
    columns: Dict[TableKey, List[ReflectedColumn]]
    pk_constraint: Dict[TableKey, Optional[ReflectedPrimaryKeyConstraint]]
    foreign_keys: Dict[TableKey, List[ReflectedForeignKeyConstraint]]
    indexes: Dict[TableKey, List[ReflectedIndex]]
    unique_constraints: Dict[TableKey, List[ReflectedUniqueConstraint]]
    table_comment: Dict[TableKey, Optional[ReflectedTableComment]]
    check_constraints: Dict[TableKey, List[ReflectedCheckConstraint]]
    table_options: Dict[TableKey, Dict[str, Any]]
    unreflectable: Dict[TableKey, exc.UnreflectableTableError]
    def update(self, other: _ReflectionInfo) -> None: ...
    def __init__(self, columns, pk_constraint, foreign_keys, indexes, unique_constraints, table_comment, check_constraints, table_options, unreflectable) -> None: ...
