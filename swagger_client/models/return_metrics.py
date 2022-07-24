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

class ReturnMetrics(object):
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
        'history_length': 'HistoryLength',
        'min': 'float',
        'max': 'float',
        'avg': 'float',
        'std': 'float',
        'positive_return_prob': 'float',
        'expected_return': 'float'
    }

    attribute_map = {
        'history_length': 'HistoryLength',
        'min': 'Min',
        'max': 'Max',
        'avg': 'Avg',
        'std': 'Std',
        'positive_return_prob': 'PositiveReturnProb',
        'expected_return': 'ExpectedReturn'
    }

    def __init__(self, history_length=None, min=None, max=None, avg=None, std=None, positive_return_prob=None, expected_return=None):  # noqa: E501
        """ReturnMetrics - a model defined in Swagger"""  # noqa: E501
        self._history_length = None
        self._min = None
        self._max = None
        self._avg = None
        self._std = None
        self._positive_return_prob = None
        self._expected_return = None
        self.discriminator = None
        if history_length is not None:
            self.history_length = history_length
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if avg is not None:
            self.avg = avg
        if std is not None:
            self.std = std
        if positive_return_prob is not None:
            self.positive_return_prob = positive_return_prob
        if expected_return is not None:
            self.expected_return = expected_return

    @property
    def history_length(self):
        """Gets the history_length of this ReturnMetrics.  # noqa: E501


        :return: The history_length of this ReturnMetrics.  # noqa: E501
        :rtype: HistoryLength
        """
        return self._history_length

    @history_length.setter
    def history_length(self, history_length):
        """Sets the history_length of this ReturnMetrics.


        :param history_length: The history_length of this ReturnMetrics.  # noqa: E501
        :type: HistoryLength
        """

        self._history_length = history_length

    @property
    def min(self):
        """Gets the min of this ReturnMetrics.  # noqa: E501


        :return: The min of this ReturnMetrics.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this ReturnMetrics.


        :param min: The min of this ReturnMetrics.  # noqa: E501
        :type: float
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this ReturnMetrics.  # noqa: E501


        :return: The max of this ReturnMetrics.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ReturnMetrics.


        :param max: The max of this ReturnMetrics.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def avg(self):
        """Gets the avg of this ReturnMetrics.  # noqa: E501


        :return: The avg of this ReturnMetrics.  # noqa: E501
        :rtype: float
        """
        return self._avg

    @avg.setter
    def avg(self, avg):
        """Sets the avg of this ReturnMetrics.


        :param avg: The avg of this ReturnMetrics.  # noqa: E501
        :type: float
        """

        self._avg = avg

    @property
    def std(self):
        """Gets the std of this ReturnMetrics.  # noqa: E501


        :return: The std of this ReturnMetrics.  # noqa: E501
        :rtype: float
        """
        return self._std

    @std.setter
    def std(self, std):
        """Sets the std of this ReturnMetrics.


        :param std: The std of this ReturnMetrics.  # noqa: E501
        :type: float
        """

        self._std = std

    @property
    def positive_return_prob(self):
        """Gets the positive_return_prob of this ReturnMetrics.  # noqa: E501


        :return: The positive_return_prob of this ReturnMetrics.  # noqa: E501
        :rtype: float
        """
        return self._positive_return_prob

    @positive_return_prob.setter
    def positive_return_prob(self, positive_return_prob):
        """Sets the positive_return_prob of this ReturnMetrics.


        :param positive_return_prob: The positive_return_prob of this ReturnMetrics.  # noqa: E501
        :type: float
        """

        self._positive_return_prob = positive_return_prob

    @property
    def expected_return(self):
        """Gets the expected_return of this ReturnMetrics.  # noqa: E501


        :return: The expected_return of this ReturnMetrics.  # noqa: E501
        :rtype: float
        """
        return self._expected_return

    @expected_return.setter
    def expected_return(self, expected_return):
        """Sets the expected_return of this ReturnMetrics.


        :param expected_return: The expected_return of this ReturnMetrics.  # noqa: E501
        :type: float
        """

        self._expected_return = expected_return

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
        if issubclass(ReturnMetrics, dict):
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
        if not isinstance(other, ReturnMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
