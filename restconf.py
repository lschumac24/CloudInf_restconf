import logging
from typing import List

import requests
import yaml

import restconf_helpers

requests.packages.urllib3.disable_warnings()

logger = logging.getLogger('restconf.example')


def load_devices() -> List[dict]:
    with open('device_infos.yaml', 'r') as host_file:
        hosts = yaml.load(host_file.read(), Loader=yaml.FullLoader)
        return hosts


def init_logger():
    _logger = logging.getLogger('restconf')
    _logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    _logger.addHandler(ch)


def main():
    devices = load_devices()


if __name__ == '__main__':
    init_logger()
    main()