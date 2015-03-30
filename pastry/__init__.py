import json

from flask.ext import restful
from flask import Flask, make_response

from pastry.db import mongo
from pastry.resources import v1
from pastry.encoder import APIEncoder


def json_renderer(data, code, headers=None):
    dumped = json.dumps(data, cls=APIEncoder)
    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp


def route(name, version=1):
    return '/api/v{}{}'.format(version, name)


app = Flask(__name__)
app.config.from_object('pastry.settings')
mongo.init_app(app)

api = restful.Api(app)
api.representations.update({
    'application/json': json_renderer
})

api.add_resource(v1.UsersListResource, route('/users/'))
api.add_resource(v1.UsersResource, route('/users/<id>'))
api.add_resource(v1.LoginResource, route('/login'))
