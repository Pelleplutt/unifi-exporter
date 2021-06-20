#!/usr/bin/env python3

import logging
import os
import pprint
from prometheus_client import start_http_server, Gauge
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY
import time
from unifi import unifi

PORT = 9108

class UnifiCollector(object):
    def __init__(self):
        self.apiendpoint = os.environ.get('API_URL', 'https://localhost:8443')
        self.apiusername = os.environ.get('API_USERNAME', 'ubnt')
        self.apipassword = os.environ.get('API_PASSWORD', 'ubnt')
        self.checkconfig()

        self.unifi = unifi.UniFi(self.apiendpoint, self.apiusername, self.apipassword)

    def checkconfig(self):
        if self.apiendpoint is None:
            raise AssertionError('API/URL is required in configuration')
        if self.apiusername is None or self.apipassword is None:
            raise AssertionError('API/Username and API/Password is required in configuration')

    def metrics_setup_device_info(self, metrics):
        metrics['device_info'] = GaugeMetricFamily('unifi_device_info', 'Device info', labels=[
                                                'name',
                                                'hostname',
                                                'ip_address',
                                                'mac',
                                                'type',
                                                'model',
                                                'device_id',
                                                'serial',
                                                'version',
                                                'upgradable',
                                                'adopted',
                                                'architecture',
                                                'cfgversion',
                                                'kernel_version',
                                                'board_rev',
                                                'provisioned_at',
                                                'last_seen',
                                                'connected_at',
                                                'uptime'
                                                #'overheating', 'power_source', 'power_source_voltage',
                                                #'next_heartbeat_at', 'considered_lost_at',
                                                #'syslog_key', 'setup_id',
                                                #'stp_version', 'stp_priority', 'x_ssh_hostkey_fingerprint',
                                                #'state', 'has_fan', 'has_temperature', 'site_id'
                                                #'uplink_up', 'uplink_type', 'uplink_full_duplex', 'uplink_speed',
                                                #'uplink_num_port', 'uplink_port_idx', 'uplink_remote_port', 'uplink_ip', 'uplink_mac'
                                            ])
        metrics['device_up']        = GaugeMetricFamily('unifi_device_up',        'Device up',   labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['device_last_seen'] = GaugeMetricFamily('unifi_device_last_seen', 'Device info', labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['device_uptime']    = GaugeMetricFamily('unifi_device_uptime',    'Device info', labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])


    def metrics_setup_sta(self, metrics):
        metrics['c_sta_rx_bytes'] = CounterMetricFamily('unifi_sta_rx_bytes', 'Client RX bytes',    labels=['mac', 'hostname', 'radio', 'essid'])
        metrics['c_sta_tx_bytes'] = CounterMetricFamily('unifi_sta_tx_bytes', 'Client TX bytes',    labels=['mac', 'hostname', 'radio', 'essid'])
        metrics['g_sta_rssi']     = GaugeMetricFamily('unifi_sta_rssi',       'Client signal RSSI', labels=['mac', 'hostname', 'radio', 'essid'])


    def metrics_setup_ports(self, metrics):
        metrics['c_port_rx_bytes']   = CounterMetricFamily('unifi_port_rx_bytes',   'Port RX bytes',   labels=['port', 'mac', 'name', 'model'])
        metrics['c_port_tx_bytes']   = CounterMetricFamily('unifi_port_tx_bytes',   'Port TX bytes',   labels=['port', 'mac', 'name', 'model'])
        metrics['c_port_rx_errors']  = CounterMetricFamily('unifi_port_rx_errors',  'Port RX errors',  labels=['port', 'mac', 'name', 'model'])
        metrics['c_port_tx_errors']  = CounterMetricFamily('unifi_port_tx_errors',  'Port TX errors',  labels=['port', 'mac', 'name', 'model'])
        metrics['c_port_rx_packets'] = CounterMetricFamily('unifi_port_rx_packets', 'Port RX packets', labels=['port', 'mac', 'name', 'model'])
        metrics['c_port_tx_packets'] = CounterMetricFamily('unifi_port_tx_packets', 'Port TX packets', labels=['port', 'mac', 'name', 'model'])
        metrics['c_port_rx_dropped'] = CounterMetricFamily('unifi_port_rx_dropped', 'Port RX dropped', labels=['port', 'mac', 'name', 'model'])
        metrics['c_port_tx_dropped'] = CounterMetricFamily('unifi_port_tx_dropped', 'Port TX dropped', labels=['port', 'mac', 'name', 'model'])

        metrics['g_port_poe_current'] = GaugeMetricFamily('unifi_port_poe_current', 'Port POE current', labels=['port', 'mac', 'name', 'model'])
        metrics['g_port_poe_power']   = GaugeMetricFamily('unifi_port_poe_power',   'Port POE power',   labels=['port', 'mac', 'name', 'model'])
        metrics['g_port_poe_voltage'] = GaugeMetricFamily('unifi_port_poe_voltage', 'Port POE voltage', labels=['port', 'mac', 'name', 'model'])


    def metrics_setup_vap(self, metrics):
        metrics['c_vap_rx_bytes']   = CounterMetricFamily('unifi_vap_rx_bytes',   'VAP RX bytes',   labels=['radio', 'essid', 'name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['c_vap_tx_bytes']   = CounterMetricFamily('unifi_vap_tx_bytes',   'VAP TX bytes',   labels=['radio', 'essid', 'name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['c_vap_rx_errors']  = CounterMetricFamily('unifi_vap_rx_errors',  'VAP RX errors',  labels=['radio', 'essid', 'name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['c_vap_tx_errors']  = CounterMetricFamily('unifi_vap_tx_errors',  'VAP TX errors',  labels=['radio', 'essid', 'name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['c_vap_rx_packets'] = CounterMetricFamily('unifi_vap_rx_packets', 'VAP RX packets', labels=['radio', 'essid', 'name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['c_vap_tx_packets'] = CounterMetricFamily('unifi_vap_tx_packets', 'VAP TX packets', labels=['radio', 'essid', 'name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['c_vap_rx_dropped'] = CounterMetricFamily('unifi_vap_rx_dropped', 'VAP RX dropped', labels=['radio', 'essid', 'name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['c_vap_tx_dropped'] = CounterMetricFamily('unifi_vap_tx_dropped', 'VAP TX dropped', labels=['radio', 'essid', 'name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['c_vap_num_sta']    = GaugeMetricFamily('unifi_vap_num_sta', 'VAP Client count',    labels=['radio', 'essid', 'name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])


    def metrics_setup_uplink(self, metrics):
        metrics['c_uplink_rx_bytes']   = CounterMetricFamily('unifi_uplink_rx_bytes',   'Uplink RX bytes',   labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['c_uplink_tx_bytes']   = CounterMetricFamily('unifi_uplink_tx_bytes',   'Uplink TX bytes',   labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['c_uplink_rx_errors']  = CounterMetricFamily('unifi_uplink_rx_errors',  'Uplink RX errors',  labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['c_uplink_tx_errors']  = CounterMetricFamily('unifi_uplink_tx_errors',  'Uplink TX errors',  labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['c_uplink_rx_packets'] = CounterMetricFamily('unifi_uplink_rx_packets', 'Uplink RX packets', labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['c_uplink_tx_packets'] = CounterMetricFamily('unifi_uplink_tx_packets', 'Uplink TX packets', labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['c_uplink_rx_dropped'] = CounterMetricFamily('unifi_uplink_rx_dropped', 'Uplink RX dropped', labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['c_uplink_tx_dropped'] = CounterMetricFamily('unifi_uplink_tx_dropped', 'Uplink TX dropped', labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])


    def metrics_setup_sysstat(self, metrics):
        metrics['g_loadavg_1']          = GaugeMetricFamily('unifi_loadavg_1',       'Loadavg 1',     labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['g_loadavg_5']          = GaugeMetricFamily('unifi_loadavg_5',       'Loadavg 5',     labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['g_loadavg_15']         = GaugeMetricFamily('unifi_loadavg_15',      'Loadavg 15',    labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['g_mem_total']          = GaugeMetricFamily('unifi_mem_total',       'Memory total',  labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['g_mem_used']           = GaugeMetricFamily('unifi_mem_used',        'Memory used',   labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['g_mem_buffer']         = GaugeMetricFamily('unifi_mem_buffer',      'Memory buffers',labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])
        metrics['g_general_temperature']= GaugeMetricFamily('unifi_general_temperature',      'General temperature',labels=['name', 'hostname', 'ip_address', 'mac', 'type', 'model', 'device_id', 'serial'])


    '''
        labels=[
            'name',
            'hostname',
            'ip_address', 'mac',
            'type', 'model',
            'device_id', 'serial',
            'version', 'upgradable',
            'adopted', 'architecture',
            'cfgversion', 'kernel_version',
            'board_rev', 'provisioned_at',
            'last_seen', 'connected_at',
            'uptime'
            ]
    '''
    def add_metric_device_info(self, dev, metrics):
        labels = [dev.name,
                  dev.hostname,
                  dev.ip_address, dev.mac,
                  dev.type, dev.model,
                  dev.device_id, dev.serial,
                  dev.version, dev.upgradable,
                  dev.adopted, dev.architecture,
                  dev.cfgversion, dev.kernel_version,
                  dev.board_rev, dev.provisioned_at,
                  dev.last_seen, dev.connected_at,
                  dev.uptime
                  ]
        if dev.adopted:
            metrics['device_info'].add_metric(labels, 1)
        else:
            metrics['device_info'].add_metric(labels, 0)


    def add_metric_device_up(self, dev, metrics):
        labels = [  dev.name, dev.hostname,
                    dev.ip_address, dev.mac,
                    dev.type, dev.model,
                    dev.device_id, dev.serial
                    ]
        metrics['device_uptime'].add_metric(labels, dev.uptime)
        metrics['device_last_seen'].add_metric(labels, dev.last_seen)

        last_seen_ago = int(time.time()) - int(dev.last_seen)
        if bool(dev.adopted) and (int(dev.uptime) > 0) and (last_seen_ago < 100):
            metrics['device_up'].add_metric(labels, 1)
        else:
            metrics['device_up'].add_metric(labels, 0)


    def add_metric_u7(self, dev, metrics):
        for vap in dev.vap:
            if vap.get('t') is None or vap['t'] != 'vap':
                continue
            labels = [  self.radio_str(vap.get('radio')),
                        vap.get('essid'),
                        dev.name, dev.hostname,
                        dev.ip_address, dev.mac,
                        dev.type, dev.model,
                        dev.device_id, dev.serial
                        ]
            if vap.get('rx_bytes') is not None:
                metrics['c_vap_rx_bytes'].add_metric(labels,   int(vap.get('rx_bytes')))
                metrics['c_vap_rx_errors'].add_metric(labels,  int(vap.get('rx_errors')))
                metrics['c_vap_rx_packets'].add_metric(labels, int(vap.get('rx_packets')))
                metrics['c_vap_rx_dropped'].add_metric(labels, int(vap.get('rx_dropped')))

            if vap.get('tx_bytes') is not None:
                metrics['c_vap_tx_bytes'].add_metric(labels,   int(vap.get('tx_bytes')))
                metrics['c_vap_tx_errors'].add_metric(labels,  int(vap.get('tx_errors')))
                metrics['c_vap_tx_packets'].add_metric(labels, int(vap.get('tx_packets')))
                metrics['c_vap_tx_dropped'].add_metric(labels, int(vap.get('tx_dropped')))

            if vap.get('num_sta') is not None:
                metrics['c_vap_num_sta'].add_metric(labels,    int(vap.get('num_sta')))


    def add_metric_us8(self, dev, metrics):
        for idx, port in dev.port.items():
            labels = [ str(port.get('port_idx')), dev.mac, dev.name, dev.model ]

            if port.get('rx_bytes') is not None:
                metrics['c_port_rx_bytes'].add_metric(labels,   int(port.get('rx_bytes')))
                metrics['c_port_rx_errors'].add_metric(labels,  int(port.get('rx_errors')))
                metrics['c_port_rx_packets'].add_metric(labels, int(port.get('rx_packets')))
                metrics['c_port_rx_dropped'].add_metric(labels, int(port.get('rx_dropped')))

            if port.get('tx_bytes') is not None:
                metrics['c_port_tx_bytes'].add_metric(labels,   int(port.get('tx_bytes')))
                metrics['c_port_tx_errors'].add_metric(labels,  int(port.get('tx_errors')))
                metrics['c_port_tx_packets'].add_metric(labels, int(port.get('tx_packets')))
                metrics['c_port_tx_dropped'].add_metric(labels, int(port.get('tx_dropped')))

            if port.get('poe_current') is not None:
                metrics['g_port_poe_current'].add_metric(labels, float(port.get('poe_current')))
                metrics['g_port_poe_power'].add_metric(labels,   float(port.get('poe_power')))
                metrics['g_port_poe_voltage'].add_metric(labels, float(port.get('poe_voltage')))

        labels = [  dev.name, dev.hostname,
                    dev.ip_address, dev.mac,
                    dev.type, dev.model,
                    dev.device_id, dev.serial
                    ]
        if dev.general_temperature is not None:
            metrics['g_general_temperature'].add_metric(labels, float(dev.general_temperature))


    def add_metric_ugw3(self, dev, metrics):
        for idx, port in dev.ports.items():
            labels = [ port.get('name'), dev.mac, dev.name, dev.model ]

            if port.get('rx_bytes') is not None:
                metrics['c_port_rx_bytes'].add_metric(labels,   int(port.get('rx_bytes')))
                metrics['c_port_rx_errors'].add_metric(labels,  int(port.get('rx_errors')))
                metrics['c_port_rx_packets'].add_metric(labels, int(port.get('rx_packets')))
                metrics['c_port_rx_dropped'].add_metric(labels, int(port.get('rx_dropped')))

            if port.get('tx_bytes') is not None:
                metrics['c_port_tx_bytes'].add_metric(labels,   int(port.get('tx_bytes')))
                metrics['c_port_tx_errors'].add_metric(labels,  int(port.get('tx_errors')))
                metrics['c_port_tx_packets'].add_metric(labels, int(port.get('tx_packets')))
                metrics['c_port_tx_dropped'].add_metric(labels, int(port.get('tx_dropped')))


    def add_metric_common_uplink(self, dev, metrics):
        if dev.uplink:
            labels = [  dev.name, dev.hostname,
                        dev.ip_address, dev.mac,
                        dev.type, dev.model,
                        dev.device_id, dev.serial
                        ]
            metrics['c_uplink_rx_bytes'].add_metric(labels,   int(dev.uplink.get('rx_bytes', 0)))
            metrics['c_uplink_tx_bytes'].add_metric(labels,   int(dev.uplink.get('tx_bytes', 0)))
            metrics['c_uplink_rx_errors'].add_metric(labels,  int(dev.uplink.get('rx_errors', 0)))
            metrics['c_uplink_tx_errors'].add_metric(labels,  int(dev.uplink.get('tx_errors', 0)))
            metrics['c_uplink_rx_packets'].add_metric(labels, int(dev.uplink.get('rx_packets', 0)))
            metrics['c_uplink_tx_packets'].add_metric(labels, int(dev.uplink.get('tx_packets', 0)))
            metrics['c_uplink_rx_dropped'].add_metric(labels, int(dev.uplink.get('rx_dropped', 0)))
            metrics['c_uplink_tx_dropped'].add_metric(labels, int(dev.uplink.get('tx_dropped', 0)))


    def add_metric_common_sysstat(self, dev, metrics):
        if dev.sysstat:
            labels = [  dev.name, dev.hostname,
                        dev.ip_address, dev.mac,
                        dev.type, dev.model,
                        dev.device_id, dev.serial
                        ]
            metrics['g_loadavg_1'].add_metric(labels, float(dev.sysstat.get('loadavg_1', 0.0)))
            metrics['g_loadavg_5'].add_metric(labels, float(dev.sysstat.get('loadavg_5', 0.0)))
            metrics['g_loadavg_15'].add_metric(labels, float(dev.sysstat.get('loadavg_15', 0.0)))
            metrics['g_mem_total'].add_metric(labels, float(dev.sysstat.get('mem_total', 0.0)))
            metrics['g_mem_used'].add_metric(labels, float(dev.sysstat.get('mem_used', 0.0)))
            metrics['g_mem_buffer'].add_metric(labels, float(dev.sysstat.get('mem_buffer', 0.0)))


    def add_metric_site_sta(self, client, metrics):
        if client.get('rx_bytes') is None:
            return

        labels = [
                    client.get('mac'),
                    client.get('hostname') or client.get('mac'),
                    self.radio_str(client.get('radio')) or '',
                    client.get('essid') or ''
                ]

        metrics['c_sta_rx_bytes'].add_metric(labels, int(client.get('rx_bytes')))
        metrics['c_sta_tx_bytes'].add_metric(labels, int(client.get('tx_bytes')))
        if client.get('rssi') is not None:
            metrics['g_sta_rssi'].add_metric(labels, int(client.get('rssi')))


    def collect(self):
        logging.info('Collect ' + self.apiendpoint)
        metrics = {}

        self.metrics_setup_device_info(metrics)
        self.metrics_setup_sta(metrics)
        self.metrics_setup_ports(metrics)
        self.metrics_setup_vap(metrics)
        self.metrics_setup_uplink(metrics)
        self.metrics_setup_sysstat(metrics)

        for site in self.unifi.sites():
            logging.debug('SITE: ' + site.name)
            for dev in site.device():
                if dev.model in ('U7PG2', 'U7HD', 'U7NHD', 'U7LT', 'UHDIW'):
                    self.add_metric_device_info(dev, metrics)
                    self.add_metric_device_up(dev, metrics)
                    self.add_metric_u7(dev, metrics)
                elif dev.model in ('US8P150', 'USL8LP', 'USL16LP', 'USF5P', 'USMINI'):
                    self.add_metric_device_info(dev, metrics)
                    self.add_metric_device_up(dev, metrics)
                    self.add_metric_us8(dev, metrics)
                elif dev.model == 'UGW3':
                    self.add_metric_ugw3(dev, metrics)
                else:
                    logging.warning('Cannot collect stats for device of model ' + dev.model)
                    continue

                self.add_metric_common_uplink(dev, metrics)
                self.add_metric_common_sysstat(dev, metrics)

            for client in site.sta():
                self.add_metric_site_sta(client, metrics)

        for key, val in metrics.items():
            yield val

    def radio_str(self, s):
        if s is None:
            return None
        elif s == 'na':
            return '5'
        elif s == 'ng':
            return '2.4'
        else:
            return s

if __name__ == '__main__':

    loglevel = os.environ.get('LOGLEVEL', 'INFO').upper()
    logging.basicConfig(format='%(levelname)s - %(message)s', level=loglevel)

    port = int(os.environ.get('METRICS_PORT', PORT))

    REGISTRY.register(UnifiCollector())
    start_http_server(port)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.warning("Break")

exit(0)
