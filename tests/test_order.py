import allure
import requests
from helpers.helpers import generate_random_user
from constants import Urls
from data import Ingredients


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.step("Создать заказ с ингредиентами: {ingredients}")
    def create_order(self, ingredients, token=None):
        headers = {'Authorization': token} if token else {}
        return requests.post(Urls.ORDERS, json={"ingredients": ingredients}, headers=headers)

    @allure.step("Зарегистрировать пользователя и получить токен")
    def register_and_get_token(self, user):
        register = requests.post(Urls.REGISTER, data=user)
        return register.json()['accessToken']

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_auth(self, delete_user_after_test):
        user = generate_random_user()

        with allure.step(f"Регистрация пользователя {user['email']}"):
            token = self.register_and_get_token(user)

        delete_user_after_test(user['email'], user['password'])

        with allure.step("Создание заказа с авторизацией"):
            response = self.create_order(Ingredients.VALID_INGREDIENTS, token)

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_auth(self):
        with allure.step("Создание заказа без авторизации"):
            response = self.create_order(Ingredients.VALID_INGREDIENTS)

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Создание заказа с ингредиентами')
    def test_create_order_with_ingredients(self):
        with allure.step("Создание заказа с одним ингредиентом"):
            response = self.create_order(Ingredients.SINGLE_INGREDIENT)

        assert response.status_code == 200
        assert 'order' in response.json()

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self):
        with allure.step("Создание заказа без ингредиентов"):
            response = self.create_order(Ingredients.EMPTY_INGREDIENTS)

        assert response.status_code == 400
        assert response.json()['message'] == 'Ingredient ids must be provided'

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_invalid_ingredients(self):
        with allure.step("Создание заказа с неверным хешем ингредиентов"):
            response = self.create_order(Ingredients.INVALID_HASH)

        assert response.status_code == 400


