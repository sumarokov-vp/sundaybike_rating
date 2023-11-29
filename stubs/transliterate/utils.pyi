from _typeshed import Incomplete

def get_translit_function(language_code): ...
def translit(value, language_code: Incomplete | None = ..., reversed: bool = ..., strict: bool = ...): ...
def suggest(value, language_code: Incomplete | None = ..., reversed: bool = ..., limit: Incomplete | None = ...): ...
def get_available_language_codes(): ...
def get_available_language_packs(): ...
def detect_language(text, num_words: Incomplete | None = ..., fail_silently: bool = ..., heavy_check: bool = ...): ...
def slugify(text, language_code: Incomplete | None = ...): ...
