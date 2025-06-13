import pytest
from data import Data
from metods import Metods
import allure


@pytest.fixture
def create_and_delete_user():
    with allure.step('Создать пользователя'):
        user_data = Data.generate_user_data()
        create_user = Metods.create_user(user_data)
        access_token = create_user.json()["accessToken"]
    yield {
        "user_data": user_data,
        "create_user": create_user,
        "access_token": access_token
    }
    with allure.step('Удалить пользователя'):
        headers = {"Authorization": access_token}
        Metods.delete_user(headers)



@pytest.fixture
def auth_user(create_and_delete_user):
    user_data = create_and_delete_user["user_data"]
    with allure.step('Авторизовать пользователя'):
        credentials = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        response = Metods.auth_user(credentials)
    return {
        "auth_response": response,
        "access_token": response.json()["accessToken"]
    }


