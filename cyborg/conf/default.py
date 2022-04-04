from oslo_config import cfg

opts = [
    cfg.StrOpt('host', default='0.0.0.0'),
    cfg.IntOpt('port', default=8090)
]


def register_opts(conf):
    conf.register_opts(opts)

