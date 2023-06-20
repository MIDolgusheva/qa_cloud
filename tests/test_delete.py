import pytest
import allure
from test_lib.assertions import Assertions

test_data_with_correct_params = [1, 50, 100]


@allure.feature("Delete a certain post")
@allure.description("This test checks the response to the DELETE requests with the correct path parameter")
@pytest.mark.parametrize("parameter", test_data_with_correct_params,
                         ids=["id_1", "id_50", "id_100"])
def test_get_post_with_correct_params(api_client, parameter):
    response = api_client.delete(f'/posts/{parameter}')
    Assertions.assert_status_code(response, 200)
    Assertions.assert_response_has_empty_body(response)


# Этот endpoint возращает код 200, даже если удаляемого поста не существует
test_data_with_incorrect_path_params = [-1, 0, 'a', 101]


@allure.feature("Delete a certain post")
@allure.description("This test checks the response to the DELETE requests with the incorrect id parameter")
@pytest.mark.parametrize("parameter", test_data_with_incorrect_path_params,
                         ids=["id_-1", "id_0", "id_a", "id_101"])
def test_get_post_with_incorrect_params(api_client, parameter):
    response = api_client.delete(f'/posts/{parameter}')
    Assertions.assert_status_code(response, 200)
    Assertions.assert_response_has_empty_body(response)
