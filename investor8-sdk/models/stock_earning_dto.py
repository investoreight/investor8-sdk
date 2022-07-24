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

class StockEarningDto(object):
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
        'security_id': 'str',
        'name': 'str',
        'exchange': 'str',
        'sector': 'str',
        'actual_report_time': 'int',
        'actual_report_date': 'str',
        'call_time': 'str',
        'fyq': 'str',
        'eps_actual': 'float',
        'eps_ws': 'float',
        'eps_beat_rate': 'float',
        'revenue_actual': 'float',
        'revenue_ws': 'float',
        'revenue_beat_rate': 'float',
        'eps_contributors_count': 'int',
        'revenue_contributors_count': 'int',
        'pos_return_prob': 'float',
        'expected_return': 'float',
        'fiscal_quarter': 'int',
        'eps_surprise': 'float',
        'revenue_surprise': 'float'
    }

    attribute_map = {
        'id': 'Id',
        'ticker': 'Ticker',
        'security_id': 'SecurityId',
        'name': 'Name',
        'exchange': 'Exchange',
        'sector': 'Sector',
        'actual_report_time': 'ActualReportTime',
        'actual_report_date': 'ActualReportDate',
        'call_time': 'CallTime',
        'fyq': 'FYQ',
        'eps_actual': 'EpsActual',
        'eps_ws': 'EpsWs',
        'eps_beat_rate': 'EpsBeatRate',
        'revenue_actual': 'RevenueActual',
        'revenue_ws': 'RevenueWs',
        'revenue_beat_rate': 'RevenueBeatRate',
        'eps_contributors_count': 'EpsContributorsCount',
        'revenue_contributors_count': 'RevenueContributorsCount',
        'pos_return_prob': 'PosReturnProb',
        'expected_return': 'ExpectedReturn',
        'fiscal_quarter': 'FiscalQuarter',
        'eps_surprise': 'EpsSurprise',
        'revenue_surprise': 'RevenueSurprise'
    }

    def __init__(self, id=None, ticker=None, security_id=None, name=None, exchange=None, sector=None, actual_report_time=None, actual_report_date=None, call_time=None, fyq=None, eps_actual=None, eps_ws=None, eps_beat_rate=None, revenue_actual=None, revenue_ws=None, revenue_beat_rate=None, eps_contributors_count=None, revenue_contributors_count=None, pos_return_prob=None, expected_return=None, fiscal_quarter=None, eps_surprise=None, revenue_surprise=None):  # noqa: E501
        """StockEarningDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._ticker = None
        self._security_id = None
        self._name = None
        self._exchange = None
        self._sector = None
        self._actual_report_time = None
        self._actual_report_date = None
        self._call_time = None
        self._fyq = None
        self._eps_actual = None
        self._eps_ws = None
        self._eps_beat_rate = None
        self._revenue_actual = None
        self._revenue_ws = None
        self._revenue_beat_rate = None
        self._eps_contributors_count = None
        self._revenue_contributors_count = None
        self._pos_return_prob = None
        self._expected_return = None
        self._fiscal_quarter = None
        self._eps_surprise = None
        self._revenue_surprise = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if ticker is not None:
            self.ticker = ticker
        if security_id is not None:
            self.security_id = security_id
        if name is not None:
            self.name = name
        if exchange is not None:
            self.exchange = exchange
        if sector is not None:
            self.sector = sector
        if actual_report_time is not None:
            self.actual_report_time = actual_report_time
        if actual_report_date is not None:
            self.actual_report_date = actual_report_date
        if call_time is not None:
            self.call_time = call_time
        if fyq is not None:
            self.fyq = fyq
        if eps_actual is not None:
            self.eps_actual = eps_actual
        if eps_ws is not None:
            self.eps_ws = eps_ws
        if eps_beat_rate is not None:
            self.eps_beat_rate = eps_beat_rate
        if revenue_actual is not None:
            self.revenue_actual = revenue_actual
        if revenue_ws is not None:
            self.revenue_ws = revenue_ws
        if revenue_beat_rate is not None:
            self.revenue_beat_rate = revenue_beat_rate
        if eps_contributors_count is not None:
            self.eps_contributors_count = eps_contributors_count
        if revenue_contributors_count is not None:
            self.revenue_contributors_count = revenue_contributors_count
        if pos_return_prob is not None:
            self.pos_return_prob = pos_return_prob
        if expected_return is not None:
            self.expected_return = expected_return
        if fiscal_quarter is not None:
            self.fiscal_quarter = fiscal_quarter
        if eps_surprise is not None:
            self.eps_surprise = eps_surprise
        if revenue_surprise is not None:
            self.revenue_surprise = revenue_surprise

    @property
    def id(self):
        """Gets the id of this StockEarningDto.  # noqa: E501


        :return: The id of this StockEarningDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StockEarningDto.


        :param id: The id of this StockEarningDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ticker(self):
        """Gets the ticker of this StockEarningDto.  # noqa: E501


        :return: The ticker of this StockEarningDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this StockEarningDto.


        :param ticker: The ticker of this StockEarningDto.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def security_id(self):
        """Gets the security_id of this StockEarningDto.  # noqa: E501


        :return: The security_id of this StockEarningDto.  # noqa: E501
        :rtype: str
        """
        return self._security_id

    @security_id.setter
    def security_id(self, security_id):
        """Sets the security_id of this StockEarningDto.


        :param security_id: The security_id of this StockEarningDto.  # noqa: E501
        :type: str
        """

        self._security_id = security_id

    @property
    def name(self):
        """Gets the name of this StockEarningDto.  # noqa: E501


        :return: The name of this StockEarningDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StockEarningDto.


        :param name: The name of this StockEarningDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def exchange(self):
        """Gets the exchange of this StockEarningDto.  # noqa: E501


        :return: The exchange of this StockEarningDto.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this StockEarningDto.


        :param exchange: The exchange of this StockEarningDto.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def sector(self):
        """Gets the sector of this StockEarningDto.  # noqa: E501


        :return: The sector of this StockEarningDto.  # noqa: E501
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this StockEarningDto.


        :param sector: The sector of this StockEarningDto.  # noqa: E501
        :type: str
        """

        self._sector = sector

    @property
    def actual_report_time(self):
        """Gets the actual_report_time of this StockEarningDto.  # noqa: E501


        :return: The actual_report_time of this StockEarningDto.  # noqa: E501
        :rtype: int
        """
        return self._actual_report_time

    @actual_report_time.setter
    def actual_report_time(self, actual_report_time):
        """Sets the actual_report_time of this StockEarningDto.


        :param actual_report_time: The actual_report_time of this StockEarningDto.  # noqa: E501
        :type: int
        """

        self._actual_report_time = actual_report_time

    @property
    def actual_report_date(self):
        """Gets the actual_report_date of this StockEarningDto.  # noqa: E501


        :return: The actual_report_date of this StockEarningDto.  # noqa: E501
        :rtype: str
        """
        return self._actual_report_date

    @actual_report_date.setter
    def actual_report_date(self, actual_report_date):
        """Sets the actual_report_date of this StockEarningDto.


        :param actual_report_date: The actual_report_date of this StockEarningDto.  # noqa: E501
        :type: str
        """

        self._actual_report_date = actual_report_date

    @property
    def call_time(self):
        """Gets the call_time of this StockEarningDto.  # noqa: E501


        :return: The call_time of this StockEarningDto.  # noqa: E501
        :rtype: str
        """
        return self._call_time

    @call_time.setter
    def call_time(self, call_time):
        """Sets the call_time of this StockEarningDto.


        :param call_time: The call_time of this StockEarningDto.  # noqa: E501
        :type: str
        """

        self._call_time = call_time

    @property
    def fyq(self):
        """Gets the fyq of this StockEarningDto.  # noqa: E501


        :return: The fyq of this StockEarningDto.  # noqa: E501
        :rtype: str
        """
        return self._fyq

    @fyq.setter
    def fyq(self, fyq):
        """Sets the fyq of this StockEarningDto.


        :param fyq: The fyq of this StockEarningDto.  # noqa: E501
        :type: str
        """

        self._fyq = fyq

    @property
    def eps_actual(self):
        """Gets the eps_actual of this StockEarningDto.  # noqa: E501


        :return: The eps_actual of this StockEarningDto.  # noqa: E501
        :rtype: float
        """
        return self._eps_actual

    @eps_actual.setter
    def eps_actual(self, eps_actual):
        """Sets the eps_actual of this StockEarningDto.


        :param eps_actual: The eps_actual of this StockEarningDto.  # noqa: E501
        :type: float
        """

        self._eps_actual = eps_actual

    @property
    def eps_ws(self):
        """Gets the eps_ws of this StockEarningDto.  # noqa: E501


        :return: The eps_ws of this StockEarningDto.  # noqa: E501
        :rtype: float
        """
        return self._eps_ws

    @eps_ws.setter
    def eps_ws(self, eps_ws):
        """Sets the eps_ws of this StockEarningDto.


        :param eps_ws: The eps_ws of this StockEarningDto.  # noqa: E501
        :type: float
        """

        self._eps_ws = eps_ws

    @property
    def eps_beat_rate(self):
        """Gets the eps_beat_rate of this StockEarningDto.  # noqa: E501


        :return: The eps_beat_rate of this StockEarningDto.  # noqa: E501
        :rtype: float
        """
        return self._eps_beat_rate

    @eps_beat_rate.setter
    def eps_beat_rate(self, eps_beat_rate):
        """Sets the eps_beat_rate of this StockEarningDto.


        :param eps_beat_rate: The eps_beat_rate of this StockEarningDto.  # noqa: E501
        :type: float
        """

        self._eps_beat_rate = eps_beat_rate

    @property
    def revenue_actual(self):
        """Gets the revenue_actual of this StockEarningDto.  # noqa: E501


        :return: The revenue_actual of this StockEarningDto.  # noqa: E501
        :rtype: float
        """
        return self._revenue_actual

    @revenue_actual.setter
    def revenue_actual(self, revenue_actual):
        """Sets the revenue_actual of this StockEarningDto.


        :param revenue_actual: The revenue_actual of this StockEarningDto.  # noqa: E501
        :type: float
        """

        self._revenue_actual = revenue_actual

    @property
    def revenue_ws(self):
        """Gets the revenue_ws of this StockEarningDto.  # noqa: E501


        :return: The revenue_ws of this StockEarningDto.  # noqa: E501
        :rtype: float
        """
        return self._revenue_ws

    @revenue_ws.setter
    def revenue_ws(self, revenue_ws):
        """Sets the revenue_ws of this StockEarningDto.


        :param revenue_ws: The revenue_ws of this StockEarningDto.  # noqa: E501
        :type: float
        """

        self._revenue_ws = revenue_ws

    @property
    def revenue_beat_rate(self):
        """Gets the revenue_beat_rate of this StockEarningDto.  # noqa: E501


        :return: The revenue_beat_rate of this StockEarningDto.  # noqa: E501
        :rtype: float
        """
        return self._revenue_beat_rate

    @revenue_beat_rate.setter
    def revenue_beat_rate(self, revenue_beat_rate):
        """Sets the revenue_beat_rate of this StockEarningDto.


        :param revenue_beat_rate: The revenue_beat_rate of this StockEarningDto.  # noqa: E501
        :type: float
        """

        self._revenue_beat_rate = revenue_beat_rate

    @property
    def eps_contributors_count(self):
        """Gets the eps_contributors_count of this StockEarningDto.  # noqa: E501


        :return: The eps_contributors_count of this StockEarningDto.  # noqa: E501
        :rtype: int
        """
        return self._eps_contributors_count

    @eps_contributors_count.setter
    def eps_contributors_count(self, eps_contributors_count):
        """Sets the eps_contributors_count of this StockEarningDto.


        :param eps_contributors_count: The eps_contributors_count of this StockEarningDto.  # noqa: E501
        :type: int
        """

        self._eps_contributors_count = eps_contributors_count

    @property
    def revenue_contributors_count(self):
        """Gets the revenue_contributors_count of this StockEarningDto.  # noqa: E501


        :return: The revenue_contributors_count of this StockEarningDto.  # noqa: E501
        :rtype: int
        """
        return self._revenue_contributors_count

    @revenue_contributors_count.setter
    def revenue_contributors_count(self, revenue_contributors_count):
        """Sets the revenue_contributors_count of this StockEarningDto.


        :param revenue_contributors_count: The revenue_contributors_count of this StockEarningDto.  # noqa: E501
        :type: int
        """

        self._revenue_contributors_count = revenue_contributors_count

    @property
    def pos_return_prob(self):
        """Gets the pos_return_prob of this StockEarningDto.  # noqa: E501


        :return: The pos_return_prob of this StockEarningDto.  # noqa: E501
        :rtype: float
        """
        return self._pos_return_prob

    @pos_return_prob.setter
    def pos_return_prob(self, pos_return_prob):
        """Sets the pos_return_prob of this StockEarningDto.


        :param pos_return_prob: The pos_return_prob of this StockEarningDto.  # noqa: E501
        :type: float
        """

        self._pos_return_prob = pos_return_prob

    @property
    def expected_return(self):
        """Gets the expected_return of this StockEarningDto.  # noqa: E501


        :return: The expected_return of this StockEarningDto.  # noqa: E501
        :rtype: float
        """
        return self._expected_return

    @expected_return.setter
    def expected_return(self, expected_return):
        """Sets the expected_return of this StockEarningDto.


        :param expected_return: The expected_return of this StockEarningDto.  # noqa: E501
        :type: float
        """

        self._expected_return = expected_return

    @property
    def fiscal_quarter(self):
        """Gets the fiscal_quarter of this StockEarningDto.  # noqa: E501


        :return: The fiscal_quarter of this StockEarningDto.  # noqa: E501
        :rtype: int
        """
        return self._fiscal_quarter

    @fiscal_quarter.setter
    def fiscal_quarter(self, fiscal_quarter):
        """Sets the fiscal_quarter of this StockEarningDto.


        :param fiscal_quarter: The fiscal_quarter of this StockEarningDto.  # noqa: E501
        :type: int
        """

        self._fiscal_quarter = fiscal_quarter

    @property
    def eps_surprise(self):
        """Gets the eps_surprise of this StockEarningDto.  # noqa: E501


        :return: The eps_surprise of this StockEarningDto.  # noqa: E501
        :rtype: float
        """
        return self._eps_surprise

    @eps_surprise.setter
    def eps_surprise(self, eps_surprise):
        """Sets the eps_surprise of this StockEarningDto.


        :param eps_surprise: The eps_surprise of this StockEarningDto.  # noqa: E501
        :type: float
        """

        self._eps_surprise = eps_surprise

    @property
    def revenue_surprise(self):
        """Gets the revenue_surprise of this StockEarningDto.  # noqa: E501


        :return: The revenue_surprise of this StockEarningDto.  # noqa: E501
        :rtype: float
        """
        return self._revenue_surprise

    @revenue_surprise.setter
    def revenue_surprise(self, revenue_surprise):
        """Sets the revenue_surprise of this StockEarningDto.


        :param revenue_surprise: The revenue_surprise of this StockEarningDto.  # noqa: E501
        :type: float
        """

        self._revenue_surprise = revenue_surprise

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
        if issubclass(StockEarningDto, dict):
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
        if not isinstance(other, StockEarningDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
