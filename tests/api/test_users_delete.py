import requests

def test_user_delete(api_base):
    """DELETE - Eliminar usuario"""
    url = f"{api_base}/users/2"

    response = requests.delete(url)

    # Según ReqRes, DELETE devuelve 204 sin contenido
    assert response.status_code == 204
    assert response.text == ""

    print("✅ Usuario eliminado correctamente.")

