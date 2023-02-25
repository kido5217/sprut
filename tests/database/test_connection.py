import pytest
from motor.motor_asyncio import AsyncIOMotorDatabase

from sprut.database.connection import DatabaseConnection, get_database_connection


def test_database_connection_creation() -> None:
    """Check that database connection object is created successfully."""

    database = get_database_connection()
    assert isinstance(database, DatabaseConnection)
    assert isinstance(database.db, AsyncIOMotorDatabase)


@pytest.mark.asyncio
async def test_database_client_connection() -> None:
    """Check that client can connect to test database."""

    database = get_database_connection()

    # TODO: open PR in motor-types
    ping: dict[str, float] = await database.db.command({"ping": 1})  # type: ignore
    assert ping == {"ok": 1.0}


@pytest.mark.asyncio
async def test_database_collection_creation(database_empty: DatabaseConnection) -> None:
    """Check that client can create all nesessary collections."""

    database = database_empty
    await database.create_collections()
    collections_in_database: list[str] = await database.db.list_collection_names()
    assert set(collections_in_database) == DatabaseConnection.COLLECTIONS
