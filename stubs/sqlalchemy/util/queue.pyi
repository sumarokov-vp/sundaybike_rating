from _typeshed import Incomplete
from typing import Any, Awaitable, Deque, Generic, Optional

class Empty(Exception): ...
class Full(Exception): ...

class QueueCommon(Generic[_T]):
    maxsize: int
    use_lifo: bool
    def __init__(self, maxsize: int = ..., use_lifo: bool = ...) -> None: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    def qsize(self) -> int: ...
    def put_nowait(self, item: _T) -> None: ...
    def put(self, item: _T, block: bool = ..., timeout: Optional[float] = ...) -> None: ...
    def get_nowait(self) -> _T: ...
    def get(self, block: bool = ..., timeout: Optional[float] = ...) -> _T: ...

class Queue(QueueCommon[_T]):
    queue: Deque[_T]
    mutex: Incomplete
    not_empty: Incomplete
    not_full: Incomplete
    use_lifo: Incomplete
    def __init__(self, maxsize: int = ..., use_lifo: bool = ...) -> None: ...
    def qsize(self) -> int: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    def put(self, item: _T, block: bool = ..., timeout: Optional[float] = ...) -> None: ...
    def put_nowait(self, item: _T) -> None: ...
    def get(self, block: bool = ..., timeout: Optional[float] = ...) -> _T: ...
    def get_nowait(self) -> _T: ...

class AsyncAdaptedQueue(QueueCommon[_T]):
    @staticmethod
    def await_(coroutine: Awaitable[Any]) -> _T: ...
    use_lifo: Incomplete
    maxsize: Incomplete
    def __init__(self, maxsize: int = ..., use_lifo: bool = ...) -> None: ...
    def empty(self) -> bool: ...
    def full(self): ...
    def qsize(self): ...
    def put_nowait(self, item: _T) -> None: ...
    def put(self, item: _T, block: bool = ..., timeout: Optional[float] = ...) -> None: ...
    def get_nowait(self) -> _T: ...
    def get(self, block: bool = ..., timeout: Optional[float] = ...) -> _T: ...

class FallbackAsyncAdaptedQueue(AsyncAdaptedQueue[_T]): ...
