import abc
from ... import util as util
from ...util.typing import Literal as Literal, Self as Self
from typing import Any, AsyncGenerator, AsyncIterator, Awaitable, Callable, Dict, Generator, Generic, Optional, Tuple

class ReversibleProxy(Generic[_PT]): ...

class StartableContext(Awaitable[_T_co], abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def start(self, is_ctxmanager: bool = ...) -> _T_co: ...
    def __await__(self) -> Generator[Any, Any, _T_co]: ...
    async def __aenter__(self) -> _T_co: ...
    @abc.abstractmethod
    async def __aexit__(self, type_: Any, value: Any, traceback: Any) -> Optional[bool]: ...

class GeneratorStartableContext(StartableContext[_T_co]):
    gen: AsyncGenerator[_T_co, Any]
    def __init__(self, func: Callable[..., AsyncIterator[_T_co]], args: Tuple[Any, ...], kwds: Dict[str, Any]) -> None: ...
    async def start(self, is_ctxmanager: bool = ...) -> _T_co: ...
    async def __aexit__(self, typ: Any, value: Any, traceback: Any) -> Optional[bool]: ...

def asyncstartablecontext(func: Callable[..., AsyncIterator[_T_co]]) -> Callable[..., GeneratorStartableContext[_T_co]]: ...

class ProxyComparable(ReversibleProxy[_PT]):
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...