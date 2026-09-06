from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:

    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        """
        Конструктор класса MainPage.

        :param driver: WebDriver — объект драйвера Selenium.
                """
        self.driver = driver

    @allure.step("Добавление рюкзака в корзину")
    def add_backpack(self):
        """Добавление рюкзака в корзину.
        """
        self.driver.find_element(*self.BACKPACK).click()

    @allure.step("Добавление футболки в корзину")
    def add_tshirt(self):
        """Добавление футболки в корзину.
        """
        self.driver.find_element(*self.TSHIRT).click()

    @allure.step("Добавление комбинезона в корзину")
    def add_onesie(self):
        """Добавление комбинезона в корзину.
        """
        self.driver.find_element(*self.ONESIE).click()

    @allure.step("Открытие корзины")
    def open_cart(self):
        """Открывает корзину.
        """
        self.driver.find_element(*self.CART).click()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("cart.html"))
