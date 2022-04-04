from pecan import hooks

from cyborg.db.sqlalchemy import api


class DBHook(hooks.PecanHook):
    def before(self, state):
        state.request.db_conn = api.Connection()
