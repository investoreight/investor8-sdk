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

class DailyMetricsDto(object):
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
        'timestamp': 'int',
        'marketcap': 'float',
        'pe_ratio_ttm': 'float',
        'dividend_yield_ttm': 'float'
    }

    attribute_map = {
        'id': 'Id',
        'ticker': 'Ticker',
        'timestamp': 'Timestamp',
        'marketcap': 'Marketcap',
        'pe_ratio_ttm': 'PERatioTTM',
        'dividend_yield_ttm': 'DividendYieldTTM'
    }

    def __init__(self, id=None, ticker=None, timestamp=None, marketcap=None, pe_ratio_ttm=None, dividend_yield_ttm=None):  # noqa: E501
        """DailyMetricsDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._ticker = None
        self._timestamp = None
        self._marketcap = None
        self._pe_ratio_ttm = None
        self._dividend_yield_ttm = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if ticker is not None:
            self.ticker = ticker
        if timestamp is not None:
            self.timestamp = timestamp
        if marketcap is not None:
            self.marketcap = marketcap
        if pe_ratio_ttm is not None:
            self.pe_ratio_ttm = pe_ratio_ttm
        if dividend_yield_ttm is not None:
            self.dividend_yield_ttm = dividend_yield_ttm

    @property
    def id(self):
        """Gets the id of this DailyMetricsDto.  # noqa: E501


        :return: The id of this DailyMetricsDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DailyMetricsDto.


        :param id: The id of this DailyMetricsDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ticker(self):
        """Gets the ticker of this DailyMetricsDto.  # noqa: E501


        :return: The ticker of this DailyMetricsDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this DailyMetricsDto.


        :param ticker: The ticker of this DailyMetricsDto.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def timestamp(self):
        """Gets the timestamp of this DailyMetricsDto.  # noqa: E501


        :return: The timestamp of this DailyMetricsDto.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this DailyMetricsDto.


        :param timestamp: The timestamp of this DailyMetricsDto.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def marketcap(self):
        """Gets the marketcap of this DailyMetricsDto.  # noqa: E501


        :return: The marketcap of this DailyMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._marketcap

    @marketcap.setter
    def marketcap(self, marketcap):
        """Sets the marketcap of this DailyMetricsDto.


        :param marketcap: The marketcap of this DailyMetricsDto.  # noqa: E501
        :type: float
        """

        self._marketcap = marketcap

    @property
    def pe_ratio_ttm(self):
        """Gets the pe_ratio_ttm of this DailyMetricsDto.  # noqa: E501


        :return: The pe_ratio_ttm of this DailyMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._pe_ratio_ttm

    @pe_ratio_ttm.setter
    def pe_ratio_ttm(self, pe_ratio_ttm):
        """Sets the pe_ratio_ttm of this DailyMetricsDto.


        :param pe_ratio_ttm: The pe_ratio_ttm of this DailyMetricsDto.  # noqa: E501
        :type: float
        """

        self._pe_ratio_ttm = pe_ratio_ttm

    @property
    def dividend_yield_ttm(self):
        """Gets the dividend_yield_ttm of this DailyMetricsDto.  # noqa: E501


        :return: The dividend_yield_ttm of this DailyMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._dividend_yield_ttm

    @dividend_yield_ttm.setter
    def dividend_yield_ttm(self, dividend_yield_ttm):
        """Sets the dividend_yield_ttm of this DailyMetricsDto.


        :param dividend_yield_ttm: The dividend_yield_ttm of this DailyMetricsDto.  # noqa: E501
        :type: float
        """

        self._dividend_yield_ttm = dividend_yield_ttm

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
        if issubclass(DailyMetricsDto, dict):
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
        if not isinstance(other, DailyMetricsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
