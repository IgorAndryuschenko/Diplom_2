import allure
import pytest
from conftest import *

class TestLoginUser:

    @allure.title('Успешный вход под существующим пользователем')
    def test_auth_with_valid_credentials(self, create_and_delete_user):
        user_data = create_and_delete_user["user_data"]
        with allure.step('Вход под существующим пользователем'):
            response = Metods.auth_user({
            "email": user_data["email"],
            "password": user_data["password"]
        })
            assert response.status_code == 200
            for field in Data.REQUIRED_FIELDS:
                assert field in response.json()
            for user in Data.REQUIRED_FIELDS_USER:
                assert user in response.json()['user']


    @allure.title('Ошибка входа с неверным паролем')
    def test_auth_with_wrong_password(self, create_and_delete_user):
        user = create_and_delete_user
        email = user["user_data"]["email"]
        wrong_password = user["user_data"]["password"][::-1]
        with allure.step('Попытка вход под несуществующим пользователем'):
            response = Metods.auth_user({"email": email, "password": wrong_password})
            assert response.status_code == 401
            assert response.json()["success"] is False
            assert response.json()["message"] == "email or password are incorrect"



