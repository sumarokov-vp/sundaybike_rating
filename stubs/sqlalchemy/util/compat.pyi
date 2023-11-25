import dataclasses
import typing
from _typeshed import Incomplete
from typing import Any, AsyncGenerator, Awaitable, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

py312: Incomplete
py311: Incomplete
py310: Incomplete
py39: Incomplete
py38: Incomplete
pypy: Incomplete
cpython: Incomplete
win32: Incomplete
osx: Incomplete
arm: Incomplete
is64bit: Incomplete
has_refcount_gc: Incomplete
dottedgetter: Incomplete

class FullArgSpec(typing.NamedTuple):
    args: List[str]
    varargs: Optional[str]
    varkw: Optional[str]
    defaults: Optional[Tuple[Any, ...]]
    kwonlyargs: List[str]
    kwonlydefaults: Dict[str, Any]
    annotations: Dict[str, Any]

def inspect_getfullargspec(func: Callable[..., Any]) -> FullArgSpec: ...
def athrow(gen: AsyncGenerator[_T_co, Any], typ: Any, value: Any, traceback: Any) -> Awaitable[_T_co]: ...
def md5_not_for_security() -> Any: ...

dict_union: Incomplete
anext_ = anext

def importlib_metadata_get(group): ...
def b(s): ...
def b64decode(x: str) -> bytes: ...
def b64encode(x: bytes) -> str: ...
def decode_backslashreplace(text: bytes, encoding: str) -> str: ...
def cmp(a, b): ...
def inspect_formatargspec(args: List[str], varargs: Optional[str] = ..., varkw: Optional[str] = ..., defaults: Optional[Sequence[Any]] = ..., kwonlyargs: Optional[Sequence[str]] = ..., kwonlydefaults: Optional[Mapping[str, Any]] = ..., annotations: Mapping[str, Any] = ..., formatarg: Callable[[str], str] = ..., formatvarargs: Callable[[str], str] = ..., formatvarkw: Callable[[str], str] = ..., formatvalue: Callable[[Any], str] = ..., formatreturns: Callable[[Any], str] = ..., formatannotation: Callable[[Any], str] = ...) -> str: ...
def dataclass_fields(cls) -> Iterable[dataclasses.Field[Any]]: ...
def local_dataclass_fields(cls) -> Iterable[dataclasses.Field[Any]]: ...
