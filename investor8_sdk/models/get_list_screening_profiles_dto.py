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

class GetListScreeningProfilesDto(object):
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
        'id': 'str',
        'profile_name': 'str',
        'display_name': 'str',
        'conditions': 'str',
        'sort_metric': 'str',
        'sort_order': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'profile_name': 'ProfileName',
        'display_name': 'DisplayName',
        'conditions': 'Conditions',
        'sort_metric': 'SortMetric',
        'sort_order': 'SortOrder'
    }

    def __init__(self, id=None, profile_name=None, display_name=None, conditions=None, sort_metric=None, sort_order=None):  # noqa: E501
        """GetListScreeningProfilesDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._profile_name = None
        self._display_name = None
        self._conditions = None
        self._sort_metric = None
        self._sort_order = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if profile_name is not None:
            self.profile_name = profile_name
        if display_name is not None:
            self.display_name = display_name
        if conditions is not None:
            self.conditions = conditions
        if sort_metric is not None:
            self.sort_metric = sort_metric
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def id(self):
        """Gets the id of this GetListScreeningProfilesDto.  # noqa: E501


        :return: The id of this GetListScreeningProfilesDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetListScreeningProfilesDto.


        :param id: The id of this GetListScreeningProfilesDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def profile_name(self):
        """Gets the profile_name of this GetListScreeningProfilesDto.  # noqa: E501


        :return: The profile_name of this GetListScreeningProfilesDto.  # noqa: E501
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this GetListScreeningProfilesDto.


        :param profile_name: The profile_name of this GetListScreeningProfilesDto.  # noqa: E501
        :type: str
        """

        self._profile_name = profile_name

    @property
    def display_name(self):
        """Gets the display_name of this GetListScreeningProfilesDto.  # noqa: E501


        :return: The display_name of this GetListScreeningProfilesDto.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GetListScreeningProfilesDto.


        :param display_name: The display_name of this GetListScreeningProfilesDto.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def conditions(self):
        """Gets the conditions of this GetListScreeningProfilesDto.  # noqa: E501


        :return: The conditions of this GetListScreeningProfilesDto.  # noqa: E501
        :rtype: str
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this GetListScreeningProfilesDto.


        :param conditions: The conditions of this GetListScreeningProfilesDto.  # noqa: E501
        :type: str
        """

        self._conditions = conditions

    @property
    def sort_metric(self):
        """Gets the sort_metric of this GetListScreeningProfilesDto.  # noqa: E501


        :return: The sort_metric of this GetListScreeningProfilesDto.  # noqa: E501
        :rtype: str
        """
        return self._sort_metric

    @sort_metric.setter
    def sort_metric(self, sort_metric):
        """Sets the sort_metric of this GetListScreeningProfilesDto.


        :param sort_metric: The sort_metric of this GetListScreeningProfilesDto.  # noqa: E501
        :type: str
        """

        self._sort_metric = sort_metric

    @property
    def sort_order(self):
        """Gets the sort_order of this GetListScreeningProfilesDto.  # noqa: E501


        :return: The sort_order of this GetListScreeningProfilesDto.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this GetListScreeningProfilesDto.


        :param sort_order: The sort_order of this GetListScreeningProfilesDto.  # noqa: E501
        :type: str
        """

        self._sort_order = sort_order

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
        if issubclass(GetListScreeningProfilesDto, dict):
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
        if not isinstance(other, GetListScreeningProfilesDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
