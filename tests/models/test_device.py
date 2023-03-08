import pytest
from bson import ObjectId
from pydantic import ValidationError

from sprut.models.device import DeviceBase, DeviceBaseT


def test_simple() -> None:
    """Test creating device object with only name sprcified."""

    device_data: dict[str, str] = {"name": "r1"}

    device: DeviceBase = DeviceBase.parse_obj(device_data)

    assert device_data == device.dict(exclude_unset=True)


def test_full_data() -> None:
    """Test creating device object with all data specified."""

    device_data: DeviceBaseT = {
        "name": "r2",
        "_id": ObjectId("507f1f77bcf86cd799439011"),
        "oam_ip": "10.10.10.2",
        "ldp_ip": "20.20.20.2",
        "domain": "example.com",
        "sources": ["rancid", "cmdb"],
        "groups": ["bb"],
        "tags": ["cisco", "bb", "up"],
        "vendor": "cisco",
        "model": "7206",
    }

    device: DeviceBase = DeviceBase.parse_obj(device_data)

    assert device_data == device.dict(by_alias=True)


def test_str_to_ip() -> None:
    """Test creating device object with ips as strings."""

    device_data: DeviceBaseT = {
        "name": "r2",
        "_id": ObjectId("507f1f77bcf86cd799439011"),
        "oam_ip": "10.10.10.2",
        "ldp_ip": "20.20.20.2",
        "domain": "example.com",
        "sources": ["rancid", "cmdb"],
        "groups": ["bb"],
        "tags": ["cisco", "bb", "up"],
        "vendor": "cisco",
        "model": "7206",
    }

    device: DeviceBase = DeviceBase.parse_obj(device_data)

    assert device_data == device.dict(by_alias=True)


def test_malformed_data() -> None:
    """Test raising pydantic exception on wrong data."""

    device_data: DeviceBaseT = {
        "name": "r2",
        "_id": ObjectId("507f1f77bcf86cd799439011"),
        "oam_ip": "10.10.10.2",
        "ldp_ip": "20.20.20.2",
        "domain": "example.com",
        "sources": ["rancid", "cmdb"],
        "groups": ["bb"],
        "tags": ["cisco", "bb", "up"],
        "vendor": "cisco",
        "model": ["7206"],  # This should be str not list.
    }

    with pytest.raises(ValidationError):
        DeviceBase.parse_obj(device_data)
