from waitress import serve
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from bonus.calculator import load_data

if __name__ == '__main__':
    with Configurator() as config:
        app = config.make_wsgi_app()
    print("Drinks incoming")
    load_data()
    serve(app, host='0.0.0.0', port=5001)
    print("Server started")

