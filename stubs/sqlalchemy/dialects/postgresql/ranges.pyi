import dataclasses
from ... import types as sqltypes
from ...sql import operators as operators
from ...sql.elements import ColumnElement as ColumnElement
from ...sql.type_api import TypeEngine as TypeEngine, TypeEngineMixin as TypeEngineMixin, _TE
from ...util import py310 as py310
from ...util.typing import Literal as Literal
from .operators import ADJACENT_TO as ADJACENT_TO, CONTAINED_BY as CONTAINED_BY, CONTAINS as CONTAINS, NOT_EXTEND_LEFT_OF as NOT_EXTEND_LEFT_OF, NOT_EXTEND_RIGHT_OF as NOT_EXTEND_RIGHT_OF, OVERLAP as OVERLAP, STRICTLY_LEFT_OF as STRICTLY_LEFT_OF, STRICTLY_RIGHT_OF as STRICTLY_RIGHT_OF
from _typeshed import Incomplete
from datetime import date, datetime
from decimal import Decimal
from typing import Any, Generic, Optional, Type, Union, overload

dc_slots: Incomplete
dc_kwonly: Incomplete

@dataclasses.dataclass(frozen=True, **dc_slots)
class Range(Generic[_T]):
    lower: Optional[_T] = ...
    upper: Optional[_T] = ...
    bounds: _BoundsType = ...
    empty: bool = ...
    def __init__(self, lower: Optional[_T] = ..., upper: Optional[_T] = ..., *, bounds: _BoundsType = ..., empty: bool = ...) -> None: ...
    def __bool__(self) -> bool: ...
    @property
    def isempty(self) -> bool: ...
    @property
    def is_empty(self) -> bool: ...
    @property
    def lower_inc(self) -> bool: ...
    @property
    def lower_inf(self) -> bool: ...
    @property
    def upper_inc(self) -> bool: ...
    @property
    def upper_inf(self) -> bool: ...
    @property
    def __sa_type_engine__(self) -> AbstractRange[Range[_T]]: ...
    def __eq__(self, other: Any) -> bool: ...
    def contained_by(self, other: Range[_T]) -> bool: ...
    def contains(self, value: Union[_T, Range[_T]]) -> bool: ...
    def overlaps(self, other: Range[_T]) -> bool: ...
    def strictly_left_of(self, other: Range[_T]) -> bool: ...
    __lshift__ = strictly_left_of
    def strictly_right_of(self, other: Range[_T]) -> bool: ...
    __rshift__ = strictly_right_of
    def not_extend_left_of(self, other: Range[_T]) -> bool: ...
    def not_extend_right_of(self, other: Range[_T]) -> bool: ...
    def adjacent_to(self, other: Range[_T]) -> bool: ...
    def union(self, other: Range[_T]) -> Range[_T]: ...
    def __add__(self, other: Range[_T]) -> Range[_T]: ...
    def difference(self, other: Range[_T]) -> Range[_T]: ...
    def __sub__(self, other: Range[_T]) -> Range[_T]: ...
    def intersection(self, other: Range[_T]) -> Range[_T]: ...
    def __mul__(self, other: Range[_T]) -> Range[_T]: ...

class AbstractRange(sqltypes.TypeEngine[Range[_T]]):
    render_bind_cast: bool
    __abstract__: bool
    @overload
    def adapt(self, cls: Type[_TE], **kw: Any) -> _TE: ...
    @overload
    def adapt(self, cls: Type[TypeEngineMixin], **kw: Any) -> TypeEngine[Any]: ...
    class comparator_factory(TypeEngine.Comparator[Range[Any]]):
        def contains(self, other: Any, **kw: Any) -> ColumnElement[bool]: ...
        def contained_by(self, other: Any) -> ColumnElement[bool]: ...
        def overlaps(self, other: Any) -> ColumnElement[bool]: ...
        def strictly_left_of(self, other: Any) -> ColumnElement[bool]: ...
        __lshift__ = strictly_left_of
        def strictly_right_of(self, other: Any) -> ColumnElement[bool]: ...
        __rshift__ = strictly_right_of
        def not_extend_right_of(self, other: Any) -> ColumnElement[bool]: ...
        def not_extend_left_of(self, other: Any) -> ColumnElement[bool]: ...
        def adjacent_to(self, other: Any) -> ColumnElement[bool]: ...
        def union(self, other: Any) -> ColumnElement[bool]: ...
        def difference(self, other: Any) -> ColumnElement[bool]: ...
        def intersection(self, other: Any) -> ColumnElement[Range[_T]]: ...

class AbstractRangeImpl(AbstractRange[Range[_T]]): ...

class AbstractMultiRange(AbstractRange[Range[_T]]):
    __abstract__: bool

class AbstractMultiRangeImpl(AbstractRangeImpl[Range[_T]], AbstractMultiRange[Range[_T]]): ...

class INT4RANGE(AbstractRange[Range[int]]):
    __visit_name__: str

class INT8RANGE(AbstractRange[Range[int]]):
    __visit_name__: str

class NUMRANGE(AbstractRange[Range[Decimal]]):
    __visit_name__: str

class DATERANGE(AbstractRange[Range[date]]):
    __visit_name__: str

class TSRANGE(AbstractRange[Range[datetime]]):
    __visit_name__: str

class TSTZRANGE(AbstractRange[Range[datetime]]):
    __visit_name__: str

class INT4MULTIRANGE(AbstractMultiRange[Range[int]]):
    __visit_name__: str

class INT8MULTIRANGE(AbstractMultiRange[Range[int]]):
    __visit_name__: str

class NUMMULTIRANGE(AbstractMultiRange[Range[Decimal]]):
    __visit_name__: str

class DATEMULTIRANGE(AbstractMultiRange[Range[date]]):
    __visit_name__: str

class TSMULTIRANGE(AbstractMultiRange[Range[datetime]]):
    __visit_name__: str

class TSTZMULTIRANGE(AbstractMultiRange[Range[datetime]]):
    __visit_name__: str