from numb3rs import validate

def test_valid_ipv4_address():
    assert validate("192.168.0.1") == True
    assert validate("10.0.0.255") == True
    assert validate("172.16.0.0") == True

def test_invalid_ipv4_address():
    assert validate("275.3.6.28") == False
    assert validate("192.168.0") == False
    assert validate("10.0.0.256") == False

