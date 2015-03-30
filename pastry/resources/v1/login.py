from pastry.models import User
from pastry.resources import validators, httpcodes

from flask.ext.restful import Resource, reqparse


class LoginResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=validators.email_address, required=True)
        self.parser.add_argument('password', type=str, required=True)
        super(LoginResource, self).__init__()

    def post(self):
        args = self.parser.parse_args()

        user = User(args.username, args.password)
        if not user.exists():
            return {'failed': 'User does not exist'}, httpcodes.BAD_REQUEST
        if not user.verify_password(args.password):
            return {'failed': 'Incorrect password'}, httpcodes.BAD_REQUEST
        return {'Auth-Token': user.generate_auth_token()}, httpcodes.OK
