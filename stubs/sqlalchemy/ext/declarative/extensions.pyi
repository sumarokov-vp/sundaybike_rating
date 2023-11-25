from ...engine import Connection as Connection, Engine as Engine
from ...orm import relationships as relationships
from ...orm.util import polymorphic_union as polymorphic_union
from ...schema import Table as Table
from ...sql.schema import MetaData as MetaData
from ...util import OrderedDict as OrderedDict
from typing import Any, Union

class ConcreteBase:
    @classmethod
    def __declare_first__(cls) -> None: ...

class AbstractConcreteBase(ConcreteBase):
    __no_table__: bool
    @classmethod
    def __declare_first__(cls) -> None: ...

class DeferredReflection:
    @classmethod
    def prepare(cls, bind: Union[Engine, Connection], **reflect_kw: Any) -> None: ...
