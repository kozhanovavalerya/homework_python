from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_backpack(self):
        self.driver.find_element(*self.BACKPACK).click()

    def add_tshirt(self):
        self.driver.find_element(*self.TSHIRT).click()

    def add_onesie(self):
        self.driver.find_element(*self.ONESIE).click()

    def open_cart(self):
        self.driver.find_element(*self.CART).click()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("cart.html"))
