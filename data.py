from generators import *


class Data:
    @staticmethod
    def generate_user_data(email=True, password=True, name=True):
        data = {}
        if email:
            data["email"] = generate_user_email()
        if password:
            data["password"] = generate_user_password()
        if name:
            data["name"] = generate_user_username()
        return data

    REQUIRED_FIELDS = ["success", "accessToken", "refreshToken", "user"]
    REQUIRED_FIELDS_USER = ["email", "name"]

