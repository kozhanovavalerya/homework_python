import requests

base_url = "https://ru.yougile.com/api-v2"


def test_create_project_without_companyId():
    # Заполнить данные для авторизации
    login = "your login"
    password = "your password"

    auth_body = {
        "login": login,
        "password": password,
        }

    auth_response = requests.post(
        base_url + "/auth/keys",
        json=auth_body
    )
    assert auth_response.status_code == 400
