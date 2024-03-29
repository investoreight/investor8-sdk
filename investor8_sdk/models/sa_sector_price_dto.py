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

class SASectorPriceDto(object):
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
        'name': 'str',
        'company': 'str',
        'alias_name': 'str',
        'real_time_price': 'SAAttributesPrices'
    }

    attribute_map = {
        'name': 'Name',
        'company': 'Company',
        'alias_name': 'AliasName',
        'real_time_price': 'RealTimePrice'
    }

    def __init__(self, name=None, company=None, alias_name=None, real_time_price=None):  # noqa: E501
        """SASectorPriceDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._company = None
        self._alias_name = None
        self._real_time_price = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if company is not None:
            self.company = company
        if alias_name is not None:
            self.alias_name = alias_name
        if real_time_price is not None:
            self.real_time_price = real_time_price

    @property
    def name(self):
        """Gets the name of this SASectorPriceDto.  # noqa: E501


        :return: The name of this SASectorPriceDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SASectorPriceDto.


        :param name: The name of this SASectorPriceDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def company(self):
        """Gets the company of this SASectorPriceDto.  # noqa: E501


        :return: The company of this SASectorPriceDto.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this SASectorPriceDto.


        :param company: The company of this SASectorPriceDto.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def alias_name(self):
        """Gets the alias_name of this SASectorPriceDto.  # noqa: E501


        :return: The alias_name of this SASectorPriceDto.  # noqa: E501
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        """Sets the alias_name of this SASectorPriceDto.


        :param alias_name: The alias_name of this SASectorPriceDto.  # noqa: E501
        :type: str
        """

        self._alias_name = alias_name

    @property
    def real_time_price(self):
        """Gets the real_time_price of this SASectorPriceDto.  # noqa: E501


        :return: The real_time_price of this SASectorPriceDto.  # noqa: E501
        :rtype: SAAttributesPrices
        """
        return self._real_time_price

    @real_time_price.setter
    def real_time_price(self, real_time_price):
        """Sets the real_time_price of this SASectorPriceDto.


        :param real_time_price: The real_time_price of this SASectorPriceDto.  # noqa: E501
        :type: SAAttributesPrices
        """

        self._real_time_price = real_time_price

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
        if issubclass(SASectorPriceDto, dict):
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
        if not isinstance(other, SASectorPriceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
