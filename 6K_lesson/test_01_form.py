from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_data_form():
    driver = webdriver.Edge(service=webdriver.EdgeService())
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.NAME, "first-name"))).send_keys(
            "Иван")
    WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.NAME, "last-name"))).send_keys(
                "Петров")
    WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.NAME, "address"))).send_keys(
                    "Ленина, 55-3")
    WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((
                        By.NAME, "zip-code"))).send_keys("")
    WebDriverWait(driver, 3).until(
                        EC.element_to_be_clickable((
                            By.NAME, "city"))).send_keys("Москва")
    WebDriverWait(driver, 3).until(
                        EC.element_to_be_clickable((
                            By.NAME, "country"))).send_keys("Россия")
    WebDriverWait(driver, 3).until(
                        EC.element_to_be_clickable((
                            By.NAME, "e-mail"))).send_keys("test@skypro.com")
    WebDriverWait(driver, 3).until(
                            EC.element_to_be_clickable((
                                By.NAME, "phone"))).send_keys("+7985899998787")
    WebDriverWait(driver, 3).until(
                                EC.element_to_be_clickable((
                                    By.NAME, "job-position"))).send_keys("QA")
    WebDriverWait(driver, 3).until(
                                EC.element_to_be_clickable((
                                    By.NAME, "company"))).send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "zip-code")))

    assert "alert-danger" in driver.find_element(
        By.ID, "zip-code").get_attribute("class")

    fields = ["first-name", "last-name", "address",
              "city", "country", "e-mail", "phone", "job-position", "company"]
    for field in fields:
        assert "alert-success" in driver.find_element(
            By.ID, field).get_attribute("class")
