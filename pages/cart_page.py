from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    URL = "https://www.saucedemo.com/cart.html"

    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _CHECKOUT_BUTTON = (By.ID, "checkout")
    _REMOVE_BUTTON = (By.CSS_SELECTOR, ".cart_item .cart_button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_page(self):
        """Espera que cargue la página del carrito."""
        self.wait.until(EC.visibility_of_element_located(self._CHECKOUT_BUTTON))

    def get_items_count(self):
        """Devuelve la cantidad de productos en el carrito."""
        items = self.driver.find_elements(*self._CART_ITEMS)
        return len(items)

    def remove_first_item(self):
        """Elimina el primer ítem del carrito."""
        remove_btn = self.wait.until(EC.element_to_be_clickable(self._REMOVE_BUTTON))
        remove_btn.click()

    def proceed_to_checkout(self):
        """Click en Checkout."""
        self.wait.until(EC.element_to_be_clickable(self._CHECKOUT_BUTTON)).click()
