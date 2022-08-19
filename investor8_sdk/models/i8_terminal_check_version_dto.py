# coding: utf-8

"""
    Investoreight Core API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: info@investoreight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class I8TerminalCheckVersionDto(object):
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
        'latest_version': 'str',
        'version_supported': 'bool'
    }

    attribute_map = {
        'min_version_support': 'MinVersionSupport',
        'latest_version': 'LatestVersion',
        'version_supported': 'VersionSupported'
    }

    def __init__(self, min_version_support=None, latest_version=None, version_supported=None):  # noqa: E501
        """I8TerminalCheckVersionDto - a model defined in Swagger"""  # noqa: E501
        self._min_version_support = None
        self._latest_version = None
        self._version_supported = None
        self.discriminator = None
        if min_version_support is not None:
            self.min_version_support = min_version_support
        if latest_version is not None:
            self.latest_version = latest_version
        if version_supported is not None:
            self.version_supported = version_supported

    @property
    def min_version_support(self):
        """Gets the min_version_support of this I8TerminalCheckVersionDto.  # noqa: E501


        :return: The min_version_support of this I8TerminalCheckVersionDto.  # noqa: E501
        :rtype: str
        """
        return self._min_version_support

    @min_version_support.setter
    def min_version_support(self, min_version_support):
        """Sets the min_version_support of this I8TerminalCheckVersionDto.


        :param min_version_support: The min_version_support of this I8TerminalCheckVersionDto.  # noqa: E501
        :type: str
        """

        self._min_version_support = min_version_support

    @property
    def latest_version(self):
        """Gets the latest_version of this I8TerminalCheckVersionDto.  # noqa: E501


        :return: The latest_version of this I8TerminalCheckVersionDto.  # noqa: E501
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this I8TerminalCheckVersionDto.


        :param latest_version: The latest_version of this I8TerminalCheckVersionDto.  # noqa: E501
        :type: str
        """

        self._latest_version = latest_version

    @property
    def version_supported(self):
        """Gets the version_supported of this I8TerminalCheckVersionDto.  # noqa: E501


        :return: The version_supported of this I8TerminalCheckVersionDto.  # noqa: E501
        :rtype: bool
        """
        return self._version_supported

    @version_supported.setter
    def version_supported(self, version_supported):
        """Sets the version_supported of this I8TerminalCheckVersionDto.


        :param version_supported: The version_supported of this I8TerminalCheckVersionDto.  # noqa: E501
        :type: bool
        """

        self._version_supported = version_supported

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
        if issubclass(I8TerminalCheckVersionDto, dict):
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
        if not isinstance(other, I8TerminalCheckVersionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
