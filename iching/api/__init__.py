from importlib.resources import Resource
from flask import Flask
from flask_restful import Api

from .config import configs
from .exceptions import EnvironmentValueError
from .resources import *

class AppFactory:

    @staticmethod
    def create_app(env: str) -> Flask:
        if env not in ['dev', 'prod']:
            raise EnvironmentValueError(env=env)
        else:
            app = Flask(__name__)
            app.config.from_object(configs[env])
            api = Api(app)
            # api.add_resource()
            return app