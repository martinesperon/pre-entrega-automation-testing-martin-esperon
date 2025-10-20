import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# --- CONFIGURACIÓN DEL DRIVER ---
@pytest.fixture
def driver():
    """Configura el navegador antes del test y lo cierra al finalizar."""
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# --- TEST DE LOGIN Y VALIDACIONES EN SAUCEDEMO ---
def test_login_and_cart(driver):
    """Valida login, redirección, productos y carrito en saucedemo.com"""
    url = "https://www.saucedemo.com"
    driver.get(url)

    # --- Validar título ---
    titulo = driver.title
    assert titulo == "Swag Labs", f"❌ Título inesperado: {titulo}"
    print(f"✅ Título correcto: {titulo}")

    # --- Login ---
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # --- Validar redirección ---
    assert "/inventory.html" in driver.current_url, "❌ No se redirigió correctamente al inventario"
    print("✅ Redirección al inventario exitosa")

    # --- Validar título visible de la página ---
    titulo_pagina = driver.find_element(By.CSS_SELECTOR, ".title").text
    assert titulo_pagina == "Products", f"❌ Título visible incorrecto: {titulo_pagina}"
    print(f"✅ Título visible correcto: {titulo_pagina}")

    # --- Validar primer producto ---
    primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    assert primer_producto == "Sauce Labs Backpack", f"❌ Producto inesperado: {primer_producto}"
    assert precio_primer_producto == "$29.99", f"❌ Precio inesperado: {precio_primer_producto}"
    print(f"✅ Producto validado: {primer_producto} | Precio: {precio_primer_producto}")

    # --- Añadir producto al carrito ---
    primer_item = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    primer_item.find_element(By.TAG_NAME, "button").click()

    cantidad_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cantidad_carrito == "1", f"❌ El carrito debería tener 1 ítem, tiene {cantidad_carrito}"
    print("✅ Producto añadido al carrito")

    # --- Ir al carrito ---
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # --- Screenshot final ---
    driver.save_screenshot("reports/saucedemo_carrito.png")
    print("📸 Screenshot del carrito guardado correctamente.")
