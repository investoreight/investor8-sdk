# coding: utf-8

"""
    Investoreight Core API

    Investoreight API Documentation:  https://api.investoreight.com/api-docs/index.html  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: info@investoreight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StandardizedFinancial(object):
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
        'fiscal_year': 'int',
        'ticker': 'str',
        'statement_code': 'str',
        'fiscal_period': 'str',
        'type': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'filing_date': 'datetime',
        'is_latest': 'bool',
        'period_type': 'str',
        'financial_tags': 'list[FinancialTag]'
    }

    attribute_map = {
        'id': 'Id',
        'fiscal_year': 'FiscalYear',
        'ticker': 'Ticker',
        'statement_code': 'StatementCode',
        'fiscal_period': 'FiscalPeriod',
        'type': 'Type',
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'filing_date': 'FilingDate',
        'is_latest': 'IsLatest',
        'period_type': 'PeriodType',
        'financial_tags': 'FinancialTags'
    }

    def __init__(self, id=None, fiscal_year=None, ticker=None, statement_code=None, fiscal_period=None, type=None, start_date=None, end_date=None, filing_date=None, is_latest=None, period_type=None, financial_tags=None):  # noqa: E501
        """StandardizedFinancial - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._fiscal_year = None
        self._ticker = None
        self._statement_code = None
        self._fiscal_period = None
        self._type = None
        self._start_date = None
        self._end_date = None
        self._filing_date = None
        self._is_latest = None
        self._period_type = None
        self._financial_tags = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if fiscal_year is not None:
            self.fiscal_year = fiscal_year
        if ticker is not None:
            self.ticker = ticker
        if statement_code is not None:
            self.statement_code = statement_code
        if fiscal_period is not None:
            self.fiscal_period = fiscal_period
        if type is not None:
            self.type = type
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if filing_date is not None:
            self.filing_date = filing_date
        if is_latest is not None:
            self.is_latest = is_latest
        if period_type is not None:
            self.period_type = period_type
        if financial_tags is not None:
            self.financial_tags = financial_tags

    @property
    def id(self):
        """Gets the id of this StandardizedFinancial.  # noqa: E501


        :return: The id of this StandardizedFinancial.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StandardizedFinancial.


        :param id: The id of this StandardizedFinancial.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def fiscal_year(self):
        """Gets the fiscal_year of this StandardizedFinancial.  # noqa: E501


        :return: The fiscal_year of this StandardizedFinancial.  # noqa: E501
        :rtype: int
        """
        return self._fiscal_year

    @fiscal_year.setter
    def fiscal_year(self, fiscal_year):
        """Sets the fiscal_year of this StandardizedFinancial.


        :param fiscal_year: The fiscal_year of this StandardizedFinancial.  # noqa: E501
        :type: int
        """

        self._fiscal_year = fiscal_year

    @property
    def ticker(self):
        """Gets the ticker of this StandardizedFinancial.  # noqa: E501


        :return: The ticker of this StandardizedFinancial.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this StandardizedFinancial.


        :param ticker: The ticker of this StandardizedFinancial.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def statement_code(self):
        """Gets the statement_code of this StandardizedFinancial.  # noqa: E501


        :return: The statement_code of this StandardizedFinancial.  # noqa: E501
        :rtype: str
        """
        return self._statement_code

    @statement_code.setter
    def statement_code(self, statement_code):
        """Sets the statement_code of this StandardizedFinancial.


        :param statement_code: The statement_code of this StandardizedFinancial.  # noqa: E501
        :type: str
        """

        self._statement_code = statement_code

    @property
    def fiscal_period(self):
        """Gets the fiscal_period of this StandardizedFinancial.  # noqa: E501


        :return: The fiscal_period of this StandardizedFinancial.  # noqa: E501
        :rtype: str
        """
        return self._fiscal_period

    @fiscal_period.setter
    def fiscal_period(self, fiscal_period):
        """Sets the fiscal_period of this StandardizedFinancial.


        :param fiscal_period: The fiscal_period of this StandardizedFinancial.  # noqa: E501
        :type: str
        """

        self._fiscal_period = fiscal_period

    @property
    def type(self):
        """Gets the type of this StandardizedFinancial.  # noqa: E501


        :return: The type of this StandardizedFinancial.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StandardizedFinancial.


        :param type: The type of this StandardizedFinancial.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def start_date(self):
        """Gets the start_date of this StandardizedFinancial.  # noqa: E501


        :return: The start_date of this StandardizedFinancial.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this StandardizedFinancial.


        :param start_date: The start_date of this StandardizedFinancial.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this StandardizedFinancial.  # noqa: E501


        :return: The end_date of this StandardizedFinancial.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this StandardizedFinancial.


        :param end_date: The end_date of this StandardizedFinancial.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def filing_date(self):
        """Gets the filing_date of this StandardizedFinancial.  # noqa: E501


        :return: The filing_date of this StandardizedFinancial.  # noqa: E501
        :rtype: datetime
        """
        return self._filing_date

    @filing_date.setter
    def filing_date(self, filing_date):
        """Sets the filing_date of this StandardizedFinancial.


        :param filing_date: The filing_date of this StandardizedFinancial.  # noqa: E501
        :type: datetime
        """

        self._filing_date = filing_date

    @property
    def is_latest(self):
        """Gets the is_latest of this StandardizedFinancial.  # noqa: E501


        :return: The is_latest of this StandardizedFinancial.  # noqa: E501
        :rtype: bool
        """
        return self._is_latest

    @is_latest.setter
    def is_latest(self, is_latest):
        """Sets the is_latest of this StandardizedFinancial.


        :param is_latest: The is_latest of this StandardizedFinancial.  # noqa: E501
        :type: bool
        """

        self._is_latest = is_latest

    @property
    def period_type(self):
        """Gets the period_type of this StandardizedFinancial.  # noqa: E501


        :return: The period_type of this StandardizedFinancial.  # noqa: E501
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this StandardizedFinancial.


        :param period_type: The period_type of this StandardizedFinancial.  # noqa: E501
        :type: str
        """

        self._period_type = period_type

    @property
    def financial_tags(self):
        """Gets the financial_tags of this StandardizedFinancial.  # noqa: E501


        :return: The financial_tags of this StandardizedFinancial.  # noqa: E501
        :rtype: list[FinancialTag]
        """
        return self._financial_tags

    @financial_tags.setter
    def financial_tags(self, financial_tags):
        """Sets the financial_tags of this StandardizedFinancial.


        :param financial_tags: The financial_tags of this StandardizedFinancial.  # noqa: E501
        :type: list[FinancialTag]
        """

        self._financial_tags = financial_tags

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
        if issubclass(StandardizedFinancial, dict):
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
        if not isinstance(other, StandardizedFinancial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
