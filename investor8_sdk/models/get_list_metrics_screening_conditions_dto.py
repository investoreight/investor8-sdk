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

class GetListMetricsScreeningConditionsDto(object):
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
        'metric_name': 'str',
        'screening_conditions': 'list[ScreeningConditionDto]'
    }

    attribute_map = {
        'id': 'Id',
        'metric_name': 'MetricName',
        'screening_conditions': 'ScreeningConditions'
    }

    def __init__(self, id=None, metric_name=None, screening_conditions=None):  # noqa: E501
        """GetListMetricsScreeningConditionsDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._metric_name = None
        self._screening_conditions = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if metric_name is not None:
            self.metric_name = metric_name
        if screening_conditions is not None:
            self.screening_conditions = screening_conditions

    @property
    def id(self):
        """Gets the id of this GetListMetricsScreeningConditionsDto.  # noqa: E501


        :return: The id of this GetListMetricsScreeningConditionsDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetListMetricsScreeningConditionsDto.


        :param id: The id of this GetListMetricsScreeningConditionsDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def metric_name(self):
        """Gets the metric_name of this GetListMetricsScreeningConditionsDto.  # noqa: E501


        :return: The metric_name of this GetListMetricsScreeningConditionsDto.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this GetListMetricsScreeningConditionsDto.


        :param metric_name: The metric_name of this GetListMetricsScreeningConditionsDto.  # noqa: E501
        :type: str
        """

        self._metric_name = metric_name

    @property
    def screening_conditions(self):
        """Gets the screening_conditions of this GetListMetricsScreeningConditionsDto.  # noqa: E501


        :return: The screening_conditions of this GetListMetricsScreeningConditionsDto.  # noqa: E501
        :rtype: list[ScreeningConditionDto]
        """
        return self._screening_conditions

    @screening_conditions.setter
    def screening_conditions(self, screening_conditions):
        """Sets the screening_conditions of this GetListMetricsScreeningConditionsDto.


        :param screening_conditions: The screening_conditions of this GetListMetricsScreeningConditionsDto.  # noqa: E501
        :type: list[ScreeningConditionDto]
        """

        self._screening_conditions = screening_conditions

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
        if issubclass(GetListMetricsScreeningConditionsDto, dict):
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
        if not isinstance(other, GetListMetricsScreeningConditionsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
