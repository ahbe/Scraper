from fastapi.testclient import TestClient

from scraper import app

client = TestClient(app)



def test_create_item():
    response = client.post(
        "/facebook",
        json={"page":"nintendo","number_pages":1},
    )
    assert response.status_code == 200
    assert type(response.json()) == float
    assert response.json().split()[0] == "done"
