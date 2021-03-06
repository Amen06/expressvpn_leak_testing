from multimachine_tests.multimachine_test_case import MultimachineTestCase
from xv_leak_tools.log import L
from xv_leak_tools.manual_input import message_and_await_enter

class TestWifiOffUpstreamWifi(MultimachineTestCase):

    def test(self):
        L.describe('Open and connect the VPN application')
        self.target_device['vpn_application'].open_and_connect()

        L.describe('Capture traffic')
        self.capture_device['packet_capturer'].start()

        L.describe('Generate whatever traffic you want')
        message_and_await_enter('Are you done?')

        L.describe('Disconnect WiFi upstream')
        # TODO: self.upstream.disable()?
        message_and_await_enter('Unplug the cable from the router')

        message_and_await_enter('Wait until the application has noticed (or however long you want)')

        L.describe('Connect WiFi upstream')
        message_and_await_enter('Plug the cable back in')

        L.describe('Generate whatever traffic you want')
        message_and_await_enter('Are you done?')

        L.describe('Stop capturing traffic')
        packets = self.capture_device['packet_capturer'].stop()

        whitelist = self.capture_device.local_ips()
        L.debug('Excluding {} from analysis'.format(whitelist))
        self.traffic_analyser.get_vpn_server_ip(packets, whitelist)
