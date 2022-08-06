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

class HistoricalValueMetrics(object):
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
        'alpha': 'list[PeriodMetricValue]',
        'beta': 'list[PeriodMetricValue]',
        'price_return': 'list[PeriodReturn]',
        'high': 'list[PeriodReturn]',
        'low': 'list[PeriodReturn]'
    }

    attribute_map = {
        'ticker': 'Ticker',
        'alpha': 'Alpha',
        'beta': 'Beta',
        'price_return': 'PriceReturn',
        'high': 'High',
        'low': 'Low'
    }

    def __init__(self, ticker=None, alpha=None, beta=None, price_return=None, high=None, low=None):  # noqa: E501
        """HistoricalValueMetrics - a model defined in Swagger"""  # noqa: E501
        self._ticker = None
        self._alpha = None
        self._beta = None
        self._price_return = None
        self._high = None
        self._low = None
        self.discriminator = None
        if ticker is not None:
            self.ticker = ticker
        if alpha is not None:
            self.alpha = alpha
        if beta is not None:
            self.beta = beta
        if price_return is not None:
            self.price_return = price_return
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low

    @property
    def ticker(self):
        """Gets the ticker of this HistoricalValueMetrics.  # noqa: E501


        :return: The ticker of this HistoricalValueMetrics.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this HistoricalValueMetrics.


        :param ticker: The ticker of this HistoricalValueMetrics.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def alpha(self):
        """Gets the alpha of this HistoricalValueMetrics.  # noqa: E501


        :return: The alpha of this HistoricalValueMetrics.  # noqa: E501
        :rtype: list[PeriodMetricValue]
        """
        return self._alpha

    @alpha.setter
    def alpha(self, alpha):
        """Sets the alpha of this HistoricalValueMetrics.


        :param alpha: The alpha of this HistoricalValueMetrics.  # noqa: E501
        :type: list[PeriodMetricValue]
        """

        self._alpha = alpha

    @property
    def beta(self):
        """Gets the beta of this HistoricalValueMetrics.  # noqa: E501


        :return: The beta of this HistoricalValueMetrics.  # noqa: E501
        :rtype: list[PeriodMetricValue]
        """
        return self._beta

    @beta.setter
    def beta(self, beta):
        """Sets the beta of this HistoricalValueMetrics.


        :param beta: The beta of this HistoricalValueMetrics.  # noqa: E501
        :type: list[PeriodMetricValue]
        """

        self._beta = beta

    @property
    def price_return(self):
        """Gets the price_return of this HistoricalValueMetrics.  # noqa: E501


        :return: The price_return of this HistoricalValueMetrics.  # noqa: E501
        :rtype: list[PeriodReturn]
        """
        return self._price_return

    @price_return.setter
    def price_return(self, price_return):
        """Sets the price_return of this HistoricalValueMetrics.


        :param price_return: The price_return of this HistoricalValueMetrics.  # noqa: E501
        :type: list[PeriodReturn]
        """

        self._price_return = price_return

    @property
    def high(self):
        """Gets the high of this HistoricalValueMetrics.  # noqa: E501


        :return: The high of this HistoricalValueMetrics.  # noqa: E501
        :rtype: list[PeriodReturn]
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this HistoricalValueMetrics.


        :param high: The high of this HistoricalValueMetrics.  # noqa: E501
        :type: list[PeriodReturn]
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this HistoricalValueMetrics.  # noqa: E501


        :return: The low of this HistoricalValueMetrics.  # noqa: E501
        :rtype: list[PeriodReturn]
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this HistoricalValueMetrics.


        :param low: The low of this HistoricalValueMetrics.  # noqa: E501
        :type: list[PeriodReturn]
        """

        self._low = low

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
        if issubclass(HistoricalValueMetrics, dict):
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
        if not isinstance(other, HistoricalValueMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other