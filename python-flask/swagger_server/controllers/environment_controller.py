import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.forecast_response import ForecastResponse  # noqa: E501
from swagger_server.models.heater_state import HeaterState  # noqa: E501
from swagger_server.models.temperatue_zone_status import TemperatueZoneStatus  # noqa: E501
from swagger_server.models.temperature_summary import TemperatureSummary  # noqa: E501
from swagger_server import util


def get_forecast(days):  # noqa: E501
    """get_forecast

     # noqa: E501

    :param days: 
    :type days: int

    :rtype: ForecastResponse
    """
    return 'do some magic!'


def get_heater_state(zoneId):  # noqa: E501
    """get_heater_state

    gets the state of the heater # noqa: E501

    :param zoneId: 
    :type zoneId: str

    :rtype: HeaterState
    """
    return 'do some magic!'


def get_zone_temperature(zoneId):  # noqa: E501
    """get_zone_temperature

     # noqa: E501

    :param zoneId: 
    :type zoneId: str

    :rtype: TemperatueZoneStatus
    """
    return 'do some magic!'


def set_heater_state(zoneId, state):  # noqa: E501
    """set_heater_state

    turns the heater on or off # noqa: E501

    :param zoneId: 
    :type zoneId: str
    :param state: 
    :type state: str

    :rtype: ApiResponse
    """
    return 'do some magic!'


def temperature_summary():  # noqa: E501
    """temperature_summary

     # noqa: E501


    :rtype: TemperatureSummary
    """
    return 'do some magic!'
