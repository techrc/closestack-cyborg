"""
wsgiref simple_server
"""

from wsgiref import simple_server
from oslo_config import cfg

from cyborg.api import app  # import pecan app
from cyborg.common import service as cyborg_service

CONF = cfg.CONF


def main():
    cyborg_service.prepare_service()

    # server
    application = app.setup_app()
    server = simple_server.make_server(CONF.host, CONF.port, application)
    print('======== running server at {}:{} ========'.format(CONF.host, CONF.port))
    server.serve_forever()


if __name__ == '__main__':
    main()

