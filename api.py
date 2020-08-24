from app.views import (
    HealthStatus,
    SingleUserView,
    UsersView,
)


def register_views(api_obj):
    api_obj.add_resource(HealthStatus, '/health/status/')

    api_obj.add_resource(UsersView, '/users/')
    api_obj.add_resource(SingleUserView, '/users/<int:user_id>/')

    return api_obj
