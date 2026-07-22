class Ingredients:
    BUN = "61c0c5a71d1f82001bdaaa6d"
    SAUCE = "61c0c5a71d1f82001bdaaa6f"

    VALID_INGREDIENTS = [BUN, SAUCE]
    SINGLE_INGREDIENT = [BUN]
    EMPTY_INGREDIENTS = []
    INVALID_HASH = ["invalid_hash"]


class Users:

    VALID_EMAIL = "test@yandex.com"
    VALID_PASSWORD = "123456"
    VALID_NAME = "Nikita"

    INVALID_PASSWORD = "wrong_password"
    NON_EXISTENT_EMAIL = "fawi##^@test.com"

    @staticmethod
    def get_valid_user():
        return {
            "email": Users.VALID_EMAIL,
            "password": Users.VALID_PASSWORD,
            "name": Users.VALID_NAME
        }

    @staticmethod
    def get_invalid_password_user():
        return {
            "email": Users.VALID_EMAIL,
            "password": Users.INVALID_PASSWORD
        }


    