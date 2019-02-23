from . import device

class U7PG2(device.Device):

    def __init__(self, site, data):
        super(U7PG2, self).__init__(site, data)

        self.radio = {}
        self.vap = []
        self.parse_radio(data['radio_table'])
        self.parse_stat(data['stat'])
        self.parse_uplink(data['uplink'])
        self.parse_vap_table(data['vap_table'])
        self.parse_sysstat(data['sys_stats'])

    def parse_radio(self, data):
        for radio in data:
            rstr = radio['radio']
            self.radio[rstr] = radio

    def parse_vap_table(self, data):
        for vap in data:
            self.vap.append(vap)

# {u'_id': u'596a2b19b410d0fb1442515e',
# u'_uptime': 3515944,
# u'adopt_ip': u'192.168.1.2',
# u'adopt_url': u'http://192.168.1.3:8080/inform',
# u'adopted': True,
# u'antenna_table': [{u'id': 4,
#                     u'name': u'Combined',
#                     u'wifi0_gain': 3,
#                     u'wifi1_gain': 3}],
# u'bandsteering_mode': u'prefer_5g',
# u'board_rev': 26,
# u'bytes': 920700496,
# u'bytes-d': 151237,
# u'bytes-r': 4448,
# u'cfgversion': u'78da8449bc4a2fab',
# u'config_network': {u'ip': u'192.168.1.217', u'type': u'dhcp'},
# u'connect_request_ip': u'192.168.1.2',
# u'connect_request_port': u'53930',
# u'considered_lost_at': 1515926531,
# u'countrycode_table': [],
# u'default': False,
# u'device_id': u'596a2b19b410d0fb1442515e',
# u'discovered_via': u'l2',
# u'downlink_table': [],
# u'ethernet_table': [{u'mac': u'f0:9f:c2:79:66:c6',
#                      u'name': u'eth0',
#                      u'num_port': 2}],
# u'fw_caps': 16151,
# u'guest-num_sta': 0,
# u'guest_token': u'D8E63428EAB9B664EA7A3001BFA2685D',
# u'has_eth1': False,
# u'has_speaker': False,
# u'inform_ip': u'192.168.1.3',
# u'inform_url': u'http://192.168.1.3:8080/inform',
# u'ip': u'192.168.1.2',
# u'isolated': False,
# u'known_cfgversion': u'78da8449bc4a2fab',
# u'last_seen': 1515926405,
# u'last_uplink': {u'uplink_mac': u'f0:9f:c2:0a:4a:ca',
#                  u'uplink_remote_port': 4},
# u'led_override': u'default',
# u'license_state': u'registered',
# u'locating': False,
# u'mac': u'f0:9f:c2:79:66:c6',
# u'map_id': u'59ecfc54b410f47d7f9665da',
# u'model': u'U7PG2',
# u'na-channel': 36,
# u'na-eirp': 20,
# u'na-extchannel': 1,
# u'na-gain': 3,
# u'na-guest-num_sta': 0,
# u'na-num_sta': 1,
# u'na-state': u'RUN',
# u'na-tx_power': 17,
# u'na-user-num_sta': 1,
# u'na_ast_be_xmit': 669,
# u'na_ast_cst': None,
# u'na_ast_txto': None,
# u'na_cu_self_rx': 0,
# u'na_cu_self_tx': 0,
# u'na_cu_total': 0,
# u'na_tx_packets': 47,
# u'na_tx_retries': 0,
# u'name': u'unifi-ov',
# u'next_heartbeat_at': 1515926447,
# u'ng-channel': 11,
# u'ng-eirp': 20,
# u'ng-extchannel': 0,
# u'ng-gain': 3,
# u'ng-guest-num_sta': 0,
# u'ng-num_sta': 1,
# u'ng-state': u'RUN',
# u'ng-tx_power': 17,
# u'ng-user-num_sta': 1,
# u'ng_ast_be_xmit': 669,
# u'ng_ast_cst': None,
# u'ng_ast_txto': None,
# u'ng_cu_self_rx': 0,
# u'ng_cu_self_tx': 4,
# u'ng_cu_total': 4,
# u'ng_tx_packets': 90,
# u'ng_tx_retries': 0,
# u'num_sta': 2,
# u'port_table': [{u'aggregated_by': False,
#                  u'attr_no_edit': True,
#                  u'autoneg': True,
#                  u'bytes-r': 5410,
#                  u'enable': True,
#                  u'flowctrl_rx': False,
#                  u'flowctrl_tx': False,
#                  u'full_duplex': True,
#                  u'is_uplink': True,
#                  u'jumbo': True,
#                  u'mac_table': [{u'age': 13,
#                                  u'mac': u'f4:0f:24:29:c7:5e',
#                                  u'static': False,
#                                  u'uptime': 3109,
#                                  u'vlan': 1},
#                                 {u'age': 0,
#                                  u'mac': u'c8:d3:a3:9f:fc:7d',
#                                  u'static': False,
#                                  u'uptime': 96735,
#                                  u'vlan': 1},
#                                 {u'age': 193,
#                                  u'mac': u'00:23:c1:0e:92:9d',
#                                  u'static': False,
#                                  u'uptime': 194,
#                                  u'vlan': 1},
#                                 {u'age': 12,
#                                  u'mac': u'f0:9f:c2:6c:15:5c',
#                                  u'static': False,
#                                  u'uptime': 152197,
#                                  u'vlan': 1},
#                                 {u'age': 79,
#                                  u'mac': u'88:87:17:b8:60:57',
#                                  u'static': False,
#                                  u'uptime': 85,
#                                  u'vlan': 1},
#                                 {u'age': 187,
#                                  u'mac': u'5c:ad:cf:e7:47:b1',
#                                  u'static': False,
#                                  u'uptime': 688,
#                                  u'vlan': 1},
#                                 {u'age': 25,
#                                  u'mac': u'88:cb:87:bd:32:ec',
#                                  u'static': False,
#                                  u'uptime': 158,
#                                  u'vlan': 1},
#                                 {u'age': 0,
#                                  u'mac': u'f0:9f:c2:0a:4a:cb',
#                                  u'static': False,
#                                  u'uptime': 3515935,
#                                  u'vlan': 1},
#                                 {u'age': 19,
#                                  u'mac': u'f0:9f:c2:0a:4a:ca',
#                                  u'static': False,
#                                  u'uptime': 3515881,
#                                  u'vlan': 1},
#                                 {u'age': 73,
#                                  u'mac': u'00:17:88:66:c8:68',
#                                  u'static': False,
#                                  u'uptime': 3295795,
#                                  u'vlan': 1},
#                                 {u'age': 6,
#                                  u'mac': u'00:0d:b9:40:80:48',
#                                  u'static': False,
#                                  u'uptime': 95825,
#                                  u'vlan': 1},
#                                 {u'age': 193,
#                                  u'mac': u'04:4b:ed:60:d0:a3',
#                                  u'static': False,
#                                  u'uptime': 194,
#                                  u'vlan': 1},
#                                 {u'age': 25,
#                                  u'mac': u'00:0e:58:28:90:22',
#                                  u'static': False,
#                                  u'uptime': 3515761,
#                                  u'vlan': 1}],
#                  u'masked': False,
#                  u'media': u'GE',
#                  u'name': u'Main',
#                  u'op_mode': u'switch',
#                  u'poe_caps': 0,
#                  u'port_idx': 1,
#                  u'port_poe': False,
#                  u'portconf_id': u'56c87bd0b41038d25762ce8f',
#                  u'rx_broadcast': 3481903,
#                  u'rx_bytes': 4569454184,
#                  u'rx_bytes-r': 1774,
#                  u'rx_dropped': 0,
#                  u'rx_errors': 0,
#                  u'rx_multicast': 3255847,
#                  u'rx_packets': 248023214,
#                  u'speed': 1000,
#                  u'stp_pathcost': 0,
#                  u'stp_state': u'forwarding',
#                  u'tx_broadcast': 900863,
#                  u'tx_bytes': -805231882,
#                  u'tx_bytes-r': 3636,
#                  u'tx_dropped': 0,
#                  u'tx_errors': 0,
#                  u'tx_multicast': 816317,
#                  u'tx_packets': 288747752,
#                  u'up': True},
#                 {u'aggregated_by': False,
#                  u'autoneg': False,
#                  u'bytes-r': 0,
#                  u'enable': True,
#                  u'flowctrl_rx': False,
#                  u'flowctrl_tx': False,
#                  u'full_duplex': False,
#                  u'is_uplink': False,
#                  u'jumbo': True,
#                  u'mac_table': [],
#                  u'masked': False,
#                  u'media': u'GE',
#                  u'name': u'Secondary',
#                  u'op_mode': u'switch',
#                  u'poe_caps': 0,
#                  u'port_idx': 2,
#                  u'port_poe': False,
#                  u'portconf_id': u'56c87bd0b41038d25762ce8f',
#                  u'rx_broadcast': 0,
#                  u'rx_bytes': 0,
#                  u'rx_bytes-r': 0,
#                  u'rx_dropped': 0,
#                  u'rx_errors': 0,
#                  u'rx_multicast': 0,
#                  u'rx_packets': 0,
#                  u'speed': 0,
#                  u'stp_pathcost': 0,
#                  u'stp_state': u'forwarding',
#                  u'tx_broadcast': 0,
#                  u'tx_bytes': 0,
#                  u'tx_bytes-r': 0,
#                  u'tx_dropped': 0,
#                  u'tx_errors': 0,
#                  u'tx_multicast': 0,
#                  u'tx_packets': 0,
#                  u'up': False}],
# u'radio_table': [{u'antenna_gain': 6,
#                   u'builtin_ant_gain': 3,
#                   u'builtin_antenna': True,
#                   u'channel': u'auto',
#                   u'current_antenna_gain': 0,
#                   u'ht': u'20',
#                   u'max_txpower': 22,
#                   u'min_rssi_enabled': False,
#                   u'min_txpower': 6,
#                   u'name': u'wifi0',
#                   u'nss': 3,
#                   u'radio': u'ng',
#                   u'radio_caps': 16420,
#                   u'tx_power_mode': u'auto'},
#                  {u'antenna_gain': 6,
#                   u'builtin_ant_gain': 3,
#                   u'builtin_antenna': True,
#                   u'channel': u'auto',
#                   u'current_antenna_gain': 0,
#                   u'has_dfs': True,
#                   u'has_fccdfs': True,
#                   u'ht': u'40',
#                   u'is_11ac': True,
#                   u'max_txpower': 22,
#                   u'min_rssi_enabled': False,
#                   u'min_txpower': 6,
#                   u'name': u'wifi1',
#                   u'nss': 3,
#                   u'radio': u'na',
#                   u'radio_caps': 50479140,
#                   u'tx_power_mode': u'auto'}],
# u'rx_bytes': 400914825,
# u'rx_bytes-d': 106549,
# u'scan_radio_table': [],
# u'scanning': False,
# u'serial': u'F09FC27966C6',
# u'site_id': u'56c87bc1b41038d25762ce86',
# u'spectrum_scanning': False,
# u'ssh_session_table': [],
# u'stat': {u'ap': u'f0:9f:c2:79:66:c6',
#           u'bytes': 920700496.0,
#           u'datetime': u'2018-01-13T07:45:00Z',
#           u'duration': 96723000.0,
#           u'guest-rx_bytes': 0.0,
#           u'guest-rx_crypts': 0.0,
#           u'guest-rx_dropped': 0.0,
#           u'guest-rx_errors': 0.0,
#           u'guest-rx_frags': 0.0,
#           u'guest-rx_packets': 0.0,
#           u'guest-tx_bytes': 0.0,
#           u'guest-tx_dropped': 0.0,
#           u'guest-tx_errors': 0.0,
#           u'guest-tx_packets': 0.0,
#           u'guest-tx_retries': 0.0,
#           u'na-rx_bytes': 109717480.0,
#           u'na-rx_crypts': 299.0,
#           u'na-rx_dropped': 299.0,
#           u'na-rx_errors': 299.0,
#           u'na-rx_frags': 0.0,
#           u'na-rx_packets': 392320.0,
#           u'na-tx_bytes': 441552647.0,
#           u'na-tx_dropped': 246779.0,
#           u'na-tx_errors': 1723.0,
#           u'na-tx_packets': 444834.0,
#           u'na-tx_retries': 0.0,
#           u'ng-rx_bytes': 291197345.0,
#           u'ng-rx_crypts': 0.0,
#           u'ng-rx_dropped': 0.0,
#           u'ng-rx_errors': 0.0,
#           u'ng-rx_frags': 0.0,
#           u'ng-rx_packets': 353520.0,
#           u'ng-tx_bytes': 78233024.0,
#           u'ng-tx_dropped': 249906.0,
#           u'ng-tx_errors': 0.0,
#           u'ng-tx_packets': 483646.0,
#           u'ng-tx_retries': 19000.0,
#           u'o': u'ap',
#           u'oid': u'f0:9f:c2:79:66:c6',
#           u'rx_bytes': 400914825.0,
#           u'rx_crypts': 299.0,
#           u'rx_dropped': 299.0,
#           u'rx_errors': 299.0,
#           u'rx_frags': 0.0,
#           u'rx_packets': 745840.0,
#           u'site_id': u'56c87bc1b41038d25762ce86',
#           u'time': 1515829500000,
#           u'tx_bytes': 519785671.0,
#           u'tx_dropped': 496685.0,
#           u'tx_errors': 1723.0,
#           u'tx_packets': 928480.0,
#           u'tx_retries': 19000.0,
#           u'user-na-ath3-56c87f21b41038d25762ce95-rx_bytes': 5395457.0,
#           u'user-na-ath3-56c87f21b41038d25762ce95-rx_crypts': 65.0,
#           u'user-na-ath3-56c87f21b41038d25762ce95-rx_dropped': 65.0,
#           u'user-na-ath3-56c87f21b41038d25762ce95-rx_errors': 65.0,
#           u'user-na-ath3-56c87f21b41038d25762ce95-rx_packets': 47952.0,
#           u'user-na-ath3-56c87f21b41038d25762ce95-tx_bytes': 135360029.0,
#           u'user-na-ath3-56c87f21b41038d25762ce95-tx_dropped': 244479.0,
#           u'user-na-ath3-56c87f21b41038d25762ce95-tx_errors': 472.0,
#           u'user-na-ath3-56c87f21b41038d25762ce95-tx_packets': 98261.0,
#           u'user-na-ath4-56c96f62b41038d25762ceac-rx_bytes': 104322023.0,
#           u'user-na-ath4-56c96f62b41038d25762ceac-rx_crypts': 234.0,
#           u'user-na-ath4-56c96f62b41038d25762ceac-rx_dropped': 234.0,
#           u'user-na-ath4-56c96f62b41038d25762ceac-rx_errors': 234.0,
#           u'user-na-ath4-56c96f62b41038d25762ceac-rx_packets': 344368.0,
#           u'user-na-ath4-56c96f62b41038d25762ceac-tx_bytes': 306192618.0,
#           u'user-na-ath4-56c96f62b41038d25762ceac-tx_dropped': 2300.0,
#           u'user-na-ath4-56c96f62b41038d25762ceac-tx_errors': 1251.0,
#           u'user-na-ath4-56c96f62b41038d25762ceac-tx_packets': 346573.0,
#           u'user-na-rx_bytes': 109717480.0,
#           u'user-na-rx_crypts': 299.0,
#           u'user-na-rx_dropped': 299.0,
#           u'user-na-rx_errors': 299.0,
#           u'user-na-rx_frags': 0.0,
#           u'user-na-rx_packets': 392320.0,
#           u'user-na-tx_bytes': 441552647.0,
#           u'user-na-tx_dropped': 246779.0,
#           u'user-na-tx_errors': 1723.0,
#           u'user-na-tx_packets': 444834.0,
#           u'user-na-tx_retries': 0.0,
#           u'user-ng-ath0-56c87f21b41038d25762ce95-rx_bytes': 290630125.0,
#           u'user-ng-ath0-56c87f21b41038d25762ce95-rx_packets': 350006.0,
#           u'user-ng-ath0-56c87f21b41038d25762ce95-tx_bytes': 74484166.0,
#           u'user-ng-ath0-56c87f21b41038d25762ce95-tx_dropped': 4024.0,
#           u'user-ng-ath0-56c87f21b41038d25762ce95-tx_packets': 471029.0,
#           u'user-ng-ath0-56c87f21b41038d25762ce95-tx_retries': 18471.0,
#           u'user-ng-ath1-56c96f62b41038d25762ceac-rx_bytes': 567220.0,
#           u'user-ng-ath1-56c96f62b41038d25762ceac-rx_packets': 3514.0,
#           u'user-ng-ath1-56c96f62b41038d25762ceac-tx_bytes': 3748858.0,
#           u'user-ng-ath1-56c96f62b41038d25762ceac-tx_dropped': 245882.0,
#           u'user-ng-ath1-56c96f62b41038d25762ceac-tx_packets': 12617.0,
#           u'user-ng-ath1-56c96f62b41038d25762ceac-tx_retries': 529.0,
#           u'user-ng-rx_bytes': 291197345.0,
#           u'user-ng-rx_crypts': 0.0,
#           u'user-ng-rx_dropped': 0.0,
#           u'user-ng-rx_errors': 0.0,
#           u'user-ng-rx_frags': 0.0,
#           u'user-ng-rx_packets': 353520.0,
#           u'user-ng-tx_bytes': 78233024.0,
#           u'user-ng-tx_dropped': 249906.0,
#           u'user-ng-tx_errors': 0.0,
#           u'user-ng-tx_packets': 483646.0,
#           u'user-ng-tx_retries': 19000.0,
#           u'user-rx_bytes': 400914825.0,
#           u'user-rx_crypts': 299.0,
#           u'user-rx_dropped': 299.0,
#           u'user-rx_errors': 299.0,
#           u'user-rx_frags': 0.0,
#           u'user-rx_packets': 745840.0,
#           u'user-tx_bytes': 519785671.0,
#           u'user-tx_dropped': 496685.0,
#           u'user-tx_errors': 1723.0,
#           u'user-tx_packets': 928480.0,
#           u'user-tx_retries': 19000.0},
# u'state': 1,
# u'sys_stats': {u'loadavg_1': u'0.31',
#                u'loadavg_15': u'0.14',
#                u'loadavg_5': u'0.15',
#                u'mem_buffer': 0,
#                u'mem_total': 129302528,
#                u'mem_used': 73994240},
# u'system-stats': {u'cpu': u'2.5',
#                   u'mem': u'57.2',
#                   u'uptime': u'3515944'},
# u'tx_bytes': 519785671,
# u'tx_bytes-d': 44688,
# u'type': u'uap',
# u'upgradable': True,
# u'upgrade_to_firmware': u'3.9.19.8123',
# u'uplink': {u'full_duplex': True,
#             u'ip': u'0.0.0.0',
#             u'mac': u'f0:9f:c2:79:66:c6',
#             u'max_speed': 1000,
#             u'max_vlan': 96,
#             u'name': u'eth0',
#             u'netmask': u'0.0.0.0',
#             u'num_port': 2,
#             u'rx_bytes': 2353115011,
#             u'rx_bytes-r': 1245,
#             u'rx_dropped': 115929,
#             u'rx_errors': 0,
#             u'rx_multicast': 0,
#             u'rx_packets': 248011972,
#             u'speed': 1000,
#             u'tx_bytes': 1331282993,
#             u'tx_bytes-r': 3196,
#             u'tx_dropped': 0,
#             u'tx_errors': 0,
#             u'tx_packets': 288747750,
#             u'type': u'wire',
#             u'up': True,
#             u'uplink_mac': u'f0:9f:c2:0a:4a:ca',
#             u'uplink_remote_port': 4},
# u'uplink_table': [],
# u'uptime': 3515944,
# u'user-num_sta': 2,
# u'vap_table': [{u'ap_mac': u'f0:9f:c2:79:66:c6',
#                 u'bssid': u'f0:9f:c2:7a:66:c6',
#                 u'ccq': 950,
#                 u'channel': 11,
#                 u'essid': u'PNet',
#                 u'id': u'56c87f21b41038d25762ce95',
#                 u'is_guest': False,
#                 u'is_wep': False,
#                 u'map_id': u'59ecfc54b410f47d7f9665da',
#                 u'name': u'ath0',
#                 u'num_sta': 1,
#                 u'radio': u'ng',
#                 u'radio_name': u'wifi0',
#                 u'rx_bytes': 290630125,
#                 u'rx_crypts': 0,
#                 u'rx_dropped': 0,
#                 u'rx_errors': 0,
#                 u'rx_frags': 0,
#                 u'rx_nwids': 16758,
#                 u'rx_packets': 350006,
#                 u'site_id': u'56c87bc1b41038d25762ce86',
#                 u'state': u'RUN',
#                 u't': u'vap',
#                 u'tx_bytes': 74484166,
#                 u'tx_dropped': 5637,
#                 u'tx_errors': 0,
#                 u'tx_packets': 471029,
#                 u'tx_power': 17,
#                 u'tx_retries': 18012,
#                 u'up': True,
#                 u'usage': u'user',
#                 u'wlanconf_id': u'56c87f21b41038d25762ce95'},
#                {u'ap_mac': u'f0:9f:c2:79:66:c6',
#                 u'bssid': u'f2:9f:c2:7a:66:c6',
#                 u'ccq': 950,
#                 u'channel': 11,
#                 u'essid': u'MyNet',
#                 u'id': u'56c96f62b41038d25762ceac',
#                 u'is_guest': False,
#                 u'is_wep': False,
#                 u'map_id': u'59ecfc54b410f47d7f9665da',
#                 u'name': u'ath1',
#                 u'num_sta': 0,
#                 u'radio': u'ng',
#                 u'radio_name': u'wifi0',
#                 u'rx_bytes': 567220,
#                 u'rx_crypts': 0,
#                 u'rx_dropped': 0,
#                 u'rx_errors': 0,
#                 u'rx_frags': 0,
#                 u'rx_nwids': 16808,
#                 u'rx_packets': 3514,
#                 u'site_id': u'56c87bc1b41038d25762ce86',
#                 u'state': u'RUN',
#                 u't': u'vap',
#                 u'tx_bytes': 3748858,
#                 u'tx_dropped': 247497,
#                 u'tx_errors': 0,
#                 u'tx_packets': 12617,
#                 u'tx_power': 17,
#                 u'tx_retries': 0,
#                 u'up': True,
#                 u'usage': u'user',
#                 u'wlanconf_id': u'56c96f62b41038d25762ceac'},
#                {u'ap_mac': u'f0:9f:c2:79:66:c6',
#                 u'bssid': u'f2:9f:c2:7b:66:c6',
#                 u'ccq': 950,
#                 u'channel': 36,
#                 u'essid': u'PNet',
#                 u'extchannel': 1,
#                 u'id': u'56c87f21b41038d25762ce95',
#                 u'is_guest': False,
#                 u'is_wep': False,
#                 u'map_id': u'59ecfc54b410f47d7f9665da',
#                 u'name': u'ath3',
#                 u'num_sta': 0,
#                 u'radio': u'na',
#                 u'radio_name': u'wifi1',
#                 u'rx_bytes': 5395457,
#                 u'rx_crypts': 65,
#                 u'rx_dropped': 65,
#                 u'rx_errors': 65,
#                 u'rx_frags': 0,
#                 u'rx_nwids': 283,
#                 u'rx_packets': 47952,
#                 u'site_id': u'56c87bc1b41038d25762ce86',
#                 u'state': u'RUN',
#                 u't': u'vap',
#                 u'tx_bytes': 135360029,
#                 u'tx_dropped': 246066,
#                 u'tx_errors': 472,
#                 u'tx_packets': 98261,
#                 u'tx_power': 17,
#                 u'tx_retries': 0,
#                 u'up': True,
#                 u'usage': u'user',
#                 u'wlanconf_id': u'56c87f21b41038d25762ce95'},
#                {u'ap_mac': u'f0:9f:c2:79:66:c6',
#                 u'bssid': u'02:9f:c2:7b:66:c6',
#                 u'ccq': 333,
#                 u'channel': 36,
#                 u'essid': u'MyNet',
#                 u'extchannel': 1,
#                 u'id': u'56c96f62b41038d25762ceac',
#                 u'is_guest': False,
#                 u'is_wep': False,
#                 u'map_id': u'59ecfc54b410f47d7f9665da',
#                 u'name': u'ath4',
#                 u'num_sta': 1,
#                 u'radio': u'na',
#                 u'radio_name': u'wifi1',
#                 u'rx_bytes': 104322023,
#                 u'rx_crypts': 234,
#                 u'rx_dropped': 234,
#                 u'rx_errors': 234,
#                 u'rx_frags': 0,
#                 u'rx_nwids': 514,
#                 u'rx_packets': 344368,
#                 u'site_id': u'56c87bc1b41038d25762ce86',
#                 u'state': u'RUN',
#                 u't': u'vap',
#                 u'tx_bytes': 306192618,
#                 u'tx_dropped': 3888,
#                 u'tx_errors': 1251,
#                 u'tx_packets': 346573,
#                 u'tx_power': 17,
#                 u'tx_retries': 0,
#                 u'up': True,
#                 u'usage': u'user',
#                 u'wlanconf_id': u'56c96f62b41038d25762ceac'}],
# u'version': u'3.9.3.7537',
# u'vwireEnabled': True,
# u'vwire_table': [],
# u'wifi_caps': 16373,
# u'wlangroup_id_na': u'56c87bd0b41038d25762ce8d',
# u'wlangroup_id_ng': u'56c87bd0b41038d25762ce8d',
# u'x': 204.995287464656,
# u'x_authkey': u'b3a574c1ad366e9dbbef3031eb67c314',
# u'x_fingerprint': u'bc:d3:63:4a:25:a9:a2:ee:97:f5:a9:f6:44:18:bd:1b',
# u'x_has_ssh_hostkey': True,
# u'x_inform_authkey': u'b3a574c1ad366e9dbbef3031eb67c314',
# u'x_ssh_hostkey_fingerprint': u'bc:d3:63:4a:25:a9:a2:ee:97:f5:a9:f6:44:18:bd:1b',
# u'x_vwirekey': u'2fdd74ae184b4381e689649d2c2abcde',
# u'y': 207.83382422243167},
