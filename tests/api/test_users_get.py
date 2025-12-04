import requests

def test_get_user_success(api_base):
    response = requests.get(f"{api_base}/users/2")

    assert response.status_code == 200
    data = response.json()

    assert "data" in data
    assert data["data"]["id"] == 2
    assert "email" in data["data"]


def test_get_user_not_found(api_base):
    response = requests.get(f"{api_base}/users/9999")

    assert response.status_code == 404
    assert response.json() == {}  # respuesta vacía en ReqRes

    print("✅ Usuario no encontrado como se esperaba.")

