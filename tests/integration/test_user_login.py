
import pytest
from helpers.status_codes import StatusCodes


@pytest.fixture
def test_user_data() -> dict:
    return {
        'username': 'username',
        'password': 'cGFzc3dvcmQ=',
    }


def test_return_200_status_with_correct_login_data_posted(client, test_user_data):
    """Should return 200 return status with correct data posted."""

    _ = client.post('/users/', json=test_user_data)

    # when ... POST is made with correct data
    response = client.post('/knock/on/door/', json=test_user_data)

    # then
    # ... response is OK
    response_json = response.json
    assert 'refresh_token' in response_json['results']
    assert 'token' in response_json['results']
    assert response.status_code == StatusCodes.OK


def test_return_400_status_with_incorrect_login_data_posted(client, test_user_data):
    """Should return 400 return status with incorrect data posted."""

    _ = client.post('/users/', json=test_user_data)

    test_user_data["password"] = "cGFzc3dvcmQx"
    # when ... POST is made with incorrect data
    response = client.post('/knock/on/door/', json=test_user_data)

    # then
    # ... response Bad Request.
    assert response.status_code == StatusCodes.BAD_REQUEST
