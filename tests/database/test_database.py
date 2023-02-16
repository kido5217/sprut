from typing import Any

from motor.motor_asyncio import AsyncIOMotorDatabase
from pytest import mark

from sprut.database.database import get_database


def test_database_client_creation() -> None:
    """Check that database connection object is created successfully."""

    database: AsyncIOMotorDatabase = get_database()
    assert isinstance(database, AsyncIOMotorDatabase)


@mark.asyncio
async def test_database_client_connection() -> None:
    """Check that client can connect to test database."""

    database: AsyncIOMotorDatabase = get_database()
    result: Any = await database.command("buildinfo")
    print(result)
