from ..schema import Column as Column
from ..types import String as String
from .entities import ComparableEntity as ComparableEntity
from _typeshed import Incomplete

class User(ComparableEntity): ...
class Order(ComparableEntity): ...
class Dingaling(ComparableEntity): ...
class EmailUser(User): ...
class Address(ComparableEntity): ...
class Child1(ComparableEntity): ...
class Child2(ComparableEntity): ...
class Parent(ComparableEntity): ...

class Screen:
    obj: Incomplete
    parent: Incomplete
    def __init__(self, obj, parent: Incomplete | None = ...) -> None: ...

class Mixin:
    email_address: Incomplete

class AddressWMixin(Mixin, ComparableEntity): ...

class Foo:
    data: str
    stuff: Incomplete
    moredata: Incomplete
    def __init__(self, moredata, stuff: str = ...) -> None: ...
    __hash__: Incomplete
    def __eq__(self, other): ...

class Bar:
    x: Incomplete
    y: Incomplete
    def __init__(self, x, y) -> None: ...
    __hash__: Incomplete
    def __eq__(self, other): ...

class OldSchool:
    x: Incomplete
    y: Incomplete
    def __init__(self, x, y) -> None: ...
    def __eq__(self, other): ...

class OldSchoolWithoutCompare:
    x: Incomplete
    y: Incomplete
    def __init__(self, x, y) -> None: ...

class BarWithoutCompare:
    x: Incomplete
    y: Incomplete
    def __init__(self, x, y) -> None: ...

class NotComparable:
    data: Incomplete
    def __init__(self, data) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class BrokenComparable:
    data: Incomplete
    def __init__(self, data) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...