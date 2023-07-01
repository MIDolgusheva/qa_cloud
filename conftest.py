import pytest
import requests
import allure


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def get(self, path="/", params=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'GET request to: {url}'):
            return requests.get(url=url, params=params, headers=headers)

    def post(self, path="/", data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'POST request to: {url}'):
            return requests.post(url=url, data=data, json=None, headers=headers)

    def delete(self, path="/", headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'DELETE request to: {url}'):
            return requests.delete(url=url, headers=headers)


@pytest.fixture(scope="session")
def api_client():
    return ApiClient(base_address="https://jsonplaceholder.typicode.com")
