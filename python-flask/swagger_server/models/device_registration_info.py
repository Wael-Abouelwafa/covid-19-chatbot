# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DeviceRegistrationInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, uri: str=None, id: str=None):  # noqa: E501
        """DeviceRegistrationInfo - a model defined in Swagger

        :param uri: The uri of this DeviceRegistrationInfo.  # noqa: E501
        :type uri: str
        :param id: The id of this DeviceRegistrationInfo.  # noqa: E501
        :type id: str
        """
        self.swagger_types = {
            'uri': str,
            'id': str
        }

        self.attribute_map = {
            'uri': 'uri',
            'id': 'id'
        }

        self._uri = uri
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'DeviceRegistrationInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DeviceRegistrationInfo of this DeviceRegistrationInfo.  # noqa: E501
        :rtype: DeviceRegistrationInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uri(self) -> str:
        """Gets the uri of this DeviceRegistrationInfo.


        :return: The uri of this DeviceRegistrationInfo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri: str):
        """Sets the uri of this DeviceRegistrationInfo.


        :param uri: The uri of this DeviceRegistrationInfo.
        :type uri: str
        """

        self._uri = uri

    @property
    def id(self) -> str:
        """Gets the id of this DeviceRegistrationInfo.


        :return: The id of this DeviceRegistrationInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this DeviceRegistrationInfo.


        :param id: The id of this DeviceRegistrationInfo.
        :type id: str
        """

        self._id = id
