import dataclasses
from . import attributes as attributes, strategy_options as strategy_options
from .. import Exists as Exists, log as log, schema as schema, sql as sql, util as util
from ..inspection import inspect as inspect
from ..sql import coercions as coercions, expression as expression, operators as operators, roles as roles, visitors as visitors
from ..sql._typing import _ColumnExpressionArgument, _EquivalentColumnMap, _InfoType
from ..sql.annotation import SupportsAnnotations as SupportsAnnotations
from ..sql.elements import BinaryExpression as BinaryExpression, BindParameter as BindParameter, ClauseElement as ClauseElement, ColumnClause as ColumnClause, ColumnElement as ColumnElement
from ..sql.schema import Table as Table
from ..sql.selectable import FromClause as FromClause
from ..sql.util import ClauseAdapter as ClauseAdapter, adapt_criterion_to_null as adapt_criterion_to_null, join_condition as join_condition, selectables_overlap as selectables_overlap, visit_binary_product as visit_binary_product
from ..util.typing import Literal as Literal, RODescriptorReference as RODescriptorReference, _AnnotationScanType, de_optionalize_union_types as de_optionalize_union_types, resolve_name_to_real_class_name as resolve_name_to_real_class_name
from ._typing import _EntityType, _IdentityKeyType, _InstanceDict, _InternalEntityType, _RegistryType, insp_is_aliased_class as insp_is_aliased_class, is_has_collection_adapter as is_has_collection_adapter
from .base import DynamicMapped as DynamicMapped, LoaderCallableStatus as LoaderCallableStatus, Mapped as Mapped, PassiveFlag as PassiveFlag, WriteOnlyMapped as WriteOnlyMapped, _DeclarativeMapped, class_mapper as class_mapper, state_str as state_str
from .decl_base import _ClassScanMapperConfig
from .dependency import DependencyProcessor as DependencyProcessor
from .interfaces import MANYTOMANY as MANYTOMANY, MANYTOONE as MANYTOONE, ONETOMANY as ONETOMANY, PropComparator as PropComparator, RelationshipDirection as RelationshipDirection, StrategizedProperty as StrategizedProperty, _AttributeOptions, _IntrospectsAnnotations
from .mapper import Mapper as Mapper
from .query import Query as Query
from .session import Session as Session
from .state import InstanceState as InstanceState
from .strategies import LazyLoader as LazyLoader
from .util import AliasedClass as AliasedClass, AliasedInsp as AliasedInsp, CascadeOptions as CascadeOptions
from _typeshed import Incomplete
from typing import Any, Callable, Collection, Dict, Generic, Iterator, NamedTuple, NoReturn, Optional, Set, Tuple, Type, Union

ORMBackrefArgument = Union[str, Tuple[str, Dict[str, Any]]]

def remote(expr: _CEA) -> _CEA: ...
def foreign(expr: _CEA) -> _CEA: ...

@dataclasses.dataclass
class _RelationshipArg(Generic[_T1, _T2]):
    name: str
    argument: _T1
    resolved: Optional[_T2]
    def __init__(self, name, argument, resolved) -> None: ...

class _RelationshipArgs(NamedTuple):
    secondary: _RelationshipArg[Optional[_RelationshipSecondaryArgument], Optional[FromClause]]
    primaryjoin: _RelationshipArg[Optional[_RelationshipJoinConditionArgument], Optional[ColumnElement[Any]]]
    secondaryjoin: _RelationshipArg[Optional[_RelationshipJoinConditionArgument], Optional[ColumnElement[Any]]]
    order_by: _RelationshipArg[_ORMOrderByArgument, _RelationshipOrderByArg]
    foreign_keys: _RelationshipArg[Optional[_ORMColCollectionArgument], Set[ColumnElement[Any]]]
    remote_side: _RelationshipArg[Optional[_ORMColCollectionArgument], Set[ColumnElement[Any]]]

class RelationshipProperty(_IntrospectsAnnotations, StrategizedProperty[_T], log.Identified):
    strategy_wildcard_key: Incomplete
    inherit_cache: bool
    primaryjoin: ColumnElement[bool]
    secondaryjoin: Optional[ColumnElement[bool]]
    secondary: Optional[FromClause]
    order_by: _RelationshipOrderByArg
    remote_side: Set[ColumnElement[Any]]
    local_columns: Set[ColumnElement[Any]]
    synchronize_pairs: _ColumnPairs
    secondary_synchronize_pairs: Optional[_ColumnPairs]
    local_remote_pairs: Optional[_ColumnPairs]
    direction: RelationshipDirection
    uselist: Incomplete
    argument: Incomplete
    post_update: Incomplete
    viewonly: Incomplete
    sync_backref: Incomplete
    lazy: Incomplete
    single_parent: Incomplete
    collection_class: Incomplete
    passive_deletes: Incomplete
    passive_updates: Incomplete
    enable_typechecks: Incomplete
    query_class: Incomplete
    innerjoin: Incomplete
    distinct_target_key: Incomplete
    doc: Incomplete
    active_history: Incomplete
    join_depth: Incomplete
    omit_join: Incomplete
    load_on_pending: Incomplete
    comparator_factory: Incomplete
    strategy_key: Incomplete
    back_populates: Incomplete
    backref: Incomplete
    def __init__(self, argument: Optional[_RelationshipArgumentType[_T]] = ..., secondary: Optional[_RelationshipSecondaryArgument] = ..., *, uselist: Optional[bool] = ..., collection_class: Optional[Union[Type[Collection[Any]], Callable[[], Collection[Any]]]] = ..., primaryjoin: Optional[_RelationshipJoinConditionArgument] = ..., secondaryjoin: Optional[_RelationshipJoinConditionArgument] = ..., back_populates: Optional[str] = ..., order_by: _ORMOrderByArgument = ..., backref: Optional[ORMBackrefArgument] = ..., overlaps: Optional[str] = ..., post_update: bool = ..., cascade: str = ..., viewonly: bool = ..., attribute_options: Optional[_AttributeOptions] = ..., lazy: _LazyLoadArgumentType = ..., passive_deletes: Union[Literal['all'], bool] = ..., passive_updates: bool = ..., active_history: bool = ..., enable_typechecks: bool = ..., foreign_keys: Optional[_ORMColCollectionArgument] = ..., remote_side: Optional[_ORMColCollectionArgument] = ..., join_depth: Optional[int] = ..., comparator_factory: Optional[Type[RelationshipProperty.Comparator[Any]]] = ..., single_parent: bool = ..., innerjoin: bool = ..., distinct_target_key: Optional[bool] = ..., load_on_pending: bool = ..., query_class: Optional[Type[Query[Any]]] = ..., info: Optional[_InfoType] = ..., omit_join: Literal[None, False] = ..., sync_backref: Optional[bool] = ..., doc: Optional[str] = ..., bake_queries: Literal[True] = ..., cascade_backrefs: Literal[False] = ..., _local_remote_pairs: Optional[_ColumnPairs] = ..., _legacy_inactive_history_style: bool = ...) -> None: ...
    def instrument_class(self, mapper: Mapper[Any]) -> None: ...
    class Comparator(util.MemoizedSlots, PropComparator[_PT]):
        prop: RODescriptorReference[RelationshipProperty[_PT]]
        def __init__(self, prop: RelationshipProperty[_PT], parentmapper: _InternalEntityType[Any], adapt_to_entity: Optional[AliasedInsp[Any]] = ..., of_type: Optional[_EntityType[_PT]] = ..., extra_criteria: Tuple[ColumnElement[bool], ...] = ...) -> None: ...
        def adapt_to_entity(self, adapt_to_entity: AliasedInsp[Any]) -> RelationshipProperty.Comparator[Any]: ...
        entity: _InternalEntityType[_PT]
        mapper: Mapper[_PT]
        def __clause_element__(self) -> ColumnElement[bool]: ...
        def of_type(self, class_: _EntityType[Any]) -> PropComparator[_PT]: ...
        def and_(self, *criteria: _ColumnExpressionArgument[bool]) -> PropComparator[Any]: ...
        def in_(self, other: Any) -> NoReturn: ...
        __hash__: Incomplete
        def __eq__(self, other: Any) -> ColumnElement[bool]: ...
        def any(self, criterion: Optional[_ColumnExpressionArgument[bool]] = ..., **kwargs: Any) -> ColumnElement[bool]: ...
        def has(self, criterion: Optional[_ColumnExpressionArgument[bool]] = ..., **kwargs: Any) -> ColumnElement[bool]: ...
        def contains(self, other: _ColumnExpressionArgument[Any], **kwargs: Any) -> ColumnElement[bool]: ...
        def __ne__(self, other: Any) -> ColumnElement[bool]: ...
    def merge(self, session: Session, source_state: InstanceState[Any], source_dict: _InstanceDict, dest_state: InstanceState[Any], dest_dict: _InstanceDict, load: bool, _recursive: Dict[Any, object], _resolve_conflict_map: Dict[_IdentityKeyType[Any], object]) -> None: ...
    def cascade_iterator(self, type_: str, state: InstanceState[Any], dict_: _InstanceDict, visited_states: Set[InstanceState[Any]], halt_on: Optional[Callable[[InstanceState[Any]], bool]] = ...) -> Iterator[Tuple[Any, Mapper[Any], InstanceState[Any], _InstanceDict]]: ...
    def entity(self) -> _InternalEntityType[_T]: ...
    def mapper(self) -> Mapper[_T]: ...
    def do_init(self) -> None: ...
    def declarative_scan(self, decl_scan: _ClassScanMapperConfig, registry: _RegistryType, cls: Type[Any], originating_module: Optional[str], key: str, mapped_container: Optional[Type[Mapped[Any]]], annotation: Optional[_AnnotationScanType], extracted_mapped_annotation: Optional[_AnnotationScanType], is_dataclass_field: bool) -> None: ...
    @property
    def cascade(self) -> CascadeOptions: ...
    @cascade.setter
    def cascade(self, cascade: Union[str, CascadeOptions]) -> None: ...

class JoinCondition:
    primaryjoin_initial: Optional[ColumnElement[bool]]
    primaryjoin: ColumnElement[bool]
    secondaryjoin: Optional[ColumnElement[bool]]
    secondary: Optional[FromClause]
    prop: RelationshipProperty[Any]
    synchronize_pairs: _ColumnPairs
    secondary_synchronize_pairs: _ColumnPairs
    direction: RelationshipDirection
    parent_persist_selectable: FromClause
    child_persist_selectable: FromClause
    parent_local_selectable: FromClause
    child_local_selectable: FromClause
    parent_equivalents: Incomplete
    child_equivalents: Incomplete
    consider_as_foreign_keys: Incomplete
    self_referential: Incomplete
    support_sync: Incomplete
    can_be_synced_fn: Incomplete
    def __init__(self, parent_persist_selectable: FromClause, child_persist_selectable: FromClause, parent_local_selectable: FromClause, child_local_selectable: FromClause, *, primaryjoin: Optional[ColumnElement[bool]] = ..., secondary: Optional[FromClause] = ..., secondaryjoin: Optional[ColumnElement[bool]] = ..., parent_equivalents: Optional[_EquivalentColumnMap] = ..., child_equivalents: Optional[_EquivalentColumnMap] = ..., consider_as_foreign_keys: Any = ..., local_remote_pairs: Optional[_ColumnPairs] = ..., remote_side: Any = ..., self_referential: Any = ..., prop: RelationshipProperty[Any], support_sync: bool = ..., can_be_synced_fn: Callable[..., bool] = ...) -> None: ...
    @property
    def primaryjoin_minus_local(self) -> ColumnElement[bool]: ...
    @property
    def secondaryjoin_minus_local(self) -> ColumnElement[bool]: ...
    def primaryjoin_reverse_remote(self) -> ColumnElement[bool]: ...
    def remote_columns(self) -> Set[ColumnElement[Any]]: ...
    def local_columns(self) -> Set[ColumnElement[Any]]: ...
    def foreign_key_columns(self) -> Set[ColumnElement[Any]]: ...
    def join_targets(self, source_selectable: Optional[FromClause], dest_selectable: FromClause, aliased: bool, single_crit: Optional[ColumnElement[bool]] = ..., extra_criteria: Tuple[ColumnElement[bool], ...] = ...) -> Tuple[ColumnElement[bool], Optional[ColumnElement[bool]], Optional[FromClause], Optional[ClauseAdapter], FromClause]: ...
    def create_lazy_clause(self, reverse_direction: bool = ...) -> Tuple[ColumnElement[bool], Dict[str, ColumnElement[Any]], Dict[ColumnElement[Any], ColumnElement[Any]]]: ...

class _ColInAnnotations:
    name: Incomplete
    def __init__(self, name: str) -> None: ...
    def __call__(self, c: ClauseElement) -> bool: ...

class Relationship(RelationshipProperty[_T], _DeclarativeMapped[_T], WriteOnlyMapped[_T], DynamicMapped[_T]):
    inherit_cache: bool
