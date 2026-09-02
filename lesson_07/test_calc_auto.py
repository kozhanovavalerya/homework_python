from selenium import webdriver
from PageObject.pages.calc_page import CalcPage


def test_calc():
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

    assert calculator.get_result() == "15"

    driver.quit()
