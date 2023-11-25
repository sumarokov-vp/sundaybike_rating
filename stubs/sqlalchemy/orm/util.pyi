import enum
from . import attributes as attributes, exc as exc
from .. import event as event, inspection as inspection, sql as sql, util as util
from ..engine import Row as Row, RowMapping as RowMapping
from ..engine.result import result_tuple as result_tuple
from ..sql import coercions as coercions, expression as expression, lambdas as lambdas, roles as roles, util as sql_util, visitors as visitors
from ..sql._typing import _ColumnExpressionArgument, _EquivalentColumnMap, _FromClauseArgument, _OnClauseArgument, is_selectable as is_selectable
from ..sql.annotation import SupportsCloneAnnotations as SupportsCloneAnnotations
from ..sql.base import ColumnCollection as ColumnCollection, ReadOnlyColumnCollection as ReadOnlyColumnCollection
from ..sql.cache_key import HasCacheKey as HasCacheKey, MemoizedHasCacheKey as MemoizedHasCacheKey
from ..sql.elements import BindParameter as BindParameter, ColumnElement as ColumnElement, KeyedColumnElement as KeyedColumnElement
from ..sql.selectable import FromClause as FromClause, Select as Select, Selectable as Selectable, _ColumnsClauseElement
from ..sql.visitors import anon_map as anon_map
from ..util.langhelpers import MemoizedSlots as MemoizedSlots
from ..util.typing import ArgsTypeProcotol as ArgsTypeProcotol, Literal as Literal, Protocol as Protocol, _AnnotationScanType, is_origin_of_cls as is_origin_of_cls, typing_get_origin as typing_get_origin
from ._typing import _EntityType, _IdentityKeyType, _InternalEntityType, _O, insp_is_aliased_class as insp_is_aliased_class, insp_is_mapper as insp_is_mapper, prop_is_relationship as prop_is_relationship
from .base import DynamicMapped as DynamicMapped, InspectionAttr as InspectionAttr, Mapped as Mapped, ORMDescriptor as ORMDescriptor, WriteOnlyMapped as WriteOnlyMapped, opt_manager_of_class as opt_manager_of_class
from .context import ORMCompileState as ORMCompileState, _MapperEntity
from .interfaces import CriteriaOption as CriteriaOption, ORMColumnsClauseRole as ORMColumnsClauseRole, ORMEntityColumnsClauseRole as ORMEntityColumnsClauseRole, ORMFromClauseRole as ORMFromClauseRole
from .mapper import Mapper as Mapper
from .path_registry import AbstractEntityRegistry as AbstractEntityRegistry
from .query import Query as Query
from .relationships import RelationshipProperty as RelationshipProperty
from _typeshed import Incomplete
from typing import AbstractSet, Any, Callable, Dict, FrozenSet, Generic, Iterable, List, Optional, Sequence, Tuple, Type, Union

all_cascades: Incomplete

class _DeStringifyAnnotation(Protocol):
    def __call__(self, cls: Type[Any], annotation: _AnnotationScanType, originating_module: str, *, str_cleanup_fn: Optional[Callable[[str, str], str]] = ..., include_generic: bool = ...) -> Type[Any]: ...

de_stringify_annotation: Incomplete

class _DeStringifyUnionElements(Protocol):
    def __call__(self, cls: Type[Any], annotation: ArgsTypeProcotol, originating_module: str, *, str_cleanup_fn: Optional[Callable[[str, str], str]] = ...) -> Type[Any]: ...

de_stringify_union_elements: Incomplete

class _EvalNameOnly(Protocol):
    def __call__(self, name: str, module_name: str) -> Any: ...

eval_name_only: Incomplete

class CascadeOptions(FrozenSet[str]):
    save_update: bool
    delete: bool
    refresh_expire: bool
    merge: bool
    expunge: bool
    delete_orphan: bool
    def __new__(cls, value_list: Optional[Union[Iterable[str], str]]) -> CascadeOptions: ...
    @classmethod
    def from_string(cls, arg): ...

def polymorphic_union(table_map, typecolname, aliasname: str = ..., cast_nulls: bool = ...): ...
def identity_key(class_: Optional[Type[_T]] = ..., ident: Union[Any, Tuple[Any, ...]] = ..., *, instance: Optional[_T] = ..., row: Optional[Union[Row[Any], RowMapping]] = ..., identity_token: Optional[Any] = ...) -> _IdentityKeyType[_T]: ...

class _TraceAdaptRole(enum.Enum):
    ALIASED_INSP: Incomplete
    JOINEDLOAD_USER_DEFINED_ALIAS: Incomplete
    JOINEDLOAD_PATH_WITH_POLYMORPHIC: Incomplete
    JOINEDLOAD_MEMOIZED_ADAPTER: Incomplete
    MAPPER_POLYMORPHIC_ADAPTER: Incomplete
    WITH_POLYMORPHIC_ADAPTER: Incomplete
    WITH_POLYMORPHIC_ADAPTER_RIGHT_JOIN: Incomplete
    DEPRECATED_JOIN_ADAPT_RIGHT_SIDE: Incomplete
    ADAPT_FROM_STATEMENT: Incomplete
    COMPOUND_EAGER_STATEMENT: Incomplete
    LEGACY_SELECT_FROM_ALIAS: Incomplete

class ORMStatementAdapter(sql_util.ColumnAdapter):
    role: Incomplete
    def __init__(self, role: _TraceAdaptRole, selectable: Selectable, *, equivalents: Optional[_EquivalentColumnMap] = ..., adapt_required: bool = ..., allow_label_resolve: bool = ..., anonymize_labels: bool = ..., adapt_on_names: bool = ..., adapt_from_selectables: Optional[AbstractSet[FromClause]] = ...) -> None: ...

class ORMAdapter(sql_util.ColumnAdapter):
    is_aliased_class: bool
    aliased_insp: Optional[AliasedInsp[Any]]
    role: Incomplete
    mapper: Incomplete
    def __init__(self, role: _TraceAdaptRole, entity: _InternalEntityType[Any], *, equivalents: Optional[_EquivalentColumnMap] = ..., adapt_required: bool = ..., allow_label_resolve: bool = ..., anonymize_labels: bool = ..., selectable: Optional[Selectable] = ..., limit_on_entity: bool = ..., adapt_on_names: bool = ..., adapt_from_selectables: Optional[AbstractSet[FromClause]] = ...) -> None: ...

class AliasedClass(inspection.Inspectable['AliasedInsp[_O]'], ORMColumnsClauseRole[_O]):
    def __init__(self, mapped_class_or_ac: _EntityType[_O], alias: Optional[FromClause] = ..., name: Optional[str] = ..., flat: bool = ..., adapt_on_names: bool = ..., with_polymorphic_mappers: Optional[Sequence[Mapper[Any]]] = ..., with_polymorphic_discriminator: Optional[ColumnElement[Any]] = ..., base_alias: Optional[AliasedInsp[Any]] = ..., use_mapper_path: bool = ..., represents_outer_join: bool = ...) -> None: ...
    def __getattr__(self, key: str) -> Any: ...

class AliasedInsp(ORMEntityColumnsClauseRole[_O], ORMFromClauseRole, HasCacheKey, InspectionAttr, MemoizedSlots, inspection.Inspectable['AliasedInsp[_O]'], Generic[_O]):
    mapper: Mapper[_O]
    selectable: FromClause
    with_polymorphic_mappers: Sequence[Mapper[Any]]
    name: Incomplete
    polymorphic_on: Incomplete
    represents_outer_join: Incomplete
    def __init__(self, entity: AliasedClass[_O], inspected: _InternalEntityType[_O], selectable: FromClause, name: Optional[str], with_polymorphic_mappers: Optional[Sequence[Mapper[Any]]], polymorphic_on: Optional[ColumnElement[Any]], _base_alias: Optional[AliasedInsp[Any]], _use_mapper_path: bool, adapt_on_names: bool, represents_outer_join: bool, nest_adapters: bool) -> None: ...
    @property
    def entity(self) -> AliasedClass[_O]: ...
    is_aliased_class: bool
    def _memoized_method___clause_element__(self) -> FromClause: ...
    @property
    def entity_namespace(self) -> AliasedClass[_O]: ...
    @property
    def class_(self) -> Type[_O]: ...

class _WrapUserEntity:
    subject: Incomplete
    def __init__(self, subject) -> None: ...
    def __getattribute__(self, name): ...

class LoaderCriteriaOption(CriteriaOption):
    root_entity: Optional[Type[Any]]
    entity: Optional[_InternalEntityType[Any]]
    where_criteria: Union[ColumnElement[bool], lambdas.DeferredLambdaElement]
    deferred_where_criteria: bool
    include_aliases: bool
    propagate_to_loaders: bool
    def __init__(self, entity_or_base: _EntityType[Any], where_criteria: _ColumnExpressionArgument[bool], loader_only: bool = ..., include_aliases: bool = ..., propagate_to_loaders: bool = ..., track_closure_variables: bool = ...) -> None: ...
    def __reduce__(self): ...
    def process_compile_state_replaced_entities(self, compile_state: ORMCompileState, mapper_entities: Iterable[_MapperEntity]) -> None: ...
    def process_compile_state(self, compile_state: ORMCompileState) -> None: ...
    def get_global_criteria(self, attributes: Dict[Any, Any]) -> None: ...

GenericAlias: Incomplete

class Bundle(ORMColumnsClauseRole[_T], SupportsCloneAnnotations, MemoizedHasCacheKey, inspection.Inspectable['Bundle[_T]'], InspectionAttr):
    single_entity: bool
    is_clause_element: bool
    is_mapper: bool
    is_aliased_class: bool
    is_bundle: bool
    proxy_set: Incomplete
    exprs: List[_ColumnsClauseElement]
    name: Incomplete
    c: Incomplete
    def __init__(self, name: str, *exprs: _ColumnExpressionArgument[Any], **kw: Any) -> None: ...
    @property
    def mapper(self) -> Optional[Mapper[Any]]: ...
    @property
    def entity(self) -> Optional[_InternalEntityType[Any]]: ...
    @property
    def entity_namespace(self) -> ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]: ...
    columns: ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]
    def __clause_element__(self): ...
    @property
    def clauses(self): ...
    def label(self, name): ...
    def create_row_processor(self, query: Select[Any], procs: Sequence[Callable[[Row[Any]], Any]], labels: Sequence[str]) -> Callable[[Row[Any]], Any]: ...

class _ORMJoin(expression.Join):
    __visit_name__: Incomplete
    inherit_cache: bool
    onclause: Incomplete
    def __init__(self, left: _FromClauseArgument, right: _FromClauseArgument, onclause: Optional[_OnClauseArgument] = ..., isouter: bool = ..., full: bool = ..., _left_memo: Optional[Any] = ..., _right_memo: Optional[Any] = ..., _extra_criteria: Tuple[ColumnElement[bool], ...] = ...) -> None: ...
    def join(self, right: _FromClauseArgument, onclause: Optional[_OnClauseArgument] = ..., isouter: bool = ..., full: bool = ...) -> _ORMJoin: ...
    def outerjoin(self, right: _FromClauseArgument, onclause: Optional[_OnClauseArgument] = ..., full: bool = ...) -> _ORMJoin: ...

def with_parent(instance: object, prop: attributes.QueryableAttribute[Any], from_entity: Optional[_EntityType[Any]] = ...) -> ColumnElement[bool]: ...
def has_identity(object_: object) -> bool: ...
def was_deleted(object_: object) -> bool: ...

class _CleanupError(Exception): ...
