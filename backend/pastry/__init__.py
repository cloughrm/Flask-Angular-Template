import json

from raven.contrib.flask import Sentry

from flask.ext import restful
from flask.ext.cors import CORS
from flask import Flask, make_response, jsonify, request

from pastry.db import mongo
from pastry.encoder import APIEncoder
from pastry.routes import register_routes


def register_errors(app):
    @app.errorhandler(404)
    def page_not_found(path):
        return jsonify({
            'message': 'URL not found: {}'.format(request.path)
        }), 404
    return app


def json_renderer(data, code, headers=None):
    dumped = json.dumps(data, cls=APIEncoder)
    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp


def create_app(config):
    app = Flask(__name__)
    app = register_errors(app)
    CORS(app, allow_headers=['Content-Type', 'Auth-Token'])
    app.config.from_object(config)
    if 'SENTRY_DSN' in app.config:
        Sentry(app)
    mongo.init_app(app)

    api = restful.Api(app)
    api.representations.update({
        'application/json': json_renderer
    })
    register_routes(api)
    return app
