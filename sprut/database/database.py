from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from sprut.settings.database import mongodb_settings


def get_database(
    url: str = mongodb_settings.url, db_name: str = mongodb_settings.db_name
) -> AsyncIOMotorDatabase:
    """Create instance of database object."""

    client: AsyncIOMotorClient = AsyncIOMotorClient(url)
    database: AsyncIOMotorDatabase = client[db_name]

    return database
