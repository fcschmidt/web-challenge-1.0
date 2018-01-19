import json
from pyramid.response import Response
from pyramid.view import view_config

from util.json_util import default
from builtins import IndexError

from quotes_app.models.models import (
    DBSession,
    SessionLogModel
)


def query_validation(query, value):
    """
    Function using validate query
    :param query:
    :param value:
    :return: true or false
    """
    return [q for q in query][value - 1]


class RestApiSessionsViewsTests:
    def __init__(self, request):
        self.request = request
        self.session = DBSession()

    @view_config(route_name='api_sessions', request_method='GET', renderer='json')
    def api_get_sessions(self):
        query_sessions = self.session.query(SessionLogModel).all()

        if len(query_sessions) > 0:
            serialize = [s.to_json() for s in query_sessions]
            response = json.dumps(serialize, default=default)
            return Response(
                json_body=json.loads(response),
                content_type='application/json; charset=UTF-8',
                status=200,
            )
        else:
            response = {'sessions': []}
            return Response(
                json_body=response,
                content_type='application/json; charset=UTF-8',
                status=200,
            )

    @view_config(route_name='api_sessions_id', request_method='GET', renderer='json')
    def api_get_session_id(self):
        get_id = int(self.request.matchdict['id'])
        query = self.session.query(SessionLogModel.id == get_id)
        try:
            query_validation(query, get_id)
        except IndexError:
            response = {'status': 404, 'message': 'Not Found'}
            return Response(
                json_body=response,
                content_type='application/json; charset=UTF-8',
                status=404,
            )

        query_session = self.session.query(SessionLogModel) \
            .get(get_id).to_json()
        response = json.dumps(query_session, default=default)
        return Response(
            json_body=json.loads(response),
            content_type='application/json; charset=UTF-8',
            status=200,
        )
