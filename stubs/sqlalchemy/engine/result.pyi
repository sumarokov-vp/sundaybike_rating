import typing
from .. import exc as exc, util as util
from ..sql.base import HasMemoized as HasMemoized, InPlaceGenerative as InPlaceGenerative
from ..sql.schema import Column as Column
from ..util import HasMemoized_ro_memoized_attribute as HasMemoized_ro_memoized_attribute, NONE_SET as NONE_SET
from ..util._has_cy import HAS_CYEXTENSION as HAS_CYEXTENSION
from ..util.typing import Literal as Literal, Self as Self
from .row import Row as Row, RowMapping as RowMapping
from _typeshed import Incomplete
from enum import Enum
from typing import Any, Callable, Generic, Iterable, Iterator, Optional, Sequence, overload

class ResultMetaData:
    @property
    def keys(self) -> RMKeyView: ...

class RMKeyView(typing.KeysView[Any]):
    def __init__(self, parent: ResultMetaData) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
    def __contains__(self, item: Any) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class SimpleResultMetaData(ResultMetaData):
    def __init__(self, keys: Sequence[str], extra: Optional[Sequence[Any]] = ..., _processors: Optional[_ProcessorsType] = ..., _tuplefilter: Optional[_TupleGetterType] = ..., _translated_indexes: Optional[Sequence[int]] = ..., _unique_filters: Optional[Sequence[Callable[[Any], Any]]] = ...) -> None: ...

def result_tuple(fields: Sequence[str], extra: Optional[Any] = ...) -> Callable[[Iterable[Any]], Row[Any]]: ...

class _NoRow(Enum): ...
class ResultInternal(InPlaceGenerative, Generic[_R]): ...

class _WithKeys:
    def keys(self) -> RMKeyView: ...

class Result(_WithKeys, ResultInternal[Row[_TP]]):
    def __init__(self, cursor_metadata: ResultMetaData) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    def close(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    def yield_per(self, num: int) -> Self: ...
    def unique(self, strategy: Optional[_UniqueFilterType] = ...) -> Self: ...
    def columns(self, *col_expressions: _KeyIndexType) -> Self: ...
    @overload
    def scalars(self) -> ScalarResult[_T]: ...
    @overload
    def scalars(self, index: Literal[0]) -> ScalarResult[_T]: ...
    @overload
    def scalars(self, index: _KeyIndexType = ...) -> ScalarResult[Any]: ...
    def mappings(self) -> MappingResult: ...
    @property
    def t(self) -> TupleResult[_TP]: ...
    def tuples(self) -> TupleResult[_TP]: ...
    def __iter__(self) -> Iterator[Row[_TP]]: ...
    def __next__(self) -> Row[_TP]: ...
    def partitions(self, size: Optional[int] = ...) -> Iterator[Sequence[Row[_TP]]]: ...
    def fetchall(self) -> Sequence[Row[_TP]]: ...
    def fetchone(self) -> Optional[Row[_TP]]: ...
    def fetchmany(self, size: Optional[int] = ...) -> Sequence[Row[_TP]]: ...
    def all(self) -> Sequence[Row[_TP]]: ...
    def first(self) -> Optional[Row[_TP]]: ...
    def one_or_none(self) -> Optional[Row[_TP]]: ...
    @overload
    def scalar_one(self) -> _T: ...
    @overload
    def scalar_one(self) -> Any: ...
    @overload
    def scalar_one_or_none(self) -> Optional[_T]: ...
    @overload
    def scalar_one_or_none(self) -> Optional[Any]: ...
    def one(self) -> Row[_TP]: ...
    @overload
    def scalar(self) -> Optional[_T]: ...
    @overload
    def scalar(self) -> Any: ...
    def freeze(self) -> FrozenResult[_TP]: ...
    def merge(self, *others: Result[Any]) -> MergedResult[_TP]: ...

class FilterResult(ResultInternal[_R]):
    def __enter__(self) -> Self: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    def yield_per(self, num: int) -> Self: ...
    @property
    def closed(self) -> bool: ...
    def close(self) -> None: ...

class ScalarResult(FilterResult[_R]):
    def __init__(self, real_result: Result[Any], index: _KeyIndexType) -> None: ...
    def unique(self, strategy: Optional[_UniqueFilterType] = ...) -> Self: ...
    def partitions(self, size: Optional[int] = ...) -> Iterator[Sequence[_R]]: ...
    def fetchall(self) -> Sequence[_R]: ...
    def fetchmany(self, size: Optional[int] = ...) -> Sequence[_R]: ...
    def all(self) -> Sequence[_R]: ...
    def __iter__(self) -> Iterator[_R]: ...
    def __next__(self) -> _R: ...
    def first(self) -> Optional[_R]: ...
    def one_or_none(self) -> Optional[_R]: ...
    def one(self) -> _R: ...

class TupleResult(FilterResult[_R], util.TypingOnly):
    def partitions(self, size: Optional[int] = ...) -> Iterator[Sequence[_R]]: ...
    def fetchone(self) -> Optional[_R]: ...
    def fetchall(self) -> Sequence[_R]: ...
    def fetchmany(self, size: Optional[int] = ...) -> Sequence[_R]: ...
    def all(self) -> Sequence[_R]: ...
    def __iter__(self) -> Iterator[_R]: ...
    def __next__(self) -> _R: ...
    def first(self) -> Optional[_R]: ...
    def one_or_none(self) -> Optional[_R]: ...
    def one(self) -> _R: ...
    @overload
    def scalar_one(self) -> _T: ...
    @overload
    def scalar_one(self) -> Any: ...
    @overload
    def scalar_one_or_none(self) -> Optional[_T]: ...
    @overload
    def scalar_one_or_none(self) -> Optional[Any]: ...
    @overload
    def scalar(self) -> Optional[_T]: ...
    @overload
    def scalar(self) -> Any: ...

class MappingResult(_WithKeys, FilterResult[RowMapping]):
    def __init__(self, result: Result[Any]) -> None: ...
    def unique(self, strategy: Optional[_UniqueFilterType] = ...) -> Self: ...
    def columns(self, *col_expressions: _KeyIndexType) -> Self: ...
    def partitions(self, size: Optional[int] = ...) -> Iterator[Sequence[RowMapping]]: ...
    def fetchall(self) -> Sequence[RowMapping]: ...
    def fetchone(self) -> Optional[RowMapping]: ...
    def fetchmany(self, size: Optional[int] = ...) -> Sequence[RowMapping]: ...
    def all(self) -> Sequence[RowMapping]: ...
    def __iter__(self) -> Iterator[RowMapping]: ...
    def __next__(self) -> RowMapping: ...
    def first(self) -> Optional[RowMapping]: ...
    def one_or_none(self) -> Optional[RowMapping]: ...
    def one(self) -> RowMapping: ...

class FrozenResult(Generic[_TP]):
    data: Sequence[Any]
    metadata: Incomplete
    def __init__(self, result: Result[_TP]) -> None: ...
    def rewrite_rows(self) -> Sequence[Sequence[Any]]: ...
    def with_new_rows(self, tuple_data: Sequence[Row[_TP]]) -> FrozenResult[_TP]: ...
    def __call__(self) -> Result[_TP]: ...

class IteratorResult(Result[_TP]):
    iterator: Incomplete
    raw: Incomplete
    def __init__(self, cursor_metadata: ResultMetaData, iterator: Iterator[_InterimSupportsScalarsRowType], raw: Optional[Result[Any]] = ..., _source_supports_scalars: bool = ...) -> None: ...
    @property
    def closed(self) -> bool: ...

def null_result() -> IteratorResult[Any]: ...

class ChunkedIteratorResult(IteratorResult[_TP]):
    chunks: Incomplete
    raw: Incomplete
    iterator: Incomplete
    dynamic_yield_per: Incomplete
    def __init__(self, cursor_metadata: ResultMetaData, chunks: Callable[[Optional[int]], Iterator[Sequence[_InterimRowType[_R]]]], source_supports_scalars: bool = ..., raw: Optional[Result[Any]] = ..., dynamic_yield_per: bool = ...) -> None: ...
    def yield_per(self, num: int) -> Self: ...

class MergedResult(IteratorResult[_TP]):
    closed: bool
    rowcount: Optional[int]
    def __init__(self, cursor_metadata: ResultMetaData, results: Sequence[Result[_TP]]) -> None: ...
