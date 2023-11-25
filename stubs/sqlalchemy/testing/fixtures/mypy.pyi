from .. import config as config
from ... import util as util
from ..assertions import eq_ as eq_
from .base import TestBase as TestBase
from _typeshed import Incomplete
from collections.abc import Generator

class MypyTest(TestBase):
    __requires__: Incomplete
    def per_func_cachedir(self) -> Generator[Incomplete, Incomplete, None]: ...
    def cachedir(self) -> Generator[Incomplete, Incomplete, None]: ...
    def mypy_runner(self, cachedir): ...
    def mypy_typecheck_file(self, mypy_runner): ...
    @staticmethod
    def file_combinations(dirname): ...
