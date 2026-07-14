def test_register(test_client):
    response = test_client.post(
        "/auth/register",
        json={
            "name": "Rafia",
            "email": "rafia@test.com",
            "password": "123456"
        }
    )

    assert response.status_code == 201

def test_login(test_client):
    response = test_client.post(
        "/auth/login",
        json={
            "email": "rafia@test.com",
            "password": "123456"
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert "access_token" in body