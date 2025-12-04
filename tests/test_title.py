import pytest
from selenium import webdriver

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
    driver.save_screenshot("reports/saucedemo_title.png")
    print("✅ Screenshot guardado correctamente.")