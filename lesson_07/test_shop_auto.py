from selenium import webdriver
from PageObject.pages.autorisation import LoginPage
from PageObject.pages.main import MainPage
from PageObject.pages.cart import CartPage
from PageObject.pages.checkout import CheckoutPage


def test_shop():
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {"profile.password_manager_leak_detection": False}
    )
    driver = webdriver.Chrome(options=options)

    login_page = LoginPage(driver, " https://www.saucedemo.com/")
    login_page.open_page()
    login_page.input_username("standard_user")
    login_page.input_password("secret_sauce")
    login_page.click_login()

    main_page = MainPage(driver)
    main_page.add_backpack()
    main_page.add_tshirt()
    main_page.add_onesie()

    main_page.open_cart()

    cart_page = CartPage(driver)
    cart_items = cart_page.cart_items()
    assert cart_items == [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)

    checkout_page.input_first_name("Valerya")
    checkout_page.input_last_name("K")
    checkout_page.input_postal_code("193000")
    checkout_page.click_continue()

    total = checkout_page.get_total()
    assert total == "Total: $58.29"

    driver.quit()
