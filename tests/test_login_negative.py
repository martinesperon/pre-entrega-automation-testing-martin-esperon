import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_negative(driver):
    driver.get("https://www.saucedemo.com")

    wait = WebDriverWait(driver, 10)

    # Esperar a que aparezca el campo username
    username_input = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    password_input = driver.find_element(By.ID, "password")

    # Datos inválidos
    username_input.send_keys("wrong_user")
    password_input.send_keys("wrong_pass")

    driver.find_element(By.ID, "login-button").click()

    # Esperar mensaje de error
    error_msg = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".error-message-container")
        )
    ).text

    assert "epic sadface" in error_msg.lower()
    print("✅ Mensaje de error mostrado correctamente para login inválido.")