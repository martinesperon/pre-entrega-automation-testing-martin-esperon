import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# --- CONFIGURACIÓN DEL DRIVER ---
@pytest.fixture
def driver():
    """Crea y cierra el navegador de forma controlada."""
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # limpia consola
    service = Service()  # permite personalizar el servicio si es necesario

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver  # devuelve el driver al test
    driver.quit()  # se ejecuta al final del test


# --- TEST PRINCIPAL ---
def test_title(driver):
    """Valida que el título del sitio sea el esperado."""
    url = "https://www.saucedemo.com"
    driver.get(url)

    # --- Validación ---
    titulo = driver.title
    print(f"Título obtenido: {titulo}")
    assert titulo == "Swag Labs", f"❌ El título esperado era 'Swag Labs', pero se obtuvo '{titulo}'"

    # --- Screenshot en caso de éxito ---
    driver.save_screenshot("reports/saucedemo.png")
    print("✅ Screenshot guardado correctamente.")