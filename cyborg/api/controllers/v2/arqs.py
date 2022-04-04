from pecan import rest
from wsme import types as wtypes

from cyborg.api import expose


class ARQ(wtypes.Base):
    name = wtypes.text


class ARQsCollection(wtypes.Base):
    arqs = [ARQ]


class ARQsController(rest.RestController):

    # GET /v2/arqs
    @expose.expose(ARQsCollection)
    def get(self):
        arq_list = [
            ARQ(**{'name': '111'}),
            ARQ(**{'name': '222'})
        ]
        return ARQsCollection(arqs=arq_list)

    # POST /v2/arqs -d '{"name": "test"}'
    @expose.expose(None, body=ARQ, states_code=201)
    def post(self, arq):
        print(arq)

