from pastry.resources import v1


def route(name, version=1):
    return '/api/v{}{}'.format(version, name)


def register_routes(api):
    api.add_resource(v1.UsersListResource, route('/users'))
    api.add_resource(v1.UsersResource, route('/users/<id>'))

    api.add_resource(v1.LoginResource, route('/login'))
