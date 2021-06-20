#!/usr/bin/env python3

import pprint
from unifi import unifi

u = unifi.UniFi.new_from_environment()

# print controller status
status = u.api_get('status')
print(f"CONTROLLER STATUS: {status.get('meta').get('rc')}\n")

sites = u.api_get('self/sites')
if 'data' in sites:
    print("SITES:")
    for s in sites.get('data'):
        print(f"\t {s.get('desc')}, {s.get('name')}, {s.get('_id')}\n")

for site in u.sites():
    print(f"SITE: {site.name}")

    print("DEVICES:")
    devices = u.api_get(site.api_endpoint('stat/device'))
    pprint.pprint(devices)

print("STA:")
sta = site.sta()
pprint.pprint(sta)
exit(0)
