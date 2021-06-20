#!/usr/bin/env python3

import json
from unifi import unifi

u = unifi.UniFi.new_from_environment()

# print controller status
status = u.api_get('status')
if status.get('meta').get('rc') != 'ok':
    print(f"CONTROLLER STATUS: {status.get('meta').get('rc')}")

sites = u.api_get('self/sites')
if 'data' in sites:

    for site in u.sites():
        devices = u.api_get(site.api_endpoint('stat/device'))
        print(json.dumps(devices['data']))
exit(0)