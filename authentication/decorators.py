from functools import wraps

from flask import request

from authentication import verify_token
from authentication import AuthRefreshTokenExpired, AuthRefreshTokenInvalid


def check_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            verify_token(request.headers.get("knock_knock", ""))
            return func(*args, **kwargs)
        except (AuthRefreshTokenExpired, AuthRefreshTokenInvalid) as e:
            return e.args
    return wrapper
