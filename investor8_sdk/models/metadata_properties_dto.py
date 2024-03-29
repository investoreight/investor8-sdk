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

class MetadataPropertiesDto(object):
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
        'categories': 'list[str]',
        'units': 'list[str]',
        'types': 'list[str]',
        'display_formats': 'list[str]',
        'data_formats': 'list[str]'
    }

    attribute_map = {
        'categories': 'Categories',
        'units': 'Units',
        'types': 'Types',
        'display_formats': 'DisplayFormats',
        'data_formats': 'DataFormats'
    }

    def __init__(self, categories=None, units=None, types=None, display_formats=None, data_formats=None):  # noqa: E501
        """MetadataPropertiesDto - a model defined in Swagger"""  # noqa: E501
        self._categories = None
        self._units = None
        self._types = None
        self._display_formats = None
        self._data_formats = None
        self.discriminator = None
        if categories is not None:
            self.categories = categories
        if units is not None:
            self.units = units
        if types is not None:
            self.types = types
        if display_formats is not None:
            self.display_formats = display_formats
        if data_formats is not None:
            self.data_formats = data_formats

    @property
    def categories(self):
        """Gets the categories of this MetadataPropertiesDto.  # noqa: E501


        :return: The categories of this MetadataPropertiesDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this MetadataPropertiesDto.


        :param categories: The categories of this MetadataPropertiesDto.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def units(self):
        """Gets the units of this MetadataPropertiesDto.  # noqa: E501


        :return: The units of this MetadataPropertiesDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this MetadataPropertiesDto.


        :param units: The units of this MetadataPropertiesDto.  # noqa: E501
        :type: list[str]
        """

        self._units = units

    @property
    def types(self):
        """Gets the types of this MetadataPropertiesDto.  # noqa: E501


        :return: The types of this MetadataPropertiesDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this MetadataPropertiesDto.


        :param types: The types of this MetadataPropertiesDto.  # noqa: E501
        :type: list[str]
        """

        self._types = types

    @property
    def display_formats(self):
        """Gets the display_formats of this MetadataPropertiesDto.  # noqa: E501


        :return: The display_formats of this MetadataPropertiesDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._display_formats

    @display_formats.setter
    def display_formats(self, display_formats):
        """Sets the display_formats of this MetadataPropertiesDto.


        :param display_formats: The display_formats of this MetadataPropertiesDto.  # noqa: E501
        :type: list[str]
        """

        self._display_formats = display_formats

    @property
    def data_formats(self):
        """Gets the data_formats of this MetadataPropertiesDto.  # noqa: E501


        :return: The data_formats of this MetadataPropertiesDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_formats

    @data_formats.setter
    def data_formats(self, data_formats):
        """Sets the data_formats of this MetadataPropertiesDto.


        :param data_formats: The data_formats of this MetadataPropertiesDto.  # noqa: E501
        :type: list[str]
        """

        self._data_formats = data_formats

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
        if issubclass(MetadataPropertiesDto, dict):
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
        if not isinstance(other, MetadataPropertiesDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
