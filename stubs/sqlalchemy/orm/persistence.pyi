from . import attributes as attributes, loading as loading, sync as sync
from .. import future as future, sql as sql, util as util
from ..sql import operators as operators
from ..sql.elements import BooleanClauseList as BooleanClauseList
from ..sql.selectable import LABEL_STYLE_TABLENAME_PLUS_COL as LABEL_STYLE_TABLENAME_PLUS_COL
from .base import state_str as state_str

def save_obj(base_mapper, states, uowtransaction, single: bool = ...) -> None: ...
def post_update(base_mapper, states, uowtransaction, post_update_cols) -> None: ...
def delete_obj(base_mapper, states, uowtransaction) -> None: ...
