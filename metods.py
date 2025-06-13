import requests
from urls import Url


class Metods:
    @staticmethod
    def create_user (data):
        return requests.post(f'{Url.BASE_URL}{Url.CREATE_USER}', data=data)

    @staticmethod
    def delete_user(data):
        return requests.delete(f'{Url.BASE_URL}{Url.CHANGING_USER}', headers=data)

    @staticmethod
    def auth_user(data):
        return requests.post(f'{Url.BASE_URL}{Url.AUTH_USER}', data=data)

    @staticmethod
    def create_order(headers=None, data=None):
     return requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDERS}', headers=headers, data=data)

    @staticmethod
    def get_ingredients():
        return requests.get (f'{Url.BASE_URL}{Url.GET_INDREDIENTS}')






