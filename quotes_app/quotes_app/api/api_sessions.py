import json
from pyramid.response import Response
from pyramid.view import view_config

from util.json_util import default

from quotes_app.models.models import (
    DBSession,
    SessionLogModel
)


class RestApiSessionsViews:
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.session = DBSession()

    @view_config(route_name='api_sessions', request_method='GET', renderer='json')
    def api_get_all_sessions(self):
        query_sessions = self.session.query(SessionLogModel).all()
        serialize = [s.to_json() for s in query_sessions]
        response = json.dumps(serialize, default=default)
        return Response(
            json_body=json.loads(response),
            content_type='application/json; charset=UTF-8',
            status=200,
        )

    @view_config(route_name='api_sessions_id', request_method='GET', renderer='json')
    def api_get_details_session(self):
        get_id = int(self.request.matchdict['id'])
        for instance in self.session.query(SessionLogModel)\
                .filter(SessionLogModel.id == get_id):
            resp = json.dumps(instance.to_json(), default=default)
            return Response(
                json_body=json.loads(resp),
                content_type='application/json; charset=UTF-8',
                status=200,
            )
