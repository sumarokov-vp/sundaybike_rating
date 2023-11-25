from .. import util as util
from ..sql.base import Executable as Executable
from ..sql.ddl import SchemaDropper as SchemaDropper, SchemaGenerator as SchemaGenerator
from ..sql.schema import HasSchemaAttr as HasSchemaAttr, SchemaItem as SchemaItem
from .base import Engine as Engine
from .interfaces import CoreExecuteOptionsParameter as CoreExecuteOptionsParameter, Dialect as Dialect, _CoreAnyExecuteParams
from .url import URL as URL
from typing import Any, Callable, Optional, Union

class MockConnection:
    def __init__(self, dialect: Dialect, execute: Callable[..., Any]) -> None: ...
    engine: Engine
    dialect: Dialect
    name: str
    def connect(self, **kwargs: Any) -> MockConnection: ...
    def schema_for_object(self, obj: HasSchemaAttr) -> Optional[str]: ...
    def execution_options(self, **kw: Any) -> MockConnection: ...
    def execute(self, obj: Executable, parameters: Optional[_CoreAnyExecuteParams] = ..., execution_options: Optional[CoreExecuteOptionsParameter] = ...) -> Any: ...

def create_mock_engine(url: Union[str, URL], executor: Any, **kw: Any) -> MockConnection: ...
