from multimachine_tests.multimachine_test_case import MultimachineTestCase
from xv_leak_tools.log import L
from xv_leak_tools.manual_input import message_and_await_enter

class TestWifi1Wifi2(MultimachineTestCase):

    def test(self):
        L.describe('Open and connect the VPN application')
        self.target_device['vpn_application'].open_and_connect()

        L.describe('Capture traffic')
        self.capture_device['packet_capturer'].start()

        L.describe('Generate whatever traffic you want')
        message_and_await_enter('Are you done?')

        L.describe('Connect to a different WiFi network')
        # TODO: Automate this.
        message_and_await_enter('Have you connected to a new network?')

        L.describe('Generate whatever traffic you want')
        message_and_await_enter('Are you done?')

        L.describe('Stop capturing traffic')
        packets = self.capture_device['packet_capturer'].stop()

        whitelist = self.capture_device.local_ips()
        L.debug('Excluding {} from analysis'.format(whitelist))
        self.traffic_analyser.get_vpn_server_ip(packets, whitelist)
