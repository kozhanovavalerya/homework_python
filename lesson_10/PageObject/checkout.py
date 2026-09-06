from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    TOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Ввод имени пользователя {first_name}")
    def input_first_name(self, first_name):
        """
        Вводит имя пользователя.
        :param first_name: str — имя пользователя.
        """
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)

    @allure.step("Ввод фамилии пользователя {last_name}")
    def input_last_name(self, last_name):
        """
        Вводит имя пользователя.
        :param last_name: str — фамилия пользователя.
        """
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)

    @allure.step("Ввод почтового кода {postal_code}")
    def input_postal_code(self, postal_code):
        """
        Вводит почтовый индекс.
        :param posta_code: str — почтовый индекса.
                """
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    @allure.step("Нажатие кнопки Continue")
    def click_continue(self):
        """Нажимает кнопку Continue.
        """
        self.driver.find_element(*self.CONTINUE).click()
        WebDriverWait(self.driver, 10).until(
                    EC.url_contains("checkout-step-two.html"))

    @allure.step("Получение итоговой суммы заказа")
    def get_total(self):
        """Возвращает итоговую сумму заказа.
        """
        return self.driver.find_element(*self.TOTAL).text
