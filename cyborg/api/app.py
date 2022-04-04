import pecan

from cyborg.api import config as api_config
from cyborg.api import hooks


# ----------------------------------------------------------------
# get pecan config & setup pecan app

def get_pecan_config():
    """get pecan configuration.
    """
    # filename: /home/qianshuai/closestack-cyborg/cyborg/api/config.py
    filename = api_config.__file__.replace('.pyc', '.py')
    return pecan.configuration.conf_from_file(filename)


def setup_app():
    config = get_pecan_config()        # pecan config

    app_hooks = [hooks.DBHook()]

    # {'root': 'cyborg.api.controllers.root.RootController', 'modules': ['cyborg.api'], 'debug': False}
    app_conf = dict(config.app)        # config.app is content of config.py

    app = pecan.make_app(
        app_conf.pop('root'),
        hooks=app_hooks,
        **app_conf
    )
    return app

# ----------------------------------------------------------------

