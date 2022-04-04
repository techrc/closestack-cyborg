from pecan import rest
from wsme import types as wtypes

from cyborg.api import expose
from cyborg.api.controllers.v2.devices import DevicesController
from cyborg.api.controllers.v2.arqs import ARQsController


class Controller(rest.RestController):

    devices = DevicesController()
    arqs = ARQsController()

    @expose.expose(wtypes.text)
    def get(self):
        return 'v2 Controller'

