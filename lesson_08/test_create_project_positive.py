import requests

base_url = "https://ru.yougile.com/api-v2"


def test_create_project_positive():
    # Заполнить данные для авторизации
    login = "your login"
    password = "your password"
    company_id = "your company ID"

    auth_body = {
        "login": login,
        "password": password,
        "companyId": company_id
        }

    auth_response = requests.post(
        base_url + "/auth/keys",
        json=auth_body
    )
    assert auth_response.status_code == 201

    token = auth_response.json()["key"]

    project_body = {
        "title": "New project1"
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(
        base_url + "/projects",
        json=project_body,
        headers=headers
    )

    assert response.status_code == 201, response.text

    body = response.json()
    assert "id" in body
