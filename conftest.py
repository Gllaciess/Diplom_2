import pytest
import requests
from helpers.helpers import generate_random_user


@pytest.fixture
def create_user():
    user_data = generate_random_user()
    response = requests.post('https://stellarburgers.education-services.ru/api/auth/register', data=user_data)
    yield user_data
    if response.status_code == 200:
        token = response.json().get('accessToken')
        if token:
            requests.delete('https://stellarburgers.education-services.ru/api/auth/user', headers={'Authorization': token})

            

