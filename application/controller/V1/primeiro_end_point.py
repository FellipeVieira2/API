from flask import request
from flask.views import MethodView


class Visualizar(MethodView):
    def get(self):
        return {"Corro":True}
        