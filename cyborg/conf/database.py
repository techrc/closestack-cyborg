from oslo_config import cfg

group = cfg.OptGroup('database')

opts = [
    cfg.StrOpt('connection')
]


def register_opts(conf):
    conf.register_group(group)
    conf.register_opts(opts, group=group)
