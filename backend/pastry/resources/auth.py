from functools import wraps
from pastry.models import User
from flask import request, abort


def parse_api_key():
    key = None
    if request.args.get('api_key'):
        key = request.args.get('api_key')
    elif request.form.get('api_key'):
        key = request.form.get('api_key')
    return key


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.method != 'OPTIONS':

            # Verify auth-token or api_key is present
            token = request.headers.get('Auth-Token')
            api_key = parse_api_key()
            if not token and not api_key:
                abort(401)

            # Verify key/token
            if api_key:
                if not User.verify_api_key(api_key):
                    abort(401)
            elif token:
                if not User.verify_auth_token(token):
                    abort(401)

        return f(*args, **kwargs)
    return decorated
