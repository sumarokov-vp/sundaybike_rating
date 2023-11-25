from .. import util
from ..util.typing import Literal, Protocol
from ._py_util import cache_anon_map as anon_map
from enum import Enum
from typing import Any, Callable, Dict, Iterable, Iterator, List, Mapping, Optional, Tuple, Type, overload

class _CompilerDispatchType(Protocol):
    def __call__(_self, self: Visitable, visitor: Any, **kw: Any) -> Any: ...

class Visitable:
    __visit_name__: str
    def __init_subclass__(cls) -> None: ...
    def __class_getitem__(cls, key: Any) -> Any: ...

class InternalTraversal(Enum):
    dp_has_cache_key: str
    dp_has_cache_key_list: str
    dp_clauseelement: str
    dp_fromclause_canonical_column_collection: str
    dp_clauseelement_tuples: str
    dp_clauseelement_list: str
    dp_clauseelement_tuple: str
    dp_executable_options: str
    dp_with_context_options: str
    dp_fromclause_ordered_set: str
    dp_string: str
    dp_string_list: str
    dp_anon_name: str
    dp_boolean: str
    dp_operator: str
    dp_type: str
    dp_plain_dict: str
    dp_dialect_options: str
    dp_string_clauseelement_dict: str
    dp_string_multi_dict: str
    dp_annotations_key: str
    dp_plain_obj: str
    dp_named_ddl_element: str
    dp_prefix_sequence: str
    dp_table_hint_list: str
    dp_setup_join_tuple: str
    dp_memoized_select_entities: str
    dp_statement_hint_list: str
    dp_unknown_structure: str
    dp_dml_ordered_values: str
    dp_dml_values: str
    dp_dml_multi_values: str
    dp_propagate_attrs: str
    dp_ignore: str
    dp_inspectable: str
    dp_multi: str
    dp_multi_list: str
    dp_has_cache_key_tuples: str
    dp_inspectable_list: str

class HasTraverseInternals:
    def get_children(self, *, omit_attrs: Tuple[str, ...] = ..., **kw: Any) -> Iterable[HasTraverseInternals]: ...

class _InternalTraversalDispatchType(Protocol):
    def __call__(s, self: object, visitor: HasTraversalDispatch) -> Any: ...

class HasTraversalDispatch:
    def dispatch(self, visit_symbol: InternalTraversal) -> Callable[..., Any]: ...
    def run_generated_dispatch(self, target: object, internal_dispatch: _TraverseInternalsType, generate_dispatcher_name: str) -> Any: ...
    def generate_dispatch(self, target_cls: Type[object], internal_dispatch: _TraverseInternalsType, generate_dispatcher_name: str) -> _InternalTraversalDispatchType: ...
ExtendedInternalTraversal = InternalTraversal

class ExternallyTraversible(HasTraverseInternals, Visitable):
    def get_children(self, *, omit_attrs: Tuple[str, ...] = ..., **kw: Any) -> Iterable[ExternallyTraversible]: ...

class _CloneCallableType(Protocol):
    def __call__(self, element: _ET, **kw: Any) -> _ET: ...

class _TraverseTransformCallableType(Protocol[_ET]):
    def __call__(self, element: _ET, **kw: Any) -> Optional[_ET]: ...

class ExternalTraversal(util.MemoizedSlots):
    __traverse_options__: Dict[str, Any]
    def traverse_single(self, obj: Visitable, **kw: Any) -> Any: ...
    def iterate(self, obj: Optional[ExternallyTraversible]) -> Iterator[ExternallyTraversible]: ...
    @overload
    def traverse(self, obj: Literal[None]) -> None: ...
    @overload
    def traverse(self, obj: ExternallyTraversible) -> ExternallyTraversible: ...
    @property
    def visitor_iterator(self) -> Iterator[ExternalTraversal]: ...
    def chain(self, visitor: ExternalTraversal) -> _ExtT: ...

class CloningExternalTraversal(ExternalTraversal):
    def copy_and_process(self, list_: List[ExternallyTraversible]) -> List[ExternallyTraversible]: ...
    @overload
    def traverse(self, obj: Literal[None]) -> None: ...
    @overload
    def traverse(self, obj: ExternallyTraversible) -> ExternallyTraversible: ...

class ReplacingExternalTraversal(CloningExternalTraversal):
    def replace(self, elem: ExternallyTraversible) -> Optional[ExternallyTraversible]: ...
    @overload
    def traverse(self, obj: Literal[None]) -> None: ...
    @overload
    def traverse(self, obj: ExternallyTraversible) -> ExternallyTraversible: ...
Traversible = Visitable
ClauseVisitor = ExternalTraversal
CloningVisitor = CloningExternalTraversal
ReplacingCloningVisitor = ReplacingExternalTraversal

def iterate(obj: Optional[ExternallyTraversible], opts: Mapping[str, Any] = ...) -> Iterator[ExternallyTraversible]: ...
@overload
def traverse_using(iterator: Iterable[ExternallyTraversible], obj: Literal[None], visitors: Mapping[str, _TraverseCallableType[Any]]) -> None: ...
@overload
def traverse_using(iterator: Iterable[ExternallyTraversible], obj: ExternallyTraversible, visitors: Mapping[str, _TraverseCallableType[Any]]) -> ExternallyTraversible: ...
@overload
def traverse(obj: Literal[None], opts: Mapping[str, Any], visitors: Mapping[str, _TraverseCallableType[Any]]) -> None: ...
@overload
def traverse(obj: ExternallyTraversible, opts: Mapping[str, Any], visitors: Mapping[str, _TraverseCallableType[Any]]) -> ExternallyTraversible: ...
@overload
def cloned_traverse(obj: Literal[None], opts: Mapping[str, Any], visitors: Mapping[str, _TraverseCallableType[Any]]) -> None: ...
@overload
def cloned_traverse(obj: _ET, opts: Mapping[str, Any], visitors: Mapping[str, _TraverseCallableType[Any]]) -> _ET: ...
@overload
def replacement_traverse(obj: Literal[None], opts: Mapping[str, Any], replace: _TraverseTransformCallableType[Any]) -> None: ...
@overload
def replacement_traverse(obj: _CE, opts: Mapping[str, Any], replace: _TraverseTransformCallableType[Any]) -> _CE: ...
@overload
def replacement_traverse(obj: ExternallyTraversible, opts: Mapping[str, Any], replace: _TraverseTransformCallableType[Any]) -> ExternallyTraversible: ...
