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

class CurrentMomentumMetricsDto(object):
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
        'macd': 'float',
        'relateive_macd': 'float',
        'ma12': 'float',
        'relateive_ma12': 'float',
        'ma26': 'float',
        'relateive_ma26': 'float',
        'ma5': 'float',
        'relateive_ma5': 'float',
        'ma52': 'float',
        'relateive_ma52': 'float',
        'ema12': 'float',
        'relateive_ema12': 'float',
        'ema26': 'float',
        'relateive_ema26': 'float',
        'ema5': 'float',
        'relateive_ema5': 'float',
        'ema52': 'float',
        'relateive_ema52': 'float',
        'rsi14_d': 'float',
        'timestamp': 'int'
    }

    attribute_map = {
        'ticker': 'Ticker',
        'macd': 'MACD',
        'relateive_macd': 'RelateiveMACD',
        'ma12': 'MA12',
        'relateive_ma12': 'RelateiveMA12',
        'ma26': 'MA26',
        'relateive_ma26': 'RelateiveMA26',
        'ma5': 'MA5',
        'relateive_ma5': 'RelateiveMA5',
        'ma52': 'MA52',
        'relateive_ma52': 'RelateiveMA52',
        'ema12': 'EMA12',
        'relateive_ema12': 'RelateiveEMA12',
        'ema26': 'EMA26',
        'relateive_ema26': 'RelateiveEMA26',
        'ema5': 'EMA5',
        'relateive_ema5': 'RelateiveEMA5',
        'ema52': 'EMA52',
        'relateive_ema52': 'RelateiveEMA52',
        'rsi14_d': 'RSI14D',
        'timestamp': 'Timestamp'
    }

    def __init__(self, ticker=None, macd=None, relateive_macd=None, ma12=None, relateive_ma12=None, ma26=None, relateive_ma26=None, ma5=None, relateive_ma5=None, ma52=None, relateive_ma52=None, ema12=None, relateive_ema12=None, ema26=None, relateive_ema26=None, ema5=None, relateive_ema5=None, ema52=None, relateive_ema52=None, rsi14_d=None, timestamp=None):  # noqa: E501
        """CurrentMomentumMetricsDto - a model defined in Swagger"""  # noqa: E501
        self._ticker = None
        self._macd = None
        self._relateive_macd = None
        self._ma12 = None
        self._relateive_ma12 = None
        self._ma26 = None
        self._relateive_ma26 = None
        self._ma5 = None
        self._relateive_ma5 = None
        self._ma52 = None
        self._relateive_ma52 = None
        self._ema12 = None
        self._relateive_ema12 = None
        self._ema26 = None
        self._relateive_ema26 = None
        self._ema5 = None
        self._relateive_ema5 = None
        self._ema52 = None
        self._relateive_ema52 = None
        self._rsi14_d = None
        self._timestamp = None
        self.discriminator = None
        if ticker is not None:
            self.ticker = ticker
        if macd is not None:
            self.macd = macd
        if relateive_macd is not None:
            self.relateive_macd = relateive_macd
        if ma12 is not None:
            self.ma12 = ma12
        if relateive_ma12 is not None:
            self.relateive_ma12 = relateive_ma12
        if ma26 is not None:
            self.ma26 = ma26
        if relateive_ma26 is not None:
            self.relateive_ma26 = relateive_ma26
        if ma5 is not None:
            self.ma5 = ma5
        if relateive_ma5 is not None:
            self.relateive_ma5 = relateive_ma5
        if ma52 is not None:
            self.ma52 = ma52
        if relateive_ma52 is not None:
            self.relateive_ma52 = relateive_ma52
        if ema12 is not None:
            self.ema12 = ema12
        if relateive_ema12 is not None:
            self.relateive_ema12 = relateive_ema12
        if ema26 is not None:
            self.ema26 = ema26
        if relateive_ema26 is not None:
            self.relateive_ema26 = relateive_ema26
        if ema5 is not None:
            self.ema5 = ema5
        if relateive_ema5 is not None:
            self.relateive_ema5 = relateive_ema5
        if ema52 is not None:
            self.ema52 = ema52
        if relateive_ema52 is not None:
            self.relateive_ema52 = relateive_ema52
        if rsi14_d is not None:
            self.rsi14_d = rsi14_d
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def ticker(self):
        """Gets the ticker of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The ticker of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this CurrentMomentumMetricsDto.


        :param ticker: The ticker of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def macd(self):
        """Gets the macd of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The macd of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._macd

    @macd.setter
    def macd(self, macd):
        """Sets the macd of this CurrentMomentumMetricsDto.


        :param macd: The macd of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._macd = macd

    @property
    def relateive_macd(self):
        """Gets the relateive_macd of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relateive_macd of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relateive_macd

    @relateive_macd.setter
    def relateive_macd(self, relateive_macd):
        """Sets the relateive_macd of this CurrentMomentumMetricsDto.


        :param relateive_macd: The relateive_macd of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relateive_macd = relateive_macd

    @property
    def ma12(self):
        """Gets the ma12 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The ma12 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._ma12

    @ma12.setter
    def ma12(self, ma12):
        """Sets the ma12 of this CurrentMomentumMetricsDto.


        :param ma12: The ma12 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._ma12 = ma12

    @property
    def relateive_ma12(self):
        """Gets the relateive_ma12 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relateive_ma12 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relateive_ma12

    @relateive_ma12.setter
    def relateive_ma12(self, relateive_ma12):
        """Sets the relateive_ma12 of this CurrentMomentumMetricsDto.


        :param relateive_ma12: The relateive_ma12 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relateive_ma12 = relateive_ma12

    @property
    def ma26(self):
        """Gets the ma26 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The ma26 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._ma26

    @ma26.setter
    def ma26(self, ma26):
        """Sets the ma26 of this CurrentMomentumMetricsDto.


        :param ma26: The ma26 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._ma26 = ma26

    @property
    def relateive_ma26(self):
        """Gets the relateive_ma26 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relateive_ma26 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relateive_ma26

    @relateive_ma26.setter
    def relateive_ma26(self, relateive_ma26):
        """Sets the relateive_ma26 of this CurrentMomentumMetricsDto.


        :param relateive_ma26: The relateive_ma26 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relateive_ma26 = relateive_ma26

    @property
    def ma5(self):
        """Gets the ma5 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The ma5 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._ma5

    @ma5.setter
    def ma5(self, ma5):
        """Sets the ma5 of this CurrentMomentumMetricsDto.


        :param ma5: The ma5 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._ma5 = ma5

    @property
    def relateive_ma5(self):
        """Gets the relateive_ma5 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relateive_ma5 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relateive_ma5

    @relateive_ma5.setter
    def relateive_ma5(self, relateive_ma5):
        """Sets the relateive_ma5 of this CurrentMomentumMetricsDto.


        :param relateive_ma5: The relateive_ma5 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relateive_ma5 = relateive_ma5

    @property
    def ma52(self):
        """Gets the ma52 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The ma52 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._ma52

    @ma52.setter
    def ma52(self, ma52):
        """Sets the ma52 of this CurrentMomentumMetricsDto.


        :param ma52: The ma52 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._ma52 = ma52

    @property
    def relateive_ma52(self):
        """Gets the relateive_ma52 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relateive_ma52 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relateive_ma52

    @relateive_ma52.setter
    def relateive_ma52(self, relateive_ma52):
        """Sets the relateive_ma52 of this CurrentMomentumMetricsDto.


        :param relateive_ma52: The relateive_ma52 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relateive_ma52 = relateive_ma52

    @property
    def ema12(self):
        """Gets the ema12 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The ema12 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._ema12

    @ema12.setter
    def ema12(self, ema12):
        """Sets the ema12 of this CurrentMomentumMetricsDto.


        :param ema12: The ema12 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._ema12 = ema12

    @property
    def relateive_ema12(self):
        """Gets the relateive_ema12 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relateive_ema12 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relateive_ema12

    @relateive_ema12.setter
    def relateive_ema12(self, relateive_ema12):
        """Sets the relateive_ema12 of this CurrentMomentumMetricsDto.


        :param relateive_ema12: The relateive_ema12 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relateive_ema12 = relateive_ema12

    @property
    def ema26(self):
        """Gets the ema26 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The ema26 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._ema26

    @ema26.setter
    def ema26(self, ema26):
        """Sets the ema26 of this CurrentMomentumMetricsDto.


        :param ema26: The ema26 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._ema26 = ema26

    @property
    def relateive_ema26(self):
        """Gets the relateive_ema26 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relateive_ema26 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relateive_ema26

    @relateive_ema26.setter
    def relateive_ema26(self, relateive_ema26):
        """Sets the relateive_ema26 of this CurrentMomentumMetricsDto.


        :param relateive_ema26: The relateive_ema26 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relateive_ema26 = relateive_ema26

    @property
    def ema5(self):
        """Gets the ema5 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The ema5 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._ema5

    @ema5.setter
    def ema5(self, ema5):
        """Sets the ema5 of this CurrentMomentumMetricsDto.


        :param ema5: The ema5 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._ema5 = ema5

    @property
    def relateive_ema5(self):
        """Gets the relateive_ema5 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relateive_ema5 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relateive_ema5

    @relateive_ema5.setter
    def relateive_ema5(self, relateive_ema5):
        """Sets the relateive_ema5 of this CurrentMomentumMetricsDto.


        :param relateive_ema5: The relateive_ema5 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relateive_ema5 = relateive_ema5

    @property
    def ema52(self):
        """Gets the ema52 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The ema52 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._ema52

    @ema52.setter
    def ema52(self, ema52):
        """Sets the ema52 of this CurrentMomentumMetricsDto.


        :param ema52: The ema52 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._ema52 = ema52

    @property
    def relateive_ema52(self):
        """Gets the relateive_ema52 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relateive_ema52 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relateive_ema52

    @relateive_ema52.setter
    def relateive_ema52(self, relateive_ema52):
        """Sets the relateive_ema52 of this CurrentMomentumMetricsDto.


        :param relateive_ema52: The relateive_ema52 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relateive_ema52 = relateive_ema52

    @property
    def rsi14_d(self):
        """Gets the rsi14_d of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The rsi14_d of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._rsi14_d

    @rsi14_d.setter
    def rsi14_d(self, rsi14_d):
        """Sets the rsi14_d of this CurrentMomentumMetricsDto.


        :param rsi14_d: The rsi14_d of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._rsi14_d = rsi14_d

    @property
    def timestamp(self):
        """Gets the timestamp of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The timestamp of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CurrentMomentumMetricsDto.


        :param timestamp: The timestamp of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

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
        if issubclass(CurrentMomentumMetricsDto, dict):
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
        if not isinstance(other, CurrentMomentumMetricsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
