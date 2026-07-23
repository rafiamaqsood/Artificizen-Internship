from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_sources():
    response = client.post(
        "/chat",
        json={
            "session_id": "test-session",
            "query": "What is this document about?"
        }
    )

    assert response.status_code == 200
    assert response.json()["sources"] != ""