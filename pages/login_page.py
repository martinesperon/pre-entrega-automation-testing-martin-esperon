from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Clase que representa la página de login de saucedemo.com ---
class LoginPage:

    URL = "https://www.saucedemo.com"

    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def load(self):
        """Carga la página de login."""
        self.driver.get(self.URL)  
    
    def login(self, username, password):
        """Realiza el login con las credenciales proporcionadas."""
        self.wait.until(EC.visibility_of_element_located(self._USERNAME_INPUT)).send_keys(username)
        self.driver.find_element(*self._PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self._LOGIN_BUTTON).click()                    