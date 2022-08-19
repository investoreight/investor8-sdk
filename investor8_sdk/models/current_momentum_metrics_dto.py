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
        'relative_macd': 'float',
        'ma12': 'float',
        'relative_ma12': 'float',
        'ma26': 'float',
        'relative_ma26': 'float',
        'ma5': 'float',
        'relative_ma5': 'float',
        'ma52': 'float',
        'relative_ma52': 'float',
        'ema12': 'float',
        'relative_ema12': 'float',
        'ema26': 'float',
        'relative_ema26': 'float',
        'ema5': 'float',
        'relative_ema5': 'float',
        'ema52': 'float',
        'relative_ema52': 'float',
        'rsi14_d': 'float',
        'timestamp': 'int'
    }

    attribute_map = {
        'ticker': 'Ticker',
        'macd': 'MACD',
        'relative_macd': 'RelativeMACD',
        'ma12': 'MA12',
        'relative_ma12': 'RelativeMA12',
        'ma26': 'MA26',
        'relative_ma26': 'RelativeMA26',
        'ma5': 'MA5',
        'relative_ma5': 'RelativeMA5',
        'ma52': 'MA52',
        'relative_ma52': 'RelativeMA52',
        'ema12': 'EMA12',
        'relative_ema12': 'RelativeEMA12',
        'ema26': 'EMA26',
        'relative_ema26': 'RelativeEMA26',
        'ema5': 'EMA5',
        'relative_ema5': 'RelativeEMA5',
        'ema52': 'EMA52',
        'relative_ema52': 'RelativeEMA52',
        'rsi14_d': 'RSI14D',
        'timestamp': 'Timestamp'
    }

    def __init__(self, ticker=None, macd=None, relative_macd=None, ma12=None, relative_ma12=None, ma26=None, relative_ma26=None, ma5=None, relative_ma5=None, ma52=None, relative_ma52=None, ema12=None, relative_ema12=None, ema26=None, relative_ema26=None, ema5=None, relative_ema5=None, ema52=None, relative_ema52=None, rsi14_d=None, timestamp=None):  # noqa: E501
        """CurrentMomentumMetricsDto - a model defined in Swagger"""  # noqa: E501
        self._ticker = None
        self._macd = None
        self._relative_macd = None
        self._ma12 = None
        self._relative_ma12 = None
        self._ma26 = None
        self._relative_ma26 = None
        self._ma5 = None
        self._relative_ma5 = None
        self._ma52 = None
        self._relative_ma52 = None
        self._ema12 = None
        self._relative_ema12 = None
        self._ema26 = None
        self._relative_ema26 = None
        self._ema5 = None
        self._relative_ema5 = None
        self._ema52 = None
        self._relative_ema52 = None
        self._rsi14_d = None
        self._timestamp = None
        self.discriminator = None
        if ticker is not None:
            self.ticker = ticker
        if macd is not None:
            self.macd = macd
        if relative_macd is not None:
            self.relative_macd = relative_macd
        if ma12 is not None:
            self.ma12 = ma12
        if relative_ma12 is not None:
            self.relative_ma12 = relative_ma12
        if ma26 is not None:
            self.ma26 = ma26
        if relative_ma26 is not None:
            self.relative_ma26 = relative_ma26
        if ma5 is not None:
            self.ma5 = ma5
        if relative_ma5 is not None:
            self.relative_ma5 = relative_ma5
        if ma52 is not None:
            self.ma52 = ma52
        if relative_ma52 is not None:
            self.relative_ma52 = relative_ma52
        if ema12 is not None:
            self.ema12 = ema12
        if relative_ema12 is not None:
            self.relative_ema12 = relative_ema12
        if ema26 is not None:
            self.ema26 = ema26
        if relative_ema26 is not None:
            self.relative_ema26 = relative_ema26
        if ema5 is not None:
            self.ema5 = ema5
        if relative_ema5 is not None:
            self.relative_ema5 = relative_ema5
        if ema52 is not None:
            self.ema52 = ema52
        if relative_ema52 is not None:
            self.relative_ema52 = relative_ema52
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
    def relative_macd(self):
        """Gets the relative_macd of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relative_macd of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relative_macd

    @relative_macd.setter
    def relative_macd(self, relative_macd):
        """Sets the relative_macd of this CurrentMomentumMetricsDto.


        :param relative_macd: The relative_macd of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relative_macd = relative_macd

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
    def relative_ma12(self):
        """Gets the relative_ma12 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relative_ma12 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relative_ma12

    @relative_ma12.setter
    def relative_ma12(self, relative_ma12):
        """Sets the relative_ma12 of this CurrentMomentumMetricsDto.


        :param relative_ma12: The relative_ma12 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relative_ma12 = relative_ma12

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
    def relative_ma26(self):
        """Gets the relative_ma26 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relative_ma26 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relative_ma26

    @relative_ma26.setter
    def relative_ma26(self, relative_ma26):
        """Sets the relative_ma26 of this CurrentMomentumMetricsDto.


        :param relative_ma26: The relative_ma26 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relative_ma26 = relative_ma26

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
    def relative_ma5(self):
        """Gets the relative_ma5 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relative_ma5 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relative_ma5

    @relative_ma5.setter
    def relative_ma5(self, relative_ma5):
        """Sets the relative_ma5 of this CurrentMomentumMetricsDto.


        :param relative_ma5: The relative_ma5 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relative_ma5 = relative_ma5

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
    def relative_ma52(self):
        """Gets the relative_ma52 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relative_ma52 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relative_ma52

    @relative_ma52.setter
    def relative_ma52(self, relative_ma52):
        """Sets the relative_ma52 of this CurrentMomentumMetricsDto.


        :param relative_ma52: The relative_ma52 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relative_ma52 = relative_ma52

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
    def relative_ema12(self):
        """Gets the relative_ema12 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relative_ema12 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relative_ema12

    @relative_ema12.setter
    def relative_ema12(self, relative_ema12):
        """Sets the relative_ema12 of this CurrentMomentumMetricsDto.


        :param relative_ema12: The relative_ema12 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relative_ema12 = relative_ema12

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
    def relative_ema26(self):
        """Gets the relative_ema26 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relative_ema26 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relative_ema26

    @relative_ema26.setter
    def relative_ema26(self, relative_ema26):
        """Sets the relative_ema26 of this CurrentMomentumMetricsDto.


        :param relative_ema26: The relative_ema26 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relative_ema26 = relative_ema26

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
    def relative_ema5(self):
        """Gets the relative_ema5 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relative_ema5 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relative_ema5

    @relative_ema5.setter
    def relative_ema5(self, relative_ema5):
        """Sets the relative_ema5 of this CurrentMomentumMetricsDto.


        :param relative_ema5: The relative_ema5 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relative_ema5 = relative_ema5

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
    def relative_ema52(self):
        """Gets the relative_ema52 of this CurrentMomentumMetricsDto.  # noqa: E501


        :return: The relative_ema52 of this CurrentMomentumMetricsDto.  # noqa: E501
        :rtype: float
        """
        return self._relative_ema52

    @relative_ema52.setter
    def relative_ema52(self, relative_ema52):
        """Sets the relative_ema52 of this CurrentMomentumMetricsDto.


        :param relative_ema52: The relative_ema52 of this CurrentMomentumMetricsDto.  # noqa: E501
        :type: float
        """

        self._relative_ema52 = relative_ema52

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
