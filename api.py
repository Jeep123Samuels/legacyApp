from app.views import (
    HealthStatus,
    LoginView,
    SingleUserView,
    UsersView,
)


def register_views(api_obj):
    to_register: list = [
        (LoginView, '/knock/on/door/',),
        (HealthStatus, '/health/status/', ),
        (UsersView, '/users/', ),
        (SingleUserView, '/users/<int:user_id>/', ),
    ]

    for item in to_register:
        api_obj.add_resource(*item)
    return api_obj
