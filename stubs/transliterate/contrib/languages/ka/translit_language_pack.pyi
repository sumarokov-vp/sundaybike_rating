from _typeshed import Incomplete
from transliterate.base import TranslitLanguagePack

class GeorgianLanguagePack(TranslitLanguagePack):
    language_code: str
    language_name: str
    character_ranges: Incomplete
    mapping: Incomplete
    pre_processor_mapping: Incomplete
    detectable: bool
    def translit(self, value, reversed: bool = ..., strict: bool = ..., fail_silently: bool = ...): ...
