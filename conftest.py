import pytest
import requests
from helpers.helpers import generate_random_user
from constants import Urls


@pytest.fixture
def create_user():
    user_data = generate_random_user()
    response = requests.post(Urls.REGISTER, data=user_data)
    token = response.json().get('accessToken')

    yield user_data

    if token:
        requests.delete(Urls.USER, headers={'Authorization': token})


@pytest.fixture
def delete_user_after_test():
    "Фикстура для удаления пользователя после теста (без условий)"
    users_to_delete = []

    def _add_user(email, password):
        users_to_delete.append((email, password))

    yield _add_user

    for email, password in users_to_delete:
        login_response = requests.post(Urls.LOGIN, data={
            'email': email,
            'password': password
        })
        token = login_response.json().get('accessToken')
        if token:
            requests.delete(Urls.USER, headers={'Authorization': token})

            

