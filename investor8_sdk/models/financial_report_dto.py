# coding: utf-8

"""
    Investor8.Core

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: info@investoreight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FinancialReportDto(object):
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
        'statement_code': 'str',
        'fiscal_year': 'str',
        'fiscal_period': 'str',
        'report_type': 'str',
        'period_type': 'str'
    }

    attribute_map = {
        'statement_code': 'StatementCode',
        'fiscal_year': 'FiscalYear',
        'fiscal_period': 'FiscalPeriod',
        'report_type': 'ReportType',
        'period_type': 'PeriodType'
    }

    def __init__(self, statement_code=None, fiscal_year=None, fiscal_period=None, report_type=None, period_type=None):  # noqa: E501
        """FinancialReportDto - a model defined in Swagger"""  # noqa: E501
        self._statement_code = None
        self._fiscal_year = None
        self._fiscal_period = None
        self._report_type = None
        self._period_type = None
        self.discriminator = None
        if statement_code is not None:
            self.statement_code = statement_code
        if fiscal_year is not None:
            self.fiscal_year = fiscal_year
        if fiscal_period is not None:
            self.fiscal_period = fiscal_period
        if report_type is not None:
            self.report_type = report_type
        if period_type is not None:
            self.period_type = period_type

    @property
    def statement_code(self):
        """Gets the statement_code of this FinancialReportDto.  # noqa: E501


        :return: The statement_code of this FinancialReportDto.  # noqa: E501
        :rtype: str
        """
        return self._statement_code

    @statement_code.setter
    def statement_code(self, statement_code):
        """Sets the statement_code of this FinancialReportDto.


        :param statement_code: The statement_code of this FinancialReportDto.  # noqa: E501
        :type: str
        """

        self._statement_code = statement_code

    @property
    def fiscal_year(self):
        """Gets the fiscal_year of this FinancialReportDto.  # noqa: E501


        :return: The fiscal_year of this FinancialReportDto.  # noqa: E501
        :rtype: str
        """
        return self._fiscal_year

    @fiscal_year.setter
    def fiscal_year(self, fiscal_year):
        """Sets the fiscal_year of this FinancialReportDto.


        :param fiscal_year: The fiscal_year of this FinancialReportDto.  # noqa: E501
        :type: str
        """

        self._fiscal_year = fiscal_year

    @property
    def fiscal_period(self):
        """Gets the fiscal_period of this FinancialReportDto.  # noqa: E501


        :return: The fiscal_period of this FinancialReportDto.  # noqa: E501
        :rtype: str
        """
        return self._fiscal_period

    @fiscal_period.setter
    def fiscal_period(self, fiscal_period):
        """Sets the fiscal_period of this FinancialReportDto.


        :param fiscal_period: The fiscal_period of this FinancialReportDto.  # noqa: E501
        :type: str
        """

        self._fiscal_period = fiscal_period

    @property
    def report_type(self):
        """Gets the report_type of this FinancialReportDto.  # noqa: E501


        :return: The report_type of this FinancialReportDto.  # noqa: E501
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this FinancialReportDto.


        :param report_type: The report_type of this FinancialReportDto.  # noqa: E501
        :type: str
        """

        self._report_type = report_type

    @property
    def period_type(self):
        """Gets the period_type of this FinancialReportDto.  # noqa: E501


        :return: The period_type of this FinancialReportDto.  # noqa: E501
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this FinancialReportDto.


        :param period_type: The period_type of this FinancialReportDto.  # noqa: E501
        :type: str
        """

        self._period_type = period_type

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
        if issubclass(FinancialReportDto, dict):
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
        if not isinstance(other, FinancialReportDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
