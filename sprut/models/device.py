from ipaddress import IPv4Address

from pydantic import BaseModel


class DeviceModel(BaseModel):
    """Device general information."""

    name: str
    id: str | None = None
    oam_ip: IPv4Address | None = None
    ldp_ip: IPv4Address | None = None
    domain: str | None = None
    sources: list[str] | None = None
    groups: list[str] | None = None
    tags: list[str] | None = None
    vendor: str | None = None
    model: str | None = None
