import pytest


@pytest.fixture
def no_env_vars(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SPRUT_MONGODB_HOSTNAME", raising=False)
    monkeypatch.delenv("SPRUT_MONGODB_USERNAME", raising=False)
    monkeypatch.delenv("SPRUT_MONGODB_PASSWORD", raising=False)
    monkeypatch.delenv("SPRUT_MONGODB_DB_NAME", raising=False)
    monkeypatch.delenv("SPRUT_MONGODB_PORT", raising=False)


@pytest.fixture
def env_vars_simple(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SPRUT_MONGODB_HOSTNAME", "hostname-simple")
    monkeypatch.setenv("SPRUT_MONGODB_USERNAME", "username_simple")
    monkeypatch.setenv("SPRUT_MONGODB_PASSWORD", "password_simple")
    monkeypatch.setenv("SPRUT_MONGODB_DB_NAME", "db_name_simple")
    monkeypatch.setenv("SPRUT_MONGODB_PORT", "27027")


@pytest.fixture
def env_vars_with_special_symbols(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SPRUT_MONGODB_HOSTNAME", "hostname-simple")
    monkeypatch.setenv("SPRUT_MONGODB_USERNAME", "Y/XVknj+TaduO4v")
    monkeypatch.setenv("SPRUT_MONGODB_PASSWORD", "F#%?Dn4mGU3Vj")
    monkeypatch.setenv("SPRUT_MONGODB_DB_NAME", "db_name_simple")
    monkeypatch.setenv("SPRUT_MONGODB_PORT", "27037")


@pytest.fixture
def env_vars_only_url(monkeypatch: pytest.MonkeyPatch) -> None:
    url = "mongodb://username_simple:password_simple@hostname-simple:27047"
    monkeypatch.setenv("SPRUT_MONGODB_URL", url)


@pytest.fixture
def env_vars_only_url_with_special_symbols(monkeypatch: pytest.MonkeyPatch) -> None:
    url = "mongodb://Z86YSXuWEq%2BgV%3A:%23C%5B%5DUT5pHif1G@hostname-simple:27067"
    monkeypatch.setenv("SPRUT_MONGODB_URL", url)


@pytest.fixture
def env_vars_url_and_other_settings(monkeypatch: pytest.MonkeyPatch) -> None:
    url = "mongodb://username_simple:password_simple@hostname-simple:27057"
    monkeypatch.setenv("SPRUT_MONGODB_URL", url)
    monkeypatch.setenv("SPRUT_MONGODB_HOSTNAME", "hostname-other")
    monkeypatch.setenv("SPRUT_MONGODB_USERNAME", "username_other")
    monkeypatch.setenv("SPRUT_MONGODB_PASSWORD", "password_other")
    monkeypatch.setenv("SPRUT_MONGODB_DB_NAME", "db_name_other")
    monkeypatch.setenv("SPRUT_MONGODB_PORT", "27057")
