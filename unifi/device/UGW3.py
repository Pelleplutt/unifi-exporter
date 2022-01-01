from . import device


class UGW3(device.Device):

    def __init__(self, site, data):
        super(UGW3, self).__init__(site, data)

        self.networks = {}
        self.ports = {}
        self.parse_network_table(data['network_table'])
        self.parse_port_table(data.get('port_table'))
        self.parse_stat(data.get('stat'))
        self.parse_sysstat(data.get('sys_stats'))
        self.parse_uplink(data.get('uplink'))

    def parse_network_table(self, data):
        if data is not None:
            for network in data:
                self.networks[network['name']] = network

    def parse_port_table(self, data):
        if data is not None:
            for port in data:
                self.ports[port['name']] = port

# {'_id': '5c6aed452372c365f028d988',
#  '_uptime': 6514,
#  'adoptable_when_upgraded': False,
#  'adopted': True,
#  'board_rev': 16,
#  'bytes': 480097588,
#  'cfgversion': '44966b0781a9e2f2',
#  'config_network': {'ip': '192.168.1.1', 'type': 'dhcp'},
#  'connect_request_ip': '192.168.1.1',
#  'connect_request_port': '33149',
#  'device_id': '5c6aed452372c365f028d988',
#  'ethernet_overrides': [{'ifname': 'eth1', 'networkgroup': 'LAN'},
#                         {'ifname': 'eth0', 'networkgroup': 'WAN'}],
#  'ethernet_table': [{'mac': 'b4:fb:e4:8a:8b:5b',
#                      'name': 'eth0',
#                      'num_port': 1},
#                     {'mac': 'b4:fb:e4:8a:8b:5c',
#                      'name': 'eth1',
#                      'num_port': 1},
#                     {'mac': 'b4:fb:e4:8a:8b:5d',
#                      'name': 'eth2',
#                      'num_port': 1}],
#  'fw_caps': 184323,
#  'guest-num_sta': 0,
#  'guest_token': '467A5CC43ADD29B551798D03CD790424',
#  'hw_caps': 0,
#  'inform_ip': '192.168.1.3',
#  'inform_url': 'http://192.168.1.3:8080/inform',
#  'ip': '46.59.53.201',
#  'known_cfgversion': '44966b0781a9e2f2',
#  'last_seen': 1550518719,
#  'led_override': 'default',
#  'led_override_color': '#0000ff',
#  'led_override_color_brightness': 100,
#  'license_state': 'registered',
#  'locating': False,
#  'mac': 'b4:fb:e4:8a:8b:5b',
#  'model': 'UGW3',
#  'name': 'hemma-usg',
#  'network_table': [{'_id': '56c87bd0b41038d25762ce8b',
#                     'attr_hidden_id': 'LAN',
#                     'attr_no_delete': True,
#                     'dhcp_relay_enabled': False,
#                     'dhcpd_dns_enabled': False,
#                     'dhcpd_enabled': True,
#                     'dhcpd_gateway_enabled': False,
#                     'dhcpd_ip_1': '',
#                     'dhcpd_leasetime': '86400',
#                     'dhcpd_start': '192.168.1.6',
#                     'dhcpd_stop': '192.168.1.254',
#                     'dhcpd_time_offset_enabled': False,
#                     'dhcpd_unifi_controller': '192.158.1.3',
#                     'dhcpd_wins_enabled': False,
#                     'dhcpguard_enabled': False,
#                     'domain_name': 'localdomain',
#                     'enabled': True,
#                     'igmp_snooping': False,
#                     'ip': '192.168.1.1',
#                     'ip_subnet': '192.168.1.1/24',
#                     'ipv6_interface_type': 'none',
#                     'is_guest': False,
#                     'is_nat': True,
#                     'mac': 'b4:fb:e4:8a:8b:5c',
#                     'name': 'LAN',
#                     'networkgroup': 'LAN',
#                     'num_sta': 14,
#                     'purpose': 'corporate',
#                     'rx_bytes': 410644212,
#                     'rx_packets': 445131,
#                     'site_id': '56c87bc1b41038d25762ce86',
#                     'tx_bytes': 62656236,
#                     'tx_packets': 291197,
#                     'up': 'true',
#                     'vlan_enabled': False}],
#  'num_desktop': 0,
#  'num_handheld': 0,
#  'num_mobile': 0,
#  'num_sta': 20,
#  'outdoor_mode_override': 'default',
#  'port_table': [{'dns': ['213.80.98.2', '213.80.101.3'],
#                  'enable': True,
#                  'full_duplex': True,
#                  'gateway': '46.59.53.1',
#                  'ifname': 'eth0',
#                  'ip': '46.59.53.201',
#                  'mac': 'b4:fb:e4:8a:8b:5b',
#                  'name': 'wan',
#                  'netmask': '255.255.255.0',
#                  'rx_bytes': 418329925,
#                  'rx_dropped': 0,
#                  'rx_errors': 0,
#                  'rx_multicast': 52,
#                  'rx_packets': 446719,
#                  'speed': 1000,
#                  'tx_bytes': 61767663,
#                  'tx_dropped': 0,
#                  'tx_errors': 0,
#                  'tx_packets': 276151,
#                  'up': True},
#                 {'enable': True,
#                  'full_duplex': True,
#                  'ifname': 'eth1',
#                  'ip': '192.168.1.1',
#                  'mac': 'b4:fb:e4:8a:8b:5c',
#                  'name': 'lan',
#                  'netmask': '255.255.255.0',
#                  'rx_bytes': 92770443,
#                  'rx_dropped': 2,
#                  'rx_errors': 0,
#                  'rx_multicast': 4065,
#                  'rx_packets': 664055,
#                  'speed': 1000,
#                  'tx_bytes': 445145337,
#                  'tx_dropped': 0,
#                  'tx_errors': 0,
#                  'tx_packets': 818604,
#                  'up': True},
#                 {'enable': False,
#                  'full_duplex': False,
#                  'ifname': 'eth2',
#                  'ip': '0.0.0.0',
#                  'mac': 'b4:fb:e4:8a:8b:5d',
#                  'name': 'lan2',
#                  'netmask': '0.0.0.0',
#                  'rx_bytes': 0,
#                  'rx_dropped': 0,
#                  'rx_errors': 0,
#                  'rx_multicast': 0,
#                  'rx_packets': 0,
#                  'speed': 0,
#                  'tx_bytes': 0,
#                  'tx_dropped': 0,
#                  'tx_errors': 0,
#                  'tx_packets': 0,
#                  'up': False}],
#  'required_version': '4.0.0',
#  'rollupgrade': False,
#  'rx_bytes': 61767663,
#  'serial': 'B4FBE48A8B5B',
#  'site_id': '56c87bc1b41038d25762ce86',
#  'speedtest-status': {'latency': 0,
#                       'rundate': 0,
#                       'runtime': 0,
#                       'status_download': 0,
#                       'status_ping': 0,
#                       'status_summary': 0,
#                       'status_upload': 0,
#                       'xput_download': 0.0,
#                       'xput_upload': 0.0},
#  'speedtest-status-saved': True,
#  'stat': {'datetime': '2019-02-18T18:05:00Z',
#           'duration': 5515000.0,
#           'gw': 'b4:fb:e4:8a:8b:5b',
#           'lan-rx_bytes': 90213064.0,
#           'lan-rx_packets': 644049.0,
#           'lan-tx_bytes': 430074897.0,
#           'lan-tx_packets': 799798.0,
#           'o': 'gw',
#           'oid': 'b4:fb:e4:8a:8b:5b',
#           'site_id': '56c87bc1b41038d25762ce86',
#           'time': 1550513100000,
#           'wan-rx_bytes': 405245946.0,
#           'wan-rx_packets': 430612.0,
#           'wan-tx_bytes': 59940857.0,
#           'wan-tx_packets': 261577.0},
#  'state': 1,
#  'sys_stats': {'loadavg_1': '0.00',
#                'loadavg_15': '0.05',
#                'loadavg_5': '0.03',
#                'mem_buffer': 28340224,
#                'mem_total': 507428864,
#                'mem_used': 242642944},
#  'system-stats': {'cpu': '0', 'mem': '21', 'uptime': '6408'},
#  'two_phase_adopt': False,
#  'tx_bytes': 418329925,
#  'type': 'ugw',
#  'unitel_token': '',
#  'unitel_url': '',
#  'unsupported': False,
#  'unsupported_reason': 0,
#  'upgradable': False,
#  'uplink': {'bytes-r': 1417,
#             'drops': 0,
#             'enable': True,
#             'full_duplex': True,
#             'gateways': ['46.59.53.1'],
#             'ip': '46.59.53.201',
#             'latency': 1,
#             'mac': 'b4:fb:e4:8a:8b:5b',
#             'max_speed': 1000,
#             'name': 'eth0',
#             'nameservers': ['213.80.98.2', '213.80.101.3'],
#             'netmask': '255.255.255.0',
#             'num_port': 1,
#             'rx_bytes': 418329925,
#             'rx_bytes-r': 732,
#             'rx_dropped': 0,
#             'rx_errors': 0,
#             'rx_multicast': 52,
#             'rx_packets': 446719,
#             'speed': 1000,
#             'speedtest_lastrun': 0,
#             'speedtest_ping': 0,
#             'speedtest_status': 'Idle',
#             'tx_bytes': 61767663,
#             'tx_bytes-r': 684,
#             'tx_dropped': 0,
#             'tx_errors': 0,
#             'tx_packets': 276151,
#             'type': 'wire',
#             'up': True,
#             'uptime': 6373,
#             'xput_down': 0.0,
#             'xput_up': 0.0},
#  'uptime': 6514,
#  'use_custom_config': False,
#  'user-num_sta': 20,
#  'usg_caps': 262143,
#  'version': '4.4.36.5146617',
#  'wan1': {'bytes-r': 1417,
#           'dns': ['213.80.98.2', '213.80.101.3'],
#           'enable': True,
#           'full_duplex': True,
#           'gateway': '46.59.53.1',
#           'ifname': 'eth0',
#           'ip': '46.59.53.201',
#           'mac': 'b4:fb:e4:8a:8b:5b',
#           'max_speed': 1000,
#           'name': 'wan',
#           'netmask': '255.255.255.0',
#           'rx_bytes': 418329925,
#           'rx_bytes-r': 732,
#           'rx_dropped': 0,
#           'rx_errors': 0,
#           'rx_multicast': 52,
#           'rx_packets': 446719,
#           'speed': 1000,
#           'tx_bytes': 61767663,
#           'tx_bytes-r': 684,
#           'tx_dropped': 0,
#           'tx_errors': 0,
#           'tx_packets': 276151,
#           'type': 'wire',
#           'up': True},
#  'x_aes_gcm': True,
#  'x_authkey': '...',
#  'x_fingerprint': '1d:ac:71:ae:d5:4a:30:de:6e:94:39:04:52:55:97:17',
#  'x_has_ssh_hostkey': True,
#  'x_inform_authkey': '...',
#  'x_ssh_hostkey_fingerprint': 'fa:8a:6f:22:9d:82:8c:84:90:92:77:d4:15:ac:d3:7d'},
