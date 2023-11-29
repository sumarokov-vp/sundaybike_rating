from _typeshed import Incomplete

class TranslitLanguagePack:
    language_code: Incomplete
    language_name: Incomplete
    character_ranges: Incomplete
    mapping: Incomplete
    reversed_specific_mapping: Incomplete
    reversed_pre_processor_mapping_keys: Incomplete
    reversed_specific_pre_processor_mapping: Incomplete
    reversed_specific_pre_processor_mapping_keys: Incomplete
    pre_processor_mapping: Incomplete
    pre_processor_mapping_keys: Incomplete
    detectable: bool
    characters: Incomplete
    reversed_characters: Incomplete
    translation_table: Incomplete
    reversed_translation_table: Incomplete
    reversed_pre_processor_mapping: Incomplete
    reversed_specific_translation_table: Incomplete
    def __init__(self) -> None: ...
    def translit(self, value, reversed: bool = ..., strict: bool = ..., fail_silently: bool = ...): ...
    def make_strict(self, value, reversed: bool = ...): ...
    @classmethod
    def contains(cls, character): ...
    @classmethod
    def suggest(value, reversed: bool = ..., limit: Incomplete | None = ...) -> None: ...
    @classmethod
    def detect(text, num_words: Incomplete | None = ...) -> None: ...

class TranslitRegistry:
    def __init__(self) -> None: ...
    @property
    def registry(self): ...
    def register(self, cls, force: bool = ...): ...
    def unregister(self, cls): ...
    def get(self, language_code, default: Incomplete | None = ...): ...

registry: Incomplete
