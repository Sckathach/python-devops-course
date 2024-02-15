def test_index(client_test):
    response = client_test.get('/')
    assert response.data == b'<p>404 Not Found</p>'


def test_health(client_test):
    response = client_test.get('/api/v1/health')
    assert response.status_code == 200
    assert response.json["success"]
