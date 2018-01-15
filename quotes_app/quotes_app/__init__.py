from wsgiref.simple_server import make_server
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')

    config.add_route('home', '/')
    config.add_route('quotes', '/quotes')
    config.add_route('quote', '/quotes/{quote_number}')
    config.add_route('random_quote', '/random')

    config.scan('.views')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    return server.serve_forever()
