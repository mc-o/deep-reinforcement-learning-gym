import os
import logging
import time
import click
from playground.configs.manager import ConfigManager


@click.command()
@click.argument('config_name')
@click.option('-m', '--model-name', default=None)
@click.option('--no-monitor', is_flag=True, default=False)
def run(config_name, model_name=None, no_monitor=False):
    cfg = ConfigManager.load(config_name)

    if model_name is None:
        model_name = '-'.join([
            cfg.env_name.lower(),
            cfg.policy_name.replace('_', '-'),
            os.path.splitext(os.path.basename(config_name))[0] if config_name else 'default',
            str(int(time.time()))
        ])

    model_name = model_name.lower()
    cfg.start_training(model_name, run_monitor=not no_monitor)


if __name__ == '__main__':
    logging.getLogger('').handlers = []
    logging.basicConfig(format='[%(asctime)s] %(message)s', level=logging.DEBUG)
    run()
