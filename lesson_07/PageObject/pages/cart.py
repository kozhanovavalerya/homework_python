from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    CHECKOUT = (By.ID, "checkout")
    INVENTORY_ITEM_NAME = (
        By.CSS_SELECTOR, '[data-test="inventory-item-name"]')

    def __init__(self, driver):
        self.driver = driver

    def cart_items(self):
        items = self.driver.find_elements(*self.INVENTORY_ITEM_NAME)
        return [item.text for item in items]

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT).click()
        WebDriverWait(self.driver, 10).until(
                    EC.url_contains("checkout-step-one.html"))
