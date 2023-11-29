# Standard Library
from typing import (
    Any,
    Mapping,
    Optional,
    Tuple,
)

from . import (  # noqa
    exc as exc,
    mapper as mapperlib,
    strategy_options,
)
from ._orm_constructors import (
    mapped_column as mapped_column,
)
from .attributes import (
    AttributeEvent as AttributeEvent,
    InstrumentedAttribute as InstrumentedAttribute,
    Mapped as Mapped,
    QueryableAttribute as QueryableAttribute,
)
from .context import QueryContext as QueryContext
from .decl_api import (
    DeclarativeBase as DeclarativeBase,
    DeclarativeMeta as DeclarativeMeta,
    as_declarative as as_declarative,
    declarative_base as declarative_base,
    declarative_mixin as declarative_mixin,
    declared_attr as declared_attr,
    has_inherited_table as has_inherited_table,
    registry as registry,
    synonym_for as synonym_for,
)
from .descriptor_props import (
    CompositeProperty as CompositeProperty,
    SynonymProperty as SynonymProperty,
)
from .dynamic import AppenderQuery as AppenderQuery
from .identity import IdentityMap as IdentityMap
from .instrumentation import ClassManager as ClassManager
from .interfaces import (
    EXT_CONTINUE as EXT_CONTINUE,
    EXT_SKIP as EXT_SKIP,
    EXT_STOP as EXT_STOP,
    MANYTOMANY as MANYTOMANY,
    MANYTOONE as MANYTOONE,
    NOT_EXTENSION as NOT_EXTENSION,
    ONETOMANY as ONETOMANY,
    InspectionAttr as InspectionAttr,
    InspectionAttrInfo as InspectionAttrInfo,
    MapperProperty as MapperProperty,
    PropComparator as PropComparator,
)
from .loading import (
    merge_frozen_result as merge_frozen_result,
    merge_result as merge_result,
)
from .mapper import (
    Mapper as Mapper,
    class_mapper as class_mapper,
    configure_mappers as configure_mappers,
    reconstructor as reconstructor,
    validates as validates,
)
from .properties import ColumnProperty as ColumnProperty
from .query import (
    AliasOption as AliasOption,
    FromStatement as FromStatement,
    Query as Query,
)
from .relationships import (
    RelationshipProperty as RelationshipProperty,
    foreign as foreign,
    remote as remote,
)
from .scoping import scoped_session as scoped_session
from .session import (
    ORMExecuteState as ORMExecuteState,
    Session as Session,
    SessionTransaction as SessionTransaction,
    close_all_sessions as close_all_sessions,
    make_transient as make_transient,
    make_transient_to_detached as make_transient_to_detached,
    object_session as object_session,
    sessionmaker as sessionmaker,
)
from .state import (
    AttributeState as AttributeState,
    InstanceState as InstanceState,
)
from .strategy_options import Load as Load
from .unitofwork import UOWTransaction as UOWTransaction
from .util import (
    Bundle as Bundle,
    CascadeOptions as CascadeOptions,
    LoaderCriteriaOption as LoaderCriteriaOption,
    aliased as aliased,
    join as join,
    object_mapper as object_mapper,
    outerjoin as outerjoin,
    polymorphic_union as polymorphic_union,
    was_deleted as was_deleted,
    with_parent as with_parent,
    with_polymorphic as with_polymorphic,
)

def create_session(bind: Optional[Any] = ..., **kwargs: Any) -> Session: ...

with_loader_criteria = LoaderCriteriaOption
relationship = RelationshipProperty

def relation(*arg: Any, **kw: Any) -> RelationshipProperty[Any]: ...
def dynamic_loader(argument: Any, **kw: Any) -> RelationshipProperty[Any]: ...

column_property = ColumnProperty
composite = CompositeProperty

_BackrefResult = Tuple[str, Mapping[str, Any]]

def backref(name: str, **kwargs: Any) -> _BackrefResult: ...
def deferred(*columns: Any, **kw: Any) -> ColumnProperty: ...
def query_expression(default_expr: Any = ...) -> ColumnProperty: ...

mapper = Mapper
synonym = SynonymProperty

def clear_mappers() -> None: ...

joinedload = strategy_options.joinedload._unbound_fn
contains_eager = strategy_options.contains_eager._unbound_fn
defer = strategy_options.defer._unbound_fn
undefer = strategy_options.undefer._unbound_fn
undefer_group = strategy_options.undefer_group._unbound_fn
with_expression = strategy_options.with_expression._unbound_fn
load_only = strategy_options.load_only._unbound_fn
lazyload = strategy_options.lazyload._unbound_fn
subqueryload = strategy_options.subqueryload._unbound_fn
selectinload = strategy_options.selectinload._unbound_fn
immediateload = strategy_options.immediateload._unbound_fn
noload = strategy_options.noload._unbound_fn
raiseload = strategy_options.raiseload._unbound_fn
defaultload = strategy_options.defaultload._unbound_fn
selectin_polymorphic = strategy_options.selectin_polymorphic._unbound_fn

eagerload = joinedload

contains_alias = AliasOption

TypingBackrefResult = _BackrefResult
