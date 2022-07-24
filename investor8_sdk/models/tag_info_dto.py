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

class TagInfoDto(object):
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
        'tag_description': 'str',
        'color_code': 'str',
        'category': 'str',
        'last_run': 'int'
    }

    attribute_map = {
        'tag_name': 'TagName',
        'tag_description': 'TagDescription',
        'color_code': 'ColorCode',
        'category': 'Category',
        'last_run': 'LastRun'
    }

    def __init__(self, tag_name=None, tag_description=None, color_code=None, category=None, last_run=None):  # noqa: E501
        """TagInfoDto - a model defined in Swagger"""  # noqa: E501
        self._tag_name = None
        self._tag_description = None
        self._color_code = None
        self._category = None
        self._last_run = None
        self.discriminator = None
        if tag_name is not None:
            self.tag_name = tag_name
        if tag_description is not None:
            self.tag_description = tag_description
        if color_code is not None:
            self.color_code = color_code
        if category is not None:
            self.category = category
        if last_run is not None:
            self.last_run = last_run

    @property
    def tag_name(self):
        """Gets the tag_name of this TagInfoDto.  # noqa: E501


        :return: The tag_name of this TagInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this TagInfoDto.


        :param tag_name: The tag_name of this TagInfoDto.  # noqa: E501
        :type: str
        """

        self._tag_name = tag_name

    @property
    def tag_description(self):
        """Gets the tag_description of this TagInfoDto.  # noqa: E501


        :return: The tag_description of this TagInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._tag_description

    @tag_description.setter
    def tag_description(self, tag_description):
        """Sets the tag_description of this TagInfoDto.


        :param tag_description: The tag_description of this TagInfoDto.  # noqa: E501
        :type: str
        """

        self._tag_description = tag_description

    @property
    def color_code(self):
        """Gets the color_code of this TagInfoDto.  # noqa: E501


        :return: The color_code of this TagInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._color_code

    @color_code.setter
    def color_code(self, color_code):
        """Sets the color_code of this TagInfoDto.


        :param color_code: The color_code of this TagInfoDto.  # noqa: E501
        :type: str
        """

        self._color_code = color_code

    @property
    def category(self):
        """Gets the category of this TagInfoDto.  # noqa: E501


        :return: The category of this TagInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this TagInfoDto.


        :param category: The category of this TagInfoDto.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def last_run(self):
        """Gets the last_run of this TagInfoDto.  # noqa: E501


        :return: The last_run of this TagInfoDto.  # noqa: E501
        :rtype: int
        """
        return self._last_run

    @last_run.setter
    def last_run(self, last_run):
        """Sets the last_run of this TagInfoDto.


        :param last_run: The last_run of this TagInfoDto.  # noqa: E501
        :type: int
        """

        self._last_run = last_run

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
        if issubclass(TagInfoDto, dict):
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
        if not isinstance(other, TagInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
