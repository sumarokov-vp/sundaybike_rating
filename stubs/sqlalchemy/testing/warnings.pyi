from . import assertions as assertions
from .. import exc as exc
from ..exc import SATestSuiteWarning as SATestSuiteWarning

def warn_test_suite(message) -> None: ...
def setup_filters() -> None: ...
def assert_warnings(fn, warning_msgs, regex: bool = ...): ...