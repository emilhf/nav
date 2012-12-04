from unittest import TestCase
import os
from nav.statemon.megaping import Host
from nav.statemon.icmppacket import Packet, PacketV4, PacketV6

class HostTestcase(TestCase):


    def test_make_v4_packet(self):
        """
        Test to make a v4 packet
        """
        host = Host('127.0.0.1')
        pid = os.getpid()
        self.assertFalse(host.is_v6())

        self.assertTrue(host.packet)
        self.assertTrue(isinstance(host.packet, PacketV4))

        packet, cookie = host.make_packet(64)

        self.assertTrue(packet)
        self.assertTrue(cookie)
        self.assertEquals(len(packet), 64)
        self.assertEquals(len(cookie), 16)

        self.assertEquals(host.packet.sequence, 0)
        self.assertEquals(host.packet.id, pid)

    def test_make_v6_packet(self):
        """
        Test to make a v6 packet
        """
        host = Host('2001:701::FFFF')
        pid = os.getpid()
        self.assertTrue(host.is_v6())

        self.assertTrue(host.packet)
        self.assertTrue(isinstance(host.packet, PacketV6))

        packet, cookie = host.make_packet(64)

        self.assertTrue(packet)
        self.assertTrue(cookie)
        self.assertEquals(len(packet), 64)
        self.assertEquals(len(cookie), 16)

        self.assertEquals(host.packet.sequence, 0)
        self.assertEquals(host.packet.id, pid)


    def test_IP_validation(self):
        """
        Test the IP valdidation helper methods for both v6 & v4
        """
        host = Host('')
        self.assertTrue(host.is_valid_ipv4('129.241.105.210'))
        self.assertFalse(host.is_valid_ipv4('129.241.105.256'))

        self.assertTrue(host.is_valid_ipv6('2001:701::FFFF'))
        self.assertFalse(host.is_valid_ipv6('127.0.0.1'))




