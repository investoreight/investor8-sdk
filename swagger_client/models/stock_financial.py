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

class StockFinancial(object):
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
        'fyq': 'str',
        'operating_revenue': 'float',
        'total_revenue': 'float',
        'total_grossprofit': 'float',
        'other_income': 'float',
        'net_income': 'float',
        'basic_eps': 'float',
        'diluted_eps': 'float',
        'dividend_per_share': 'float',
        'filing_date': 'int',
        'adjusted_basic_eps': 'float',
        'year': 'int',
        'fiscal_quarter': 'int'
    }

    attribute_map = {
        'id': 'Id',
        'fyq': 'FYQ',
        'operating_revenue': 'OperatingRevenue',
        'total_revenue': 'TotalRevenue',
        'total_grossprofit': 'TotalGrossprofit',
        'other_income': 'OtherIncome',
        'net_income': 'NetIncome',
        'basic_eps': 'BasicEps',
        'diluted_eps': 'DilutedEps',
        'dividend_per_share': 'DividendPerShare',
        'filing_date': 'Filing_Date',
        'adjusted_basic_eps': 'AdjustedBasicEps',
        'year': 'Year',
        'fiscal_quarter': 'FiscalQuarter'
    }

    def __init__(self, id=None, fyq=None, operating_revenue=None, total_revenue=None, total_grossprofit=None, other_income=None, net_income=None, basic_eps=None, diluted_eps=None, dividend_per_share=None, filing_date=None, adjusted_basic_eps=None, year=None, fiscal_quarter=None):  # noqa: E501
        """StockFinancial - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._fyq = None
        self._operating_revenue = None
        self._total_revenue = None
        self._total_grossprofit = None
        self._other_income = None
        self._net_income = None
        self._basic_eps = None
        self._diluted_eps = None
        self._dividend_per_share = None
        self._filing_date = None
        self._adjusted_basic_eps = None
        self._year = None
        self._fiscal_quarter = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if fyq is not None:
            self.fyq = fyq
        if operating_revenue is not None:
            self.operating_revenue = operating_revenue
        if total_revenue is not None:
            self.total_revenue = total_revenue
        if total_grossprofit is not None:
            self.total_grossprofit = total_grossprofit
        if other_income is not None:
            self.other_income = other_income
        if net_income is not None:
            self.net_income = net_income
        if basic_eps is not None:
            self.basic_eps = basic_eps
        if diluted_eps is not None:
            self.diluted_eps = diluted_eps
        if dividend_per_share is not None:
            self.dividend_per_share = dividend_per_share
        if filing_date is not None:
            self.filing_date = filing_date
        if adjusted_basic_eps is not None:
            self.adjusted_basic_eps = adjusted_basic_eps
        if year is not None:
            self.year = year
        if fiscal_quarter is not None:
            self.fiscal_quarter = fiscal_quarter

    @property
    def id(self):
        """Gets the id of this StockFinancial.  # noqa: E501


        :return: The id of this StockFinancial.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StockFinancial.


        :param id: The id of this StockFinancial.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def fyq(self):
        """Gets the fyq of this StockFinancial.  # noqa: E501


        :return: The fyq of this StockFinancial.  # noqa: E501
        :rtype: str
        """
        return self._fyq

    @fyq.setter
    def fyq(self, fyq):
        """Sets the fyq of this StockFinancial.


        :param fyq: The fyq of this StockFinancial.  # noqa: E501
        :type: str
        """

        self._fyq = fyq

    @property
    def operating_revenue(self):
        """Gets the operating_revenue of this StockFinancial.  # noqa: E501


        :return: The operating_revenue of this StockFinancial.  # noqa: E501
        :rtype: float
        """
        return self._operating_revenue

    @operating_revenue.setter
    def operating_revenue(self, operating_revenue):
        """Sets the operating_revenue of this StockFinancial.


        :param operating_revenue: The operating_revenue of this StockFinancial.  # noqa: E501
        :type: float
        """

        self._operating_revenue = operating_revenue

    @property
    def total_revenue(self):
        """Gets the total_revenue of this StockFinancial.  # noqa: E501


        :return: The total_revenue of this StockFinancial.  # noqa: E501
        :rtype: float
        """
        return self._total_revenue

    @total_revenue.setter
    def total_revenue(self, total_revenue):
        """Sets the total_revenue of this StockFinancial.


        :param total_revenue: The total_revenue of this StockFinancial.  # noqa: E501
        :type: float
        """

        self._total_revenue = total_revenue

    @property
    def total_grossprofit(self):
        """Gets the total_grossprofit of this StockFinancial.  # noqa: E501


        :return: The total_grossprofit of this StockFinancial.  # noqa: E501
        :rtype: float
        """
        return self._total_grossprofit

    @total_grossprofit.setter
    def total_grossprofit(self, total_grossprofit):
        """Sets the total_grossprofit of this StockFinancial.


        :param total_grossprofit: The total_grossprofit of this StockFinancial.  # noqa: E501
        :type: float
        """

        self._total_grossprofit = total_grossprofit

    @property
    def other_income(self):
        """Gets the other_income of this StockFinancial.  # noqa: E501


        :return: The other_income of this StockFinancial.  # noqa: E501
        :rtype: float
        """
        return self._other_income

    @other_income.setter
    def other_income(self, other_income):
        """Sets the other_income of this StockFinancial.


        :param other_income: The other_income of this StockFinancial.  # noqa: E501
        :type: float
        """

        self._other_income = other_income

    @property
    def net_income(self):
        """Gets the net_income of this StockFinancial.  # noqa: E501


        :return: The net_income of this StockFinancial.  # noqa: E501
        :rtype: float
        """
        return self._net_income

    @net_income.setter
    def net_income(self, net_income):
        """Sets the net_income of this StockFinancial.


        :param net_income: The net_income of this StockFinancial.  # noqa: E501
        :type: float
        """

        self._net_income = net_income

    @property
    def basic_eps(self):
        """Gets the basic_eps of this StockFinancial.  # noqa: E501


        :return: The basic_eps of this StockFinancial.  # noqa: E501
        :rtype: float
        """
        return self._basic_eps

    @basic_eps.setter
    def basic_eps(self, basic_eps):
        """Sets the basic_eps of this StockFinancial.


        :param basic_eps: The basic_eps of this StockFinancial.  # noqa: E501
        :type: float
        """

        self._basic_eps = basic_eps

    @property
    def diluted_eps(self):
        """Gets the diluted_eps of this StockFinancial.  # noqa: E501


        :return: The diluted_eps of this StockFinancial.  # noqa: E501
        :rtype: float
        """
        return self._diluted_eps

    @diluted_eps.setter
    def diluted_eps(self, diluted_eps):
        """Sets the diluted_eps of this StockFinancial.


        :param diluted_eps: The diluted_eps of this StockFinancial.  # noqa: E501
        :type: float
        """

        self._diluted_eps = diluted_eps

    @property
    def dividend_per_share(self):
        """Gets the dividend_per_share of this StockFinancial.  # noqa: E501


        :return: The dividend_per_share of this StockFinancial.  # noqa: E501
        :rtype: float
        """
        return self._dividend_per_share

    @dividend_per_share.setter
    def dividend_per_share(self, dividend_per_share):
        """Sets the dividend_per_share of this StockFinancial.


        :param dividend_per_share: The dividend_per_share of this StockFinancial.  # noqa: E501
        :type: float
        """

        self._dividend_per_share = dividend_per_share

    @property
    def filing_date(self):
        """Gets the filing_date of this StockFinancial.  # noqa: E501


        :return: The filing_date of this StockFinancial.  # noqa: E501
        :rtype: int
        """
        return self._filing_date

    @filing_date.setter
    def filing_date(self, filing_date):
        """Sets the filing_date of this StockFinancial.


        :param filing_date: The filing_date of this StockFinancial.  # noqa: E501
        :type: int
        """

        self._filing_date = filing_date

    @property
    def adjusted_basic_eps(self):
        """Gets the adjusted_basic_eps of this StockFinancial.  # noqa: E501


        :return: The adjusted_basic_eps of this StockFinancial.  # noqa: E501
        :rtype: float
        """
        return self._adjusted_basic_eps

    @adjusted_basic_eps.setter
    def adjusted_basic_eps(self, adjusted_basic_eps):
        """Sets the adjusted_basic_eps of this StockFinancial.


        :param adjusted_basic_eps: The adjusted_basic_eps of this StockFinancial.  # noqa: E501
        :type: float
        """

        self._adjusted_basic_eps = adjusted_basic_eps

    @property
    def year(self):
        """Gets the year of this StockFinancial.  # noqa: E501


        :return: The year of this StockFinancial.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this StockFinancial.


        :param year: The year of this StockFinancial.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def fiscal_quarter(self):
        """Gets the fiscal_quarter of this StockFinancial.  # noqa: E501


        :return: The fiscal_quarter of this StockFinancial.  # noqa: E501
        :rtype: int
        """
        return self._fiscal_quarter

    @fiscal_quarter.setter
    def fiscal_quarter(self, fiscal_quarter):
        """Sets the fiscal_quarter of this StockFinancial.


        :param fiscal_quarter: The fiscal_quarter of this StockFinancial.  # noqa: E501
        :type: int
        """

        self._fiscal_quarter = fiscal_quarter

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
        if issubclass(StockFinancial, dict):
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
        if not isinstance(other, StockFinancial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other