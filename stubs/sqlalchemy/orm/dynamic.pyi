from . import QueryableAttribute as QueryableAttribute, attributes as attributes, relationships as relationships
from .. import util as util
from ..engine import result as result
from ..event import _Dispatch
from ..sql.elements import ColumnElement as ColumnElement
from .base import PassiveFlag as PassiveFlag
from .mapper import Mapper as Mapper
from .query import Query as Query
from .relationships import _RelationshipOrderByArg
from .session import Session as Session, object_session as object_session
from .state import InstanceState as InstanceState
from .util import AliasedClass as AliasedClass
from .writeonly import AbstractCollectionWriter as AbstractCollectionWriter, WriteOnlyAttributeImpl as WriteOnlyAttributeImpl, WriteOnlyHistory as WriteOnlyHistory, WriteOnlyLoader as WriteOnlyLoader
from _typeshed import Incomplete
from typing import Any, Iterable, Iterator, List, Optional, Type, Union

class DynamicCollectionHistory(WriteOnlyHistory[_T]):
    unchanged_items: Incomplete
    added_items: Incomplete
    deleted_items: Incomplete
    def __init__(self, attr: DynamicAttributeImpl, state: InstanceState[_T], passive: PassiveFlag, apply_to: Optional[DynamicCollectionHistory[_T]] = ...) -> None: ...

class DynamicAttributeImpl(WriteOnlyAttributeImpl):
    collection_history_cls = DynamicCollectionHistory[Any]
    query_class: Type[AppenderMixin[Any]]
    target_mapper: Incomplete
    order_by: Incomplete
    def __init__(self, class_: Union[Type[Any], AliasedClass[Any]], key: str, dispatch: _Dispatch[QueryableAttribute[Any]], target_mapper: Mapper[_T], order_by: _RelationshipOrderByArg, query_class: Optional[Type[AppenderMixin[_T]]] = ..., **kw: Any) -> None: ...

class DynaLoader(WriteOnlyLoader):
    impl_class = DynamicAttributeImpl

class AppenderMixin(AbstractCollectionWriter[_T]):
    query_class: Optional[Type[Query[_T]]]
    def __init__(self, attr: DynamicAttributeImpl, state: InstanceState[_T]) -> None: ...
    @property
    def session(self) -> Optional[Session]: ...
    sess: Incomplete
    @session.setter
    def session(self, session: Session) -> None: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __getitem__(self, index: Any) -> Union[_T, List[_T]]: ...
    def count(self) -> int: ...
    def add_all(self, iterator: Iterable[_T]) -> None: ...
    def add(self, item: _T) -> None: ...
    def extend(self, iterator: Iterable[_T]) -> None: ...
    def append(self, item: _T) -> None: ...
    def remove(self, item: _T) -> None: ...

class AppenderQuery(AppenderMixin[_T], Query[_T]): ...

def mixin_user_query(cls) -> type[AppenderMixin[Any]]: ...
