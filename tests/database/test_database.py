from motor.motor_asyncio import AsyncIOMotorDatabase
from pytest import mark

from sprut.database.database import get_database


@mark.asyncio
async def test_database_client_creation() -> None:
    """Check that database connection object is created successfully."""

    database: AsyncIOMotorDatabase = await get_database()
    assert isinstance(database, AsyncIOMotorDatabase)


@mark.asyncio
async def test_database_client_connection() -> None:
    """Check that client can connect to test database."""

    database: AsyncIOMotorDatabase = await get_database()
    # TODO: open PR in motor-types
    ping: dict[str, float] = await database.command({"ping": 1})  # type: ignore
    assert ping == {"ok": 1.0}
