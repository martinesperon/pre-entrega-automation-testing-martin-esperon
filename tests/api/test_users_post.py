import requests

def test_create_user(api_base):
    """POST - Crear usuario"""
    url = f"{api_base}/users"

    body = {
        "name": "martin",
        "job": "tester"
    }

    response = requests.post(url, json=body)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "martin"
    assert data["job"] == "tester"
    assert "id" in data
    assert "createdAt" in data

    print(f"✅ Usuario creado correctamente con ID: {data['id']}")
