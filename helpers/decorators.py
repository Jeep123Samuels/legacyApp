from functools import wraps

from helpers.status_codes import StatusCodes as Status


def db_expect(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return (
                e.args[0],
                Status.BAD_REQUEST,
            )

    return wrapper
