import allure
import requests
from helpers.helpers import generate_random_user
from constants import Urls


@allure.feature('Логин пользователя')
class TestLogin:

    @allure.title('Вход под существующим пользователем')
    def test_login_existing_user(self, create_user):
        user = create_user

        response = requests.post(Urls.LOGIN, data={
            'email': user['email'],
            'password': user['password']
        })

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Вход с неверным логином или паролем')
    def test_login_invalid_credentials(self, create_user):
        user = create_user

        response = requests.post(Urls.LOGIN, data={
            'email': user['email'],
            'password': 'wrong_password'
        })

        assert response.status_code == 401
        assert response.json()['message'] == 'email or password are incorrect'


