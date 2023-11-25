from ..util.typing import Literal as Literal
from .cache_key import CacheConst as CacheConst
from typing import Any, Dict, Tuple, Union

class prefix_anon_map(Dict[str, str]):
    def __missing__(self, key: str) -> str: ...

class cache_anon_map(Dict[Union[int, 'Literal[CacheConst.NO_CACHE]'], Union[Literal[True], str]]):
    def get_anon(self, object_: Any) -> Tuple[str, bool]: ...
    def __missing__(self, key: int) -> str: ...
