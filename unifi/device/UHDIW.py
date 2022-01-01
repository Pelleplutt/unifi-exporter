from . import device

class UHDIW(device.Device):

    def __init__(self, site, data):
        super(UHDIW, self).__init__(site, data)

        self.radio = {}
        self.vap = []
        self.parse_radio(data['radio_table'])
        self.parse_stat(data.get('stat'))
        self.parse_uplink(data.get('uplink'))
        self.parse_vap_table(data.get('vap_table'))
        self.parse_sysstat(data.get('sys_stats'))

    def parse_radio(self, data):
        if data is not None:
            for radio in data:
                rstr = radio['radio']
                self.radio[rstr] = radio

    def parse_vap_table(self, data):
        if data is not None:
            for vap in data:
                self.vap.append(vap)
