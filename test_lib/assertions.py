import jsonschema
import requests
import allure
from requests import Response

class Assertions():

    @staticmethod
    def assert_status_code(response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"

    @staticmethod
    def assert_json_validity(response):
        try:
            response.json()
        except requests.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

    @staticmethod
    def assert_response_has_empty_body(response):
        assert response.text == "[]" or response.text == "{}", f"Response has object(s). " \
                                                                   f"Response text is '{response.text}'"

    @staticmethod
    def assert_response_has_required_fields(response, fields):
        missing_fields = [field for field in fields if response.get(field) is None]
        assert not missing_fields, f"Response doesn't have expected fields: {missing_fields}"

    @staticmethod
    def assert_response_does_not_have_unexpected_fields(response, fields):
        unexpected_fields = [key for key in response.keys() if key not in fields]
        assert not unexpected_fields, f"Response has unexpected fields: {unexpected_fields}"

    @staticmethod
    def assert_response_has_field_with_value(response, expected_result):
        for field, value in expected_result.items():
            actual_field_value = response.get(field)
            assert actual_field_value, f'Response does not have expected {field} field'

            with allure.step(f"Expected '{field}' = {value}. Actual '{field}' ={actual_field_value}"):
                assert value == actual_field_value, f""" Expected '{field}' field value don't equal to: {value}. \
                                                Actual '{field}' field value:{actual_field_value} """

    @staticmethod
    def assert_json_schema_for_get(responses):
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer", "minimum": 1, "maximum": 100},
                "userId": {"type": "integer", "minimum": 1, "maximum": 10},
                "title": {"type": "string"},
                "body": {"type": "string"}
            },
            "required": ["id", "userId", "title", "body"]
        }
        responses = responses.json()
        for response in responses:
            try:
                jsonschema.validate(instance=response, schema=schema)
            except jsonschema.exceptions.ValidationError:
                assert False, f"Response is not well-formed JSON. One of responses text is '{response.text}'"


