from ipaddress import IPv4Address

import pytest
from bson import ObjectId

from sprut.database.connection import DatabaseConnection
from sprut.exceptions import DocumentExists
from sprut.database.models import DeviceModel

DeviceModelT = dict[str, str | ObjectId | list[str] | None]


@pytest.mark.asyncio
async def test_create_basic(database_fresh: DatabaseConnection) -> None:
    device_data: DeviceModelT = {
        "name": "r1",
    }
    device: DeviceModel = DeviceModel.parse_obj(device_data)
    device.id = await database_fresh.create_device(device)

    device_in_db: DeviceModel = DeviceModel.parse_obj(
        await database_fresh.devices.find_one({"name": device_data["name"]})
    )

    device_in_db_by_id: DeviceModel = DeviceModel.parse_obj(
        await database_fresh.devices.find_one({"_id": device.id})
    )

    assert device == device_in_db == device_in_db_by_id


@pytest.mark.asyncio
async def test_create_full(database_fresh: DatabaseConnection) -> None:
    device_data: DeviceModelT = {
        "name": "r1",
        "oam_ip": "10.10.10.1",
        "ldp_ip": "10.1.1.1",
        "domain": "example.com",
        "source": None,
        "groups": ["group1", "group2"],
        "tags": ["router", "down", "bb"],
        "vendor": "cisco",
        "model": "7600",
    }
    device: DeviceModel = DeviceModel.parse_obj(device_data)
    device.id = await database_fresh.create_device(device)

    device_in_db: DeviceModel = DeviceModel.parse_obj(
        await database_fresh.devices.find_one({"name": device_data["name"]})
    )

    device_in_db_by_id: DeviceModel = DeviceModel.parse_obj(
        await database_fresh.devices.find_one({"_id": device.id})
    )

    assert device == device_in_db == device_in_db_by_id


@pytest.mark.asyncio
async def test_exception_on_create_existing(database_fresh: DatabaseConnection) -> None:
    device_data: DeviceModelT = {
        "name": "r1",
    }
    device: DeviceModel = DeviceModel.parse_obj(device_data)

    await database_fresh.create_device(device)

    with pytest.raises(DocumentExists):
        await database_fresh.create_device(device)
