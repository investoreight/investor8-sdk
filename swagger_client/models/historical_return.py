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

class HistoricalReturn(object):
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
        'metrics_id': 'str',
        'ticker': 'str',
        'next_close_return': 'ReturnMetrics',
        'next_open_return': 'ReturnMetrics',
        'intra_day_return': 'ReturnMetrics',
        'history_length': 'HistoryLength',
        'num_eps_beat': 'int',
        'num_eps_miss': 'int',
        'num_rev_beat': 'int',
        'num_rev_miss': 'int'
    }

    attribute_map = {
        'metrics_id': 'MetricsId',
        'ticker': 'Ticker',
        'next_close_return': 'NextCloseReturn',
        'next_open_return': 'NextOpenReturn',
        'intra_day_return': 'IntraDayReturn',
        'history_length': 'HistoryLength',
        'num_eps_beat': 'NumEpsBeat',
        'num_eps_miss': 'NumEpsMiss',
        'num_rev_beat': 'NumRevBeat',
        'num_rev_miss': 'NumRevMiss'
    }

    def __init__(self, metrics_id=None, ticker=None, next_close_return=None, next_open_return=None, intra_day_return=None, history_length=None, num_eps_beat=None, num_eps_miss=None, num_rev_beat=None, num_rev_miss=None):  # noqa: E501
        """HistoricalReturn - a model defined in Swagger"""  # noqa: E501
        self._metrics_id = None
        self._ticker = None
        self._next_close_return = None
        self._next_open_return = None
        self._intra_day_return = None
        self._history_length = None
        self._num_eps_beat = None
        self._num_eps_miss = None
        self._num_rev_beat = None
        self._num_rev_miss = None
        self.discriminator = None
        if metrics_id is not None:
            self.metrics_id = metrics_id
        if ticker is not None:
            self.ticker = ticker
        if next_close_return is not None:
            self.next_close_return = next_close_return
        if next_open_return is not None:
            self.next_open_return = next_open_return
        if intra_day_return is not None:
            self.intra_day_return = intra_day_return
        if history_length is not None:
            self.history_length = history_length
        if num_eps_beat is not None:
            self.num_eps_beat = num_eps_beat
        if num_eps_miss is not None:
            self.num_eps_miss = num_eps_miss
        if num_rev_beat is not None:
            self.num_rev_beat = num_rev_beat
        if num_rev_miss is not None:
            self.num_rev_miss = num_rev_miss

    @property
    def metrics_id(self):
        """Gets the metrics_id of this HistoricalReturn.  # noqa: E501


        :return: The metrics_id of this HistoricalReturn.  # noqa: E501
        :rtype: str
        """
        return self._metrics_id

    @metrics_id.setter
    def metrics_id(self, metrics_id):
        """Sets the metrics_id of this HistoricalReturn.


        :param metrics_id: The metrics_id of this HistoricalReturn.  # noqa: E501
        :type: str
        """

        self._metrics_id = metrics_id

    @property
    def ticker(self):
        """Gets the ticker of this HistoricalReturn.  # noqa: E501


        :return: The ticker of this HistoricalReturn.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this HistoricalReturn.


        :param ticker: The ticker of this HistoricalReturn.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def next_close_return(self):
        """Gets the next_close_return of this HistoricalReturn.  # noqa: E501


        :return: The next_close_return of this HistoricalReturn.  # noqa: E501
        :rtype: ReturnMetrics
        """
        return self._next_close_return

    @next_close_return.setter
    def next_close_return(self, next_close_return):
        """Sets the next_close_return of this HistoricalReturn.


        :param next_close_return: The next_close_return of this HistoricalReturn.  # noqa: E501
        :type: ReturnMetrics
        """

        self._next_close_return = next_close_return

    @property
    def next_open_return(self):
        """Gets the next_open_return of this HistoricalReturn.  # noqa: E501


        :return: The next_open_return of this HistoricalReturn.  # noqa: E501
        :rtype: ReturnMetrics
        """
        return self._next_open_return

    @next_open_return.setter
    def next_open_return(self, next_open_return):
        """Sets the next_open_return of this HistoricalReturn.


        :param next_open_return: The next_open_return of this HistoricalReturn.  # noqa: E501
        :type: ReturnMetrics
        """

        self._next_open_return = next_open_return

    @property
    def intra_day_return(self):
        """Gets the intra_day_return of this HistoricalReturn.  # noqa: E501


        :return: The intra_day_return of this HistoricalReturn.  # noqa: E501
        :rtype: ReturnMetrics
        """
        return self._intra_day_return

    @intra_day_return.setter
    def intra_day_return(self, intra_day_return):
        """Sets the intra_day_return of this HistoricalReturn.


        :param intra_day_return: The intra_day_return of this HistoricalReturn.  # noqa: E501
        :type: ReturnMetrics
        """

        self._intra_day_return = intra_day_return

    @property
    def history_length(self):
        """Gets the history_length of this HistoricalReturn.  # noqa: E501


        :return: The history_length of this HistoricalReturn.  # noqa: E501
        :rtype: HistoryLength
        """
        return self._history_length

    @history_length.setter
    def history_length(self, history_length):
        """Sets the history_length of this HistoricalReturn.


        :param history_length: The history_length of this HistoricalReturn.  # noqa: E501
        :type: HistoryLength
        """

        self._history_length = history_length

    @property
    def num_eps_beat(self):
        """Gets the num_eps_beat of this HistoricalReturn.  # noqa: E501


        :return: The num_eps_beat of this HistoricalReturn.  # noqa: E501
        :rtype: int
        """
        return self._num_eps_beat

    @num_eps_beat.setter
    def num_eps_beat(self, num_eps_beat):
        """Sets the num_eps_beat of this HistoricalReturn.


        :param num_eps_beat: The num_eps_beat of this HistoricalReturn.  # noqa: E501
        :type: int
        """

        self._num_eps_beat = num_eps_beat

    @property
    def num_eps_miss(self):
        """Gets the num_eps_miss of this HistoricalReturn.  # noqa: E501


        :return: The num_eps_miss of this HistoricalReturn.  # noqa: E501
        :rtype: int
        """
        return self._num_eps_miss

    @num_eps_miss.setter
    def num_eps_miss(self, num_eps_miss):
        """Sets the num_eps_miss of this HistoricalReturn.


        :param num_eps_miss: The num_eps_miss of this HistoricalReturn.  # noqa: E501
        :type: int
        """

        self._num_eps_miss = num_eps_miss

    @property
    def num_rev_beat(self):
        """Gets the num_rev_beat of this HistoricalReturn.  # noqa: E501


        :return: The num_rev_beat of this HistoricalReturn.  # noqa: E501
        :rtype: int
        """
        return self._num_rev_beat

    @num_rev_beat.setter
    def num_rev_beat(self, num_rev_beat):
        """Sets the num_rev_beat of this HistoricalReturn.


        :param num_rev_beat: The num_rev_beat of this HistoricalReturn.  # noqa: E501
        :type: int
        """

        self._num_rev_beat = num_rev_beat

    @property
    def num_rev_miss(self):
        """Gets the num_rev_miss of this HistoricalReturn.  # noqa: E501


        :return: The num_rev_miss of this HistoricalReturn.  # noqa: E501
        :rtype: int
        """
        return self._num_rev_miss

    @num_rev_miss.setter
    def num_rev_miss(self, num_rev_miss):
        """Sets the num_rev_miss of this HistoricalReturn.


        :param num_rev_miss: The num_rev_miss of this HistoricalReturn.  # noqa: E501
        :type: int
        """

        self._num_rev_miss = num_rev_miss

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
        if issubclass(HistoricalReturn, dict):
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
        if not isinstance(other, HistoricalReturn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
