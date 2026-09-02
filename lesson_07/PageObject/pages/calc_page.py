from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def input_delay(self, delay):
        self.driver.find_element(*self.DELAY_INPUT).clear()
        self.driver.find_element(*self.DELAY_INPUT).send_keys(delay)

    def click_7(self):
        self.driver.find_element(*self.BUTTON_7).click()

    def click_plus(self):
        self.driver.find_element(*self.BUTTON_PLUS).click()

    def click_8(self):
        self.driver.find_element(*self.BUTTON_8).click()

    def click_equals(self):
        self.driver.find_element(*self.BUTTON_EQUALS).click()

    def wait_for_result(self):
        WebDriverWait(self.driver, 55).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"))

    def get_result(self):
        return self.driver.find_element(*self.RESULT).text
