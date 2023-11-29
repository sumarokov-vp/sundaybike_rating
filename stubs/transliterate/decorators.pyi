from _typeshed import Incomplete

class TransliterateFunction:
    language_code: Incomplete
    reversed: Incomplete
    def __init__(self, language_code, reversed: bool = ...) -> None: ...
    def __call__(self, func): ...
transliterate_function = TransliterateFunction

class TransliterateMethod:
    language_code: Incomplete
    reversed: Incomplete
    def __init__(self, language_code, reversed: bool = ...) -> None: ...
    def __call__(self, func): ...
transliterate_method = TransliterateMethod
