from ..engine.base import Connection, Engine, OptionEngine
from ..orm._typing import OrmExecuteOptionsParameter, _O
from ..orm.interfaces import ORMOption
from ..orm.mapper import Mapper
from ..orm.query import Query
from ..orm.session import ORMExecuteState, Session, _BindArguments, _EntityBindKey, _PKIdentityArgument, _SessionBind
from ..orm.state import InstanceState
from ..sql import Executable
from ..sql.elements import ClauseElement
from ..util.typing import Protocol, Self
from _typeshed import Incomplete
from typing import Any, Callable, Dict, Iterable, Optional, Type, Union

ShardIdentifier = str

class ShardChooser(Protocol):
    def __call__(self, mapper: Optional[Mapper[_T]], instance: Any, clause: Optional[ClauseElement]) -> Any: ...

class IdentityChooser(Protocol):
    def __call__(self, mapper: Mapper[_T], primary_key: _PKIdentityArgument, *, lazy_loaded_from: Optional[InstanceState[Any]], execution_options: OrmExecuteOptionsParameter, bind_arguments: _BindArguments, **kw: Any) -> Any: ...

class ShardedQuery(Query[_T]):
    identity_chooser: Incomplete
    execute_chooser: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def set_shard(self, shard_id: ShardIdentifier) -> Self: ...

class ShardedSession(Session):
    shard_chooser: ShardChooser
    identity_chooser: IdentityChooser
    execute_chooser: Callable[[ORMExecuteState], Iterable[Any]]
    def __init__(self, shard_chooser: ShardChooser, identity_chooser: Optional[IdentityChooser] = ..., execute_chooser: Optional[Callable[[ORMExecuteState], Iterable[Any]]] = ..., shards: Optional[Dict[str, Any]] = ..., query_cls: Type[Query[_T]] = ..., *, id_chooser: Optional[Callable[[Query[_T], Iterable[_T]], Iterable[Any]]] = ..., query_chooser: Optional[Callable[[Executable], Iterable[Any]]] = ..., **kwargs: Any) -> None: ...
    def connection_callable(self, mapper: Optional[Mapper[_T]] = ..., instance: Optional[Any] = ..., shard_id: Optional[ShardIdentifier] = ..., **kw: Any) -> Connection: ...
    def get_bind(self, mapper: Optional[_EntityBindKey[_O]] = ..., *, shard_id: Optional[ShardIdentifier] = ..., instance: Optional[Any] = ..., clause: Optional[ClauseElement] = ..., **kw: Any) -> _SessionBind: ...
    def bind_shard(self, shard_id: ShardIdentifier, bind: Union[Engine, OptionEngine]) -> None: ...

class set_shard_id(ORMOption):
    shard_id: Incomplete
    propagate_to_loaders: Incomplete
    def __init__(self, shard_id: ShardIdentifier, propagate_to_loaders: bool = ...) -> None: ...
