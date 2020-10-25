
from helpers.status_codes import StatusCodes


def test_return_200_status_with_bulk_get_request(client, test_token):
    """Should return 200 return status with bulk get request."""
    # given ... two users are created.
    post_data_1 = {
        'username': 'username_test',
        'password': 'cGFzc3dvcmQ=',
    }
    client.post(
        '/users/',
        json=post_data_1,
        headers=dict(knock_knock=test_token['token']),
    )
    post_data_2 = {
        'username': 'username_test1',
        'password': 'cGFzc3dvcmQ1=',
    }
    client.post(
        '/users/',
        json=post_data_2,
        headers=dict(knock_knock=test_token['token']),
    )

    # when ... get request is made
    response = client.get('/users/', headers=dict(knock_knock=test_token['token']))

    # then ...
    # ... response is created and contains data posted,
    results = response.get_json()['results']
    assert response.status_code == StatusCodes.OK
    assert len(results) == 3
    for user_result in results:
        assert user_result['username'] in [
            post_data_1['username'],
            post_data_2['username'],
            'username',
        ]


def test_return_200_status_with_single_get_request(client, test_token):
    """Should return 200 return status with single get request."""
    # given ... two users are created.

    post_data = {
        'username': 'username123',
        'password': 'cGFzc3dvcmQ=',
    }
    user_created = client.post(
        '/users/',
        json=post_data,
        headers=dict(knock_knock=test_token['token']),
    )
    user_created = user_created.get_json()
    # when ... get request is made
    response = client.get(
        f'/users/{user_created["id"]}/',
        headers=dict(knock_knock=test_token['token']),
    )

    # then ...
    # ... response is created and contains data posted,
    results = response.get_json()
    assert response.status_code == StatusCodes.OK
    assert results['username'] == str(post_data['username'])
