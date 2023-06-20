import allure
import pytest
from test_lib.assertions import Assertions


@allure.feature("Get all 100 posts")
@allure.description("This test checks the response with 100 posts to the GET request")
def test_get_all_posts(api_client):
    responses = api_client.get(f'/posts')
    Assertions.assert_status_code(responses, 200)
    Assertions.assert_json_validity(responses)
    Assertions.assert_json_schema_for_get(responses)


test_data_with_correct_params = [{"id": 1}, {"id": 50}, {"id": 100},
                                 {"userId": 1}, {"userId": 5}, {"userId": 10},
                                 {"userId": 10, "id": 100}]


@allure.feature("Get a certain post")
@allure.description("This test checks the response to the GET request with the correct query parameters")
@pytest.mark.parametrize("parameter", test_data_with_correct_params)
def test_get_post_with_correct_params(api_client, parameter):
    response = api_client.get(f'/posts', params=parameter)
    Assertions.assert_status_code(response, 200)
    Assertions.assert_json_validity(response)

    response = response.json()
    Assertions.assert_response_has_required_fields(response[0], ["userId", "id", "title", "body"])
    Assertions.assert_response_does_not_have_unexpected_fields(response[0], ["userId", "id", "title", "body"])
    Assertions.assert_response_has_field_with_value(response[0], parameter)


test_data_with_incorrect_params = [{"id": -1}, {"id": 0}, {"id": 'a'}, {"id": 101},
                                   {"userId": -1}, {"userId": 0}, {"userId": 'a'}, {"userId": 11},
                                   {"id": -1, "userId": -1}, {"id": 1, "userId": -1}, {"id": -1, "userId": 1}]


@allure.feature("Unable to get a certain post")
@allure.description("This test checks the response to the GET request with the incorrect query parameters")
@pytest.mark.parametrize("parameter", test_data_with_incorrect_params,
                         ids=["id_-1", "id_0", "id_'a'", "id_101", "userId_-1", "userId_0", "userId_'a'",
                              "userId_11", "both_incorrect", "first_correct-second_incorrect",
                              "second_correct-first_incorrect"])
def test_get_post_with_incorrect_params(api_client, parameter):
    response = api_client.get(f'/posts', params=parameter)
    Assertions.assert_status_code(response, 200)
    Assertions.assert_response_has_empty_body(response)


test_data_with_correct_path_params = [1, 50, 100]


@allure.feature("Get a certain post")
@allure.description("This test checks the response to the GET request with the correct path parameter")
@pytest.mark.parametrize("parameter", test_data_with_correct_path_params,
                         ids=["id_1", "id_50", "id_100"])
def test_get_post_with_correct_path_params(api_client, parameter):
    response = api_client.get(f'/posts/{parameter}')
    Assertions.assert_status_code(response, 200)
    Assertions.assert_json_validity(response)

    response = response.json()
    Assertions.assert_response_has_required_fields(response, ['id', 'userId', 'title', 'body'])
    Assertions.assert_response_does_not_have_unexpected_fields(response, ['id', 'userId', 'title', 'body'])
    Assertions.assert_response_has_field_with_value(response, {"id": parameter})


test_data_with_incorrect_path_params = [-1, 0, 'a', 101]


@allure.feature("Unable to get a certain post")
@allure.description("This test checks the response to the GET request with the incorrect path parameter")
@pytest.mark.parametrize("parameter", test_data_with_incorrect_path_params,
                         ids=["id_-1", "id_0", "id_'a'", "id_101"])
def test_get_post_with_incorrect_path_params(api_client, parameter):
    response = api_client.get(f'/posts/{parameter}')
    Assertions.assert_status_code(response, 404)
    Assertions.assert_response_has_empty_body(response)
