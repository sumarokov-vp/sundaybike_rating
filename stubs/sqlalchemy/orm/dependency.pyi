from . import attributes as attributes, exc as exc, sync as sync, unitofwork as unitofwork
from .. import sql as sql, util as util
from .interfaces import MANYTOMANY as MANYTOMANY, MANYTOONE as MANYTOONE, ONETOMANY as ONETOMANY
from _typeshed import Incomplete

class DependencyProcessor:
    prop: Incomplete
    cascade: Incomplete
    mapper: Incomplete
    parent: Incomplete
    secondary: Incomplete
    direction: Incomplete
    post_update: Incomplete
    passive_deletes: Incomplete
    passive_updates: Incomplete
    enable_typechecks: Incomplete
    sort_key: Incomplete
    key: Incomplete
    def __init__(self, prop) -> None: ...
    @classmethod
    def from_relationship(cls, prop): ...
    def hasparent(self, state): ...
    def per_property_preprocessors(self, uow) -> None: ...
    def per_property_flush_actions(self, uow) -> None: ...
    def per_state_flush_actions(self, uow, states, isdelete) -> None: ...
    def presort_deletes(self, uowcommit, states): ...
    def presort_saves(self, uowcommit, states): ...
    def process_deletes(self, uowcommit, states) -> None: ...
    def process_saves(self, uowcommit, states) -> None: ...
    def prop_has_changes(self, uowcommit, states, isdelete): ...

class OneToManyDP(DependencyProcessor):
    def per_property_dependencies(self, uow, parent_saves, child_saves, parent_deletes, child_deletes, after_save, before_delete) -> None: ...
    def per_state_dependencies(self, uow, save_parent, delete_parent, child_action, after_save, before_delete, isdelete, childisdelete) -> None: ...
    def presort_deletes(self, uowcommit, states) -> None: ...
    def presort_saves(self, uowcommit, states) -> None: ...
    def process_deletes(self, uowcommit, states) -> None: ...
    def process_saves(self, uowcommit, states) -> None: ...

class ManyToOneDP(DependencyProcessor):
    def __init__(self, prop) -> None: ...
    def per_property_dependencies(self, uow, parent_saves, child_saves, parent_deletes, child_deletes, after_save, before_delete) -> None: ...
    def per_state_dependencies(self, uow, save_parent, delete_parent, child_action, after_save, before_delete, isdelete, childisdelete) -> None: ...
    def presort_deletes(self, uowcommit, states) -> None: ...
    def presort_saves(self, uowcommit, states) -> None: ...
    def process_deletes(self, uowcommit, states) -> None: ...
    def process_saves(self, uowcommit, states) -> None: ...

class DetectKeySwitch(DependencyProcessor):
    def per_property_preprocessors(self, uow) -> None: ...
    def per_property_flush_actions(self, uow) -> None: ...
    def per_state_flush_actions(self, uow, states, isdelete) -> None: ...
    def presort_deletes(self, uowcommit, states) -> None: ...
    def presort_saves(self, uow, states) -> None: ...
    def prop_has_changes(self, uow, states, isdelete): ...
    def process_deletes(self, uowcommit, states) -> None: ...
    def process_saves(self, uowcommit, states) -> None: ...

class ManyToManyDP(DependencyProcessor):
    def per_property_dependencies(self, uow, parent_saves, child_saves, parent_deletes, child_deletes, after_save, before_delete) -> None: ...
    def per_state_dependencies(self, uow, save_parent, delete_parent, child_action, after_save, before_delete, isdelete, childisdelete) -> None: ...
    def presort_deletes(self, uowcommit, states) -> None: ...
    def presort_saves(self, uowcommit, states) -> None: ...
    def process_deletes(self, uowcommit, states) -> None: ...
    def process_saves(self, uowcommit, states) -> None: ...
