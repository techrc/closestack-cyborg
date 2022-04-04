from oslo_config import cfg

from cyborg.conf import default
from cyborg.conf import database

CONF = cfg.CONF

default.register_opts(CONF)
database.register_opts(CONF)
