from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGINBUTTON = (By.ID, "login-button")

    def __init__(self, driver, url):
        """
        Конструктор класса LoginPage.

        :param driver: WebDriver — объект драйвера Selenium.
        :param url: str - адрес страницы
        """
        self.driver = driver
        self.url = url

    @allure.step("Открытие страницы магазина")
    def open_page(self):
        """
        Открывает страницу магазина.
        """
        self.driver.get(self.url)

    @allure.step("Ввод имени пользователя {username}")
    def input_username(self, username):
        """
        Вводит имя пользователя.
        :param username: str - имя пользователя.
        """
        self.driver.find_element(*self.USERNAME).send_keys(username)

    @allure.step("Ввод пароля {password}")
    def input_password(self, password):
        """
        Вводит имя пользователя.
        :param password: str - пароль.
        """
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    @allure.step("Нажатие кнопки login")
    def click_login(self):
        """
        Нажимает на кнопку login.
        """
        self.driver.find_element(*self.LOGINBUTTON).click()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("inventory.html"))
