
from flask import request
from flask_restful import Resource

from app import db
from authentication.decorators import check_token
from helpers.decorators import db_expect
from helpers.status_codes import StatusCodes
from helpers.validations import check_required_fields
from models import Storages


class StoragesView(Resource):

    @db_expect
    @check_token
    def post(self):
        if not check_required_fields(set(request.get_json()), Storages):
            return (
                'Missing parameters in request.',
                StatusCodes.BAD_REQUEST,
            )
        storage = Storages(**request.get_json())
        error_on_save = storage.save_instance()
        response = (
            {
                'description': storage.description,
                'id': storage.id,
                'user_id': storage.user_id,
                'text': 'Storage successfully created',
            },
            StatusCodes.CREATED,
        )
        # If something went wrong
        if error_on_save:
            response = (
                error_on_save.args[0],
                StatusCodes.NOT_ACCEPTABLE,
            )
        return response

    @check_token
    def get(self, user_id):
        storages = db.session.query(Storages).filter_by(user_id=user_id)

        results: list = list()
        for storage_ in storages:
            results.append(storage_.to_dict())
        return results, StatusCodes.OK

