import pytest

from sprut.settings.database import MongoDBSettings


def test_no_env_vars(no_env_vars: pytest.MonkeyPatch) -> None:
    settings: MongoDBSettings = MongoDBSettings()
    assert settings.hostname == "localhost"
    assert settings.username == "mongouser"
    assert settings.password == "mongopass"
    assert settings.db_name == "sprut"
    assert settings.port == 27017
    assert settings.url == "mongodb://mongouser:mongopass@localhost:27017"


def test_env_vars_simple(env_vars_simple: pytest.MonkeyPatch) -> None:
    settings: MongoDBSettings = MongoDBSettings()
    assert settings.hostname == "hostname-simple"
    assert settings.username == "username_simple"
    assert settings.password == "password_simple"
    assert settings.db_name == "db_name_simple"
    assert settings.port == 27027
    assert (
        settings.url
        == "mongodb://username_simple:password_simple@hostname-simple:27027"
    )


def test_env_vars_with_special_symbols(
    env_vars_with_special_symbols: pytest.MonkeyPatch,
) -> None:
    settings: MongoDBSettings = MongoDBSettings()
    assert settings.hostname == "hostname-simple"
    assert settings.username == "Y/XVknj+TaduO4v"
    assert settings.password == "F#%?Dn4mGU3Vj"
    assert settings.db_name == "db_name_simple"
    assert settings.port == 27037
    assert (
        settings.url
        == "mongodb://Y%2FXVknj%2BTaduO4v:F%23%25%3FDn4mGU3Vj@hostname-simple:27037"
    )


def test_env_vars_only_url(env_vars_only_url: pytest.MonkeyPatch) -> None:
    settings: MongoDBSettings = MongoDBSettings()
    assert settings.hostname == "hostname-simple"
    assert settings.username == "username_simple"
    assert settings.password == "password_simple"
    assert settings.db_name == "sprut"
    assert settings.port == 27047
    assert (
        settings.url
        == "mongodb://username_simple:password_simple@hostname-simple:27047"
    )


def test_env_vars_only_url_with_special_symbols(
    env_vars_only_url_with_special_symbols: pytest.MonkeyPatch,
) -> None:
    settings: MongoDBSettings = MongoDBSettings()
    assert settings.hostname == "hostname-simple"
    assert settings.username == "Z86YSXuWEq+gV:"
    assert settings.password == "#C[]UT5pHif1G"
    assert settings.db_name == "sprut"
    assert settings.port == 27067
    assert (
        settings.url
        == "mongodb://Z86YSXuWEq%2BgV%3A:%23C%5B%5DUT5pHif1G@hostname-simple:27067"
    )


def test_env_vars_url_and_other_settings(
    env_vars_url_and_other_settings: pytest.MonkeyPatch,
) -> None:
    settings: MongoDBSettings = MongoDBSettings()
    assert settings.hostname == "hostname-simple"
    assert settings.username == "username_simple"
    assert settings.password == "password_simple"
    assert settings.db_name == "db_name_other"
    assert settings.port == 27057
    assert (
        settings.url
        == "mongodb://username_simple:password_simple@hostname-simple:27057"
    )
