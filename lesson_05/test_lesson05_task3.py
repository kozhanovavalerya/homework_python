from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")
    sleep(2)

    links = driver.find_elements(By.TAG_NAME, value="a")
    assert len(links) == 9
    for link in links:
        assert link.is_displayed()
    assert "1" in links[0].text

    driver.quit()
