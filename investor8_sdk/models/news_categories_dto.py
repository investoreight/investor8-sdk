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

class NewsCategoriesDto(object):
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
        'categories_coarse': 'list[str]',
        'categories_fine': 'list[str]'
    }

    attribute_map = {
        'categories_coarse': 'CategoriesCoarse',
        'categories_fine': 'CategoriesFine'
    }

    def __init__(self, categories_coarse=None, categories_fine=None):  # noqa: E501
        """NewsCategoriesDto - a model defined in Swagger"""  # noqa: E501
        self._categories_coarse = None
        self._categories_fine = None
        self.discriminator = None
        if categories_coarse is not None:
            self.categories_coarse = categories_coarse
        if categories_fine is not None:
            self.categories_fine = categories_fine

    @property
    def categories_coarse(self):
        """Gets the categories_coarse of this NewsCategoriesDto.  # noqa: E501


        :return: The categories_coarse of this NewsCategoriesDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories_coarse

    @categories_coarse.setter
    def categories_coarse(self, categories_coarse):
        """Sets the categories_coarse of this NewsCategoriesDto.


        :param categories_coarse: The categories_coarse of this NewsCategoriesDto.  # noqa: E501
        :type: list[str]
        """

        self._categories_coarse = categories_coarse

    @property
    def categories_fine(self):
        """Gets the categories_fine of this NewsCategoriesDto.  # noqa: E501


        :return: The categories_fine of this NewsCategoriesDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories_fine

    @categories_fine.setter
    def categories_fine(self, categories_fine):
        """Sets the categories_fine of this NewsCategoriesDto.


        :param categories_fine: The categories_fine of this NewsCategoriesDto.  # noqa: E501
        :type: list[str]
        """

        self._categories_fine = categories_fine

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
        if issubclass(NewsCategoriesDto, dict):
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
        if not isinstance(other, NewsCategoriesDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
