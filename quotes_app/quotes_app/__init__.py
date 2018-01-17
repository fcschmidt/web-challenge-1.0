from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.session import SignedCookieSessionFactory

from .models.models import DBSession, Base


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    engine = engine_from_config(settings, prefix='sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

    session_factory = SignedCookieSessionFactory('itsaseekreet')
    config.set_session_factory(session_factory)

    config.include('pyramid_jinja2')
    config.include('.routes')
    config.scan()

    return config.make_wsgi_app()
