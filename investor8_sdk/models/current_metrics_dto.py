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

class CurrentMetricsDto(object):
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
        'symbol': 'str',
        'metric': 'str',
        'input_metric': 'str',
        'value': 'str',
        'period': 'str',
        'last_modified': 'datetime',
        'overall_rank': 'int',
        'overall_count': 'int',
        'spx_rank': 'int',
        'spx_count': 'int',
        'nasdaq_rank': 'int',
        'nasdaq_count': 'int',
        'dow_rank': 'int',
        'dow_count': 'int',
        'sector_rank': 'int',
        'sector_count': 'int',
        'industry_rank': 'int',
        'industry_count': 'int'
    }

    attribute_map = {
        'symbol': 'Symbol',
        'metric': 'Metric',
        'input_metric': 'InputMetric',
        'value': 'Value',
        'period': 'Period',
        'last_modified': 'LastModified',
        'overall_rank': 'OverallRank',
        'overall_count': 'OverallCount',
        'spx_rank': 'SpxRank',
        'spx_count': 'SpxCount',
        'nasdaq_rank': 'NasdaqRank',
        'nasdaq_count': 'NasdaqCount',
        'dow_rank': 'DowRank',
        'dow_count': 'DowCount',
        'sector_rank': 'SectorRank',
        'sector_count': 'SectorCount',
        'industry_rank': 'IndustryRank',
        'industry_count': 'IndustryCount'
    }

    def __init__(self, symbol=None, metric=None, input_metric=None, value=None, period=None, last_modified=None, overall_rank=None, overall_count=None, spx_rank=None, spx_count=None, nasdaq_rank=None, nasdaq_count=None, dow_rank=None, dow_count=None, sector_rank=None, sector_count=None, industry_rank=None, industry_count=None):  # noqa: E501
        """CurrentMetricsDto - a model defined in Swagger"""  # noqa: E501
        self._symbol = None
        self._metric = None
        self._input_metric = None
        self._value = None
        self._period = None
        self._last_modified = None
        self._overall_rank = None
        self._overall_count = None
        self._spx_rank = None
        self._spx_count = None
        self._nasdaq_rank = None
        self._nasdaq_count = None
        self._dow_rank = None
        self._dow_count = None
        self._sector_rank = None
        self._sector_count = None
        self._industry_rank = None
        self._industry_count = None
        self.discriminator = None
        if symbol is not None:
            self.symbol = symbol
        if metric is not None:
            self.metric = metric
        if input_metric is not None:
            self.input_metric = input_metric
        if value is not None:
            self.value = value
        if period is not None:
            self.period = period
        if last_modified is not None:
            self.last_modified = last_modified
        if overall_rank is not None:
            self.overall_rank = overall_rank
        if overall_count is not None:
            self.overall_count = overall_count
        if spx_rank is not None:
            self.spx_rank = spx_rank
        if spx_count is not None:
            self.spx_count = spx_count
        if nasdaq_rank is not None:
            self.nasdaq_rank = nasdaq_rank
        if nasdaq_count is not None:
            self.nasdaq_count = nasdaq_count
        if dow_rank is not None:
            self.dow_rank = dow_rank
        if dow_count is not None:
            self.dow_count = dow_count
        if sector_rank is not None:
            self.sector_rank = sector_rank
        if sector_count is not None:
            self.sector_count = sector_count
        if industry_rank is not None:
            self.industry_rank = industry_rank
        if industry_count is not None:
            self.industry_count = industry_count

    @property
    def symbol(self):
        """Gets the symbol of this CurrentMetricsDto.  # noqa: E501


        :return: The symbol of this CurrentMetricsDto.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this CurrentMetricsDto.


        :param symbol: The symbol of this CurrentMetricsDto.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def metric(self):
        """Gets the metric of this CurrentMetricsDto.  # noqa: E501


        :return: The metric of this CurrentMetricsDto.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this CurrentMetricsDto.


        :param metric: The metric of this CurrentMetricsDto.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def input_metric(self):
        """Gets the input_metric of this CurrentMetricsDto.  # noqa: E501


        :return: The input_metric of this CurrentMetricsDto.  # noqa: E501
        :rtype: str
        """
        return self._input_metric

    @input_metric.setter
    def input_metric(self, input_metric):
        """Sets the input_metric of this CurrentMetricsDto.


        :param input_metric: The input_metric of this CurrentMetricsDto.  # noqa: E501
        :type: str
        """

        self._input_metric = input_metric

    @property
    def value(self):
        """Gets the value of this CurrentMetricsDto.  # noqa: E501


        :return: The value of this CurrentMetricsDto.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CurrentMetricsDto.


        :param value: The value of this CurrentMetricsDto.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def period(self):
        """Gets the period of this CurrentMetricsDto.  # noqa: E501


        :return: The period of this CurrentMetricsDto.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this CurrentMetricsDto.


        :param period: The period of this CurrentMetricsDto.  # noqa: E501
        :type: str
        """

        self._period = period

    @property
    def last_modified(self):
        """Gets the last_modified of this CurrentMetricsDto.  # noqa: E501


        :return: The last_modified of this CurrentMetricsDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this CurrentMetricsDto.


        :param last_modified: The last_modified of this CurrentMetricsDto.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def overall_rank(self):
        """Gets the overall_rank of this CurrentMetricsDto.  # noqa: E501


        :return: The overall_rank of this CurrentMetricsDto.  # noqa: E501
        :rtype: int
        """
        return self._overall_rank

    @overall_rank.setter
    def overall_rank(self, overall_rank):
        """Sets the overall_rank of this CurrentMetricsDto.


        :param overall_rank: The overall_rank of this CurrentMetricsDto.  # noqa: E501
        :type: int
        """

        self._overall_rank = overall_rank

    @property
    def overall_count(self):
        """Gets the overall_count of this CurrentMetricsDto.  # noqa: E501


        :return: The overall_count of this CurrentMetricsDto.  # noqa: E501
        :rtype: int
        """
        return self._overall_count

    @overall_count.setter
    def overall_count(self, overall_count):
        """Sets the overall_count of this CurrentMetricsDto.


        :param overall_count: The overall_count of this CurrentMetricsDto.  # noqa: E501
        :type: int
        """

        self._overall_count = overall_count

    @property
    def spx_rank(self):
        """Gets the spx_rank of this CurrentMetricsDto.  # noqa: E501


        :return: The spx_rank of this CurrentMetricsDto.  # noqa: E501
        :rtype: int
        """
        return self._spx_rank

    @spx_rank.setter
    def spx_rank(self, spx_rank):
        """Sets the spx_rank of this CurrentMetricsDto.


        :param spx_rank: The spx_rank of this CurrentMetricsDto.  # noqa: E501
        :type: int
        """

        self._spx_rank = spx_rank

    @property
    def spx_count(self):
        """Gets the spx_count of this CurrentMetricsDto.  # noqa: E501


        :return: The spx_count of this CurrentMetricsDto.  # noqa: E501
        :rtype: int
        """
        return self._spx_count

    @spx_count.setter
    def spx_count(self, spx_count):
        """Sets the spx_count of this CurrentMetricsDto.


        :param spx_count: The spx_count of this CurrentMetricsDto.  # noqa: E501
        :type: int
        """

        self._spx_count = spx_count

    @property
    def nasdaq_rank(self):
        """Gets the nasdaq_rank of this CurrentMetricsDto.  # noqa: E501


        :return: The nasdaq_rank of this CurrentMetricsDto.  # noqa: E501
        :rtype: int
        """
        return self._nasdaq_rank

    @nasdaq_rank.setter
    def nasdaq_rank(self, nasdaq_rank):
        """Sets the nasdaq_rank of this CurrentMetricsDto.


        :param nasdaq_rank: The nasdaq_rank of this CurrentMetricsDto.  # noqa: E501
        :type: int
        """

        self._nasdaq_rank = nasdaq_rank

    @property
    def nasdaq_count(self):
        """Gets the nasdaq_count of this CurrentMetricsDto.  # noqa: E501


        :return: The nasdaq_count of this CurrentMetricsDto.  # noqa: E501
        :rtype: int
        """
        return self._nasdaq_count

    @nasdaq_count.setter
    def nasdaq_count(self, nasdaq_count):
        """Sets the nasdaq_count of this CurrentMetricsDto.


        :param nasdaq_count: The nasdaq_count of this CurrentMetricsDto.  # noqa: E501
        :type: int
        """

        self._nasdaq_count = nasdaq_count

    @property
    def dow_rank(self):
        """Gets the dow_rank of this CurrentMetricsDto.  # noqa: E501


        :return: The dow_rank of this CurrentMetricsDto.  # noqa: E501
        :rtype: int
        """
        return self._dow_rank

    @dow_rank.setter
    def dow_rank(self, dow_rank):
        """Sets the dow_rank of this CurrentMetricsDto.


        :param dow_rank: The dow_rank of this CurrentMetricsDto.  # noqa: E501
        :type: int
        """

        self._dow_rank = dow_rank

    @property
    def dow_count(self):
        """Gets the dow_count of this CurrentMetricsDto.  # noqa: E501


        :return: The dow_count of this CurrentMetricsDto.  # noqa: E501
        :rtype: int
        """
        return self._dow_count

    @dow_count.setter
    def dow_count(self, dow_count):
        """Sets the dow_count of this CurrentMetricsDto.


        :param dow_count: The dow_count of this CurrentMetricsDto.  # noqa: E501
        :type: int
        """

        self._dow_count = dow_count

    @property
    def sector_rank(self):
        """Gets the sector_rank of this CurrentMetricsDto.  # noqa: E501


        :return: The sector_rank of this CurrentMetricsDto.  # noqa: E501
        :rtype: int
        """
        return self._sector_rank

    @sector_rank.setter
    def sector_rank(self, sector_rank):
        """Sets the sector_rank of this CurrentMetricsDto.


        :param sector_rank: The sector_rank of this CurrentMetricsDto.  # noqa: E501
        :type: int
        """

        self._sector_rank = sector_rank

    @property
    def sector_count(self):
        """Gets the sector_count of this CurrentMetricsDto.  # noqa: E501


        :return: The sector_count of this CurrentMetricsDto.  # noqa: E501
        :rtype: int
        """
        return self._sector_count

    @sector_count.setter
    def sector_count(self, sector_count):
        """Sets the sector_count of this CurrentMetricsDto.


        :param sector_count: The sector_count of this CurrentMetricsDto.  # noqa: E501
        :type: int
        """

        self._sector_count = sector_count

    @property
    def industry_rank(self):
        """Gets the industry_rank of this CurrentMetricsDto.  # noqa: E501


        :return: The industry_rank of this CurrentMetricsDto.  # noqa: E501
        :rtype: int
        """
        return self._industry_rank

    @industry_rank.setter
    def industry_rank(self, industry_rank):
        """Sets the industry_rank of this CurrentMetricsDto.


        :param industry_rank: The industry_rank of this CurrentMetricsDto.  # noqa: E501
        :type: int
        """

        self._industry_rank = industry_rank

    @property
    def industry_count(self):
        """Gets the industry_count of this CurrentMetricsDto.  # noqa: E501


        :return: The industry_count of this CurrentMetricsDto.  # noqa: E501
        :rtype: int
        """
        return self._industry_count

    @industry_count.setter
    def industry_count(self, industry_count):
        """Sets the industry_count of this CurrentMetricsDto.


        :param industry_count: The industry_count of this CurrentMetricsDto.  # noqa: E501
        :type: int
        """

        self._industry_count = industry_count

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
        if issubclass(CurrentMetricsDto, dict):
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
        if not isinstance(other, CurrentMetricsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
