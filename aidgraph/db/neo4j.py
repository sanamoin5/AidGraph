"""Neo4j connection helpers."""

from neo4j import GraphDatabase
from typing import Optional


def get_driver(uri: str, user: str, password: str) -> GraphDatabase.driver:
    """Return a Neo4j driver instance."""
    return GraphDatabase.driver(uri, auth=(user, password))


# Placeholder for additional database utilities
