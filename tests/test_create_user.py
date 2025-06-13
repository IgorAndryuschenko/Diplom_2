import allure
import pytest
from conftest import *

class TestCreateUser:

    @allure.title('Успешное создание пользователя')
    def test_create_user_sucsesful_create(self):
        with allure.step('Создать пользователя'):
            create_user = Metods.create_user(Data.generate_user_data())
            assert create_user.status_code == 200 and create_user.json()['success'] == True
            for field in Data.REQUIRED_FIELDS:
                assert field in create_user.json()
            for user in Data.REQUIRED_FIELDS_USER:
                assert user in create_user.json()['user']


    @allure.title('Ошибка создания пользователя, который уже зарегистрирован')
    def test_create_user_already_registered(self, create_and_delete_user):
        with allure.step('Создать пользователя'):
            data_create_user = create_and_delete_user ["user_data"]
            create_user = create_and_delete_user["create_user"]
            assert create_user.status_code == 200
        with allure.step('Создать пользователя, который уже зарегистрирован '):
            user_already_registered = Metods.create_user(data_create_user)
            assert user_already_registered.status_code == 403
            assert user_already_registered.json()["success"] == False
            assert user_already_registered.json()["message"] == "User already exists"


    @allure.title('Ошибка создание пользователя с отсутствующими полями')
    @pytest.mark.parametrize("select", [
        {"email": False},
        {"password": False},
        {"name": False}
    ])
    def test_create_user_without_a_email(self, select):
        with allure.step(f'Создать пользователя без поля: {list(select.keys())[0]}'):
            data= Data.generate_user_data(**select)
            create_user = Metods.create_user(data)
            assert create_user.status_code == 403
            assert create_user.json()["success"] == False
            assert create_user.json()["message"] == "Email, password and name are required fields"



















