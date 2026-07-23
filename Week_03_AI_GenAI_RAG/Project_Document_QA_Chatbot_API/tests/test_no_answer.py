from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_no_answer():
    response = client.post(
        "/chat",
        json={
            "session_id": "test-session",
            "query": "Who won the FIFA World Cup in 1998?"
        }
    )

    assert response.status_code == 200
    assert response.json()["answer"] == "I don't know."