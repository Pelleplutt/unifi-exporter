from . import device

class U7NHD(device.Device):

    def __init__(self, site, data):
        super(U7NHD, self).__init__(site, data)

        self.radio = {}
        self.vap = []
        self.parse_radio(data['radio_table'])
        self.parse_stat(data['stat'])
        self.parse_uplink(data.get('uplink'))
        self.parse_vap_table(data['vap_table'])
        self.parse_sysstat(data.get('sys_stats'))

    def parse_radio(self, data):
        for radio in data:
            rstr = radio['radio']
            self.radio[rstr] = radio

    def parse_vap_table(self, data):
        for vap in data:
            self.vap.append(vap)
