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

class CompanyInfoDto(object):
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
        'sector': 'str',
        'industry_category': 'str',
        'industry_group': 'str',
        'employees': 'int',
        'business_address': 'str',
        'company_url': 'str',
        'description': 'str'
    }

    attribute_map = {
        'ticker': 'Ticker',
        'sector': 'Sector',
        'industry_category': 'IndustryCategory',
        'industry_group': 'IndustryGroup',
        'employees': 'Employees',
        'business_address': 'BusinessAddress',
        'company_url': 'CompanyUrl',
        'description': 'Description'
    }

    def __init__(self, ticker=None, sector=None, industry_category=None, industry_group=None, employees=None, business_address=None, company_url=None, description=None):  # noqa: E501
        """CompanyInfoDto - a model defined in Swagger"""  # noqa: E501
        self._ticker = None
        self._sector = None
        self._industry_category = None
        self._industry_group = None
        self._employees = None
        self._business_address = None
        self._company_url = None
        self._description = None
        self.discriminator = None
        if ticker is not None:
            self.ticker = ticker
        if sector is not None:
            self.sector = sector
        if industry_category is not None:
            self.industry_category = industry_category
        if industry_group is not None:
            self.industry_group = industry_group
        if employees is not None:
            self.employees = employees
        if business_address is not None:
            self.business_address = business_address
        if company_url is not None:
            self.company_url = company_url
        if description is not None:
            self.description = description

    @property
    def ticker(self):
        """Gets the ticker of this CompanyInfoDto.  # noqa: E501


        :return: The ticker of this CompanyInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this CompanyInfoDto.


        :param ticker: The ticker of this CompanyInfoDto.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def sector(self):
        """Gets the sector of this CompanyInfoDto.  # noqa: E501


        :return: The sector of this CompanyInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this CompanyInfoDto.


        :param sector: The sector of this CompanyInfoDto.  # noqa: E501
        :type: str
        """

        self._sector = sector

    @property
    def industry_category(self):
        """Gets the industry_category of this CompanyInfoDto.  # noqa: E501


        :return: The industry_category of this CompanyInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._industry_category

    @industry_category.setter
    def industry_category(self, industry_category):
        """Sets the industry_category of this CompanyInfoDto.


        :param industry_category: The industry_category of this CompanyInfoDto.  # noqa: E501
        :type: str
        """

        self._industry_category = industry_category

    @property
    def industry_group(self):
        """Gets the industry_group of this CompanyInfoDto.  # noqa: E501


        :return: The industry_group of this CompanyInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._industry_group

    @industry_group.setter
    def industry_group(self, industry_group):
        """Sets the industry_group of this CompanyInfoDto.


        :param industry_group: The industry_group of this CompanyInfoDto.  # noqa: E501
        :type: str
        """

        self._industry_group = industry_group

    @property
    def employees(self):
        """Gets the employees of this CompanyInfoDto.  # noqa: E501


        :return: The employees of this CompanyInfoDto.  # noqa: E501
        :rtype: int
        """
        return self._employees

    @employees.setter
    def employees(self, employees):
        """Sets the employees of this CompanyInfoDto.


        :param employees: The employees of this CompanyInfoDto.  # noqa: E501
        :type: int
        """

        self._employees = employees

    @property
    def business_address(self):
        """Gets the business_address of this CompanyInfoDto.  # noqa: E501


        :return: The business_address of this CompanyInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._business_address

    @business_address.setter
    def business_address(self, business_address):
        """Sets the business_address of this CompanyInfoDto.


        :param business_address: The business_address of this CompanyInfoDto.  # noqa: E501
        :type: str
        """

        self._business_address = business_address

    @property
    def company_url(self):
        """Gets the company_url of this CompanyInfoDto.  # noqa: E501


        :return: The company_url of this CompanyInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._company_url

    @company_url.setter
    def company_url(self, company_url):
        """Sets the company_url of this CompanyInfoDto.


        :param company_url: The company_url of this CompanyInfoDto.  # noqa: E501
        :type: str
        """

        self._company_url = company_url

    @property
    def description(self):
        """Gets the description of this CompanyInfoDto.  # noqa: E501


        :return: The description of this CompanyInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CompanyInfoDto.


        :param description: The description of this CompanyInfoDto.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(CompanyInfoDto, dict):
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
        if not isinstance(other, CompanyInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
