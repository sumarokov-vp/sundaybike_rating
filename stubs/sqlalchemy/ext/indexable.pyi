from ..ext.hybrid import hybrid_property
from _typeshed import Incomplete

class index_property(hybrid_property):
    attr_name: Incomplete
    index: Incomplete
    default: Incomplete
    datatype: Incomplete
    onebased: Incomplete
    def __init__(self, attr_name, index, default=..., datatype: Incomplete | None = ..., mutable: bool = ..., onebased: bool = ...) -> None: ...
    def fget(self, instance): ...
    def fset(self, instance, value) -> None: ...
    def fdel(self, instance) -> None: ...
    def expr(self, model): ...
