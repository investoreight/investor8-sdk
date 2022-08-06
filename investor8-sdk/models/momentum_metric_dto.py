# coding: utf-8

"""
    Investor8.Core

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MomentumMetricDto(object):
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
        'timestamp': 'int',
        'ma12': 'float',
        'ma26': 'float',
        'ma52': 'float',
        'rsi14_d': 'float',
        'change': 'float'
    }

    attribute_map = {
        'timestamp': 'Timestamp',
        'ma12': 'MA12',
        'ma26': 'MA26',
        'ma52': 'MA52',
        'rsi14_d': 'RSI14D',
        'change': 'Change'
    }

    def __init__(self, timestamp=None, ma12=None, ma26=None, ma52=None, rsi14_d=None, change=None):  # noqa: E501
        """MomentumMetricDto - a model defined in Swagger"""  # noqa: E501
        self._timestamp = None
        self._ma12 = None
        self._ma26 = None
        self._ma52 = None
        self._rsi14_d = None
        self._change = None
        self.discriminator = None
        if timestamp is not None:
            self.timestamp = timestamp
        if ma12 is not None:
            self.ma12 = ma12
        if ma26 is not None:
            self.ma26 = ma26
        if ma52 is not None:
            self.ma52 = ma52
        if rsi14_d is not None:
            self.rsi14_d = rsi14_d
        if change is not None:
            self.change = change

    @property
    def timestamp(self):
        """Gets the timestamp of this MomentumMetricDto.  # noqa: E501


        :return: The timestamp of this MomentumMetricDto.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this MomentumMetricDto.


        :param timestamp: The timestamp of this MomentumMetricDto.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def ma12(self):
        """Gets the ma12 of this MomentumMetricDto.  # noqa: E501


        :return: The ma12 of this MomentumMetricDto.  # noqa: E501
        :rtype: float
        """
        return self._ma12

    @ma12.setter
    def ma12(self, ma12):
        """Sets the ma12 of this MomentumMetricDto.


        :param ma12: The ma12 of this MomentumMetricDto.  # noqa: E501
        :type: float
        """

        self._ma12 = ma12

    @property
    def ma26(self):
        """Gets the ma26 of this MomentumMetricDto.  # noqa: E501


        :return: The ma26 of this MomentumMetricDto.  # noqa: E501
        :rtype: float
        """
        return self._ma26

    @ma26.setter
    def ma26(self, ma26):
        """Sets the ma26 of this MomentumMetricDto.


        :param ma26: The ma26 of this MomentumMetricDto.  # noqa: E501
        :type: float
        """

        self._ma26 = ma26

    @property
    def ma52(self):
        """Gets the ma52 of this MomentumMetricDto.  # noqa: E501


        :return: The ma52 of this MomentumMetricDto.  # noqa: E501
        :rtype: float
        """
        return self._ma52

    @ma52.setter
    def ma52(self, ma52):
        """Sets the ma52 of this MomentumMetricDto.


        :param ma52: The ma52 of this MomentumMetricDto.  # noqa: E501
        :type: float
        """

        self._ma52 = ma52

    @property
    def rsi14_d(self):
        """Gets the rsi14_d of this MomentumMetricDto.  # noqa: E501


        :return: The rsi14_d of this MomentumMetricDto.  # noqa: E501
        :rtype: float
        """
        return self._rsi14_d

    @rsi14_d.setter
    def rsi14_d(self, rsi14_d):
        """Sets the rsi14_d of this MomentumMetricDto.


        :param rsi14_d: The rsi14_d of this MomentumMetricDto.  # noqa: E501
        :type: float
        """

        self._rsi14_d = rsi14_d

    @property
    def change(self):
        """Gets the change of this MomentumMetricDto.  # noqa: E501


        :return: The change of this MomentumMetricDto.  # noqa: E501
        :rtype: float
        """
        return self._change

    @change.setter
    def change(self, change):
        """Sets the change of this MomentumMetricDto.


        :param change: The change of this MomentumMetricDto.  # noqa: E501
        :type: float
        """

        self._change = change

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
        if issubclass(MomentumMetricDto, dict):
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
        if not isinstance(other, MomentumMetricDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other