from ... import util as util
from .base import BIT as BIT, MySQLDialect as MySQLDialect
from .mysqldb import MySQLDialect_mysqldb as MySQLDialect_mysqldb
from _typeshed import Incomplete

class _cymysqlBIT(BIT):
    def result_processor(self, dialect, coltype): ...

class MySQLDialect_cymysql(MySQLDialect_mysqldb):
    driver: str
    supports_statement_cache: bool
    description_encoding: Incomplete
    supports_sane_rowcount: bool
    supports_sane_multi_rowcount: bool
    supports_unicode_statements: bool
    colspecs: Incomplete
    @classmethod
    def import_dbapi(cls): ...
    def is_disconnect(self, e, connection, cursor): ...
dialect = MySQLDialect_cymysql
