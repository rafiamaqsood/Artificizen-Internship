from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ingest():
    with open("tests/sample.pdf", "rb") as pdf:
        response = client.post(
            "/ingest",
            files={"file": ("sample.pdf", pdf, "application/pdf")}
        )

    assert response.status_code == 200