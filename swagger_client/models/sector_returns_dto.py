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

class SectorReturnsDto(object):
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
        'sector': 'str',
        '_return': 'float'
    }

    attribute_map = {
        'sector': 'Sector',
        '_return': 'Return'
    }

    def __init__(self, sector=None, _return=None):  # noqa: E501
        """SectorReturnsDto - a model defined in Swagger"""  # noqa: E501
        self._sector = None
        self.__return = None
        self.discriminator = None
        if sector is not None:
            self.sector = sector
        if _return is not None:
            self._return = _return

    @property
    def sector(self):
        """Gets the sector of this SectorReturnsDto.  # noqa: E501


        :return: The sector of this SectorReturnsDto.  # noqa: E501
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this SectorReturnsDto.


        :param sector: The sector of this SectorReturnsDto.  # noqa: E501
        :type: str
        """

        self._sector = sector

    @property
    def _return(self):
        """Gets the _return of this SectorReturnsDto.  # noqa: E501


        :return: The _return of this SectorReturnsDto.  # noqa: E501
        :rtype: float
        """
        return self.__return

    @_return.setter
    def _return(self, _return):
        """Sets the _return of this SectorReturnsDto.


        :param _return: The _return of this SectorReturnsDto.  # noqa: E501
        :type: float
        """

        self.__return = _return

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
        if issubclass(SectorReturnsDto, dict):
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
        if not isinstance(other, SectorReturnsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other