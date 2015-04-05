import urllib

from flask import url_for
from subprocess import call
from pastry import create_app
from flask.ext.script import Manager


app = create_app('pastry.settings.BaseConfig')
manager = Manager(app)


@manager.command
def list_routes():
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = '[{0}]'.format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote('{:50s} {:20s} {}'.format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print line


@manager.command
def test():
    call(['python', '-m', 'unittest', 'discover'])


if __name__ == '__main__':
    manager.run()
