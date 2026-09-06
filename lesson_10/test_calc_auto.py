from selenium import webdriver
from PageObject.calc_page import CalcPage
import allure


@allure.title("Тестирование калькулятора: 7+8=15")
@allure.description(
    "Тест проверяет корректность работы калькулятора на примере")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc():
    """
    Тест проверяет работу калькулятора на примере сложения 7+8.
    Ожидаемый результат: 15.
    """
    driver = webdriver.Chrome()

    calculator = CalcPage(
        driver,
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calculator.open()
    calculator.input_delay("45")
    calculator.click_7()
    calculator.click_plus()
    calculator.click_8()
    calculator.click_equals()

    calculator.wait_for_result()

    with allure.step("Проверка результата"):
        assert calculator.get_result() == "15"
        """Проверяет, что полученный результат равен 15"""

    driver.quit()
