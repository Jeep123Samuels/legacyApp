
from authentication import create_auth_tokens
from flask import request
from flask_restful import Resource

from app import db
from helpers.decorators import db_expect
from helpers.status_codes import StatusCodes
from models import Users


class LoginView(Resource):

    @db_expect
    def post(self):
        username = request.get_json().get('username')
        password = request.get_json().get('password')

        # Check correct parameters passed
        if not password or not username:
            return (
                {'error': 'Missing password/username parameters.'},
                StatusCodes.BAD_REQUEST,
            )

        user = db.session.query(Users).filter_by(username=username).first()
        # If user not pulled from db...
        if not user:
            return (
                {'error': f'Username - {username} cannot be found.'},
                StatusCodes.BAD_REQUEST,
            )

        # Return success if correct password
        if user.is_correct_password(password):
            tokens = create_auth_tokens(user_id=user.id)
            return (
                {
                    'message': 'Authenticated Succeeded.',
                    'results': tokens,
                },
                StatusCodes.OK,
            )

        # If something went wrong
        return (
            {'message': 'Authenticated Failed.'},
            StatusCodes.BAD_REQUEST,
        )
