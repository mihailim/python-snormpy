#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from snormpy import (SnormpyClient, SnormpyException, V1, V2, V2C)
from pysnmp.smi.error import SmiError

# Please note that the tests use the snmplabs.com public SNMP simulation service
# thus require a working Internet connection and a working DNS resolver.

TEST_HOST='demo.snmplabs.com'
TEST_AUTHDATA_V2C={'community': 'public', 'port': 161, 'version': V2C}
TEST_AUTHDATA_V2C_ALTPORT={'community': 'public', 'port': 1161, 'version': V2C}


class TestSnormpyClientConstruction(unittest.TestCase):

    def test_construction(self):
        try:
            SnormpyClient(TEST_HOST, TEST_AUTHDATA_V2C)
            self.assertTrue('Successfully constructed SnormpyClient instance')
        except SnormpyException:
            self.fail('Unable to construct SnormpyClient instance')

    def test_construction_alternative_port(self):
        try:
            SnormpyClient(TEST_HOST, TEST_AUTHDATA_V2C_ALTPORT)
            self.assertTrue('Successfully constructed SnormpyClient instance')
        except SnormpyException:
            self.fail('Unable to construct SnormpyClient instance')

    def test_load_common_mibs(self):
        try:
            sc = SnormpyClient(TEST_HOST, TEST_AUTHDATA_V2C)
            sc.load_mibs('SNMPv2-MIB', 'IF-MIB', 'IP-MIB', 'HOST-RESOURCES-MIB')
        except SnormpyException, e:
            self.fail('Unable to construct SnormpyClient instance: ' + e.message)
        except SmiError, e:
            self.fail('Error loading MIBs: ' + e.message)


class TestSnormpyClient(unittest.TestCase):

    def setUp(self):
        self._sc = SnormpyClient(TEST_HOST, TEST_AUTHDATA_V2C)

    def test_get_numeric_oid(self):
        self.assertTrue(len(self._sc.get((1,3,6,1,2,1,1,5,0))) > 0) # .1.3.6.1.2.1.1.5.0 is SNMPv2-MIB::sysName.0

    def test_get_named_oid(self):
        self._sc.load_mibs('SNMPv2-MIB')
        res = self._sc.get('SNMPv2-MIB::sysName.0')
        self.assertTrue(len(str(res)) > 0)

    def test_match_tables(self):
        # This test will fail until we fix the buggy matchtables length check behavior
        self._sc.load_mibs('SNMPv2-MIB', 'IF-MIB')
        res = self._sc.matchtables('IF-MIB::ifIndex',
                                   ('IF-MIB::ifDescr', 'IF-MIB::ifPhysAddress', 'IF-MIB::ifOperStatus'))
        self.assertTrue(len(res) > 0)


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(TestSnormpyClientConstruction))
    suite.addTest(loader.loadTestsFromTestCase(TestSnormpyClient))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
