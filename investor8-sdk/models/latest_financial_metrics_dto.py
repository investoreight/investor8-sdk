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

class LatestFinancialMetricsDto(object):
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
        'basic_eps_ttm': 'float',
        'adjusted_basic_eps_ttm': 'float'
    }

    attribute_map = {
        'ticker': 'Ticker',
        'basic_eps_ttm': 'BasicEps_TTM',
        'adjusted_basic_eps_ttm': 'AdjustedBasicEps_TTM'
    }

    def __init__(self, ticker=None, basic_eps_ttm=None, adjusted_basic_eps_ttm=None):  # noqa: E501
        """LatestFinancialMetricsDto - a model defined in Swagger"""  # noqa: E501
        self._ticker = None
        self._basic_eps_ttm = None
        self._adjusted_basic_eps_ttm = None
        self.discriminator = None
        if ticker is not None:
            self.ticker = ticker
        if basic_eps_ttm is not None:
            self.basic_eps_ttm = basic_eps_ttm
        if adjusted_basic_eps_ttm is not None:
            self.adjusted_basic_eps_ttm = adjusted_basic_eps_ttm

    @property
    def ticker(self):
        """Gets the ticker of this LatestFinancialMetricsDto.  # noqa: E501


        :return: The ticker of this LatestFinancialMetricsDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this LatestFinancialMetricsDto.


        :param ticker: The ticker of this LatestFinancialMetricsDto.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def basic_eps_ttm(self):
        """Gets the basic_eps_ttm of this LatestFinancialMetricsDto.  # noqa: E501


        :return: The basic_eps_ttm of this LatestFinancialMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._basic_eps_ttm

    @basic_eps_ttm.setter
    def basic_eps_ttm(self, basic_eps_ttm):
        """Sets the basic_eps_ttm of this LatestFinancialMetricsDto.


        :param basic_eps_ttm: The basic_eps_ttm of this LatestFinancialMetricsDto.  # noqa: E501
        :type: float
        """

        self._basic_eps_ttm = basic_eps_ttm

    @property
    def adjusted_basic_eps_ttm(self):
        """Gets the adjusted_basic_eps_ttm of this LatestFinancialMetricsDto.  # noqa: E501


        :return: The adjusted_basic_eps_ttm of this LatestFinancialMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._adjusted_basic_eps_ttm

    @adjusted_basic_eps_ttm.setter
    def adjusted_basic_eps_ttm(self, adjusted_basic_eps_ttm):
        """Sets the adjusted_basic_eps_ttm of this LatestFinancialMetricsDto.


        :param adjusted_basic_eps_ttm: The adjusted_basic_eps_ttm of this LatestFinancialMetricsDto.  # noqa: E501
        :type: float
        """

        self._adjusted_basic_eps_ttm = adjusted_basic_eps_ttm

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
        if issubclass(LatestFinancialMetricsDto, dict):
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
        if not isinstance(other, LatestFinancialMetricsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
