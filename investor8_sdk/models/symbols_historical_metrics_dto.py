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

class SymbolsHistoricalMetricsDto(object):
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
        'data': 'dict(str, dict(str, list[HistoricalMetricValueDto]))',
        'metadata': 'list[MetricsMetadataResponseDto]'
    }

    attribute_map = {
        'data': 'Data',
        'metadata': 'Metadata'
    }

    def __init__(self, data=None, metadata=None):  # noqa: E501
        """SymbolsHistoricalMetricsDto - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._metadata = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if metadata is not None:
            self.metadata = metadata

    @property
    def data(self):
        """Gets the data of this SymbolsHistoricalMetricsDto.  # noqa: E501


        :return: The data of this SymbolsHistoricalMetricsDto.  # noqa: E501
        :rtype: dict(str, dict(str, list[HistoricalMetricValueDto]))
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SymbolsHistoricalMetricsDto.


        :param data: The data of this SymbolsHistoricalMetricsDto.  # noqa: E501
        :type: dict(str, dict(str, list[HistoricalMetricValueDto]))
        """

        self._data = data

    @property
    def metadata(self):
        """Gets the metadata of this SymbolsHistoricalMetricsDto.  # noqa: E501


        :return: The metadata of this SymbolsHistoricalMetricsDto.  # noqa: E501
        :rtype: list[MetricsMetadataResponseDto]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SymbolsHistoricalMetricsDto.


        :param metadata: The metadata of this SymbolsHistoricalMetricsDto.  # noqa: E501
        :type: list[MetricsMetadataResponseDto]
        """

        self._metadata = metadata

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
        if issubclass(SymbolsHistoricalMetricsDto, dict):
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
        if not isinstance(other, SymbolsHistoricalMetricsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
