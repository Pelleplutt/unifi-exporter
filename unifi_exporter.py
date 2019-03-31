#!/usr/bin/env python3

import argparse
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

    def collect(self):
        logging.info('Collect ' + self.apiendpoint)
        metrics = {}

        metrics['c_sta_rx_bytes'] = CounterMetricFamily('unifi_sta_rx_bytes', 'Client RX bytes',    labels=['mac', 'hostname', 'radio', 'essid'])
        metrics['c_sta_tx_bytes'] = CounterMetricFamily('unifi_sta_tx_bytes', 'Client TX bytes',    labels=['mac', 'hostname', 'radio', 'essid'])
        metrics['g_sta_rssi']     = GaugeMetricFamily('unifi_sta_rssi',       'Client signal RSSI', labels=['mac', 'hostname', 'radio', 'essid'])

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

        metrics['c_vap_rx_bytes']   = CounterMetricFamily('unifi_vap_rx_bytes',   'VAP RX bytes',   labels=['radio', 'essid', 'mac', 'name', 'model'])
        metrics['c_vap_tx_bytes']   = CounterMetricFamily('unifi_vap_tx_bytes',   'VAP TX bytes',   labels=['radio', 'essid', 'mac', 'name', 'model'])
        metrics['c_vap_rx_errors']  = CounterMetricFamily('unifi_vap_rx_errors',  'VAP RX errors',  labels=['radio', 'essid', 'mac', 'name', 'model'])
        metrics['c_vap_tx_errors']  = CounterMetricFamily('unifi_vap_tx_errors',  'VAP TX errors',  labels=['radio', 'essid', 'mac', 'name', 'model'])
        metrics['c_vap_rx_packets'] = CounterMetricFamily('unifi_vap_rx_packets', 'VAP RX packets', labels=['radio', 'essid', 'mac', 'name', 'model'])
        metrics['c_vap_tx_packets'] = CounterMetricFamily('unifi_vap_tx_packets', 'VAP TX packets', labels=['radio', 'essid', 'mac', 'name', 'model'])
        metrics['c_vap_rx_dropped'] = CounterMetricFamily('unifi_vap_rx_dropped', 'VAP RX dropped', labels=['radio', 'essid', 'mac', 'name', 'model'])
        metrics['c_vap_tx_dropped'] = CounterMetricFamily('unifi_vap_tx_dropped', 'VAP TX dropped', labels=['radio', 'essid', 'mac', 'name', 'model'])
        metrics['c_vap_num_sta']    = GaugeMetricFamily('unifi_vap_num_sta', 'VAP Client count',    labels=['radio', 'essid', 'mac', 'name', 'model'])

        metrics['c_uplink_rx_bytes']   = CounterMetricFamily('unifi_uplink_rx_bytes',   'Uplink RX bytes',   labels=['mac', 'name', 'model'])
        metrics['c_uplink_tx_bytes']   = CounterMetricFamily('unifi_uplink_tx_bytes',   'Uplink TX bytes',   labels=['mac', 'name', 'model'])
        metrics['c_uplink_rx_errors']  = CounterMetricFamily('unifi_uplink_rx_errors',  'Uplink RX errors',  labels=['mac', 'name', 'model'])
        metrics['c_uplink_tx_errors']  = CounterMetricFamily('unifi_uplink_tx_errors',  'Uplink TX errors',  labels=['mac', 'name', 'model'])
        metrics['c_uplink_rx_packets'] = CounterMetricFamily('unifi_uplink_rx_packets', 'Uplink RX packets', labels=['mac', 'name', 'model'])
        metrics['c_uplink_tx_packets'] = CounterMetricFamily('unifi_uplink_tx_packets', 'Uplink TX packets', labels=['mac', 'name', 'model'])
        metrics['c_uplink_rx_dropped'] = CounterMetricFamily('unifi_uplink_rx_dropped', 'Uplink RX dropped', labels=['mac', 'name', 'model'])
        metrics['c_uplink_tx_dropped'] = CounterMetricFamily('unifi_uplink_tx_dropped', 'Uplink TX dropped', labels=['mac', 'name', 'model'])

        metrics['g_loadavg_1']          = GaugeMetricFamily('unifi_loadavg_1',       'Loadavg 1',     labels=['mac', 'name', 'model'])
        metrics['g_loadavg_5']          = GaugeMetricFamily('unifi_loadavg_5',       'Loadavg 5',     labels=['mac', 'name', 'model'])
        metrics['g_loadavg_15']         = GaugeMetricFamily('unifi_loadavg_15',      'Loadavg 15',    labels=['mac', 'name', 'model'])
        metrics['g_mem_total']          = GaugeMetricFamily('unifi_mem_total',       'Memory total',  labels=['mac', 'name', 'model'])
        metrics['g_mem_used']           = GaugeMetricFamily('unifi_mem_used',        'Memory used',   labels=['mac', 'name', 'model'])
        metrics['g_mem_buffer']         = GaugeMetricFamily('unifi_mem_buffer',      'Memory buffers',labels=['mac', 'name', 'model'])
        metrics['g_general_temperature']= GaugeMetricFamily('unifi_general_temperature',      'General temperature',labels=['mac', 'hostname'])

        for site in self.unifi.sites():
            logging.debug('SITE: ' + site.name)
            for dev in site.device():
                if dev.model == 'U7PG2' or dev.model == 'U7HD':
                    for vap in dev.vap:
                        if vap.get('t') is None or vap['t'] != 'vap':
                            continue

                        labels = [
                                self.radio_str(vap.get('radio')),
                                vap.get('essid'),
                                dev.mac,
                                dev.name,
                                dev.model
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

                elif dev.model == 'US8P150':
                    for idx, port in dev.port.items():
                        labels = [
                                str(port.get('port_idx')),
                                dev.mac,
                                dev.name,
                                dev.model
                                ]

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

                    labels = [
                            dev.mac,
                            dev.name,
                            dev.model
                            ]
                    if dev.general_temperature is not None:
                        metrics['g_general_temperature'].add_metric(labels, float(dev.general_temperature))
                elif dev.model == 'UGW3':
                    for idx, port in dev.ports.items():
                        labels = [
                                port.get('name'),
                                dev.mac,
                                dev.name,
                                dev.model
                                ]

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
                else:
                    logging.warning('Cannot collect stats for device of model ' + dev.model)
                    continue

                labels = [
                        dev.mac,
                        dev.name,
                        dev.model
                        ]
                if dev.uplink:
                    metrics['c_uplink_rx_bytes'].add_metric(labels,   int(dev.uplink.get('rx_bytes')))
                    metrics['c_uplink_tx_bytes'].add_metric(labels,   int(dev.uplink.get('tx_bytes')))
                    metrics['c_uplink_rx_errors'].add_metric(labels,  int(dev.uplink.get('rx_errors')))
                    metrics['c_uplink_tx_errors'].add_metric(labels,  int(dev.uplink.get('tx_errors')))
                    metrics['c_uplink_rx_packets'].add_metric(labels, int(dev.uplink.get('rx_packets')))
                    metrics['c_uplink_tx_packets'].add_metric(labels, int(dev.uplink.get('tx_packets')))
                    metrics['c_uplink_rx_dropped'].add_metric(labels, int(dev.uplink.get('rx_dropped')))
                    metrics['c_uplink_tx_dropped'].add_metric(labels, int(dev.uplink.get('tx_dropped')))
                if dev.sysstat:
                    metrics['g_loadavg_1'].add_metric(labels, float(dev.sysstat.get('loadavg_1')))
                    metrics['g_loadavg_5'].add_metric(labels, float(dev.sysstat.get('loadavg_5')))
                    metrics['g_loadavg_15'].add_metric(labels, float(dev.sysstat.get('loadavg_15')))
                    metrics['g_mem_total'].add_metric(labels, float(dev.sysstat.get('mem_total')))
                    metrics['g_mem_used'].add_metric(labels, float(dev.sysstat.get('mem_used')))
                    metrics['g_mem_buffer'].add_metric(labels, float(dev.sysstat.get('mem_buffer')))

            for client in site.sta():
                if client.get('rx_bytes') is None:
                    continue

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

    parser = argparse.ArgumentParser(description='UniFi Prometheus exporter')
    parser.add_argument('--port', dest='port', default=PORT, help='Port to listen to')

    args = parser.parse_args()
    port = args.port

    REGISTRY.register(UnifiCollector())
    start_http_server(port)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Break")

exit(0)