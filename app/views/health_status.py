
from flask_restful import Resource

from helpers.status_codes import StatusCodes


class HealthStatus(Resource):

    def get(self):
        return {'status': 'OK'}, StatusCodes.OK
