from bson import ObjectId
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)

from sprut.database.models import DeviceModel
from sprut.exceptions import DocumentExists
from sprut.settings.database import mongodb_settings


class DatabaseConnection:
    """Database connection and data manipulation."""

    COLLECTIONS: set[str] = {"devices"}

    def __init__(self, url: str, db_name: str) -> None:
        """Create connection."""

        self.client: AsyncIOMotorClient = AsyncIOMotorClient(url)
        self.db: AsyncIOMotorDatabase = self.client[db_name]
        self.devices: AsyncIOMotorCollection = self.db["devices"]

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

    async def create_device(self, device: DeviceModel) -> ObjectId:
        """Create new device in database."""

        device_in_db = await self.devices.find_one({"name": device.name})
        if device_in_db is not None:
            raise DocumentExists(device_in_db.get("_id"))

        result = await self.devices.insert_one(device.dict(exclude={"id"}))
        return result.inserted_id


def get_database_connection() -> DatabaseConnection:
    """Create new database_connection."""

    database_connection: DatabaseConnection = DatabaseConnection(
        url=mongodb_settings.url, db_name=mongodb_settings.db_name
    )
    return database_connection
