from .. import ForeignKey, log, util
from ..sql import roles
from ..sql._typing import _InfoType
from ..sql.base import _NoArg
from ..sql.elements import ColumnElement, NamedColumn
from ..sql.operators import OperatorType
from ..sql.schema import Column
from ..util.typing import RODescriptorReference, _AnnotationScanType
from ._typing import _IdentityKeyType, _InstanceDict, _ORMColumnExprArgument, _RegistryType
from .base import Mapped, _DeclarativeMapped
from .decl_base import _ClassScanMapperConfig
from .descriptor_props import CompositeProperty as CompositeProperty, ConcreteInheritedProperty as ConcreteInheritedProperty, SynonymProperty as SynonymProperty
from .interfaces import MapperProperty, PropComparator, StrategizedProperty, _AttributeOptions, _IntrospectsAnnotations, _MapsColumns
from .mapper import Mapper
from .relationships import RelationshipProperty as RelationshipProperty
from .session import Session
from .state import InstanceState
from _typeshed import Incomplete
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple, Type, Union

class ColumnProperty(_MapsColumns[_T], StrategizedProperty[_T], _IntrospectsAnnotations, log.Identified):
    strategy_wildcard_key: Incomplete
    inherit_cache: bool
    columns: List[NamedColumn[Any]]
    comparator_factory: Type[PropComparator[_T]]
    group: Incomplete
    deferred: Incomplete
    raiseload: Incomplete
    instrument: Incomplete
    active_history: Incomplete
    expire_on_flush: Incomplete
    doc: Incomplete
    strategy_key: Incomplete
    def __init__(self, column: _ORMColumnExprArgument[_T], *additional_columns: _ORMColumnExprArgument[Any], attribute_options: Optional[_AttributeOptions] = ..., group: Optional[str] = ..., deferred: bool = ..., raiseload: bool = ..., comparator_factory: Optional[Type[PropComparator[_T]]] = ..., active_history: bool = ..., expire_on_flush: bool = ..., info: Optional[_InfoType] = ..., doc: Optional[str] = ..., _instrument: bool = ..., _assume_readonly_dc_attributes: bool = ...) -> None: ...
    def declarative_scan(self, decl_scan: _ClassScanMapperConfig, registry: _RegistryType, cls: Type[Any], originating_module: Optional[str], key: str, mapped_container: Optional[Type[Mapped[Any]]], annotation: Optional[_AnnotationScanType], extracted_mapped_annotation: Optional[_AnnotationScanType], is_dataclass_field: bool) -> None: ...
    @property
    def mapper_property_to_assign(self) -> Optional[MapperProperty[_T]]: ...
    @property
    def columns_to_assign(self) -> List[Tuple[Column[Any], int]]: ...
    def __clause_element__(self) -> roles.ColumnsClauseRole: ...
    @property
    def expression(self) -> roles.ColumnsClauseRole: ...
    def instrument_class(self, mapper: Mapper[Any]) -> None: ...
    def do_init(self) -> None: ...
    def copy(self) -> ColumnProperty[_T]: ...
    def merge(self, session: Session, source_state: InstanceState[Any], source_dict: _InstanceDict, dest_state: InstanceState[Any], dest_dict: _InstanceDict, load: bool, _recursive: Dict[Any, object], _resolve_conflict_map: Dict[_IdentityKeyType[Any], object]) -> None: ...
    class Comparator(util.MemoizedSlots, PropComparator[_PT]):
        prop: RODescriptorReference[ColumnProperty[_PT]]
        expressions: Sequence[NamedColumn[Any]]
        def __clause_element__(self) -> NamedColumn[_PT]: ...
        def _memoized_method___clause_element__(self) -> NamedColumn[_PT]: ...
        def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
        def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> ColumnElement[Any]: ...

class MappedSQLExpression(ColumnProperty[_T], _DeclarativeMapped[_T]):
    inherit_cache: bool

class MappedColumn(_IntrospectsAnnotations, _MapsColumns[_T], _DeclarativeMapped[_T]):
    deferred: Union[_NoArg, bool]
    deferred_raiseload: bool
    deferred_group: Optional[str]
    column: Column[_T]
    foreign_keys: Optional[Set[ForeignKey]]
    active_history: Incomplete
    def __init__(self, *arg: Any, **kw: Any) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def mapper_property_to_assign(self) -> Optional[MapperProperty[_T]]: ...
    @property
    def columns_to_assign(self) -> List[Tuple[Column[Any], int]]: ...
    def __clause_element__(self) -> Column[_T]: ...
    def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    def found_in_pep593_annotated(self) -> Any: ...
    def declarative_scan(self, decl_scan: _ClassScanMapperConfig, registry: _RegistryType, cls: Type[Any], originating_module: Optional[str], key: str, mapped_container: Optional[Type[Mapped[Any]]], annotation: Optional[_AnnotationScanType], extracted_mapped_annotation: Optional[_AnnotationScanType], is_dataclass_field: bool) -> None: ...
    def declarative_scan_for_composite(self, registry: _RegistryType, cls: Type[Any], originating_module: Optional[str], key: str, param_name: str, param_annotation: _AnnotationScanType) -> None: ...
