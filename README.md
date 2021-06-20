# UniFi-Exporter
# ==============
Unifi Controller Metrics Exporter for Prometheus

+ Shoutout to [@c0psrul3](https://github.com/c0psrul3) for adding support for multiple device and extensions

+ UniFi-Exporter was tested with Ubiquiti's **UniFi Controller**
  collecting metrics for 8 devices in total:
  - 1 _CloudKey Gen2+_
  - 4 Switches: _USW-8-Lite-Poe_, _USW-16-Lite-Poe_, _USW-Flex_, _USW-Flex-Mini_
  - 3 Access Points: _UAP-AC-PRO_, _UAP-NanoHD_, _UAP-IWHD_

+ Device metrics are defined by their model names.
  Taking the In-wall Access Point for example: has device model **UHDIW**, see "./unifi/device/UHDIW.py"

### Installation
  Install requirements with pip
  ```sh
  python3 -m pip install --user --requirement ./requirements.txt
  ```

unifi-exporter uses the following environment variables:
- `API_URL`: port to use for the exporter, default `https://localhost:8443`
- `API_USERNAME`: Controller username, default `ubnt`
- `API_PASSWORD`: Controller password, default `ubnt`
- `METRICS_PORT`: Bind port for http metrics endpoint, default `9108`
- `LOGLEVEL`: Loglevel to use (see https://docs.python.org/3/library/logging.html#logging-levels), default `INFO`


### Metric Series
|  metric                        |  type      |  description          |
|:------------------------------:|:----------:|:---------------------:|
|  unifi_vap_tx_errors_total     |  counter   |  VAP TX errors        |
|  unifi_vap_rx_packets_total    |  counter   |  VAP RX packets       |
|  unifi_vap_tx_packets_total    |  counter   |  VAP TX packets       |
|  unifi_vap_rx_dropped_total    |  counter   |  VAP RX dropped       |
|  unifi_vap_tx_dropped_total    |  counter   |  VAP TX dropped       |
|  unifi_vap_num_sta             |  gauge     |  VAP Client count     |
|  unifi_uplink_rx_bytes_total   |  counter   |  Uplink RX bytes      |
|  unifi_uplink_tx_bytes_total   |  counter   |  Uplink TX bytes      |
|  unifi_uplink_rx_errors_total  |  counter   |  Uplink RX errors     |
|  unifi_uplink_tx_errors_total  |  counter   |  Uplink TX errors     |
|  unifi_uplink_rx_packets_total |  counter   |  Uplink RX packets    |
|  unifi_uplink_tx_packets_total |  counter   |  Uplink TX packets    |
|  unifi_uplink_rx_dropped_total |  counter   |  Uplink RX dropped    |
|  unifi_uplink_tx_dropped_total |  counter   |  Uplink TX dropped    |
|  unifi_loadavg_1               |  gauge     |  Loadavg 1            |
|  unifi_loadavg_5               |  gauge     |  Loadavg 5            |
|  unifi_loadavg_15              |  gauge     |  Loadavg 15           |
|  unifi_mem_total               |  gauge     |  Memory total         |
|  unifi_mem_used                |  gauge     |  Memory used          |
|  unifi_mem_buffer              |  gauge     |  Memory buffers       |
|  unifi_general_temperature     |  gauge     |  General temperature  |


### Dump raw metrics from UniFi Controller API
  execute script 'unifi-dump.py' for testing raw metrics
  ```sh
  API_URL=https://192.168.0.1 API_USERNAME=ubnt API_PASSWORD=ubnt python3 ./unifi-dump.py
  ```

### Start exporter listening on default port TCP/9108
  ```sh
  API_URL=https://192.168.0.3 API_USERNAME=ubnt API_PASSWORD=ubnt python3 unifi-exporter.py --port=9108
  ```

### Install Systemd Service Unit
  ```sh
  cp ./unifi-exporter.service /etc/systemd/system/unifi-exporter.service
  systemctl enable --now unifi-exporter.service
  ```