from functools import wraps

from flask import make_response

from helpers.status_codes import StatusCodes as Status


def db_expect(func):
    @wraps(func)
    def wrapper():
        try:
            return func()
        except Exception as e:
            return make_response(
                e.args[0],
                Status.BAD_REQUEST,
            )

    return wrapper
