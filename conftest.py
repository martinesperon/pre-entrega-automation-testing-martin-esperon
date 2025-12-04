import sys
import os

# --- Agregar raiz del proyecto al PYTHONPATH ---
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT)

from pages.login_page import LoginPage
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


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

@pytest.fixture
def login(driver):
    """Abre la página y realiza login con credenciales válidas."""
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    yield driver    
    

@pytest.fixture
def api_base():
    return "https://reqres.in/api"

# --- Screenshots automáticos en caso de fallo ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura un screenshot si un test falla."""
    outcome = yield
    result = outcome.get_result()

    # Solo capturar en la fase de ejecución del test
    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            # Carpeta de reportes
            reports_dir = "reports"
            os.makedirs(reports_dir, exist_ok=True)

            # Path del screenshot
            screenshot_path = os.path.join(reports_dir, f"{item.name}.png")

            # Guardar screenshot
            driver.save_screenshot(screenshot_path)

            # Adjuntar al reporte HTML (si pytest-html está instalado)
            if hasattr(result, "extra"):
                pytest_html = item.config.pluginmanager.getplugin("html")
                if pytest_html:
                    result.extra.append(pytest_html.extras.image(screenshot_path))  