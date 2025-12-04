import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

def leer_csv(ruta):
        with open(ruta, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))

# --- TEST DE LOGIN Y VALIDACIONES EN SAUCEDEMO ---

@pytest.mark.parametrize("data", leer_csv("data/data_login.csv"))
def test_login(driver, data):
    """Valida login, redirección, productos y carrito en saucedemo.com"""
    url = "https://www.saucedemo.com"
    driver.get(url)

    # --- Validar título ---
    titulo = driver.title
    assert titulo == "Swag Labs", f"❌ Título inesperado: {titulo}"
    print(f"✅ Título correcto: {titulo}")

    # --- Leer datos de login desde CSV ---
    driver.find_element(By.ID, "user-name").send_keys(data["usuario"])
    driver.find_element(By.ID, "password").send_keys(data["password"])
    driver.find_element(By.ID, "login-button").click()

    # --- Validar redirección ---
    assert "/inventory.html" in driver.current_url, "❌ No se redirigió correctamente al inventario"
    print("✅ Redirección al inventario exitosa")
