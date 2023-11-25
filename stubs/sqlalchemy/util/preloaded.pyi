from _typeshed import Incomplete
from typing import Callable

dialects: Incomplete
engine_cursor: Incomplete
engine_default: Incomplete
engine_reflection: Incomplete
engine_result: Incomplete
engine_url: Incomplete
orm_clsregistry: Incomplete
orm_base: Incomplete
orm: Incomplete
orm_attributes: Incomplete
orm_decl_api: Incomplete
orm_decl_base: Incomplete
orm_descriptor_props: Incomplete
orm_dependency: Incomplete
orm_mapper: Incomplete
orm_properties: Incomplete
orm_relationships: Incomplete
orm_session: Incomplete
orm_strategies: Incomplete
orm_strategy_options: Incomplete
orm_state: Incomplete
orm_util: Incomplete
sql_default_comparator: Incomplete
sql_dml: Incomplete
sql_elements: Incomplete
sql_functions: Incomplete
sql_naming: Incomplete
sql_selectable: Incomplete
sql_traversals: Incomplete
sql_schema: Incomplete
sql_sqltypes: Incomplete
sql_util: Incomplete

class _ModuleRegistry:
    module_registry: Incomplete
    prefix: Incomplete
    def __init__(self, prefix: str = ...) -> None: ...
    def preload_module(self, *deps: str) -> Callable[[_FN], _FN]: ...
    def import_prefix(self, path: str) -> None: ...

preload_module: Incomplete
import_prefix: Incomplete
