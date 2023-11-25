from ._typing import _DMLTableArgument
from .dml import Delete as Delete, Insert as Insert, Update as Update

def insert(table: _DMLTableArgument) -> Insert: ...
def update(table: _DMLTableArgument) -> Update: ...
def delete(table: _DMLTableArgument) -> Delete: ...
