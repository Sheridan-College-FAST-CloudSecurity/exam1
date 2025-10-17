import pytest
from src.app import app  # ensure __init__.py exists in src/


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_hello_with_name(client):
    response = client.get("/hello?name=Alice")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Alice"}


def test_hello_default(client):
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World"}
