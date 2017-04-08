import pytest

from fixtures.Pulse_api_client import PulseTestApi


@pytest.fixture()
def book_app():
    return PulseTestApi("books")