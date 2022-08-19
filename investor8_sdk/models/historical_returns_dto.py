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

class HistoricalReturnsDto(object):
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
        'fyq': 'str',
        'next_close_return': 'float',
        'next_open_return': 'float',
        'intra_day_return': 'float'
    }

    attribute_map = {
        'fyq': 'FYQ',
        'next_close_return': 'NextCloseReturn',
        'next_open_return': 'NextOpenReturn',
        'intra_day_return': 'IntraDayReturn'
    }

    def __init__(self, fyq=None, next_close_return=None, next_open_return=None, intra_day_return=None):  # noqa: E501
        """HistoricalReturnsDto - a model defined in Swagger"""  # noqa: E501
        self._fyq = None
        self._next_close_return = None
        self._next_open_return = None
        self._intra_day_return = None
        self.discriminator = None
        if fyq is not None:
            self.fyq = fyq
        if next_close_return is not None:
            self.next_close_return = next_close_return
        if next_open_return is not None:
            self.next_open_return = next_open_return
        if intra_day_return is not None:
            self.intra_day_return = intra_day_return

    @property
    def fyq(self):
        """Gets the fyq of this HistoricalReturnsDto.  # noqa: E501


        :return: The fyq of this HistoricalReturnsDto.  # noqa: E501
        :rtype: str
        """
        return self._fyq

    @fyq.setter
    def fyq(self, fyq):
        """Sets the fyq of this HistoricalReturnsDto.


        :param fyq: The fyq of this HistoricalReturnsDto.  # noqa: E501
        :type: str
        """

        self._fyq = fyq

    @property
    def next_close_return(self):
        """Gets the next_close_return of this HistoricalReturnsDto.  # noqa: E501


        :return: The next_close_return of this HistoricalReturnsDto.  # noqa: E501
        :rtype: float
        """
        return self._next_close_return

    @next_close_return.setter
    def next_close_return(self, next_close_return):
        """Sets the next_close_return of this HistoricalReturnsDto.


        :param next_close_return: The next_close_return of this HistoricalReturnsDto.  # noqa: E501
        :type: float
        """

        self._next_close_return = next_close_return

    @property
    def next_open_return(self):
        """Gets the next_open_return of this HistoricalReturnsDto.  # noqa: E501


        :return: The next_open_return of this HistoricalReturnsDto.  # noqa: E501
        :rtype: float
        """
        return self._next_open_return

    @next_open_return.setter
    def next_open_return(self, next_open_return):
        """Sets the next_open_return of this HistoricalReturnsDto.


        :param next_open_return: The next_open_return of this HistoricalReturnsDto.  # noqa: E501
        :type: float
        """

        self._next_open_return = next_open_return

    @property
    def intra_day_return(self):
        """Gets the intra_day_return of this HistoricalReturnsDto.  # noqa: E501


        :return: The intra_day_return of this HistoricalReturnsDto.  # noqa: E501
        :rtype: float
        """
        return self._intra_day_return

    @intra_day_return.setter
    def intra_day_return(self, intra_day_return):
        """Sets the intra_day_return of this HistoricalReturnsDto.


        :param intra_day_return: The intra_day_return of this HistoricalReturnsDto.  # noqa: E501
        :type: float
        """

        self._intra_day_return = intra_day_return

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
        if issubclass(HistoricalReturnsDto, dict):
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
        if not isinstance(other, HistoricalReturnsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
