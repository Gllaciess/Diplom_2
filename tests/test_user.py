import allure
import pytest
import requests
from helpers.helpers import generate_random_user


@allure.feature('Создание пользователя')
class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self):
        user = generate_random_user()
        response = requests.post('https://stellarburgers.education-services.ru/api/auth/register', data=user)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_existing_user(self, create_user):
        user = create_user
        response = requests.post('https://stellarburgers.education-services.ru/api/auth/register', data=user)
        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'

    @allure.title('Создание пользователя без обязательного поля')
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_create_user_missing_field(self, field):
        user = generate_random_user()
        del user[field]
        response = requests.post('https://stellarburgers.education-services.ru/api/auth/register', data=user)
        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'


