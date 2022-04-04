from oslo_config import cfg


def parse_args():
    cfg.CONF(default_config_files=['/etc/cyborg/cyborg.conf'])

