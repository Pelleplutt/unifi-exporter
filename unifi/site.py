#!/usr/bin/env python3

import logging
from .device import *

class Site(object):
    def __init__(self, unifi, data):
        self.unifi = unifi
        self.id = data['_id']
        self.desc = data['desc']
        self.name = data['name']
        self.role = data['role']

    def api_endpoint(self, endpoint):
        return 's/' + self.name + '/' + endpoint

    def device(self):
        # https://hemma:8443/api/s/default/stat/device

        data = self.unifi.api_get(self.api_endpoint('stat/device'))
        ret = []
        for d in data['data']:
            if d['model'] == 'UGW3':
                ret.append(UGW3.UGW3(self, d))
            elif d['model'] in ('UDMPRO', 'UDMPROSE'):
                ret.append(UDMPRO.UDMPRO(self, d))
            elif d['model'] == 'US8P150':
                ret.append(US8P150.US8P150(self, d))
            elif d['model'] == 'USL16LP':
                ret.append(USL16LP.USL16LP(self, d))
            elif d['model'] == 'USL8LP':
                ret.append(USL8LP.USL8LP(self, d))
            elif d['model'] == 'USMINI':
                ret.append(USMINI.USMINI(self, d))
            elif d['model'] == 'USF5P':
                ret.append(USF5P.USF5P(self, d))
            elif d['model'] == 'U7PG2':
                ret.append(U7PG2.U7PG2(self, d))
            elif d['model'] == 'U7HD':
                ret.append(U7HD.U7HD(self, d))
            elif d['model'] == 'U7LT':
                ret.append(U7LT.U7LT(self, d))
            elif d['model'] == 'U7NHD':
                ret.append(U7NHD.U7NHD(self, d))
            elif d['model'] == 'UHDIW':
                ret.append(UHDIW.UHDIW(self, d))
            else:
                logging.warning(f"Unknown device type/model: {d['type']}/{d['model']}")

        return ret

    def sta(self):
        # https://hemma:8443/api/s/default/stat/sta
        data = self.unifi.api_get(self.api_endpoint('stat/sta'))
        return data['data']


# sta:
# "data": [
#     {
#         "_id": "58556a70b410cf6b940e570e",
#         "_is_guest_by_usw": false,
#         "_last_seen_by_usw": 1485694644,
#         "_uptime_by_usw": 3701886,
#         "assoc_time": 1481992812,
#         "first_seen": 1481992816,
#         "ip": "192.168.1.1",
#         "is_guest": false,
#         "is_wired": true,
#         "last_seen": 1485694644,
#         "latest_assoc_time": 1481992813,
#         "mac": "00:0d:b9:40:80:48",
#         "network": "LAN",
#         "network_id": "56c87bd0b41038d25762ce8b",
#         "oui": "PcEngine",
#         "site_id": "56c87bc1b41038d25762ce86",
#         "sw_depth": 0,
#         "sw_mac": "f0:9f:c2:0a:4a:ca",
#         "sw_port": 8,
#         "uptime": 3701832,
#         "user_id": "58556a70b410cf6b940e570e"
#     },
#     {
#         "_id": "56c994a0b41038d25762cee2",
#         "_is_guest_by_uap": false,
#         "_is_guest_by_usw": false,
#         "_last_seen_by_uap": 1485694651,
#         "_last_seen_by_usw": 1485694644,
#         "_uptime_by_uap": 14226,
#         "_uptime_by_usw": 46707,
#         "ap_mac": "44:d9:e7:f6:9f:99",
#         "assoc_time": 1485647936,
#         "authorized": true,
#         "bssid": "46:d9:e7:f8:9f:99",
#         "bytes-r": 7,
#         "ccq": 333,
#         "channel": 36,
#         "essid": "PNet",
#         "first_seen": 1456051360,
#         "hostname": "Lenas-iPhone",
#         "idletime": 8,
#         "ip": "192.168.1.247",
#         "is_guest": false,
#         "is_wired": false,
#         "last_seen": 1485694651,
#         "latest_assoc_time": 1485680425,
#         "mac": "80:ea:96:08:ed:81",
#         "network": "LAN",
#         "network_id": "56c87bd0b41038d25762ce8b",
#         "noise": -104,
#         "oui": "Apple",
#         "powersave_enabled": true,
#         "qos_policy_applied": true,
#         "radio": "na",
#         "radio_proto": "na",
#         "rssi": 24,
#         "rx_bytes": 44044326,
#         "rx_bytes-r": 1,
#         "rx_packets": 250896,
#         "rx_rate": 150000,
#         "signal": -80,
#         "site_id": "56c87bc1b41038d25762ce86",
#         "sw_depth": 1,
#         "sw_mac": "f0:9f:c2:0a:4a:ca",
#         "sw_port": 5,
#         "tx_bytes": 347850716,
#         "tx_bytes-r": 6,
#         "tx_packets": 255025,
#         "tx_power": 40,
#         "tx_rate": 150000,
#         "uptime": 46715,
#         "user_id": "56c994a0b41038d25762cee2"
#     }
