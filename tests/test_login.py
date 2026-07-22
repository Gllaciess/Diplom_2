import allure
import requests
from helpers.helpers import generate_random_user
from constants import Urls
from data import Users


@allure.feature('Логин пользователя')
class TestLogin:

    @allure.step("Отправить запрос на логин с данными: {email}")
    def login_user(self, email, password):
        return requests.post(Urls.LOGIN, data={
            'email': email,
            'password': password
        })

    @allure.title('Вход под существующим пользователем')
    def test_login_existing_user(self, create_user):
        user = create_user

        with allure.step(f"Логин пользователя {user['email']}"):
            response = self.login_user(user['email'], user['password'])

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Вход с неверным логином или паролем')
    def test_login_invalid_credentials(self, create_user):
        user = create_user

        with allure.step(f"Попытка логина с неверным паролем для {user['email']}"):
            response = self.login_user(user['email'], Users.INVALID_PASSWORD)

        assert response.status_code == 401
        assert response.json()['message'] == 'email or password are incorrect'


