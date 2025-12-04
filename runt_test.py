import pytest
import os

def test_files():
    # Lista de archivos de prueba a ejecutar
    test_files = [
        "tests/test_title.py",
        "tests/test_login.py",
        "tests/test_shopping_cart.py",
    ]

    # Argumentos para ejecutar pytest con los archivos de prueba especificados
    pytest_args = test_files + [
        "-v",
        "--html=reports/report.html",
        "--self-contained-html"
    ]

    # Ejecutar pytest con los argumentos proporcionados
    pytest.main(pytest_args)

if __name__ == "__main__":
    test_files()
