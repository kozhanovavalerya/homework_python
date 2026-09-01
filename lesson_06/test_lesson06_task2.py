from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get(" https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "NTYxMGU2Y2ItOWU1Zi00OWNhLTk1NmItM2RiOTUyMTE1ZjM3"
    })
    driver.refresh()

    driver.get("https://gitflic.ru/user/test01")
    url_user1 = driver.current_url

    driver.delete_all_cookies()

    driver.add_cookie({
        "name": "SESSION",
        "value": "M2RhMjUzOWItNjQ2Mi00OWQzLWJhNmEtMWI0YWRhZDRkYWYw"})
    driver.refresh()

    driver.get("https://gitflic.ru/user/test02")
    url_user2 = driver.current_url

    assert url_user1 != url_user2

    driver.quit()
