import requests

base_url = "https://ru.yougile.com/api-v2"


def test_get_project_by_id_positive():
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

    headers = {
        "Authorization": f"Bearer {token}"
    }

    project_response = requests.get(
        base_url + "/projects",
        headers=headers
    )

    project_id = project_response.json()["content"][0]["id"]

    response = requests.get(
        base_url + f"/projects/{project_id}",
        headers=headers
    )

    assert response.status_code == 200

    project = response.json()

    assert project["id"] == project_id
    assert "title" in project
    assert "timestamp" in project
