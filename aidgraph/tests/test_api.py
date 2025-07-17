"""Basic API test placeholders."""

from fastapi.testclient import TestClient
from aidgraph.api.main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "AidGraph API"}
