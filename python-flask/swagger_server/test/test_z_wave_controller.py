# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.device_state import DeviceState  # noqa: E501
from swagger_server.models.lighting_summary import LightingSummary  # noqa: E501
from swagger_server.test import BaseTestCase


class TestZWaveController(BaseTestCase):
    """ZWaveController integration test stubs"""

    def test_get_lighting_summary(self):
        """Test case for get_lighting_summary

        
        """
        response = self.client.open(
            '/Wael-Abouelwafa/All_In_One_Covid-19/1.0.0/lightingSummary',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_switch_state(self):
        """Test case for get_switch_state

        
        """
        response = self.client.open(
            '/Wael-Abouelwafa/All_In_One_Covid-19/1.0.0/lighting/switches/{deviceId}'.format(deviceId='deviceId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_dimmer(self):
        """Test case for set_dimmer

        
        """
        response = self.client.open(
            '/Wael-Abouelwafa/All_In_One_Covid-19/1.0.0/lighting/dimmers/{deviceId}/{value}'.format(deviceId='deviceId_example', value=100),
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_dimmer_timer(self):
        """Test case for set_dimmer_timer

        
        """
        query_string = [('units', 'milliseconds')]
        response = self.client.open(
            '/Wael-Abouelwafa/All_In_One_Covid-19/1.0.0/lighting/dimmers/{deviceId}/{value}/timer/{timeunit}'.format(deviceId='deviceId_example', value=56, timeunit=56),
            method='POST',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_switch(self):
        """Test case for set_switch

        
        """
        response = self.client.open(
            '/Wael-Abouelwafa/All_In_One_Covid-19/1.0.0/lighting/switches/{deviceId}/{value}'.format(deviceId='deviceId_example', value='value_example'),
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_switch_timer(self):
        """Test case for set_switch_timer

        
        """
        response = self.client.open(
            '/Wael-Abouelwafa/All_In_One_Covid-19/1.0.0/lighting/switches/{deviceId}/{value}/timer/{minutes}'.format(deviceId='deviceId_example', value='value_example', minutes=56),
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
