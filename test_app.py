
import pytest
from app import login

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("admin", "123456", True),     # valid credentials
        ("admin", "wrong", False),     # wrong password
        ("user", "123456", False),     # wrong username
        ("", "123456", False),         # empty username
        ("admin", "", False),          # empty password
        (None, "123456", False),       # None username
        ("admin", None, False),        # None password
        (None, None, False),           # both None
    ],
)
def test_login_various(username, password, expected):
    assert login(username, password) is expected

def test_login_return_type_is_bool():
    result = login("admin", "123456")
    assert isinstance(result, bool)
