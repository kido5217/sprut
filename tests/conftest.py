import pytest_asyncio

from sprut.database.connection import DatabaseConnection, get_database_connection


@pytest_asyncio.fixture
async def database_empty() -> DatabaseConnection:
    database = get_database_connection()
    for collection in await database.db.list_collection_names():
        await database.db.drop_collection(collection)
    return database


@pytest_asyncio.fixture
async def database_fresh() -> DatabaseConnection:
    database = get_database_connection()
    for collection in await database.db.list_collection_names():
        await database.db.drop_collection(collection)
    await database.create_collections()
    return database
