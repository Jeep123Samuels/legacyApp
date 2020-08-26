from flask import request
from flask_restful import Resource

from app import db
from helpers.status_codes import StatusCodes
from helpers.utils import save_instance
from helpers.validations import check_required_fields
from models.users import Users


class UsersView(Resource):

    def post(self):
        if check_required_fields(set(request.get_json()), Users):
            # encrypt_password(re)
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

    def get(self):
        users = db.session.query(Users).all()
        results = []
        # TODO: add pagination/limit request.
        for user in users:
            user = user.to_dict()
            del user['password']
            results.append(user)
        return (
            {'results': results},
            StatusCodes.OK,
        )


class SingleUserView(Resource):

    def get(self, user_id):
        user = db.session.query(Users).filter_by(id=user_id).first()
        if not user:
            return (
                f'User not found for id => {user_id}\n',
                StatusCodes.BAD_REQUEST,
            )
        user = user.to_dict()
        del user['password']
        return user, StatusCodes.OK
