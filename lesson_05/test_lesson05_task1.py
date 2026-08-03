from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")
    sleep(2)

    driver.find_element(By.LINK_TEXT, value="HTML Form").click()
    assert "forms/post" in driver.current_url
    driver.back()
    assert "httpbin.qa-territory.online" in driver.current_url

    driver.quit()
