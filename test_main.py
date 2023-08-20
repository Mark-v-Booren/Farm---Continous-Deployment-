import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_cow(client):
    response = client.get("/cow")

    assert response.status_code == 200
    assert response.data == b"MOoooOo!"


def test_rooster(client):
    response = client.get("/rooster")

    assert response.status_code == 200
    assert response.data == b"Kukeleeekuuu! "

def test_rooster(client):
    response = client.get("/mice")

    assert response.status_code == 200
    assert response.data == b"Cheese! "
