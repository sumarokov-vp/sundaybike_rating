from . import base as orm_base
from .. import exc as exc, util as util
from ..sql import visitors as visitors
from ..sql.cache_key import HasCacheKey as HasCacheKey
from ..sql.elements import BindParameter as BindParameter
from ..sql.visitors import anon_map as anon_map
from ..util.typing import TypeGuard as TypeGuard
from ._typing import _InternalEntityType, insp_is_mapper_property as insp_is_mapper_property
from .interfaces import MapperProperty as MapperProperty
from .mapper import Mapper as Mapper
from .relationships import RelationshipProperty as RelationshipProperty
from .util import AliasedInsp as AliasedInsp
from _typeshed import Incomplete
from typing import Any, Dict, Iterator, Optional, Tuple, Union, overload

def is_root(path: PathRegistry) -> TypeGuard[RootRegistry]: ...
def is_entity(path: PathRegistry) -> TypeGuard[AbstractEntityRegistry]: ...

log: Incomplete

class PathRegistry(HasCacheKey):
    is_token: bool
    is_root: bool
    has_entity: bool
    is_property: bool
    is_entity: bool
    is_unnatural: bool
    path: _PathRepresentation
    natural_path: _PathRepresentation
    parent: Optional[PathRegistry]
    root: RootRegistry
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def odd_element(self, index: int) -> _InternalEntityType[Any]: ...
    def set(self, attributes: Dict[Any, Any], key: Any, value: Any) -> None: ...
    def setdefault(self, attributes: Dict[Any, Any], key: Any, value: Any) -> None: ...
    def get(self, attributes: Dict[Any, Any], key: Any, value: Optional[Any] = ...) -> Any: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    @overload
    def __getitem__(self, entity: _StrPathToken) -> TokenRegistry: ...
    @overload
    def __getitem__(self, entity: int) -> _PathElementType: ...
    @overload
    def __getitem__(self, entity: slice) -> _PathRepresentation: ...
    @overload
    def __getitem__(self, entity: _InternalEntityType[Any]) -> AbstractEntityRegistry: ...
    @overload
    def __getitem__(self, entity: MapperProperty[Any]) -> PropRegistry: ...
    @property
    def length(self) -> int: ...
    def pairs(self) -> Iterator[Tuple[_InternalEntityType[Any], Union[str, MapperProperty[Any]]]]: ...
    def contains_mapper(self, mapper: Mapper[Any]) -> bool: ...
    def contains(self, attributes: Dict[Any, Any], key: Any) -> bool: ...
    def __reduce__(self) -> Any: ...
    def serialize(self) -> _SerializedPath: ...
    @classmethod
    def deserialize(cls, path: _SerializedPath) -> PathRegistry: ...
    @overload
    @classmethod
    def per_mapper(cls, mapper: Mapper[Any]) -> CachingEntityRegistry: ...
    @overload
    @classmethod
    def per_mapper(cls, mapper: AliasedInsp[Any]) -> SlotsEntityRegistry: ...
    @classmethod
    def coerce(cls, raw: _PathRepresentation) -> PathRegistry: ...
    def __add__(self, other: PathRegistry) -> PathRegistry: ...

class CreatesToken(PathRegistry):
    is_aliased_class: bool
    is_root: bool
    def token(self, token: _StrPathToken) -> TokenRegistry: ...

class RootRegistry(CreatesToken):
    inherit_cache: bool
    path: Incomplete
    natural_path: Incomplete
    has_entity: bool
    is_aliased_class: bool
    is_root: bool
    is_unnatural: bool

class PathToken(orm_base.InspectionAttr, HasCacheKey, str):
    @classmethod
    def intern(cls, strvalue: str) -> PathToken: ...

class TokenRegistry(PathRegistry):
    inherit_cache: bool
    token: _StrPathToken
    parent: CreatesToken
    path: Incomplete
    natural_path: Incomplete
    def __init__(self, parent: CreatesToken, token: _StrPathToken) -> None: ...
    has_entity: bool
    is_token: bool
    def generate_for_superclasses(self) -> Iterator[PathRegistry]: ...

class PropRegistry(PathRegistry):
    inherit_cache: bool
    is_property: bool
    prop: MapperProperty[Any]
    mapper: Optional[Mapper[Any]]
    entity: Optional[_InternalEntityType[Any]]
    is_unnatural: Incomplete
    parent: Incomplete
    path: Incomplete
    natural_path: Incomplete
    has_entity: Incomplete
    def __init__(self, parent: AbstractEntityRegistry, prop: MapperProperty[Any]) -> None: ...
    @property
    def entity_path(self) -> AbstractEntityRegistry: ...

class AbstractEntityRegistry(CreatesToken):
    has_entity: bool
    is_entity: bool
    parent: Union[RootRegistry, PropRegistry]
    key: _InternalEntityType[Any]
    entity: _InternalEntityType[Any]
    is_aliased_class: bool
    path: Incomplete
    natural_path: Incomplete
    def __init__(self, parent: Union[RootRegistry, PropRegistry], entity: _InternalEntityType[Any]) -> None: ...
    @property
    def root_entity(self) -> _InternalEntityType[Any]: ...
    @property
    def entity_path(self) -> PathRegistry: ...
    @property
    def mapper(self) -> Mapper[Any]: ...
    def __bool__(self) -> bool: ...

class SlotsEntityRegistry(AbstractEntityRegistry):
    inherit_cache: bool

class _ERDict(Dict[Any, Any]):
    registry: Incomplete
    def __init__(self, registry: CachingEntityRegistry) -> None: ...
    def __missing__(self, key: Any) -> PropRegistry: ...

class CachingEntityRegistry(AbstractEntityRegistry):
    inherit_cache: bool
    def __init__(self, parent: Union[RootRegistry, PropRegistry], entity: _InternalEntityType[Any]) -> None: ...
    def pop(self, key: Any, default: Any) -> Any: ...

def path_is_entity(path: PathRegistry) -> TypeGuard[AbstractEntityRegistry]: ...
def path_is_property(path: PathRegistry) -> TypeGuard[PropRegistry]: ...
