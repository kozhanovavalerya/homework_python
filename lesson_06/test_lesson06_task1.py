from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_btn = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_btn.click()

    wait.until(EC.text_to_be_present_in_element(
        (By.XPATH, "//h4[text()='Hello World!']"), "Hello World!"))
    driver.save_screenshot("hello_world.png")
    message_element = driver.find_element(
        By.XPATH, "//h4[text()='Hello World!']")
    assert message_element.text == "Hello World!"

    driver.quit()
