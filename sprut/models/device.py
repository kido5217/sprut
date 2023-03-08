from bson import ObjectId

from sprut.models.base import BaseSprutModel

DeviceBaseT = dict[str, str | ObjectId | list[str] | None]


class DeviceBase(BaseSprutModel):
    """Device general information."""

    name: str
    oam_ip: str | None = None
    ldp_ip: str | None = None
    domain: str | None = None
    sources: list[str] | None = None
    groups: list[str] | None = None
    tags: list[str] | None = None
    vendor: str | None = None
    model: str | None = None
