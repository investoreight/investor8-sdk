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

class FinancialTag(object):
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
        'tag_name': 'str',
        'display_name': 'str',
        'unit': 'str',
        'value': 'float',
        'parent': 'str',
        'balance': 'str',
        'factor': 'str',
        'order': 'int',
        'is_significant': 'bool',
        'section_name': 'str',
        'sub_section_name': 'str',
        'tag_order': 'int',
        'section_order': 'int',
        'sub_section_order': 'int'
    }

    attribute_map = {
        'tag_name': 'TagName',
        'display_name': 'DisplayName',
        'unit': 'Unit',
        'value': 'Value',
        'parent': 'Parent',
        'balance': 'Balance',
        'factor': 'Factor',
        'order': 'Order',
        'is_significant': 'IsSignificant',
        'section_name': 'SectionName',
        'sub_section_name': 'SubSectionName',
        'tag_order': 'TagOrder',
        'section_order': 'SectionOrder',
        'sub_section_order': 'SubSectionOrder'
    }

    def __init__(self, tag_name=None, display_name=None, unit=None, value=None, parent=None, balance=None, factor=None, order=None, is_significant=None, section_name=None, sub_section_name=None, tag_order=None, section_order=None, sub_section_order=None):  # noqa: E501
        """FinancialTag - a model defined in Swagger"""  # noqa: E501
        self._tag_name = None
        self._display_name = None
        self._unit = None
        self._value = None
        self._parent = None
        self._balance = None
        self._factor = None
        self._order = None
        self._is_significant = None
        self._section_name = None
        self._sub_section_name = None
        self._tag_order = None
        self._section_order = None
        self._sub_section_order = None
        self.discriminator = None
        if tag_name is not None:
            self.tag_name = tag_name
        if display_name is not None:
            self.display_name = display_name
        if unit is not None:
            self.unit = unit
        if value is not None:
            self.value = value
        if parent is not None:
            self.parent = parent
        if balance is not None:
            self.balance = balance
        if factor is not None:
            self.factor = factor
        if order is not None:
            self.order = order
        if is_significant is not None:
            self.is_significant = is_significant
        if section_name is not None:
            self.section_name = section_name
        if sub_section_name is not None:
            self.sub_section_name = sub_section_name
        if tag_order is not None:
            self.tag_order = tag_order
        if section_order is not None:
            self.section_order = section_order
        if sub_section_order is not None:
            self.sub_section_order = sub_section_order

    @property
    def tag_name(self):
        """Gets the tag_name of this FinancialTag.  # noqa: E501


        :return: The tag_name of this FinancialTag.  # noqa: E501
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this FinancialTag.


        :param tag_name: The tag_name of this FinancialTag.  # noqa: E501
        :type: str
        """

        self._tag_name = tag_name

    @property
    def display_name(self):
        """Gets the display_name of this FinancialTag.  # noqa: E501


        :return: The display_name of this FinancialTag.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FinancialTag.


        :param display_name: The display_name of this FinancialTag.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def unit(self):
        """Gets the unit of this FinancialTag.  # noqa: E501


        :return: The unit of this FinancialTag.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this FinancialTag.


        :param unit: The unit of this FinancialTag.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def value(self):
        """Gets the value of this FinancialTag.  # noqa: E501


        :return: The value of this FinancialTag.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FinancialTag.


        :param value: The value of this FinancialTag.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def parent(self):
        """Gets the parent of this FinancialTag.  # noqa: E501


        :return: The parent of this FinancialTag.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this FinancialTag.


        :param parent: The parent of this FinancialTag.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def balance(self):
        """Gets the balance of this FinancialTag.  # noqa: E501


        :return: The balance of this FinancialTag.  # noqa: E501
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this FinancialTag.


        :param balance: The balance of this FinancialTag.  # noqa: E501
        :type: str
        """

        self._balance = balance

    @property
    def factor(self):
        """Gets the factor of this FinancialTag.  # noqa: E501


        :return: The factor of this FinancialTag.  # noqa: E501
        :rtype: str
        """
        return self._factor

    @factor.setter
    def factor(self, factor):
        """Sets the factor of this FinancialTag.


        :param factor: The factor of this FinancialTag.  # noqa: E501
        :type: str
        """

        self._factor = factor

    @property
    def order(self):
        """Gets the order of this FinancialTag.  # noqa: E501


        :return: The order of this FinancialTag.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this FinancialTag.


        :param order: The order of this FinancialTag.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def is_significant(self):
        """Gets the is_significant of this FinancialTag.  # noqa: E501


        :return: The is_significant of this FinancialTag.  # noqa: E501
        :rtype: bool
        """
        return self._is_significant

    @is_significant.setter
    def is_significant(self, is_significant):
        """Sets the is_significant of this FinancialTag.


        :param is_significant: The is_significant of this FinancialTag.  # noqa: E501
        :type: bool
        """

        self._is_significant = is_significant

    @property
    def section_name(self):
        """Gets the section_name of this FinancialTag.  # noqa: E501


        :return: The section_name of this FinancialTag.  # noqa: E501
        :rtype: str
        """
        return self._section_name

    @section_name.setter
    def section_name(self, section_name):
        """Sets the section_name of this FinancialTag.


        :param section_name: The section_name of this FinancialTag.  # noqa: E501
        :type: str
        """

        self._section_name = section_name

    @property
    def sub_section_name(self):
        """Gets the sub_section_name of this FinancialTag.  # noqa: E501


        :return: The sub_section_name of this FinancialTag.  # noqa: E501
        :rtype: str
        """
        return self._sub_section_name

    @sub_section_name.setter
    def sub_section_name(self, sub_section_name):
        """Sets the sub_section_name of this FinancialTag.


        :param sub_section_name: The sub_section_name of this FinancialTag.  # noqa: E501
        :type: str
        """

        self._sub_section_name = sub_section_name

    @property
    def tag_order(self):
        """Gets the tag_order of this FinancialTag.  # noqa: E501


        :return: The tag_order of this FinancialTag.  # noqa: E501
        :rtype: int
        """
        return self._tag_order

    @tag_order.setter
    def tag_order(self, tag_order):
        """Sets the tag_order of this FinancialTag.


        :param tag_order: The tag_order of this FinancialTag.  # noqa: E501
        :type: int
        """

        self._tag_order = tag_order

    @property
    def section_order(self):
        """Gets the section_order of this FinancialTag.  # noqa: E501


        :return: The section_order of this FinancialTag.  # noqa: E501
        :rtype: int
        """
        return self._section_order

    @section_order.setter
    def section_order(self, section_order):
        """Sets the section_order of this FinancialTag.


        :param section_order: The section_order of this FinancialTag.  # noqa: E501
        :type: int
        """

        self._section_order = section_order

    @property
    def sub_section_order(self):
        """Gets the sub_section_order of this FinancialTag.  # noqa: E501


        :return: The sub_section_order of this FinancialTag.  # noqa: E501
        :rtype: int
        """
        return self._sub_section_order

    @sub_section_order.setter
    def sub_section_order(self, sub_section_order):
        """Sets the sub_section_order of this FinancialTag.


        :param sub_section_order: The sub_section_order of this FinancialTag.  # noqa: E501
        :type: int
        """

        self._sub_section_order = sub_section_order

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
        if issubclass(FinancialTag, dict):
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
        if not isinstance(other, FinancialTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
