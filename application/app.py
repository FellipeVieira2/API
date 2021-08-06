from __init__ import app, api

from application.controller.V1 import primeiro_end_point





def bump_version(cls, version: int):
    str_version = str(version)
    return type(cls.__name__ + f"_V{str_version}", cls.__bases__, cls.__dict__.copy())

api.add_resource(bump_version(primeiro_end_point,1),'/v1/primeiro')