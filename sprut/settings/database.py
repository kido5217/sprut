import urllib.parse
from typing import Any

from pydantic import root_validator

from sprut.settings.base import APP_PREFIX, AppBaseSettings


class MongoDBSettings(AppBaseSettings):
    """MongoDB settings and url generator."""

    hostname: str = "localhost"
    username: str = "mongouser"
    password: str = "mongopass"
    db_name: str = "sprut"
    port: int = 27017
    url: str | None = None

    class Config(AppBaseSettings.Config):
        """Pydantic-specific options."""

        env_prefix: str = f"{APP_PREFIX}_mongodb_"

    @root_validator(pre=True)
    def parse_url(cls, values: dict[str, Any]) -> dict[str, Any]:
        """Split url and unquote login/password.

        If url is specified, it precedes other options.
        This behaviour may change in the future.
        """

        if values.get("url") is not None:
            url: urllib.parse.ParseResult = urllib.parse.urlparse(
                str(values.get("url"))
            )

            if url.hostname is not None:
                values["hostname"] = url.hostname
            if url.username is not None:
                values["username"] = urllib.parse.unquote(url.username)
            if url.password is not None:
                values["password"] = urllib.parse.unquote(url.password)
            if url.path != "":
                values["db_name"] = url.path.lstrip("/")
            if url.port is not None:
                values["port"] = url.port
        return values

    @root_validator()
    def generate_url(cls, values: dict[str, Any]) -> dict[str, Any]:
        """Generate url from separate options."""

        if values.get("url") is None:
            quoted_username: str = urllib.parse.quote(
                str(values.get("username")), safe=""
            )
            quoted_password: str = urllib.parse.quote(
                str(values.get("password")), safe=""
            )
            values[
                "url"
            ] = f'mongodb://{quoted_username}:{quoted_password}@{values["hostname"]}:{values["port"]}/{values["db_name"]}'
        return values


mongodb_settings = MongoDBSettings()
