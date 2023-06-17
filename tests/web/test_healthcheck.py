from starlette.testclient import TestClient


def test_healthcheck(client: TestClient) -> None:
    response = client.get("/api/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"is_ok": True}
