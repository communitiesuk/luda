from typing import Any, Generator

import pytest
from starlette.testclient import TestClient

from app.main import app


def pytest_configure(config: pytest.Config) -> None:
    """Pytest configuration hook."""
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")


@pytest.fixture()
def testclient() -> Generator[TestClient, Any, None]:
    """Create a test client for the application."""
    with TestClient(app) as client:
        yield client
