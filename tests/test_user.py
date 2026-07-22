import allure
import pytest
import requests
from helpers.helpers import generate_random_user
from constants import Urls
from data import Users


@allure.feature('Создание пользователя')
class TestCreateUser:

    @allure.step("Отправить запрос на регистрацию пользователя: {user}")
    def register_user(self, user):
        return requests.post(Urls.REGISTER, data=user)

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self, delete_user_after_test):
        user = generate_random_user()

        with allure.step(f"Регистрация нового пользователя {user['email']}"):
            response = self.register_user(user)

        assert response.status_code == 200
        assert response.json()['success'] is True

        delete_user_after_test(user['email'], user['password'])

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_existing_user(self, create_user):
        user = create_user

        with allure.step(f"Попытка повторной регистрации {user['email']}"):
            response = self.register_user(user)

        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'

    @allure.title('Создание пользователя без обязательного поля')
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_create_user_missing_field(self, field, delete_user_after_test):
        user = Users.get_valid_user()
        del user[field]

        with allure.step(f"Регистрация без поля {field}"):
            response = self.register_user(user)

        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'

        if response.status_code == 200 and 'email' in user and 'password' in user:
            delete_user_after_test(user['email'], user['password'])


