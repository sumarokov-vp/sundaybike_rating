from . import config as config, engines as engines, util as util
from .. import exc as exc, inspect as inspect
from ..sql import ddl as ddl, schema as schema
from _typeshed import Incomplete
from collections.abc import Generator

log: Incomplete
FOLLOWER_IDENT: Incomplete

class register:
    fns: Incomplete
    decorator: Incomplete
    def __init__(self, decorator: Incomplete | None = ...) -> None: ...
    @classmethod
    def init(cls, fn): ...
    @classmethod
    def init_decorator(cls, decorator): ...
    def for_db(self, *dbnames): ...
    def __call__(self, cfg, *arg, **kw): ...

def create_follower_db(follower_ident) -> None: ...
def setup_config(db_url, options, file_config, follower_ident): ...
def drop_follower_db(follower_ident) -> None: ...
def generate_db_urls(db_urls, extra_drivers) -> Generator[Incomplete, None, None]: ...
def generate_driver_url(url, driver, query_str): ...
def drop_all_schema_objects_pre_tables(cfg, eng) -> None: ...
def drop_all_schema_objects_post_tables(cfg, eng) -> None: ...
def drop_all_schema_objects(cfg, eng) -> None: ...
def drop_views(cfg, eng) -> None: ...
def drop_materialized_views(cfg, eng) -> None: ...
def create_db(cfg, eng, ident) -> None: ...
def drop_db(cfg, eng, ident) -> None: ...
def update_db_opts(db_url, db_opts, options) -> None: ...
def post_configure_engine(url, engine, follower_ident) -> None: ...
def follower_url_from_main(url, ident): ...
def configure_follower(cfg, ident) -> None: ...
def run_reap_dbs(url, ident) -> None: ...
def reap_dbs(idents_file) -> None: ...
def temp_table_keyword_args(cfg, eng) -> None: ...
def prepare_for_drop_tables(config, connection) -> None: ...
def stop_test_class_outside_fixtures(config, db, testcls) -> None: ...
def get_temp_table_name(cfg, eng, base_name): ...
def set_default_schema_on_connection(cfg, dbapi_connection, schema_name) -> None: ...
def upsert(cfg, table, returning, *, set_lambda: Incomplete | None = ..., sort_by_parameter_order: bool = ...) -> None: ...
def normalize_sequence(cfg, sequence): ...
