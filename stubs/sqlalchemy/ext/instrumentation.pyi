from .. import util as util
from ..orm import attributes as attributes, collections as collections
from ..orm.instrumentation import ClassManager as ClassManager, InstrumentationFactory as InstrumentationFactory
from _typeshed import Incomplete

INSTRUMENTATION_MANAGER: str

def find_native_user_instrumentation_hook(cls): ...

instrumentation_finders: Incomplete

class ExtendedInstrumentationRegistry(InstrumentationFactory):
    def unregister(self, class_) -> None: ...
    def opt_manager_of_class(self, cls): ...
    def manager_of_class(self, cls): ...
    def state_of(self, instance): ...
    def dict_of(self, instance): ...

class InstrumentationManager:
    def __init__(self, class_) -> None: ...
    def manage(self, class_, manager) -> None: ...
    def unregister(self, class_, manager) -> None: ...
    def manager_getter(self, class_): ...
    def instrument_attribute(self, class_, key, inst) -> None: ...
    def post_configure_attribute(self, class_, key, inst) -> None: ...
    def install_descriptor(self, class_, key, inst) -> None: ...
    def uninstall_descriptor(self, class_, key) -> None: ...
    def install_member(self, class_, key, implementation) -> None: ...
    def uninstall_member(self, class_, key) -> None: ...
    def instrument_collection_class(self, class_, key, collection_class): ...
    def get_instance_dict(self, class_, instance): ...
    def initialize_instance_dict(self, class_, instance) -> None: ...
    def install_state(self, class_, instance, state) -> None: ...
    def remove_state(self, class_, instance) -> None: ...
    def state_getter(self, class_): ...
    def dict_getter(self, class_): ...

class _ClassInstrumentationAdapter(ClassManager):
    def __init__(self, class_, override) -> None: ...
    def manage(self) -> None: ...
    def unregister(self) -> None: ...
    def manager_getter(self): ...
    def instrument_attribute(self, key, inst, propagated: bool = ...) -> None: ...
    def post_configure_attribute(self, key) -> None: ...
    def install_descriptor(self, key, inst) -> None: ...
    def uninstall_descriptor(self, key) -> None: ...
    def install_member(self, key, implementation) -> None: ...
    def uninstall_member(self, key) -> None: ...
    def instrument_collection_class(self, key, collection_class): ...
    def initialize_collection(self, key, state, factory): ...
    def new_instance(self, state: Incomplete | None = ...): ...
    def setup_instance(self, instance, state: Incomplete | None = ...): ...
    def teardown_instance(self, instance) -> None: ...
    def has_state(self, instance): ...
    def state_getter(self): ...
    def dict_getter(self): ...
