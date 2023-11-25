from ... import log as log, util as util
from .enumerated import ENUM as ENUM, SET as SET
from .types import DATETIME as DATETIME, TIME as TIME, TIMESTAMP as TIMESTAMP
from _typeshed import Incomplete

class ReflectedState:
    columns: Incomplete
    table_options: Incomplete
    table_name: Incomplete
    keys: Incomplete
    fk_constraints: Incomplete
    ck_constraints: Incomplete
    def __init__(self) -> None: ...

class MySQLTableDefinitionParser:
    dialect: Incomplete
    preparer: Incomplete
    def __init__(self, dialect, preparer) -> None: ...
    def parse(self, show_create, charset): ...

def cleanup_text(raw_text: str) -> str: ...
