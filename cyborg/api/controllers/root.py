from pecan import rest
from wsme import types as wtypes
# import wsmeext.pecan as wsme_pecan  # xml

from cyborg.api import expose
from cyborg.api.controllers.v2 import Controller as V2Controller


class RootController(rest.RestController):

    v2 = V2Controller()

    # @wsme_pecan.wsexpose(wtypes.text)  # xml
    @expose.expose(wtypes.text)          # json
    def get(self):
        return 'root Controller'

