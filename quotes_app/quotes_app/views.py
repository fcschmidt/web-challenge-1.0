from lib.consumer_api import ConsumerAPI
from pyramid.view import view_config, view_defaults
import random


@view_defaults(route_name='home')
class QuoteViews:
    def __init__(self, request):
        self.request = request
        self.api = ConsumerAPI()

    @view_config(renderer='templates/index.jinja2')
    def home(self):
        return {'project_name': 'Web challenge 1.0'}

    @view_config(route_name='quotes', renderer='templates/quotes.jinja2')
    def get_quotes(self):
        quotes = self.api.get_quotes()
        return quotes

    @view_config(route_name='quote', renderer='templates/quote.jinja2')
    def get_quote(self):
        number = self.request.matchdict['quote_number']
        quote = self.api.get_quote(number)
        return {'quote_number': number, 'quote': quote['quote']}

    @view_config(route_name='random_quote', renderer='templates/random.jinja2')
    def get_random_quote(self):
        size = len(self.api.get_quotes()['quotes'])
        random_number = random.randint(0, size - 1)
        quote = self.api.get_quote(random_number)
        return {'random_number': random_number, 'quote': quote['quote']}
