# HTTP Status code
def verify_http_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Expected HTTP Staus : " + str(expected_data)

# Any key should not be null or empty
def verify_bookingId_key(key):
    assert key != 0, "Key is non empty : " + key
    assert key > 0, "Key should be greater than zero : " + key

