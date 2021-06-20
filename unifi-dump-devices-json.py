#!/usr/bin/env python3

import time
import os
import argparse
import pprint
import json
from unifi import unifi

parser = argparse.ArgumentParser(description='UniFi Prometheus dump')

args = parser.parse_args()

apiendpoint = os.environ.get('API_URL', 'https://localhost:8443')
apiusername = os.environ.get('API_USERNAME', 'ubnt')
apipassword = os.environ.get('API_PASSWORD', 'ubnt')

u = unifi.UniFi(apiendpoint, apiusername, apipassword)


# Just as a help really, code will not be reached as config.get() will blow up
if apiendpoint is None:
    raise AssertionError('API/URL is required in configuration')
if apiusername is None or apipassword is None:
    raise AssertionError('API/Username and API/Password is required in configuration')

# print controller status
status = u.api_get('status')
if status.get('meta').get('rc') != 'ok':
    print("CONTROLLER STATUS: ", status.get('meta').get('rc'))

sites = u.api_get('self/sites')
if 'data' in sites:

    for site in u.sites():
        devices = u.api_get(site.api_endpoint('stat/device'))
        print(json.dumps(devices['data']))
exit(0)
