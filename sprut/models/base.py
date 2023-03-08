from bson import ObjectId
from pydantic import BaseModel, Field


class ObjectIdField:
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid id")

        return ObjectId(value)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class BaseSprutModel(BaseModel):
    """Base model for sprut objects."""

    id: ObjectIdField | ObjectId | None = Field(alias="_id", default=None)

    class Config:
        arbitrary_types_allowed: bool = True
        orm_mode: bool = True
