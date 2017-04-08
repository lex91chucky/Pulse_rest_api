import pytest

from fixtures.Pulse_api_client import PulseTestApi


@pytest.fixture(scope="session")
def book_app():
    return PulseTestApi(resourse="books")

