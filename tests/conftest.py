import pytest
from app.api import client


@pytest.fixture
def client_test():
    return client.test_client()
