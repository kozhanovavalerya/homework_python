from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:

    CHECKOUT = (By.ID, "checkout")
    INVENTORY_ITEM_NAME = (
        By.CSS_SELECTOR, '[data-test="inventory-item-name"]')

    def __init__(self, driver):
        """
        Конструктор класса CartPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Получения товаров из корзины")
    def cart_items(self):
        """
        Получает список товаров, добавленных в корзину.
                """
        items = self.driver.find_elements(*self.INVENTORY_ITEM_NAME)
        return [item.text for item in items]

    @allure.step("Нажатие кнопки Checkout")
    def click_checkout(self):
        """Нажимает на кнопку Checkout"""
        self.driver.find_element(*self.CHECKOUT).click()
        WebDriverWait(self.driver, 10).until(
                    EC.url_contains("checkout-step-one.html"))
