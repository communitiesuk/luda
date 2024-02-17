import requests
from starlette.testclient import TestClient


def test_root_endpoint(testclient: TestClient) -> None:
    """Test the root endpoint."""
    r = testclient.get("/")
    assert r.status_code == requests.codes.ok


def test_get_missions(testclient: TestClient) -> None:
    """Test the /missions endpoint."""
    r = testclient.get("/missions")
    assert r.status_code == requests.codes.ok, r.text
