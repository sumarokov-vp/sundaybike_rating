from _typeshed import Incomplete
from collections.abc import Generator
from redis.client import Redis as Redis
from redis.commands import SentinelCommands as SentinelCommands
from redis.connection import Connection as Connection, ConnectionPool as ConnectionPool, SSLConnection as SSLConnection
from redis.exceptions import ConnectionError as ConnectionError, ReadOnlyError as ReadOnlyError, ResponseError as ResponseError, TimeoutError as TimeoutError
from redis.utils import str_if_bytes as str_if_bytes
from typing import Optional

class MasterNotFoundError(ConnectionError): ...
class SlaveNotFoundError(ConnectionError): ...

class SentinelManagedConnection(Connection):
    connection_pool: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def connect_to(self, address) -> None: ...
    def connect(self): ...
    def read_response(self, disable_decoding: bool = ..., *, disconnect_on_error: Optional[bool] = ..., push_request: Optional[bool] = ...): ...

class SentinelManagedSSLConnection(SentinelManagedConnection, SSLConnection): ...

class SentinelConnectionPoolProxy:
    connection_pool_ref: Incomplete
    is_master: Incomplete
    check_connection: Incomplete
    service_name: Incomplete
    sentinel_manager: Incomplete
    def __init__(self, connection_pool, is_master, check_connection, service_name, sentinel_manager) -> None: ...
    master_address: Incomplete
    slave_rr_counter: Incomplete
    def reset(self) -> None: ...
    def get_master_address(self): ...
    def rotate_slaves(self) -> Generator[Incomplete, None, None]: ...

class SentinelConnectionPool(ConnectionPool):
    is_master: Incomplete
    check_connection: Incomplete
    proxy: Incomplete
    service_name: Incomplete
    sentinel_manager: Incomplete
    def __init__(self, service_name, sentinel_manager, **kwargs) -> None: ...
    def reset(self) -> None: ...
    @property
    def master_address(self): ...
    def owns_connection(self, connection): ...
    def get_master_address(self): ...
    def rotate_slaves(self): ...

class Sentinel(SentinelCommands):
    sentinel_kwargs: Incomplete
    sentinels: Incomplete
    min_other_sentinels: Incomplete
    connection_kwargs: Incomplete
    def __init__(self, sentinels, min_other_sentinels: int = ..., sentinel_kwargs: Incomplete | None = ..., **connection_kwargs) -> None: ...
    def execute_command(self, *args, **kwargs): ...
    def check_master_state(self, state, service_name): ...
    def discover_master(self, service_name): ...
    def filter_slaves(self, slaves): ...
    def discover_slaves(self, service_name): ...
    def master_for(self, service_name, redis_class=..., connection_pool_class=..., **kwargs): ...
    def slave_for(self, service_name, redis_class=..., connection_pool_class=..., **kwargs): ...
