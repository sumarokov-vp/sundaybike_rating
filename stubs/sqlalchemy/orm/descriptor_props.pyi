from . import attributes as attributes, util as orm_util
from .. import event as event, schema as schema, sql as sql, util as util
from ..engine.base import Connection as Connection
from ..engine.row import Row as Row
from ..sql import expression as expression, operators as operators
from ..sql._typing import _InfoType
from ..sql.elements import BindParameter as BindParameter, ClauseList as ClauseList, ColumnElement as ColumnElement
from ..sql.operators import OperatorType as OperatorType
from ..sql.schema import Column as Column
from ..sql.selectable import Select as Select
from ..util.typing import CallableReference as CallableReference, DescriptorReference as DescriptorReference, RODescriptorReference as RODescriptorReference, _AnnotationScanType, is_fwd_ref as is_fwd_ref, is_pep593 as is_pep593, typing_get_args as typing_get_args
from ._typing import _InstanceDict, _RegistryType
from .attributes import History as History, InstrumentedAttribute as InstrumentedAttribute, QueryableAttribute as QueryableAttribute
from .base import LoaderCallableStatus as LoaderCallableStatus, Mapped as Mapped, PassiveFlag as PassiveFlag, SQLORMOperations as SQLORMOperations, _DeclarativeMapped
from .context import ORMCompileState as ORMCompileState
from .decl_base import _ClassScanMapperConfig
from .interfaces import MapperProperty as MapperProperty, PropComparator as PropComparator, _AttributeOptions, _IntrospectsAnnotations, _MapsColumns
from .mapper import Mapper as Mapper
from .properties import ColumnProperty as ColumnProperty, MappedColumn as MappedColumn
from .state import InstanceState as InstanceState
from .util import de_stringify_annotation as de_stringify_annotation
from _typeshed import Incomplete
from typing import Any, Callable, List, Optional, Sequence, Tuple, Type, Union

class DescriptorProperty(MapperProperty[_T]):
    doc: Optional[str]
    uses_objects: bool
    descriptor: DescriptorReference[Any]
    def get_history(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> History: ...
    key: Incomplete
    def instrument_class(self, mapper: Mapper[Any]) -> None: ...

class CompositeProperty(_MapsColumns[_CC], _IntrospectsAnnotations, DescriptorProperty[_CC]):
    composite_class: Union[Type[_CC], Callable[..., _CC]]
    attrs: Tuple[_CompositeAttrType[Any], ...]
    comparator_factory: Type[Comparator[_CC]]
    active_history: Incomplete
    deferred: Incomplete
    group: Incomplete
    def __init__(self, _class_or_attr: Union[None, Type[_CC], Callable[..., _CC], _CompositeAttrType[Any]] = ..., *attrs: _CompositeAttrType[Any], attribute_options: Optional[_AttributeOptions] = ..., active_history: bool = ..., deferred: bool = ..., group: Optional[str] = ..., comparator_factory: Optional[Type[Comparator[_CC]]] = ..., info: Optional[_InfoType] = ..., **kwargs: Any) -> None: ...
    def instrument_class(self, mapper: Mapper[Any]) -> None: ...
    def do_init(self) -> None: ...
    def declarative_scan(self, decl_scan: _ClassScanMapperConfig, registry: _RegistryType, cls: Type[Any], originating_module: Optional[str], key: str, mapped_container: Optional[Type[Mapped[Any]]], annotation: Optional[_AnnotationScanType], extracted_mapped_annotation: Optional[_AnnotationScanType], is_dataclass_field: bool) -> None: ...
    def props(self) -> Sequence[MapperProperty[Any]]: ...
    def columns(self) -> Sequence[Column[Any]]: ...
    @property
    def mapper_property_to_assign(self) -> Optional[MapperProperty[_CC]]: ...
    @property
    def columns_to_assign(self) -> List[Tuple[schema.Column[Any], int]]: ...
    def get_history(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> History: ...
    class CompositeBundle(orm_util.Bundle[_T]):
        property: Incomplete
        def __init__(self, property_: Composite[_T], expr: ClauseList) -> None: ...
        def create_row_processor(self, query: Select[Any], procs: Sequence[Callable[[Row[Any]], Any]], labels: Sequence[str]) -> Callable[[Row[Any]], Any]: ...
    class Comparator(PropComparator[_PT]):
        __hash__: Incomplete
        prop: RODescriptorReference[Composite[_PT]]
        def clauses(self) -> ClauseList: ...
        def __clause_element__(self) -> CompositeProperty.CompositeBundle[_PT]: ...
        def expression(self) -> CompositeProperty.CompositeBundle[_PT]: ...
        def __eq__(self, other: Any) -> ColumnElement[bool]: ...
        def __ne__(self, other: Any) -> ColumnElement[bool]: ...
        def __lt__(self, other: Any) -> ColumnElement[bool]: ...
        def __gt__(self, other: Any) -> ColumnElement[bool]: ...
        def __le__(self, other: Any) -> ColumnElement[bool]: ...
        def __ge__(self, other: Any) -> ColumnElement[bool]: ...

class Composite(CompositeProperty[_T], _DeclarativeMapped[_T]):
    inherit_cache: bool

class ConcreteInheritedProperty(DescriptorProperty[_T]):
    descriptor: Incomplete
    def __init__(self) -> None: ...

class SynonymProperty(DescriptorProperty[_T]):
    comparator_factory: Optional[Type[PropComparator[_T]]]
    name: Incomplete
    map_column: Incomplete
    descriptor: Incomplete
    doc: Incomplete
    def __init__(self, name: str, map_column: Optional[bool] = ..., descriptor: Optional[Any] = ..., comparator_factory: Optional[Type[PropComparator[_T]]] = ..., attribute_options: Optional[_AttributeOptions] = ..., info: Optional[_InfoType] = ..., doc: Optional[str] = ...) -> None: ...
    def get_history(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> History: ...
    parent: Incomplete
    def set_parent(self, parent: Mapper[Any], init: bool) -> None: ...

class Synonym(SynonymProperty[_T], _DeclarativeMapped[_T]):
    inherit_cache: bool
