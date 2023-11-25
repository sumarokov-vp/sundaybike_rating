from . import AttributeEventToken as AttributeEventToken, Mapper as Mapper, base as base
from .. import util as util
from ..sql import coercions as coercions, expression as expression, roles as roles
from ..sql.elements import ColumnElement as ColumnElement
from ..util.typing import Literal as Literal
from .collections import CollectionAdapter as CollectionAdapter, collection as collection, collection_adapter as collection_adapter
from _typeshed import Incomplete
from typing import Any, Callable, Dict, Generic, Optional, Sequence, Tuple, Type, Union

class _PlainColumnGetter(Generic[_KT]):
    cols: Incomplete
    composite: Incomplete
    def __init__(self, cols: Sequence[ColumnElement[_KT]]) -> None: ...
    def __reduce__(self) -> Tuple[Type[_SerializableColumnGetterV2[_KT]], Tuple[Sequence[Tuple[Optional[str], Optional[str]]]]]: ...
    def __call__(self, value: _KT) -> Union[_KT, Tuple[_KT, ...]]: ...

class _SerializableColumnGetterV2(_PlainColumnGetter[_KT]):
    colkeys: Incomplete
    composite: Incomplete
    def __init__(self, colkeys: Sequence[Tuple[Optional[str], Optional[str]]]) -> None: ...
    def __reduce__(self) -> Tuple[Type[_SerializableColumnGetterV2[_KT]], Tuple[Sequence[Tuple[Optional[str], Optional[str]]]]]: ...

def column_keyed_dict(mapping_spec: Union[Type[_KT], Callable[[_KT], _VT]], *, ignore_unpopulated_attribute: bool = ...) -> Type[KeyFuncDict[_KT, _KT]]: ...

class _AttrGetter:
    attr_name: Incomplete
    getter: Incomplete
    def __init__(self, attr_name: str) -> None: ...
    def __call__(self, mapped_object: Any) -> Any: ...
    def __reduce__(self) -> Tuple[Type[_AttrGetter], Tuple[str]]: ...

def attribute_keyed_dict(attr_name: str, *, ignore_unpopulated_attribute: bool = ...) -> Type[KeyFuncDict[_KT, _KT]]: ...
def keyfunc_mapping(keyfunc: _F, *, ignore_unpopulated_attribute: bool = ...) -> Type[KeyFuncDict[_KT, Any]]: ...

class KeyFuncDict(Dict[_KT, _VT]):
    keyfunc: Incomplete
    ignore_unpopulated_attribute: Incomplete
    def __init__(self, keyfunc: _F, *dict_args: Any, ignore_unpopulated_attribute: bool = ...) -> None: ...
    def __reduce__(self) -> Tuple[Callable[[_KT, _KT], KeyFuncDict[_KT, _KT]], Tuple[Any, Union[Dict[_KT, _KT], Dict[_KT, _KT]], CollectionAdapter]]: ...
    def set(self, value: _KT, _sa_initiator: Union[AttributeEventToken, Literal[None, False]] = ...) -> None: ...
    def remove(self, value: _KT, _sa_initiator: Union[AttributeEventToken, Literal[None, False]] = ...) -> None: ...
MappedCollection = KeyFuncDict
mapped_collection = keyfunc_mapping
attribute_mapped_collection = attribute_keyed_dict
column_mapped_collection = column_keyed_dict
