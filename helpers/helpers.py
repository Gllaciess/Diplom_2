import random
import string


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_user():
    return {
        "email": f"{generate_random_string(8)}@test.com",
        "password": generate_random_string(8),
        "name": generate_random_string(6)
    }


