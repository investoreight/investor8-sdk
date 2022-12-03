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

class I8TerminalVersion(object):
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
        'min_version_support': 'str',
        'latest_version': 'str'
    }

    attribute_map = {
        'min_version_support': 'MinVersionSupport',
        'latest_version': 'LatestVersion'
    }

    def __init__(self, min_version_support=None, latest_version=None):  # noqa: E501
        """I8TerminalVersion - a model defined in Swagger"""  # noqa: E501
        self._min_version_support = None
        self._latest_version = None
        self.discriminator = None
        if min_version_support is not None:
            self.min_version_support = min_version_support
        if latest_version is not None:
            self.latest_version = latest_version

    @property
    def min_version_support(self):
        """Gets the min_version_support of this I8TerminalVersion.  # noqa: E501


        :return: The min_version_support of this I8TerminalVersion.  # noqa: E501
        :rtype: str
        """
        return self._min_version_support

    @min_version_support.setter
    def min_version_support(self, min_version_support):
        """Sets the min_version_support of this I8TerminalVersion.


        :param min_version_support: The min_version_support of this I8TerminalVersion.  # noqa: E501
        :type: str
        """

        self._min_version_support = min_version_support

    @property
    def latest_version(self):
        """Gets the latest_version of this I8TerminalVersion.  # noqa: E501


        :return: The latest_version of this I8TerminalVersion.  # noqa: E501
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this I8TerminalVersion.


        :param latest_version: The latest_version of this I8TerminalVersion.  # noqa: E501
        :type: str
        """

        self._latest_version = latest_version

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
        if issubclass(I8TerminalVersion, dict):
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
        if not isinstance(other, I8TerminalVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
