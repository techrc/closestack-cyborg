from oslo_config import cfg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cyborg.db.sqlalchemy import models

CONF = cfg.CONF

_ENGINE = None
_SESSION_MAKER = None


def get_engine():
    global _ENGINE

    if _ENGINE:
        return _ENGINE
    _ENGINE = create_engine(CONF.database.connection)
    #models.Base.metadata.create_all(_ENGINE)

    return _ENGINE


def get_session_maker(engine):
    global _SESSION_MAKER

    if _SESSION_MAKER:
        return _SESSION_MAKER
    _SESSION_MAKER = sessionmaker(bind=engine)

    return _SESSION_MAKER


def get_session():
    engine = get_engine()
    maker = get_session_maker(engine)
    session = maker()
    return session


class Connection(object):
    def device_list(self):
        query = get_session().query(models.Device)
        return query.all()

