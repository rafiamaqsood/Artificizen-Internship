from fastapi.testclient import TestClient
from app.main import app

def get_token(client):
    response = client.post(
        "/auth/login",
        json={
            "email": "rafia@test.com",
            "password": "123456"
        }
    )

    return response.json()["access_token"]

def test_create_task(test_client):
    token = get_token(test_client)

    response = test_client.post(
        "/tasks/",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "title": "Assignment",
            "description": "Finish FastAPI project"
        }
    )

    assert response.status_code == 201

def test_get_tasks(test_client):
    token = get_token(test_client)

    response = test_client.get(
        "/tasks/",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

def test_unauthorized():
    client = TestClient(app)

    response = client.get("/tasks/")

    assert response.status_code == 401