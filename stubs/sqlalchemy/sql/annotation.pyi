from . import operators as operators
from .. import util as util
from ..util.typing import Literal as Literal, Self as Self
from .base import _EntityNamespace
from .cache_key import HasCacheKey as HasCacheKey
from .visitors import ExternallyTraversible as ExternallyTraversible, InternalTraversal as InternalTraversal, anon_map as anon_map
from _typeshed import Incomplete
from typing import Any, Dict, FrozenSet, Tuple, Type

EMPTY_ANNOTATIONS: util.immutabledict[str, Any]

class SupportsAnnotations(ExternallyTraversible):
    proxy_set: util.generic_fn_descriptor[FrozenSet[Any]]

class SupportsWrappingAnnotations(SupportsAnnotations):
    def entity_namespace(self) -> _EntityNamespace: ...

class SupportsCloneAnnotations(SupportsWrappingAnnotations): ...

class Annotated(SupportsAnnotations):
    def __new__(cls, *args: Any) -> Self: ...
    __dict__: Incomplete
    def __init__(self, element: SupportsWrappingAnnotations, values: _AnnotationDict) -> None: ...
    def __reduce__(self) -> Tuple[Type[Annotated], Tuple[Any, ...]]: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def entity_namespace(self) -> _EntityNamespace: ...

annotated_classes: Dict[Type[SupportsWrappingAnnotations], Type[Annotated]]
