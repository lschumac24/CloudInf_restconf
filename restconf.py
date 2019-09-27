import logging
from typing import List

import requests
import yaml
from jinja2 import FileSystemLoader, Environment

import restconf_helpers

requests.packages.urllib3.disable_warnings()

logger = logging.getLogger('restconf.example')


def load_devices() -> List[dict]:
    with open('device_infos.yaml', 'r') as host_file:
        hosts = yaml.load(host_file.read(), Loader=yaml.FullLoader)
        return hosts


def put_configuration(host: dict, config: str) -> str:
    response = restconf_helpers.RestconfRequestHelper().put(
        url=f'https://{host["connection_address"]}/restconf/data/Cisco-IOS-XE-native:native/',
        username=host['username'],
        password=host['password'],
        config=config
        )
    return response


def init_logger():
    _logger = logging.getLogger('restconf')
    _logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    _logger.addHandler(ch)


def main():
    devices = load_devices()
    for device in devices:
        env = Environment(loader=FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
        template = env.get_template('config_template.xml')
        config = template.render(device)
        response = put_configuration(host=device, config=config)
        print(response)


if __name__ == '__main__':
    init_logger()
    main()