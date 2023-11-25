from . import base as base
from .. import event as event, exc as exc, util as util
from ..log import _EchoFlagType
from ..pool import ConnectionPoolEntry as ConnectionPoolEntry, Pool as Pool, _CreatorFnType, _CreatorWRecFnType, _ResetStyleArgType
from ..sql import compiler as compiler
from ..util import immutabledict as immutabledict
from ..util.typing import Literal as Literal
from .base import Engine as Engine
from .interfaces import DBAPIConnection as DBAPIConnection, IsolationLevel as IsolationLevel, _ExecuteOptions, _ParamStyle
from .mock import create_mock_engine as create_mock_engine
from .url import URL as URL
from typing import Any, Callable, Dict, List, Optional, Type, Union, overload

@overload
def create_engine(url: Union[str, URL], *, connect_args: Dict[Any, Any] = ..., convert_unicode: bool = ..., creator: Union[_CreatorFnType, _CreatorWRecFnType] = ..., echo: _EchoFlagType = ..., echo_pool: _EchoFlagType = ..., enable_from_linting: bool = ..., execution_options: _ExecuteOptions = ..., future: Literal[True], hide_parameters: bool = ..., implicit_returning: Literal[True] = ..., insertmanyvalues_page_size: int = ..., isolation_level: IsolationLevel = ..., json_deserializer: Callable[..., Any] = ..., json_serializer: Callable[..., Any] = ..., label_length: Optional[int] = ..., logging_name: str = ..., max_identifier_length: Optional[int] = ..., max_overflow: int = ..., module: Optional[Any] = ..., paramstyle: Optional[_ParamStyle] = ..., pool: Optional[Pool] = ..., poolclass: Optional[Type[Pool]] = ..., pool_logging_name: str = ..., pool_pre_ping: bool = ..., pool_size: int = ..., pool_recycle: int = ..., pool_reset_on_return: Optional[_ResetStyleArgType] = ..., pool_timeout: float = ..., pool_use_lifo: bool = ..., plugins: List[str] = ..., query_cache_size: int = ..., use_insertmanyvalues: bool = ..., **kwargs: Any) -> Engine: ...
@overload
def create_engine(url: Union[str, URL], **kwargs: Any) -> Engine: ...
def engine_from_config(configuration: Dict[str, Any], prefix: str = ..., **kwargs: Any) -> Engine: ...
@overload
def create_pool_from_url(url: Union[str, URL], *, poolclass: Optional[Type[Pool]] = ..., logging_name: str = ..., pre_ping: bool = ..., size: int = ..., recycle: int = ..., reset_on_return: Optional[_ResetStyleArgType] = ..., timeout: float = ..., use_lifo: bool = ..., **kwargs: Any) -> Pool: ...
@overload
def create_pool_from_url(url: Union[str, URL], **kwargs: Any) -> Pool: ...
