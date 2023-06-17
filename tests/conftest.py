import pytest
from starlette.testclient import TestClient

from web.run import create_app


@pytest.fixture(scope="session")
def client() -> TestClient:
    return TestClient(app=create_app())
