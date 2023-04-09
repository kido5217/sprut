from bson import ObjectId
from pydantic import BaseModel, Field, validator


class BaseDocumentModel(BaseModel):
    """Base model for MongoDB Documents."""

    id: ObjectId | None = Field(alias="_id", default=None)

    @validator("id")
    def create_object_id(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid id")

        return ObjectId(value)

    class Config:
        arbitrary_types_allowed: bool = True
        orm_mode: bool = True

    def to_mongodb(self):
        """Export as mongodb-compatimle dict."""
        return self.dict(by_alias=True)


class DeviceModel(BaseDocumentModel):
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
