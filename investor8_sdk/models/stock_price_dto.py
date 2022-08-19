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

class StockPriceDto(object):
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
        'exchange': 'str',
        'name': 'str',
        'sector': 'str',
        'latest_price': 'float',
        'change': 'float',
        'change_perc': 'float',
        'marketcap': 'float',
        'price_time': 'int',
        'high52': 'float',
        'low52': 'float',
        'pe_ratio_ttm': 'float',
        'ticker_slug': 'str'
    }

    attribute_map = {
        'ticker': 'Ticker',
        'exchange': 'Exchange',
        'name': 'Name',
        'sector': 'Sector',
        'latest_price': 'LatestPrice',
        'change': 'Change',
        'change_perc': 'ChangePerc',
        'marketcap': 'Marketcap',
        'price_time': 'PriceTime',
        'high52': 'High52',
        'low52': 'Low52',
        'pe_ratio_ttm': 'PERatioTTM',
        'ticker_slug': 'TickerSlug'
    }

    def __init__(self, ticker=None, exchange=None, name=None, sector=None, latest_price=None, change=None, change_perc=None, marketcap=None, price_time=None, high52=None, low52=None, pe_ratio_ttm=None, ticker_slug=None):  # noqa: E501
        """StockPriceDto - a model defined in Swagger"""  # noqa: E501
        self._ticker = None
        self._exchange = None
        self._name = None
        self._sector = None
        self._latest_price = None
        self._change = None
        self._change_perc = None
        self._marketcap = None
        self._price_time = None
        self._high52 = None
        self._low52 = None
        self._pe_ratio_ttm = None
        self._ticker_slug = None
        self.discriminator = None
        if ticker is not None:
            self.ticker = ticker
        if exchange is not None:
            self.exchange = exchange
        if name is not None:
            self.name = name
        if sector is not None:
            self.sector = sector
        if latest_price is not None:
            self.latest_price = latest_price
        if change is not None:
            self.change = change
        if change_perc is not None:
            self.change_perc = change_perc
        if marketcap is not None:
            self.marketcap = marketcap
        if price_time is not None:
            self.price_time = price_time
        if high52 is not None:
            self.high52 = high52
        if low52 is not None:
            self.low52 = low52
        if pe_ratio_ttm is not None:
            self.pe_ratio_ttm = pe_ratio_ttm
        if ticker_slug is not None:
            self.ticker_slug = ticker_slug

    @property
    def ticker(self):
        """Gets the ticker of this StockPriceDto.  # noqa: E501


        :return: The ticker of this StockPriceDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this StockPriceDto.


        :param ticker: The ticker of this StockPriceDto.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def exchange(self):
        """Gets the exchange of this StockPriceDto.  # noqa: E501


        :return: The exchange of this StockPriceDto.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this StockPriceDto.


        :param exchange: The exchange of this StockPriceDto.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def name(self):
        """Gets the name of this StockPriceDto.  # noqa: E501


        :return: The name of this StockPriceDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StockPriceDto.


        :param name: The name of this StockPriceDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sector(self):
        """Gets the sector of this StockPriceDto.  # noqa: E501


        :return: The sector of this StockPriceDto.  # noqa: E501
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this StockPriceDto.


        :param sector: The sector of this StockPriceDto.  # noqa: E501
        :type: str
        """

        self._sector = sector

    @property
    def latest_price(self):
        """Gets the latest_price of this StockPriceDto.  # noqa: E501


        :return: The latest_price of this StockPriceDto.  # noqa: E501
        :rtype: float
        """
        return self._latest_price

    @latest_price.setter
    def latest_price(self, latest_price):
        """Sets the latest_price of this StockPriceDto.


        :param latest_price: The latest_price of this StockPriceDto.  # noqa: E501
        :type: float
        """

        self._latest_price = latest_price

    @property
    def change(self):
        """Gets the change of this StockPriceDto.  # noqa: E501


        :return: The change of this StockPriceDto.  # noqa: E501
        :rtype: float
        """
        return self._change

    @change.setter
    def change(self, change):
        """Sets the change of this StockPriceDto.


        :param change: The change of this StockPriceDto.  # noqa: E501
        :type: float
        """

        self._change = change

    @property
    def change_perc(self):
        """Gets the change_perc of this StockPriceDto.  # noqa: E501


        :return: The change_perc of this StockPriceDto.  # noqa: E501
        :rtype: float
        """
        return self._change_perc

    @change_perc.setter
    def change_perc(self, change_perc):
        """Sets the change_perc of this StockPriceDto.


        :param change_perc: The change_perc of this StockPriceDto.  # noqa: E501
        :type: float
        """

        self._change_perc = change_perc

    @property
    def marketcap(self):
        """Gets the marketcap of this StockPriceDto.  # noqa: E501


        :return: The marketcap of this StockPriceDto.  # noqa: E501
        :rtype: float
        """
        return self._marketcap

    @marketcap.setter
    def marketcap(self, marketcap):
        """Sets the marketcap of this StockPriceDto.


        :param marketcap: The marketcap of this StockPriceDto.  # noqa: E501
        :type: float
        """

        self._marketcap = marketcap

    @property
    def price_time(self):
        """Gets the price_time of this StockPriceDto.  # noqa: E501


        :return: The price_time of this StockPriceDto.  # noqa: E501
        :rtype: int
        """
        return self._price_time

    @price_time.setter
    def price_time(self, price_time):
        """Sets the price_time of this StockPriceDto.


        :param price_time: The price_time of this StockPriceDto.  # noqa: E501
        :type: int
        """

        self._price_time = price_time

    @property
    def high52(self):
        """Gets the high52 of this StockPriceDto.  # noqa: E501


        :return: The high52 of this StockPriceDto.  # noqa: E501
        :rtype: float
        """
        return self._high52

    @high52.setter
    def high52(self, high52):
        """Sets the high52 of this StockPriceDto.


        :param high52: The high52 of this StockPriceDto.  # noqa: E501
        :type: float
        """

        self._high52 = high52

    @property
    def low52(self):
        """Gets the low52 of this StockPriceDto.  # noqa: E501


        :return: The low52 of this StockPriceDto.  # noqa: E501
        :rtype: float
        """
        return self._low52

    @low52.setter
    def low52(self, low52):
        """Sets the low52 of this StockPriceDto.


        :param low52: The low52 of this StockPriceDto.  # noqa: E501
        :type: float
        """

        self._low52 = low52

    @property
    def pe_ratio_ttm(self):
        """Gets the pe_ratio_ttm of this StockPriceDto.  # noqa: E501


        :return: The pe_ratio_ttm of this StockPriceDto.  # noqa: E501
        :rtype: float
        """
        return self._pe_ratio_ttm

    @pe_ratio_ttm.setter
    def pe_ratio_ttm(self, pe_ratio_ttm):
        """Sets the pe_ratio_ttm of this StockPriceDto.


        :param pe_ratio_ttm: The pe_ratio_ttm of this StockPriceDto.  # noqa: E501
        :type: float
        """

        self._pe_ratio_ttm = pe_ratio_ttm

    @property
    def ticker_slug(self):
        """Gets the ticker_slug of this StockPriceDto.  # noqa: E501


        :return: The ticker_slug of this StockPriceDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker_slug

    @ticker_slug.setter
    def ticker_slug(self, ticker_slug):
        """Sets the ticker_slug of this StockPriceDto.


        :param ticker_slug: The ticker_slug of this StockPriceDto.  # noqa: E501
        :type: str
        """

        self._ticker_slug = ticker_slug

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
        if issubclass(StockPriceDto, dict):
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
        if not isinstance(other, StockPriceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
