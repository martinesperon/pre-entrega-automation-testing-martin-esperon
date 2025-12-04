from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    URL = "https://www.saucedemo.com/inventory.html"

    # Selectores
    _ITEM_ADD_BUTTON = (By.CSS_SELECTOR, ".inventory_item button")   # Agregar al carrito
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_page(self):
        """Espera a que cargue el inventario."""
        self.wait.until(EC.visibility_of_element_located(self._CART_BUTTON))

    def add_first_item_to_cart(self):
        """Agrega el primer producto de la lista al carrito."""
        first_add_btn = self.wait.until(EC.element_to_be_clickable(self._ITEM_ADD_BUTTON))
        first_add_btn.click()

    def get_cart_count(self):
        """Devuelve la cantidad de ítems en el carrito."""
        try:
            badge = self.wait.until(EC.visibility_of_element_located(self._CART_BADGE))
            return int(badge.text)
        except:
            return 0

    def go_to_cart(self):
        """Navega a la página del carrito."""
        self.wait.until(EC.element_to_be_clickable(self._CART_BUTTON)).click()
