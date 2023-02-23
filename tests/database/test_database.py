from motor.motor_asyncio import AsyncIOMotorDatabase
from pytest import mark

from sprut.database.database import Database, database_connection


def test_database_connection_creation() -> None:
    """Check that database connection object is created successfully."""

    assert isinstance(database_connection, Database)
    assert isinstance(database_connection.db, AsyncIOMotorDatabase)


@mark.asyncio
async def test_database_client_connection() -> None:
    """Check that client can connect to test database."""

    # TODO: open PR in motor-types
    ping: dict[str, float] = await database_connection.db.command({"ping": 1})  # type: ignore
    assert ping == {"ok": 1.0}
