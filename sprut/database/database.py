from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from sprut.settings.database import mongodb_settings

COLLECTIONS: tuple[str, ...] = ("devices",)


async def init_database(database: AsyncIOMotorDatabase) -> None:
    existing_collections: list[str] = await database.list_collection_names()  # type: ignore
    commections_to_create: list[str] = [
        collection
        for collection in COLLECTIONS
        if collection not in existing_collections
    ]
    for collection in commections_to_create:
        await database.create_collection(collection)  # type: ignore


async def get_database(
    url: str = mongodb_settings.url, db_name: str = mongodb_settings.db_name
) -> AsyncIOMotorDatabase:
    """Create instance of database object."""

    client: AsyncIOMotorClient = AsyncIOMotorClient(url)
    database: AsyncIOMotorDatabase = client[db_name]

    await init_database(database)

    return database
