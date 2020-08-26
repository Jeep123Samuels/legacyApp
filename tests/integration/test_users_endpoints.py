
from helpers.status_codes import StatusCodes


def test_return_201_status_with_correct_data_posted(client):
    """Should return 201 return status with correct data posted."""
    # when ... POST is made with correct data
    post_data = {
        'username': 'username',
        'password': 'cGFzc3dvcmQ=',
    }
    response = client.post('/users/', json=post_data)

    # then
    # ... response is created and contains data posted,
    assert response.status_code == StatusCodes.CREATED
    assert response.get_json()['username'] == str(post_data['username'])


def test_return_200_status_with_bulk_get_request(client):
    """Should return 200 return status with bulk get request."""
    # given ... two users are created.
    post_data_1 = {
        'username': 'username',
        'password': 'cGFzc3dvcmQ=',
    }
    client.post('/users/', json=post_data_1)
    post_data_2 = {
        'username': 'username1',
        'password': 'cGFzc3dvcmQ1=',
    }
    client.post('/users/', json=post_data_2)

    # when ... get request is made
    response = client.get('/users/')

    # then ...
    # ... response is created and contains data posted,
    results = response.get_json()['results']
    assert response.status_code == StatusCodes.OK
    assert len(results) == 2
    assert results[0]['username'] == str(post_data_1['username'])
    assert results[1]['username'] == str(post_data_2['username'])


def test_return_200_status_with_single_get_request(client):
    """Should return 200 return status with single get request."""
    # given ... two users are created.

    post_data = {
        'username': 'username123',
        'password': 'cGFzc3dvcmQ=',
    }
    user_created = client.post('/users/', json=post_data)
    user_created = user_created.get_json()
    # when ... get request is made
    response = client.get(f'/users/{user_created["id"]}/')

    # then ...
    # ... response is created and contains data posted,
    results = response.get_json()
    assert response.status_code == StatusCodes.OK
    assert results['username'] == str(post_data['username'])
