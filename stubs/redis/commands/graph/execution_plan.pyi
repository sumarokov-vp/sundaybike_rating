from _typeshed import Incomplete

class ProfileStats:
    records_produced: Incomplete
    execution_time: Incomplete
    def __init__(self, records_produced, execution_time) -> None: ...

class Operation:
    name: Incomplete
    args: Incomplete
    profile_stats: Incomplete
    children: Incomplete
    def __init__(self, name, args: Incomplete | None = ..., profile_stats: Incomplete | None = ...) -> None: ...
    def append_child(self, child): ...
    def child_count(self): ...
    def __eq__(self, o: object) -> bool: ...

class ExecutionPlan:
    plan: Incomplete
    structured_plan: Incomplete
    def __init__(self, plan) -> None: ...
    def __eq__(self, o: object) -> bool: ...
