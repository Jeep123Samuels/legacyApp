from flask_restful import Api

from app import app
from api import register_views

api_ = Api(app)
api_ = register_views(api_)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
