import pytest
import allure
from test_lib.assertions import Assertions

# Данный endpoint принимает любые параметры. Нет валидации userId, ожно отправить любое число.
# При отправке userId типа number, с сервера возвращается string,
# однвко согласно документации должно возвращаться number. Будем считать это багом документации.
test_data_with_params = [{"title": "foo", "body": "bar", "userId": "1", "id": 101},
                         {"userId": "1", "id": 101},
                         {"userId": "1", "title": "foo", "id": 101},
                         {"userId": "1", "body": "bar", "id": 101},
                         {"body": "bar", "id": 101},
                         {"body": "bar", "title": "foo", "id": 101},
                         {"title": "foo", "id": 101},
                         {"id": 101},
                         {"random": "random", "fields": "fields"}]


@allure.feature("Create a post")
@allure.description("This test checks the response to the POST request with data")
@pytest.mark.parametrize("data", test_data_with_params)
def test_post_post_by_data(api_client, data):
    response = api_client.post(f'/posts', data=data)
    Assertions.assert_status_code(response, 201)
    Assertions.assert_json_validity(response)
    response = response.json()
    Assertions.assert_response_has_required_fields(response, data)
    Assertions.assert_response_has_field_with_value(response, data)


test_data_with_incorrect_id = [{"id": -1}, {"id": 1}, {"id": 102}, {"id": "string"}]


# Возвращаемый id всегда равен 101, т.к. пользователь не может задать номер поста
@allure.feature("Create a post with incorrect id")
@allure.description("This test checks th response to the POST request with the incorrect id")
@pytest.mark.parametrize("data", test_data_with_incorrect_id)
def test_post_post_by_incorrect_id(api_client, data):
    response = api_client.post(f'/posts', data=data)
    Assertions.assert_status_code(response, 201)
    Assertions.assert_json_validity(response)
    response = response.json()
    Assertions.assert_response_has_required_fields(response, data)
    Assertions.assert_response_has_field_with_value(response, {"id": 101})
