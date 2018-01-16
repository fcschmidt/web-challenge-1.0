# from .scripts.initializedb import myRootFactory


def includeme(config):
    config.add_route('home', '/')
    config.add_route('quotes', '/quotes')
    config.add_route('quote', '/quotes/{quote_number}')
    config.add_route('random_quote', '/random')
    # config.add_route('random_quote', '/quotes/random*traverse', factory=myRootFactory)
    # config.add_route('quotes', '/random', factory='QuoteViews', use_global_views=True)
