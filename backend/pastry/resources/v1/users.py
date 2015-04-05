from pastry.db import mongo
from pastry.models import User
from pastry.resources.auth import login_required
from pastry.resources import validators, httpcodes

from bson.objectid import ObjectId

from flask import request
from flask.ext.restful import Resource, reqparse


class UsersResource(Resource):
    @login_required
    def get(self, id):
        return mongo.db.users.find_one_or_404({'_id': ObjectId(id)})

    @login_required
    def delete(self, id):
        return mongo.db.users.remove({'_id': ObjectId(id)})


class UsersListResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        if request.method == 'GET':
            self.parser.add_argument('limit', type=int, default=20)
            self.parser.add_argument('offset', type=int, default=0)
        elif request.method == 'POST':
            self.parser.add_argument('username', type=validators.email_address, required=True)
            self.parser.add_argument('password', type=str, required=True)
        super(UsersListResource, self).__init__()

    @login_required
    def get(self):
        args = self.parser.parse_args()
        users = mongo.db.users.find().skip(args.offset).limit(args.limit)
        return {
            'objects': users,
            'offset': args.offset,
            'limit': args.limit,
        }

    @login_required
    def post(self):
        args = self.parser.parse_args()
        user = User(args.username, args.password)
        if mongo.db.users.find_one({'username': user.username}):
            return {'failed': 'User {} already exists'.format(user.username)}, httpcodes.BAD_REQUEST
        user_id = user.create()
        return {'id': user_id}, httpcodes.CREATED
