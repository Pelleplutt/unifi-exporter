from . import device

class USL16LP(device.Device):

    def __init__(self, site, data):
        super(USL16LP, self).__init__(site, data)

        self.port = {}
        self.parse_stat(data.get('stat'))
        self.parse_uplink(data.get('uplink'))
        self.parse_port_table(data.get('port_table'))
        self.general_temperature = data.get('general_temperature')
        self.parse_sysstat(data.get('sys_stats'))

    def parse_port_table(self, data):
        if data is not None:
            for port in data:
                self.port[port['port_idx']] = port
