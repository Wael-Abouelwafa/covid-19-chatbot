# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestZonesController(BaseTestCase):
    """ZonesController integration test stubs"""

    def test_get_zones(self):
        """Test case for get_zones

        
        """
        response = self.client.open(
            '/Wael-Abouelwafa/All_In_One_Covid-19/1.0.0/zones',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quiet_zone(self):
        """Test case for quiet_zone

        
        """
        response = self.client.open(
            '/Wael-Abouelwafa/All_In_One_Covid-19/1.0.0/zones/{zoneId}/quiet'.format(zoneId='zoneId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
