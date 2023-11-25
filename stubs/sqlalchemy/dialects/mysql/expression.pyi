from ... import exc as exc, util as util
from ...sql import coercions as coercions, elements as elements, operators as operators, roles as roles
from ...sql.base import Generative as Generative
from ...util.typing import Self as Self
from _typeshed import Incomplete

class match(Generative, elements.BinaryExpression):
    __visit_name__: str
    inherit_cache: bool
    def __init__(self, *cols, **kw) -> None: ...
    modifiers: Incomplete
    def in_boolean_mode(self) -> Self: ...
    def in_natural_language_mode(self) -> Self: ...
    def with_query_expansion(self) -> Self: ...
