from .. import exc as exc
from ..sql import sqltypes as sqltypes
from _typeshed import Incomplete

def compiles(class_, *specs): ...
def deregister(class_) -> None: ...

class _dispatcher:
    specs: Incomplete
    def __init__(self) -> None: ...
    def __call__(self, element, compiler, **kw): ...
