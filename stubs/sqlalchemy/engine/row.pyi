import typing
from ..util import deprecated as deprecated
from ..util._has_cy import HAS_CYEXTENSION as HAS_CYEXTENSION
from ._py_row import BaseRow as BaseRow
from .result import RMKeyView as RMKeyView, _KeyType
from _typeshed import Incomplete
from abc import ABC
from typing import Any, Generic, Iterator, Mapping, NoReturn, Sequence, overload

class Row(BaseRow, Sequence[Any], Generic[_TP]):
    def __setattr__(self, name: str, value: Any) -> NoReturn: ...
    def __delattr__(self, name: str) -> NoReturn: ...
    def tuple(self) -> _TP: ...
    @property
    def t(self) -> _TP: ...
    def __contains__(self, key: Any) -> bool: ...
    __hash__: Incomplete
    @overload
    def __getitem__(self, index: int) -> Any: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[Any]: ...
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
BaseRowProxy = BaseRow
RowProxy = Row

class ROMappingView(ABC):
    def __init__(self, mapping: Mapping['_KeyType', Any], items: Sequence[Any]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __contains__(self, item: Any) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class ROMappingKeysValuesView(ROMappingView, typing.KeysView['_KeyType'], typing.ValuesView[Any]): ...
class ROMappingItemsView(ROMappingView, typing.ItemsView['_KeyType', Any]): ...

class RowMapping(BaseRow, typing.Mapping['_KeyType', Any]):
    def __getitem__(self, key: _KeyType) -> Any: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __contains__(self, key: object) -> bool: ...
    def items(self) -> ROMappingItemsView: ...
    def keys(self) -> RMKeyView: ...
    def values(self) -> ROMappingKeysValuesView: ...