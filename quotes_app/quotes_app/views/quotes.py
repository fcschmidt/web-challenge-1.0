import json
import random
import transaction
from pyramid.response import Response
from pyramid.view import view_config, view_defaults

from lib.consumer_api import ConsumerAPI

from util.json_util import default
from util.uid_generator import uid_generator

from quotes_app.models.models import (
    DBSession,
    SessionLogModel
)


def save_session(session, url):
    """Function using a save a sessions"""
    if 'id' in session:
        pass
    else:
        session['id'] = uid_generator()

    model = SessionLogModel(
        session_uid=session['id'],
        session_url=url,
    )
    DBSession.add(model)
    transaction.commit()


@view_defaults(route_name='home')
class QuoteViews:
    def __init__(self, request):
        self.request = request
        self.api = ConsumerAPI()

    @view_config(renderer='templates/index.jinja2')
    def home(self):
        save_session(self.request.session, self.request.current_route_url())
        return {'project_name': 'Web challenge 1.0'}

    @view_config(route_name='quotes', renderer='templates/quotes.jinja2')
    def get_quotes(self):
        save_session(self.request.session, self.request.current_route_url())
        quotes = self.api.get_quotes()
        return quotes

    @view_config(route_name='quote', renderer='templates/quote.jinja2')
    def get_quote(self):
        save_session(self.request.session, self.request.current_route_url())
        number = self.request.matchdict['quote_number']
        quote = self.api.get_quote(number)
        return {'quote_number': number, 'quote': quote['quote']}

    @view_config(route_name='random_quote', renderer='templates/random.jinja2')
    def get_random_quote(self):
        save_session(self.request.session, self.request.current_route_url())
        size = len(self.api.get_quotes()['quotes'])
        random_number = random.randint(0, size - 1)
        quote = self.api.get_quote(random_number)
        return {'random_number': random_number, 'quote': quote['quote']}

    @view_config(route_name='sessions', renderer='json')
    def get_sessions(self):
        save_session(self.request.session, self.request.current_route_url())
        query_sessions = DBSession.query(SessionLogModel).all()
        serialize = [s.to_json() for s in query_sessions]
        js = json.dumps(serialize, default=default)
        return Response(json_body=json.loads(js))
