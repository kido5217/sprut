from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from sprut.settings.database import mongodb_settings


class Database:
    """Database connection and data manipulation."""

    COLLECTIONS: set[str] = {"devices"}

    def __init__(self, url: str, db_name: str) -> None:
        """Create connection."""

        self.client: AsyncIOMotorClient = AsyncIOMotorClient(url)
        self.db: AsyncIOMotorDatabase = self.client[db_name]

    async def create_collections(self) -> None:
        """Create all necessary collections."""

        existing_collections: list[str] = await self.db.list_collection_names()  # type: ignore
        commections_to_create: list[str] = [
            collection
            for collection in self.COLLECTIONS
            if collection not in existing_collections
        ]
        for collection in commections_to_create:
            await self.db.create_collection(collection)  # type: ignore


def get_database_connection() -> Database:
    """Create new database_connection."""

    database_connection: Database = Database(
        url=mongodb_settings.url, db_name=mongodb_settings.db_name
    )
    return database_connection
