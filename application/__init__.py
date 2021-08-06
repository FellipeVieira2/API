from flask import Flask
from .utils.conts import BASE_PATH
import flask_restful


app = Flask(__name__, BASE_PATH)

api = flask_restful.Api(app)