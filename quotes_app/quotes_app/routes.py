# Routes


def includeme(config):
    config.add_route('home', '/')
    config.add_route('quotes', '/quotes')
    config.add_route('quote', '/quotes/{quote_number}')
    config.add_route('random_quote', '/quotes/random/')
    config.add_route('api_sessions', '/api/sessions')
    config.add_route('api_sessions_id', '/api/sessions/{id}')
    config.add_route('api_sessions_uid', '/api/sessions/uid/{uid}')
