from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html"))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    WebDriverWait(driver, 10).until(
            EC.url_contains("cart.html"))

    driver.find_element(By.ID, "checkout").click()

    WebDriverWait(driver, 10).until(
                EC.url_contains("checkout-step-one.html"))

    driver.find_element(By.ID, "first-name").send_keys("Valeria")
    driver.find_element(By.ID, "last-name").send_keys("Kozhanova")
    driver.find_element(By.ID, "postal-code").send_keys("193000")

    driver.find_element(By.ID, "continue").click()

    WebDriverWait(driver, 10).until(
                    EC.url_contains("checkout-step-two.html"))

    total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text

    assert total == "Total: $58.29"

    driver.quit()
