from ...connectors.aioodbc import aiodbcConnector as aiodbcConnector
from .pyodbc import MSDialect_pyodbc as MSDialect_pyodbc, MSExecutionContext_pyodbc as MSExecutionContext_pyodbc

class MSExecutionContext_aioodbc(MSExecutionContext_pyodbc):
    def create_server_side_cursor(self): ...

class MSDialectAsync_aioodbc(aiodbcConnector, MSDialect_pyodbc):
    driver: str
    supports_statement_cache: bool
    execution_ctx_cls = MSExecutionContext_aioodbc
dialect = MSDialectAsync_aioodbc
