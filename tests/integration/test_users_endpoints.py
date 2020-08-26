
import pytest

from app import db
from models import Users


@pytest.fixture
def test_user_data() -> dict:
    return dict(
        username="username",
        password="5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
    )


def test_return_201_status_with_correct_data_posted(client, test_user_data):
    """Should return 201 return status with correct data posted."""
    # when ... POST is made with correct data
    response = client.post('/users/', json=test_user_data)

    # then
    # ... response is created and contains data posted,
    assert response.status_code == 201
    assert response.get_json()['username'] == str(test_user_data['username'])


def test_return_200_status_with_get_request(client, test_user_data):
    """Should return 200 return status get request."""
    # when ... GET is made
    user = db.session.query(Users).filter_by(username=test_user_data['username']).first()
    response = client.get(f'/users/')

    # then
    # ... response contains user data,
    results = response.get_json()['results'][0]
    assert response.status_code == 200
    assert results['username'] == str(test_user_data['username'])


def test_return_200_status_with_single_get_request(client, test_user_data):
    """Should return 200 return status single get request."""
    # when ... GET is made
    user = db.session.query(Users).filter_by(username=test_user_data['username']).first()
    response = client.get(f'/users/?id{user.id}')

    # then
    # ... response contains user data,
    results = response.get_json()['results'][0]
    assert response.status_code == 200
    assert results['username'] == str(test_user_data['username'])

