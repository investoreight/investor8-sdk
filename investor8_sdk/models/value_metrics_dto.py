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

class ValueMetricsDto(object):
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
        'ticker': 'str',
        'timestamp': 'int',
        'high52': 'float',
        'low52': 'float'
    }

    attribute_map = {
        'ticker': 'Ticker',
        'timestamp': 'Timestamp',
        'high52': 'High52',
        'low52': 'Low52'
    }

    def __init__(self, ticker=None, timestamp=None, high52=None, low52=None):  # noqa: E501
        """ValueMetricsDto - a model defined in Swagger"""  # noqa: E501
        self._ticker = None
        self._timestamp = None
        self._high52 = None
        self._low52 = None
        self.discriminator = None
        if ticker is not None:
            self.ticker = ticker
        if timestamp is not None:
            self.timestamp = timestamp
        if high52 is not None:
            self.high52 = high52
        if low52 is not None:
            self.low52 = low52

    @property
    def ticker(self):
        """Gets the ticker of this ValueMetricsDto.  # noqa: E501


        :return: The ticker of this ValueMetricsDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this ValueMetricsDto.


        :param ticker: The ticker of this ValueMetricsDto.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def timestamp(self):
        """Gets the timestamp of this ValueMetricsDto.  # noqa: E501


        :return: The timestamp of this ValueMetricsDto.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ValueMetricsDto.


        :param timestamp: The timestamp of this ValueMetricsDto.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def high52(self):
        """Gets the high52 of this ValueMetricsDto.  # noqa: E501


        :return: The high52 of this ValueMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._high52

    @high52.setter
    def high52(self, high52):
        """Sets the high52 of this ValueMetricsDto.


        :param high52: The high52 of this ValueMetricsDto.  # noqa: E501
        :type: float
        """

        self._high52 = high52

    @property
    def low52(self):
        """Gets the low52 of this ValueMetricsDto.  # noqa: E501


        :return: The low52 of this ValueMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._low52

    @low52.setter
    def low52(self, low52):
        """Sets the low52 of this ValueMetricsDto.


        :param low52: The low52 of this ValueMetricsDto.  # noqa: E501
        :type: float
        """

        self._low52 = low52

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
        if issubclass(ValueMetricsDto, dict):
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
        if not isinstance(other, ValueMetricsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
