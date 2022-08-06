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

class StockSummaryDto(object):
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
        'high52_w': 'float',
        'low52_w': 'float',
        'basic_eps': 'float',
        'adjusted_basic_eps': 'float',
        'market_cap': 'float',
        'pe_ratio_ttm': 'float',
        'dividend_yield_ttm': 'float',
        'current_price': 'float',
        'change': 'float',
        'change_perc': 'float',
        'previous_close': 'float',
        'latest_price_time': 'int',
        'eps_fyq': 'str',
        'about_company': 'str',
        'industry_category': 'str',
        'industry_group': 'str',
        'employees': 'int',
        'ticker_slug': 'str',
        'low_price': 'float',
        'high_price': 'float'
    }

    attribute_map = {
        'ticker': 'Ticker',
        'exchange': 'Exchange',
        'name': 'Name',
        'sector': 'Sector',
        'high52_w': 'High52W',
        'low52_w': 'Low52W',
        'basic_eps': 'BasicEps',
        'adjusted_basic_eps': 'AdjustedBasicEps',
        'market_cap': 'MarketCap',
        'pe_ratio_ttm': 'PERatioTTM',
        'dividend_yield_ttm': 'DividendYieldTTM',
        'current_price': 'CurrentPrice',
        'change': 'Change',
        'change_perc': 'ChangePerc',
        'previous_close': 'PreviousClose',
        'latest_price_time': 'LatestPriceTime',
        'eps_fyq': 'EpsFyq',
        'about_company': 'AboutCompany',
        'industry_category': 'IndustryCategory',
        'industry_group': 'IndustryGroup',
        'employees': 'Employees',
        'ticker_slug': 'TickerSlug',
        'low_price': 'LowPrice',
        'high_price': 'HighPrice'
    }

    def __init__(self, ticker=None, exchange=None, name=None, sector=None, high52_w=None, low52_w=None, basic_eps=None, adjusted_basic_eps=None, market_cap=None, pe_ratio_ttm=None, dividend_yield_ttm=None, current_price=None, change=None, change_perc=None, previous_close=None, latest_price_time=None, eps_fyq=None, about_company=None, industry_category=None, industry_group=None, employees=None, ticker_slug=None, low_price=None, high_price=None):  # noqa: E501
        """StockSummaryDto - a model defined in Swagger"""  # noqa: E501
        self._ticker = None
        self._exchange = None
        self._name = None
        self._sector = None
        self._high52_w = None
        self._low52_w = None
        self._basic_eps = None
        self._adjusted_basic_eps = None
        self._market_cap = None
        self._pe_ratio_ttm = None
        self._dividend_yield_ttm = None
        self._current_price = None
        self._change = None
        self._change_perc = None
        self._previous_close = None
        self._latest_price_time = None
        self._eps_fyq = None
        self._about_company = None
        self._industry_category = None
        self._industry_group = None
        self._employees = None
        self._ticker_slug = None
        self._low_price = None
        self._high_price = None
        self.discriminator = None
        if ticker is not None:
            self.ticker = ticker
        if exchange is not None:
            self.exchange = exchange
        if name is not None:
            self.name = name
        if sector is not None:
            self.sector = sector
        if high52_w is not None:
            self.high52_w = high52_w
        if low52_w is not None:
            self.low52_w = low52_w
        if basic_eps is not None:
            self.basic_eps = basic_eps
        if adjusted_basic_eps is not None:
            self.adjusted_basic_eps = adjusted_basic_eps
        if market_cap is not None:
            self.market_cap = market_cap
        if pe_ratio_ttm is not None:
            self.pe_ratio_ttm = pe_ratio_ttm
        if dividend_yield_ttm is not None:
            self.dividend_yield_ttm = dividend_yield_ttm
        if current_price is not None:
            self.current_price = current_price
        if change is not None:
            self.change = change
        if change_perc is not None:
            self.change_perc = change_perc
        if previous_close is not None:
            self.previous_close = previous_close
        if latest_price_time is not None:
            self.latest_price_time = latest_price_time
        if eps_fyq is not None:
            self.eps_fyq = eps_fyq
        if about_company is not None:
            self.about_company = about_company
        if industry_category is not None:
            self.industry_category = industry_category
        if industry_group is not None:
            self.industry_group = industry_group
        if employees is not None:
            self.employees = employees
        if ticker_slug is not None:
            self.ticker_slug = ticker_slug
        if low_price is not None:
            self.low_price = low_price
        if high_price is not None:
            self.high_price = high_price

    @property
    def ticker(self):
        """Gets the ticker of this StockSummaryDto.  # noqa: E501


        :return: The ticker of this StockSummaryDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this StockSummaryDto.


        :param ticker: The ticker of this StockSummaryDto.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def exchange(self):
        """Gets the exchange of this StockSummaryDto.  # noqa: E501


        :return: The exchange of this StockSummaryDto.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this StockSummaryDto.


        :param exchange: The exchange of this StockSummaryDto.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def name(self):
        """Gets the name of this StockSummaryDto.  # noqa: E501


        :return: The name of this StockSummaryDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StockSummaryDto.


        :param name: The name of this StockSummaryDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sector(self):
        """Gets the sector of this StockSummaryDto.  # noqa: E501


        :return: The sector of this StockSummaryDto.  # noqa: E501
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this StockSummaryDto.


        :param sector: The sector of this StockSummaryDto.  # noqa: E501
        :type: str
        """

        self._sector = sector

    @property
    def high52_w(self):
        """Gets the high52_w of this StockSummaryDto.  # noqa: E501


        :return: The high52_w of this StockSummaryDto.  # noqa: E501
        :rtype: float
        """
        return self._high52_w

    @high52_w.setter
    def high52_w(self, high52_w):
        """Sets the high52_w of this StockSummaryDto.


        :param high52_w: The high52_w of this StockSummaryDto.  # noqa: E501
        :type: float
        """

        self._high52_w = high52_w

    @property
    def low52_w(self):
        """Gets the low52_w of this StockSummaryDto.  # noqa: E501


        :return: The low52_w of this StockSummaryDto.  # noqa: E501
        :rtype: float
        """
        return self._low52_w

    @low52_w.setter
    def low52_w(self, low52_w):
        """Sets the low52_w of this StockSummaryDto.


        :param low52_w: The low52_w of this StockSummaryDto.  # noqa: E501
        :type: float
        """

        self._low52_w = low52_w

    @property
    def basic_eps(self):
        """Gets the basic_eps of this StockSummaryDto.  # noqa: E501


        :return: The basic_eps of this StockSummaryDto.  # noqa: E501
        :rtype: float
        """
        return self._basic_eps

    @basic_eps.setter
    def basic_eps(self, basic_eps):
        """Sets the basic_eps of this StockSummaryDto.


        :param basic_eps: The basic_eps of this StockSummaryDto.  # noqa: E501
        :type: float
        """

        self._basic_eps = basic_eps

    @property
    def adjusted_basic_eps(self):
        """Gets the adjusted_basic_eps of this StockSummaryDto.  # noqa: E501


        :return: The adjusted_basic_eps of this StockSummaryDto.  # noqa: E501
        :rtype: float
        """
        return self._adjusted_basic_eps

    @adjusted_basic_eps.setter
    def adjusted_basic_eps(self, adjusted_basic_eps):
        """Sets the adjusted_basic_eps of this StockSummaryDto.


        :param adjusted_basic_eps: The adjusted_basic_eps of this StockSummaryDto.  # noqa: E501
        :type: float
        """

        self._adjusted_basic_eps = adjusted_basic_eps

    @property
    def market_cap(self):
        """Gets the market_cap of this StockSummaryDto.  # noqa: E501


        :return: The market_cap of this StockSummaryDto.  # noqa: E501
        :rtype: float
        """
        return self._market_cap

    @market_cap.setter
    def market_cap(self, market_cap):
        """Sets the market_cap of this StockSummaryDto.


        :param market_cap: The market_cap of this StockSummaryDto.  # noqa: E501
        :type: float
        """

        self._market_cap = market_cap

    @property
    def pe_ratio_ttm(self):
        """Gets the pe_ratio_ttm of this StockSummaryDto.  # noqa: E501


        :return: The pe_ratio_ttm of this StockSummaryDto.  # noqa: E501
        :rtype: float
        """
        return self._pe_ratio_ttm

    @pe_ratio_ttm.setter
    def pe_ratio_ttm(self, pe_ratio_ttm):
        """Sets the pe_ratio_ttm of this StockSummaryDto.


        :param pe_ratio_ttm: The pe_ratio_ttm of this StockSummaryDto.  # noqa: E501
        :type: float
        """

        self._pe_ratio_ttm = pe_ratio_ttm

    @property
    def dividend_yield_ttm(self):
        """Gets the dividend_yield_ttm of this StockSummaryDto.  # noqa: E501


        :return: The dividend_yield_ttm of this StockSummaryDto.  # noqa: E501
        :rtype: float
        """
        return self._dividend_yield_ttm

    @dividend_yield_ttm.setter
    def dividend_yield_ttm(self, dividend_yield_ttm):
        """Sets the dividend_yield_ttm of this StockSummaryDto.


        :param dividend_yield_ttm: The dividend_yield_ttm of this StockSummaryDto.  # noqa: E501
        :type: float
        """

        self._dividend_yield_ttm = dividend_yield_ttm

    @property
    def current_price(self):
        """Gets the current_price of this StockSummaryDto.  # noqa: E501


        :return: The current_price of this StockSummaryDto.  # noqa: E501
        :rtype: float
        """
        return self._current_price

    @current_price.setter
    def current_price(self, current_price):
        """Sets the current_price of this StockSummaryDto.


        :param current_price: The current_price of this StockSummaryDto.  # noqa: E501
        :type: float
        """

        self._current_price = current_price

    @property
    def change(self):
        """Gets the change of this StockSummaryDto.  # noqa: E501


        :return: The change of this StockSummaryDto.  # noqa: E501
        :rtype: float
        """
        return self._change

    @change.setter
    def change(self, change):
        """Sets the change of this StockSummaryDto.


        :param change: The change of this StockSummaryDto.  # noqa: E501
        :type: float
        """

        self._change = change

    @property
    def change_perc(self):
        """Gets the change_perc of this StockSummaryDto.  # noqa: E501


        :return: The change_perc of this StockSummaryDto.  # noqa: E501
        :rtype: float
        """
        return self._change_perc

    @change_perc.setter
    def change_perc(self, change_perc):
        """Sets the change_perc of this StockSummaryDto.


        :param change_perc: The change_perc of this StockSummaryDto.  # noqa: E501
        :type: float
        """

        self._change_perc = change_perc

    @property
    def previous_close(self):
        """Gets the previous_close of this StockSummaryDto.  # noqa: E501


        :return: The previous_close of this StockSummaryDto.  # noqa: E501
        :rtype: float
        """
        return self._previous_close

    @previous_close.setter
    def previous_close(self, previous_close):
        """Sets the previous_close of this StockSummaryDto.


        :param previous_close: The previous_close of this StockSummaryDto.  # noqa: E501
        :type: float
        """

        self._previous_close = previous_close

    @property
    def latest_price_time(self):
        """Gets the latest_price_time of this StockSummaryDto.  # noqa: E501


        :return: The latest_price_time of this StockSummaryDto.  # noqa: E501
        :rtype: int
        """
        return self._latest_price_time

    @latest_price_time.setter
    def latest_price_time(self, latest_price_time):
        """Sets the latest_price_time of this StockSummaryDto.


        :param latest_price_time: The latest_price_time of this StockSummaryDto.  # noqa: E501
        :type: int
        """

        self._latest_price_time = latest_price_time

    @property
    def eps_fyq(self):
        """Gets the eps_fyq of this StockSummaryDto.  # noqa: E501


        :return: The eps_fyq of this StockSummaryDto.  # noqa: E501
        :rtype: str
        """
        return self._eps_fyq

    @eps_fyq.setter
    def eps_fyq(self, eps_fyq):
        """Sets the eps_fyq of this StockSummaryDto.


        :param eps_fyq: The eps_fyq of this StockSummaryDto.  # noqa: E501
        :type: str
        """

        self._eps_fyq = eps_fyq

    @property
    def about_company(self):
        """Gets the about_company of this StockSummaryDto.  # noqa: E501


        :return: The about_company of this StockSummaryDto.  # noqa: E501
        :rtype: str
        """
        return self._about_company

    @about_company.setter
    def about_company(self, about_company):
        """Sets the about_company of this StockSummaryDto.


        :param about_company: The about_company of this StockSummaryDto.  # noqa: E501
        :type: str
        """

        self._about_company = about_company

    @property
    def industry_category(self):
        """Gets the industry_category of this StockSummaryDto.  # noqa: E501


        :return: The industry_category of this StockSummaryDto.  # noqa: E501
        :rtype: str
        """
        return self._industry_category

    @industry_category.setter
    def industry_category(self, industry_category):
        """Sets the industry_category of this StockSummaryDto.


        :param industry_category: The industry_category of this StockSummaryDto.  # noqa: E501
        :type: str
        """

        self._industry_category = industry_category

    @property
    def industry_group(self):
        """Gets the industry_group of this StockSummaryDto.  # noqa: E501


        :return: The industry_group of this StockSummaryDto.  # noqa: E501
        :rtype: str
        """
        return self._industry_group

    @industry_group.setter
    def industry_group(self, industry_group):
        """Sets the industry_group of this StockSummaryDto.


        :param industry_group: The industry_group of this StockSummaryDto.  # noqa: E501
        :type: str
        """

        self._industry_group = industry_group

    @property
    def employees(self):
        """Gets the employees of this StockSummaryDto.  # noqa: E501


        :return: The employees of this StockSummaryDto.  # noqa: E501
        :rtype: int
        """
        return self._employees

    @employees.setter
    def employees(self, employees):
        """Sets the employees of this StockSummaryDto.


        :param employees: The employees of this StockSummaryDto.  # noqa: E501
        :type: int
        """

        self._employees = employees

    @property
    def ticker_slug(self):
        """Gets the ticker_slug of this StockSummaryDto.  # noqa: E501


        :return: The ticker_slug of this StockSummaryDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker_slug

    @ticker_slug.setter
    def ticker_slug(self, ticker_slug):
        """Sets the ticker_slug of this StockSummaryDto.


        :param ticker_slug: The ticker_slug of this StockSummaryDto.  # noqa: E501
        :type: str
        """

        self._ticker_slug = ticker_slug

    @property
    def low_price(self):
        """Gets the low_price of this StockSummaryDto.  # noqa: E501


        :return: The low_price of this StockSummaryDto.  # noqa: E501
        :rtype: float
        """
        return self._low_price

    @low_price.setter
    def low_price(self, low_price):
        """Sets the low_price of this StockSummaryDto.


        :param low_price: The low_price of this StockSummaryDto.  # noqa: E501
        :type: float
        """

        self._low_price = low_price

    @property
    def high_price(self):
        """Gets the high_price of this StockSummaryDto.  # noqa: E501


        :return: The high_price of this StockSummaryDto.  # noqa: E501
        :rtype: float
        """
        return self._high_price

    @high_price.setter
    def high_price(self, high_price):
        """Sets the high_price of this StockSummaryDto.


        :param high_price: The high_price of this StockSummaryDto.  # noqa: E501
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
        if issubclass(StockSummaryDto, dict):
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
        if not isinstance(other, StockSummaryDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other