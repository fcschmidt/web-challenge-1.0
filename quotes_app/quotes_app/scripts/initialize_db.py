from sqlalchemy import engine_from_config
from ..models.models import Base, DBSession
from pyramid.paster import get_appsettings


def main():
    """Script used to initialize an empty database"""
    settings = get_appsettings('./development.ini')
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    
    Base.metadata.create_all(engine)
    return 'Database created successfully!'

if __name__ == '__main__':
    main()
