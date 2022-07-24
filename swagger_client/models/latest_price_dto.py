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

class LatestPriceDto(object):
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
        'security_id': 'str',
        'ticker': 'str',
        'latest_price': 'float',
        'price_time': 'int',
        'change': 'float',
        'change_perc': 'float',
        'previous_close': 'float',
        'open_price': 'float',
        'low_price': 'float',
        'high_price': 'float'
    }

    attribute_map = {
        'security_id': 'SecurityId',
        'ticker': 'Ticker',
        'latest_price': 'LatestPrice',
        'price_time': 'PriceTime',
        'change': 'Change',
        'change_perc': 'ChangePerc',
        'previous_close': 'PreviousClose',
        'open_price': 'OpenPrice',
        'low_price': 'LowPrice',
        'high_price': 'HighPrice'
    }

    def __init__(self, security_id=None, ticker=None, latest_price=None, price_time=None, change=None, change_perc=None, previous_close=None, open_price=None, low_price=None, high_price=None):  # noqa: E501
        """LatestPriceDto - a model defined in Swagger"""  # noqa: E501
        self._security_id = None
        self._ticker = None
        self._latest_price = None
        self._price_time = None
        self._change = None
        self._change_perc = None
        self._previous_close = None
        self._open_price = None
        self._low_price = None
        self._high_price = None
        self.discriminator = None
        if security_id is not None:
            self.security_id = security_id
        if ticker is not None:
            self.ticker = ticker
        if latest_price is not None:
            self.latest_price = latest_price
        if price_time is not None:
            self.price_time = price_time
        if change is not None:
            self.change = change
        if change_perc is not None:
            self.change_perc = change_perc
        if previous_close is not None:
            self.previous_close = previous_close
        if open_price is not None:
            self.open_price = open_price
        if low_price is not None:
            self.low_price = low_price
        if high_price is not None:
            self.high_price = high_price

    @property
    def security_id(self):
        """Gets the security_id of this LatestPriceDto.  # noqa: E501


        :return: The security_id of this LatestPriceDto.  # noqa: E501
        :rtype: str
        """
        return self._security_id

    @security_id.setter
    def security_id(self, security_id):
        """Sets the security_id of this LatestPriceDto.


        :param security_id: The security_id of this LatestPriceDto.  # noqa: E501
        :type: str
        """

        self._security_id = security_id

    @property
    def ticker(self):
        """Gets the ticker of this LatestPriceDto.  # noqa: E501


        :return: The ticker of this LatestPriceDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this LatestPriceDto.


        :param ticker: The ticker of this LatestPriceDto.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def latest_price(self):
        """Gets the latest_price of this LatestPriceDto.  # noqa: E501


        :return: The latest_price of this LatestPriceDto.  # noqa: E501
        :rtype: float
        """
        return self._latest_price

    @latest_price.setter
    def latest_price(self, latest_price):
        """Sets the latest_price of this LatestPriceDto.


        :param latest_price: The latest_price of this LatestPriceDto.  # noqa: E501
        :type: float
        """

        self._latest_price = latest_price

    @property
    def price_time(self):
        """Gets the price_time of this LatestPriceDto.  # noqa: E501


        :return: The price_time of this LatestPriceDto.  # noqa: E501
        :rtype: int
        """
        return self._price_time

    @price_time.setter
    def price_time(self, price_time):
        """Sets the price_time of this LatestPriceDto.


        :param price_time: The price_time of this LatestPriceDto.  # noqa: E501
        :type: int
        """

        self._price_time = price_time

    @property
    def change(self):
        """Gets the change of this LatestPriceDto.  # noqa: E501


        :return: The change of this LatestPriceDto.  # noqa: E501
        :rtype: float
        """
        return self._change

    @change.setter
    def change(self, change):
        """Sets the change of this LatestPriceDto.


        :param change: The change of this LatestPriceDto.  # noqa: E501
        :type: float
        """

        self._change = change

    @property
    def change_perc(self):
        """Gets the change_perc of this LatestPriceDto.  # noqa: E501


        :return: The change_perc of this LatestPriceDto.  # noqa: E501
        :rtype: float
        """
        return self._change_perc

    @change_perc.setter
    def change_perc(self, change_perc):
        """Sets the change_perc of this LatestPriceDto.


        :param change_perc: The change_perc of this LatestPriceDto.  # noqa: E501
        :type: float
        """

        self._change_perc = change_perc

    @property
    def previous_close(self):
        """Gets the previous_close of this LatestPriceDto.  # noqa: E501


        :return: The previous_close of this LatestPriceDto.  # noqa: E501
        :rtype: float
        """
        return self._previous_close

    @previous_close.setter
    def previous_close(self, previous_close):
        """Sets the previous_close of this LatestPriceDto.


        :param previous_close: The previous_close of this LatestPriceDto.  # noqa: E501
        :type: float
        """

        self._previous_close = previous_close

    @property
    def open_price(self):
        """Gets the open_price of this LatestPriceDto.  # noqa: E501


        :return: The open_price of this LatestPriceDto.  # noqa: E501
        :rtype: float
        """
        return self._open_price

    @open_price.setter
    def open_price(self, open_price):
        """Sets the open_price of this LatestPriceDto.


        :param open_price: The open_price of this LatestPriceDto.  # noqa: E501
        :type: float
        """

        self._open_price = open_price

    @property
    def low_price(self):
        """Gets the low_price of this LatestPriceDto.  # noqa: E501


        :return: The low_price of this LatestPriceDto.  # noqa: E501
        :rtype: float
        """
        return self._low_price

    @low_price.setter
    def low_price(self, low_price):
        """Sets the low_price of this LatestPriceDto.


        :param low_price: The low_price of this LatestPriceDto.  # noqa: E501
        :type: float
        """

        self._low_price = low_price

    @property
    def high_price(self):
        """Gets the high_price of this LatestPriceDto.  # noqa: E501


        :return: The high_price of this LatestPriceDto.  # noqa: E501
        :rtype: float
        """
        return self._high_price

    @high_price.setter
    def high_price(self, high_price):
        """Sets the high_price of this LatestPriceDto.


        :param high_price: The high_price of this LatestPriceDto.  # noqa: E501
        :type: float
        """

        self._high_price = high_price

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
        if issubclass(LatestPriceDto, dict):
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
        if not isinstance(other, LatestPriceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
