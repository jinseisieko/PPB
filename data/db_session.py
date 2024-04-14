import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

import log_functions
from log_functions.outs import log_exception

SqlAlchemyBase = orm.declarative_base()

__factory: [type, None] = None


def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        log_exception("empty name")
        raise Exception("empty name")

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    log_functions.log_information(f"connect {conn_str}")
    engine = sa.create_engine(conn_str, echo=True)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models
    _ = repr(__all_models)

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    if __factory is None:
        raise Exception("not initialized")
    else:
        return __factory()
