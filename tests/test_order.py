import allure
import pytest
import requests
from helpers.helpers import generate_random_user
from constants import Urls


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_auth(self):
        user = generate_random_user()

        register = requests.post(Urls.REGISTER, data=user)
        token = register.json()['accessToken']

        order_data = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}

        response = requests.post(
            Urls.ORDERS,
            json=order_data,
            headers={'Authorization': token}
        )

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_auth(self):
        order_data = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}

        response = requests.post(Urls.ORDERS, json=order_data)

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Создание заказа с ингредиентами')
    def test_create_order_with_ingredients(self):
        order_data = {"ingredients": ["61c0c5a71d1f82001bdaaa6d"]}

        response = requests.post(Urls.ORDERS, json=order_data)

        assert response.status_code == 200
        assert 'order' in response.json()

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self):
        order_data = {"ingredients": []}

        response = requests.post(Urls.ORDERS, json=order_data)

        assert response.status_code == 400
        assert response.json()['message'] == 'Ingredient ids must be provided'

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_invalid_ingredients(self):
        order_data = {"ingredients": ["invalid_hash"]}

        response = requests.post(Urls.ORDERS, json=order_data)

        assert response.status_code == 400


