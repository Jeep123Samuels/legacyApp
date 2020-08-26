from flask import request
from flask_restful import Resource

from app import db
from helpers.status_codes import StatusCodes
from helpers.utils import delete_instance, encrypt_password, save_instance
from helpers.validations import check_required_fields
from models.users import Users


class AuthenticateView(Resource):

    def post(self):
        user = Users(**request.get_json())
        error_on_save = save_instance(user)
        response = (
            {
                'id': user.id,
                'username': user.username,
                'text': 'User successfully saved',
            },
            StatusCodes.CREATED,
        )
        # If something went wrong
        if error_on_save:
            response = (
                error_on_save.args[0],
                StatusCodes.NOT_FOUND,
            )
        return response
