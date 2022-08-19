# coding: utf-8

"""
    Investoreight Core API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: info@investoreight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class HistoricalMetricValueDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'period': 'str',
        'value': 'str',
        'period_date_time': 'datetime'
    }

    attribute_map = {
        'period': 'Period',
        'value': 'Value',
        'period_date_time': 'PeriodDateTime'
    }

    def __init__(self, period=None, value=None, period_date_time=None):  # noqa: E501
        """HistoricalMetricValueDto - a model defined in Swagger"""  # noqa: E501
        self._period = None
        self._value = None
        self._period_date_time = None
        self.discriminator = None
        if period is not None:
            self.period = period
        if value is not None:
            self.value = value
        if period_date_time is not None:
            self.period_date_time = period_date_time

    @property
    def period(self):
        """Gets the period of this HistoricalMetricValueDto.  # noqa: E501


        :return: The period of this HistoricalMetricValueDto.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this HistoricalMetricValueDto.


        :param period: The period of this HistoricalMetricValueDto.  # noqa: E501
        :type: str
        """

        self._period = period

    @property
    def value(self):
        """Gets the value of this HistoricalMetricValueDto.  # noqa: E501


        :return: The value of this HistoricalMetricValueDto.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this HistoricalMetricValueDto.


        :param value: The value of this HistoricalMetricValueDto.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def period_date_time(self):
        """Gets the period_date_time of this HistoricalMetricValueDto.  # noqa: E501


        :return: The period_date_time of this HistoricalMetricValueDto.  # noqa: E501
        :rtype: datetime
        """
        return self._period_date_time

    @period_date_time.setter
    def period_date_time(self, period_date_time):
        """Sets the period_date_time of this HistoricalMetricValueDto.


        :param period_date_time: The period_date_time of this HistoricalMetricValueDto.  # noqa: E501
        :type: datetime
        """

        self._period_date_time = period_date_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(HistoricalMetricValueDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HistoricalMetricValueDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
