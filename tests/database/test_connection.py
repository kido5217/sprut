from motor.motor_asyncio import AsyncIOMotorDatabase
from pytest import mark

from sprut.database.connection import DatabaseConnection, get_database_connection


def test_database_connection_creation() -> None:
    """Check that database connection object is created successfully."""

    database_connection = get_database_connection()
    assert isinstance(database_connection, DatabaseConnection)
    assert isinstance(database_connection.db, AsyncIOMotorDatabase)


@mark.asyncio
async def test_database_client_connection() -> None:
    """Check that client can connect to test database."""

    database_connection = get_database_connection()

    # TODO: open PR in motor-types
    ping: dict[str, float] = await database_connection.db.command({"ping": 1})  # type: ignore
    assert ping == {"ok": 1.0}


@mark.asyncio
async def test_database_collection_creation() -> None:
    """Check that client can create all nesessary collections."""

    database_connection = get_database_connection()

    await database_connection.create_collections()
    collections_in_database: list[
        str
    ] = await database_connection.db.list_collection_names()
    assert set(collections_in_database) == DatabaseConnection.COLLECTIONS
