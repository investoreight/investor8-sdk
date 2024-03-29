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

class StockInfoDto(object):
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
        'security_id': 'str',
        'ticker': 'str',
        'exchange': 'str',
        'name': 'str',
        'sector': 'str',
        'is_spx': 'bool',
        'is_active': 'bool',
        'ticker_slug': 'str',
        'peers': 'list[str]'
    }

    attribute_map = {
        'security_id': 'SecurityId',
        'ticker': 'Ticker',
        'exchange': 'Exchange',
        'name': 'Name',
        'sector': 'Sector',
        'is_spx': 'IsSpx',
        'is_active': 'IsActive',
        'ticker_slug': 'TickerSlug',
        'peers': 'Peers'
    }

    def __init__(self, security_id=None, ticker=None, exchange=None, name=None, sector=None, is_spx=None, is_active=None, ticker_slug=None, peers=None):  # noqa: E501
        """StockInfoDto - a model defined in Swagger"""  # noqa: E501
        self._security_id = None
        self._ticker = None
        self._exchange = None
        self._name = None
        self._sector = None
        self._is_spx = None
        self._is_active = None
        self._ticker_slug = None
        self._peers = None
        self.discriminator = None
        if security_id is not None:
            self.security_id = security_id
        if ticker is not None:
            self.ticker = ticker
        if exchange is not None:
            self.exchange = exchange
        if name is not None:
            self.name = name
        if sector is not None:
            self.sector = sector
        if is_spx is not None:
            self.is_spx = is_spx
        if is_active is not None:
            self.is_active = is_active
        if ticker_slug is not None:
            self.ticker_slug = ticker_slug
        if peers is not None:
            self.peers = peers

    @property
    def security_id(self):
        """Gets the security_id of this StockInfoDto.  # noqa: E501


        :return: The security_id of this StockInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._security_id

    @security_id.setter
    def security_id(self, security_id):
        """Sets the security_id of this StockInfoDto.


        :param security_id: The security_id of this StockInfoDto.  # noqa: E501
        :type: str
        """

        self._security_id = security_id

    @property
    def ticker(self):
        """Gets the ticker of this StockInfoDto.  # noqa: E501


        :return: The ticker of this StockInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this StockInfoDto.


        :param ticker: The ticker of this StockInfoDto.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def exchange(self):
        """Gets the exchange of this StockInfoDto.  # noqa: E501


        :return: The exchange of this StockInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this StockInfoDto.


        :param exchange: The exchange of this StockInfoDto.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def name(self):
        """Gets the name of this StockInfoDto.  # noqa: E501


        :return: The name of this StockInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StockInfoDto.


        :param name: The name of this StockInfoDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sector(self):
        """Gets the sector of this StockInfoDto.  # noqa: E501


        :return: The sector of this StockInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this StockInfoDto.


        :param sector: The sector of this StockInfoDto.  # noqa: E501
        :type: str
        """

        self._sector = sector

    @property
    def is_spx(self):
        """Gets the is_spx of this StockInfoDto.  # noqa: E501


        :return: The is_spx of this StockInfoDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_spx

    @is_spx.setter
    def is_spx(self, is_spx):
        """Sets the is_spx of this StockInfoDto.


        :param is_spx: The is_spx of this StockInfoDto.  # noqa: E501
        :type: bool
        """

        self._is_spx = is_spx

    @property
    def is_active(self):
        """Gets the is_active of this StockInfoDto.  # noqa: E501


        :return: The is_active of this StockInfoDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this StockInfoDto.


        :param is_active: The is_active of this StockInfoDto.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def ticker_slug(self):
        """Gets the ticker_slug of this StockInfoDto.  # noqa: E501


        :return: The ticker_slug of this StockInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker_slug

    @ticker_slug.setter
    def ticker_slug(self, ticker_slug):
        """Sets the ticker_slug of this StockInfoDto.


        :param ticker_slug: The ticker_slug of this StockInfoDto.  # noqa: E501
        :type: str
        """

        self._ticker_slug = ticker_slug

    @property
    def peers(self):
        """Gets the peers of this StockInfoDto.  # noqa: E501


        :return: The peers of this StockInfoDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._peers

    @peers.setter
    def peers(self, peers):
        """Sets the peers of this StockInfoDto.


        :param peers: The peers of this StockInfoDto.  # noqa: E501
        :type: list[str]
        """

        self._peers = peers

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
        if issubclass(StockInfoDto, dict):
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
        if not isinstance(other, StockInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
