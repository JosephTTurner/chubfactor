from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.ddl import CreateSchema
from sqlalchemy import create_engine
from contextlib import contextmanager

#
from core.config import config

connection_string = (
    f"{config.DB_DIALECT}://"
    + f"{config.DB_USER}:"
    + f"{config.DB_PASS}@"
    + f"{config.DB_HOST}:"
    + f"{config.DB_PORT}/"
    + f"{config.DB_SCHEMA}"
)

engine = create_engine(connection_string)

session_factory = sessionmaker(bind=engine)

Session = scoped_session(session_factory)


@contextmanager
def db_session_scope() -> Session:
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def create_database_if_not_exists():
    test_engine = create_engine(
        f"{config.DB_DIALECT}://"
        + f"{config.DB_USER}:"
        + f"{config.DB_PASS}@"
        + f"{config.DB_HOST}:"
        + f"{config.DB_PORT}"
    )
    conn = test_engine.connect()
    if not conn.dialect.has_schema(conn, config.DB_SCHEMA):
        engine.execute(CreateSchema(config.DB_SCHEMA))
