from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:

    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, url):
        """
        Конструктор класса CalcPage.

        :param driver: WebDriver — объект драйвера Selenium.
        :param url: str - адрес страницы
        """
        self.driver = driver
        self.url = url

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(self.url)

    @allure.step("Установка задержки {delay} секунд")
    def input_delay(self, delay):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param delay: int — время задержки в секундах.
        """
        self.driver.find_element(*self.DELAY_INPUT).clear()
        self.driver.find_element(*self.DELAY_INPUT).send_keys(delay)

    @allure.step("Нажатие кнопки 7")
    def click_7(self):
        """
        Нажимает на кнопку '7' калькулятора.
        """
        self.driver.find_element(*self.BUTTON_7).click()

    @allure.step("Нажатие кнопки +")
    def click_plus(self):
        """
        Нажимает на кнопку '+' калькулятора.
        """
        self.driver.find_element(*self.BUTTON_PLUS).click()

    @allure.step("Нажатие кнопки 8")
    def click_8(self):
        """
        Нажимает на кнопку '8' калькулятора.
        """
        self.driver.find_element(*self.BUTTON_8).click()

    @allure.step("Нажатие кнопки =")
    def click_equals(self):
        """
        Нажимает на кнопку '=' калькулятора.
        """
        self.driver.find_element(*self.BUTTON_EQUALS).click()

    @allure.step("Ожидание результата 15")
    def wait_for_result(self):
        """
        Ожидает появления результата 15 на экране калькулятора.
        """
        WebDriverWait(self.driver, 55).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"))

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self):
        """
        Возвращает текущий результат с экрана калькулятора.
        """
        return self.driver.find_element(*self.RESULT).text
