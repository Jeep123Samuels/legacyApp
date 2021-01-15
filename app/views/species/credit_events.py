from flask import request
from flask_restful import Resource

from authentication.decorators import check_token
from helpers.decorators import db_expect
from helpers.status_codes import StatusCodes
from helpers.validations import check_required_fields
from models import CreditEvents


class CreditEventsView(Resource):

    @db_expect
    @check_token
    def post(self):
        if check_required_fields(set(request.get_json()), CreditEvents):
            event = request.get_json()
            if not event.get('storage_id'):
                return (
                    'Missing parameters: storage_id',
                    StatusCodes.BAD_REQUEST,
                )
            event = CreditEvents(**event)
            error_on_save = event.save_instance()
            response = (
                {
                    'event': event.description,
                    'id': event.id,
                    'text': 'Credit event successfully saved',
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
