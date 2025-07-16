"""PostgreSQL connection helpers."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def get_engine(dsn: str):
    """Create an SQLAlchemy engine."""
    return create_engine(dsn)


def get_session(dsn: str) -> Session:
    """Return a session connected to PostgreSQL."""
    engine = get_engine(dsn)
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()


# Placeholder for ORM models and queries
