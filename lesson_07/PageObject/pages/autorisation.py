from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGINBUTTON = (By.ID, "login-button")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_page(self):
        self.driver.get(self.url)

    def input_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGINBUTTON).click()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("inventory.html"))
