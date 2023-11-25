from .. import util as util
from ..util.typing import Literal as Literal
from enum import Enum
from typing import Callable, Tuple, Union

class _StateChangeState(Enum): ...

class _StateChangeStates(_StateChangeState):
    ANY: int
    NO_CHANGE: int
    CHANGE_IN_PROGRESS: int

class _StateChange:
    @classmethod
    def declare_states(cls, prerequisite_states: Union[Literal[_StateChangeStates.ANY], Tuple[_StateChangeState, ...]], moves_to: _StateChangeState) -> Callable[[_F], _F]: ...
