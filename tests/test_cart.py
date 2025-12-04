from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.login_page import LoginPage
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_cart(driver):
    # --- Instanciar la página de login ---
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    
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
    driver.save_screenshot("reports/saucedemo_cart.png")
    print("📸 Screenshot del carrito guardado correctamente.")    