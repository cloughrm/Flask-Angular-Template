import json

from flask.ext import restful
from flask import Flask, make_response

from pastry.db import mongo
from pastry.encoder import APIEncoder
from pastry.routes import register_routes


def json_renderer(data, code, headers=None):
    dumped = json.dumps(data, cls=APIEncoder)
    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    mongo.init_app(app)

    api = restful.Api(app)
    api.representations.update({
        'application/json': json_renderer
    })
    register_routes(api)
    return app
