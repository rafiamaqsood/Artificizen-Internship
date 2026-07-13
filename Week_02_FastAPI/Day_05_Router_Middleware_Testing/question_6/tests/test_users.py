from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():

    response = client.post(
        "/users",
        json={
            "name": "Rafia",
            "email": "rafia@gmail.com"
        }
    )

    assert response.status_code == 201
    assert response.json()["message"] == "User created successfully"

def test_duplicate_email():

    client.post(
        "/users",
        json={
            "name": "Sawera",
            "email": "sawera@gamil.com"
        }
    )

    response = client.post(
        "/users",
        json={
            "name": "Muniba",
            "email": "sawera@gamil.com"
        }
    )

    assert response.status_code == 409
    assert response.json()["detail"] == "Email already exists"

def test_profile_without_token():
    response = client.get("/profile")

    assert response.status_code == 401
    assert response.json()["detail"] == "Unauthorized"