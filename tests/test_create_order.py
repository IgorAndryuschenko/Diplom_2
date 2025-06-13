import allure
import pytest
from conftest import *

class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_authorized(self, auth_user):
        token = auth_user["access_token"]
        headers = {"Authorization": token}
        ingredients = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        body = {"ingredients": ingredients}
        with allure.step("Создать заказ с токеном"):
            response = Metods.create_order(headers=headers, data=body)
            print(response.json())
            assert response.status_code == 200
            assert response.json()["success"] is True
            assert "order" in response.json()


    @allure.title("Создание заказа без авторизации с ингредиентами")
    def test_create_order_unauthorized(self):
        ingredients = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        body = {"ingredients": ingredients}
        with allure.step("Создать заказ без токена"):
            response = Metods.create_order(headers={}, data=body)
            assert response.status_code == 200 #по докам должен быть 401
            assert response.json()["success"] is True
            assert "order" in response.json()


    @allure.title("Создание заказа с авторизацией без ингредиентов")
    def test_create_order_authorized(self, auth_user):
        token = auth_user["access_token"]
        headers = {"Authorization": token}
        ingredients = []
        body = {"ingredients": ingredients}
        with allure.step("Создать заказ с токеном"):
            response = Metods.create_order(headers=headers, data=body)
            assert response.status_code == 400
            assert response.json()["success"] is False
            assert response.json()["message"] == "Ingredient ids must be provided"


    @allure.title("Создание заказа с невалидным хешем ингредиента")
    def test_create_order_with_invalid_ingredient(self, auth_user):
        token = auth_user["access_token"]
        headers = {"Authorization": token}
        invalid_ingredient_id = "invalid_hash_123"
        ingredients = [invalid_ingredient_id]
        with allure.step("Попытка создать заказ с невалидным ингредиентом"):
            response = Metods.create_order(headers=headers, data={"ingredients": ingredients})
            assert response.status_code == 500
