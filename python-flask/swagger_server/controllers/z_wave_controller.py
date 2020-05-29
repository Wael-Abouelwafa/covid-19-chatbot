import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.device_state import DeviceState  # noqa: E501
from swagger_server.models.lighting_summary import LightingSummary  # noqa: E501
from swagger_server import util


def get_lighting_summary():  # noqa: E501
    """get_lighting_summary

     # noqa: E501


    :rtype: LightingSummary
    """
    return 'do some magic!'


def get_switch_state(deviceId):  # noqa: E501
    """get_switch_state

     # noqa: E501

    :param deviceId: 
    :type deviceId: str

    :rtype: DeviceState
    """
    return 'do some magic!'


def set_dimmer(deviceId, value):  # noqa: E501
    """set_dimmer

     # noqa: E501

    :param deviceId: 
    :type deviceId: str
    :param value: 
    :type value: int

    :rtype: ApiResponse
    """
    return 'do some magic!'


def set_dimmer_timer(deviceId, value, timeunit, units=None):  # noqa: E501
    """set_dimmer_timer

    sets a dimmer to a specific value on a timer # noqa: E501

    :param deviceId: 
    :type deviceId: str
    :param value: 
    :type value: int
    :param timeunit: 
    :type timeunit: int
    :param units: 
    :type units: str

    :rtype: ApiResponse
    """
    return 'do some magic!'


def set_switch(deviceId, value):  # noqa: E501
    """set_switch

     # noqa: E501

    :param deviceId: 
    :type deviceId: str
    :param value: 
    :type value: str

    :rtype: ApiResponse
    """
    return 'do some magic!'


def set_switch_timer(deviceId, value, minutes):  # noqa: E501
    """set_switch_timer

    sets a switch to a specific value on a timer # noqa: E501

    :param deviceId: 
    :type deviceId: str
    :param value: 
    :type value: str
    :param minutes: 
    :type minutes: int

    :rtype: ApiResponse
    """
    return 'do some magic!'
