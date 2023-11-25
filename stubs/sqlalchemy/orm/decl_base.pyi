from . import attributes as attributes, clsregistry as clsregistry, instrumentation as instrumentation, mapperlib as mapperlib
from .. import event as event, exc as exc, util as util
from ..sql import expression as expression
from ..sql.base import _NoArg
from ..sql.elements import NamedColumn as NamedColumn
from ..sql.schema import Column as Column, MetaData as MetaData, Table as Table
from ..sql.selectable import FromClause as FromClause
from ..util import topological as topological
from ..util.typing import Protocol as Protocol, TypedDict as TypedDict, _AnnotationScanType, is_fwd_ref as is_fwd_ref, is_literal as is_literal, typing_get_args as typing_get_args
from ._typing import _ClassDict, _O, _RegistryType, attr_is_internal_proxy as attr_is_internal_proxy
from .attributes import InstrumentedAttribute as InstrumentedAttribute, QueryableAttribute as QueryableAttribute
from .base import InspectionAttr as InspectionAttr, Mapped as Mapped
from .decl_api import declared_attr as declared_attr
from .descriptor_props import CompositeProperty as CompositeProperty, SynonymProperty as SynonymProperty
from .instrumentation import ClassManager as ClassManager
from .interfaces import MapperProperty as MapperProperty
from .mapper import Mapper as Mapper
from .properties import ColumnProperty as ColumnProperty, MappedColumn as MappedColumn
from .util import class_mapper as class_mapper, de_stringify_annotation as de_stringify_annotation
from _typeshed import Incomplete
from typing import Any, Callable, Dict, List, Mapping, NamedTuple, NoReturn, Optional, Sequence, Type, Union

class MappedClassProtocol(Protocol[_O]):
    __mapper__: Mapper[_O]
    __table__: FromClause
    def __call__(self, **kw: Any) -> _O: ...

class _DeclMappedClassProtocol(MappedClassProtocol[_O], Protocol):
    metadata: MetaData
    __tablename__: str
    __mapper_args__: _MapperKwArgs
    __table_args__: Optional[_TableArgsType]
    def __declare_first__(self) -> None: ...
    def __declare_last__(self) -> None: ...

class _DataclassArguments(TypedDict):
    init: Union[_NoArg, bool]
    repr: Union[_NoArg, bool]
    eq: Union[_NoArg, bool]
    order: Union[_NoArg, bool]
    unsafe_hash: Union[_NoArg, bool]
    match_args: Union[_NoArg, bool]
    kw_only: Union[_NoArg, bool]
    dataclass_callable: Union[_NoArg, Callable[..., Type[Any]]]

class _MapperConfig:
    cls: Type[Any]
    classname: str
    properties: util.OrderedDict[str, Union[Sequence[NamedColumn[Any]], NamedColumn[Any], MapperProperty[Any]]]
    declared_attr_reg: Dict[declared_attr[Any], Any]
    @classmethod
    def setup_mapping(cls, registry: _RegistryType, cls_: Type[_O], dict_: _ClassDict, table: Optional[FromClause], mapper_kw: _MapperKwArgs) -> Optional[_MapperConfig]: ...
    def __init__(self, registry: _RegistryType, cls_: Type[Any], mapper_kw: _MapperKwArgs) -> None: ...
    def set_cls_attribute(self, attrname: str, value: _T) -> _T: ...
    def map(self, mapper_kw: _MapperKwArgs = ...) -> Mapper[Any]: ...

class _ImperativeMapperConfig(_MapperConfig):
    local_table: Incomplete
    def __init__(self, registry: _RegistryType, cls_: Type[_O], table: Optional[FromClause], mapper_kw: _MapperKwArgs) -> None: ...
    def map(self, mapper_kw: _MapperKwArgs = ...) -> Mapper[Any]: ...

class _CollectedAnnotation(NamedTuple):
    raw_annotation: _AnnotationScanType
    mapped_container: Optional[Type[Mapped[Any]]]
    extracted_mapped_annotation: Union[Type[Any], str]
    is_dataclass: bool
    attr_value: Any
    originating_module: str
    originating_class: Type[Any]

class _ClassScanMapperConfig(_MapperConfig):
    is_deferred: bool
    registry: _RegistryType
    clsdict_view: _ClassDict
    collected_annotations: Dict[str, _CollectedAnnotation]
    collected_attributes: Dict[str, Any]
    local_table: Optional[FromClause]
    persist_selectable: Optional[FromClause]
    declared_columns: util.OrderedSet[Column[Any]]
    column_ordering: Dict[Column[Any], int]
    column_copies: Dict[Union[MappedColumn[Any], Column[Any]], Union[MappedColumn[Any], Column[Any]]]
    tablename: Optional[str]
    mapper_args: Mapping[str, Any]
    table_args: Optional[_TableArgsType]
    mapper_args_fn: Optional[Callable[[], Dict[str, Any]]]
    inherits: Optional[Type[Any]]
    single: bool
    is_dataclass_prior_to_mapping: bool
    allow_unmapped_annotations: bool
    dataclass_setup_arguments: Optional[_DataclassArguments]
    allow_dataclass_fields: bool
    def __init__(self, registry: _RegistryType, cls_: Type[_O], dict_: _ClassDict, table: Optional[FromClause], mapper_kw: _MapperKwArgs) -> None: ...
    def map(self, mapper_kw: _MapperKwArgs = ...) -> Mapper[Any]: ...

class _DeferredMapperConfig(_ClassScanMapperConfig):
    is_deferred: bool
    @property
    def cls(self) -> Type[Any]: ...
    @cls.setter
    def cls(self, class_: Type[Any]) -> None: ...
    @classmethod
    def has_cls(cls, class_: Type[Any]) -> bool: ...
    @classmethod
    def raise_unmapped_for_cls(cls, class_: Type[Any]) -> NoReturn: ...
    @classmethod
    def config_for_cls(cls, class_: Type[Any]) -> _DeferredMapperConfig: ...
    @classmethod
    def classes_for_base(cls, base_cls: Type[Any], sort: bool = ...) -> List[_DeferredMapperConfig]: ...
    def map(self, mapper_kw: _MapperKwArgs = ...) -> Mapper[Any]: ...
