import dataclasses
from .. import util as util
from ..engine.base import Engine as Engine
from ..orm import backref as backref, interfaces as interfaces, relationship as relationship
from ..orm.base import RelationshipDirection as RelationshipDirection
from ..orm.relationships import ORMBackrefArgument as ORMBackrefArgument, Relationship as Relationship
from ..schema import ForeignKeyConstraint as ForeignKeyConstraint
from ..sql import and_ as and_
from ..sql.schema import Column as Column, MetaData as MetaData, Table as Table
from ..util import Properties as Properties, immutabledict as immutabledict
from ..util.typing import Protocol as Protocol
from _typeshed import Incomplete
from typing import Any, Callable, ClassVar, Dict, Optional, Set, Type, Union, overload

class PythonNameForTableType(Protocol):
    def __call__(self, base: Type[Any], tablename: str, table: Table) -> str: ...

def classname_for_table(base: Type[Any], tablename: str, table: Table) -> str: ...

class NameForScalarRelationshipType(Protocol):
    def __call__(self, base: Type[Any], local_cls: Type[Any], referred_cls: Type[Any], constraint: ForeignKeyConstraint) -> str: ...

def name_for_scalar_relationship(base: Type[Any], local_cls: Type[Any], referred_cls: Type[Any], constraint: ForeignKeyConstraint) -> str: ...

class NameForCollectionRelationshipType(Protocol):
    def __call__(self, base: Type[Any], local_cls: Type[Any], referred_cls: Type[Any], constraint: ForeignKeyConstraint) -> str: ...

def name_for_collection_relationship(base: Type[Any], local_cls: Type[Any], referred_cls: Type[Any], constraint: ForeignKeyConstraint) -> str: ...

class GenerateRelationshipType(Protocol):
    @overload
    def __call__(self, base: Type[Any], direction: RelationshipDirection, return_fn: Callable[..., Relationship[Any]], attrname: str, local_cls: Type[Any], referred_cls: Type[Any], **kw: Any) -> Relationship[Any]: ...
    @overload
    def __call__(self, base: Type[Any], direction: RelationshipDirection, return_fn: Callable[..., ORMBackrefArgument], attrname: str, local_cls: Type[Any], referred_cls: Type[Any], **kw: Any) -> ORMBackrefArgument: ...

@overload
def generate_relationship(base: Type[Any], direction: RelationshipDirection, return_fn: Callable[..., Relationship[Any]], attrname: str, local_cls: Type[Any], referred_cls: Type[Any], **kw: Any) -> Relationship[Any]: ...
@overload
def generate_relationship(base: Type[Any], direction: RelationshipDirection, return_fn: Callable[..., ORMBackrefArgument], attrname: str, local_cls: Type[Any], referred_cls: Type[Any], **kw: Any) -> ORMBackrefArgument: ...

ByModuleProperties: Incomplete

class AutomapBase:
    __abstract__: bool
    classes: ClassVar[Properties[Type[Any]]]
    by_module: ClassVar[ByModuleProperties]
    metadata: ClassVar[MetaData]
    @classmethod
    def prepare(cls, autoload_with: Optional[Engine] = ..., engine: Optional[Any] = ..., reflect: bool = ..., schema: Optional[str] = ..., classname_for_table: Optional[PythonNameForTableType] = ..., modulename_for_table: Optional[PythonNameForTableType] = ..., collection_class: Optional[Any] = ..., name_for_scalar_relationship: Optional[NameForScalarRelationshipType] = ..., name_for_collection_relationship: Optional[NameForCollectionRelationshipType] = ..., generate_relationship: Optional[GenerateRelationshipType] = ..., reflection_options: Union[Dict[_KT, _VT], immutabledict[_KT, _VT]] = ...) -> None: ...

@dataclasses.dataclass
class _Bookkeeping:
    table_keys: Set[str]
    def __init__(self, table_keys) -> None: ...

def automap_base(declarative_base: Optional[Type[Any]] = ..., **kw: Any) -> Any: ...
