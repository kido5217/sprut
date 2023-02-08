from pydantic import BaseSettings

APP_PREFIX: str = "sprut"


class AppBaseSettings(BaseSettings):
    """Base settings object."""

    class Config:
        allow_mutations: bool = False
