from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    sleep(2)

    driver.find_element(By.NAME, value="custname").send_keys(
        "Valeria")
    driver.find_element(
        By.XPATH, value="//button[contains(., 'Submit')]").click()
    assert "httpbin.qa-territory.online/post" in driver.current_url
