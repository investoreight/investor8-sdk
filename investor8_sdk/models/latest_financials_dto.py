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

class LatestFinancialsDto(object):
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
        'id': 'str',
        'ticker': 'str',
        'basic_eps': 'float',
        'fyq': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'ticker': 'Ticker',
        'basic_eps': 'BasicEps',
        'fyq': 'FYQ'
    }

    def __init__(self, id=None, ticker=None, basic_eps=None, fyq=None):  # noqa: E501
        """LatestFinancialsDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._ticker = None
        self._basic_eps = None
        self._fyq = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if ticker is not None:
            self.ticker = ticker
        if basic_eps is not None:
            self.basic_eps = basic_eps
        if fyq is not None:
            self.fyq = fyq

    @property
    def id(self):
        """Gets the id of this LatestFinancialsDto.  # noqa: E501


        :return: The id of this LatestFinancialsDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LatestFinancialsDto.


        :param id: The id of this LatestFinancialsDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ticker(self):
        """Gets the ticker of this LatestFinancialsDto.  # noqa: E501


        :return: The ticker of this LatestFinancialsDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this LatestFinancialsDto.


        :param ticker: The ticker of this LatestFinancialsDto.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def basic_eps(self):
        """Gets the basic_eps of this LatestFinancialsDto.  # noqa: E501


        :return: The basic_eps of this LatestFinancialsDto.  # noqa: E501
        :rtype: float
        """
        return self._basic_eps

    @basic_eps.setter
    def basic_eps(self, basic_eps):
        """Sets the basic_eps of this LatestFinancialsDto.


        :param basic_eps: The basic_eps of this LatestFinancialsDto.  # noqa: E501
        :type: float
        """

        self._basic_eps = basic_eps

    @property
    def fyq(self):
        """Gets the fyq of this LatestFinancialsDto.  # noqa: E501


        :return: The fyq of this LatestFinancialsDto.  # noqa: E501
        :rtype: str
        """
        return self._fyq

    @fyq.setter
    def fyq(self, fyq):
        """Sets the fyq of this LatestFinancialsDto.


        :param fyq: The fyq of this LatestFinancialsDto.  # noqa: E501
        :type: str
        """

        self._fyq = fyq

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
        if issubclass(LatestFinancialsDto, dict):
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
        if not isinstance(other, LatestFinancialsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
