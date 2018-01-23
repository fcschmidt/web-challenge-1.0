from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings
from ..models.models import Base, DBSession


def main():
    """Script used to initialize an empty database

    """
    settings = get_appsettings('./development.ini')
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    return 'Database created successfully!'


if __name__ == '__main__':
    main()
