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

class StockRatingDto(object):
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
        'ticker': 'str',
        'action': 'str',
        'brokerage': 'str',
        'price_target_old': 'float',
        'price_target_new': 'float',
        'rating_old': 'str',
        'rating_new': 'str',
        'impact_on_price': 'str',
        'currency': 'str',
        'rating_date': 'int',
        'collection_timestamp': 'int',
        'source': 'str'
    }

    attribute_map = {
        'ticker': 'Ticker',
        'action': 'Action',
        'brokerage': 'Brokerage',
        'price_target_old': 'PriceTargetOld',
        'price_target_new': 'PriceTargetNew',
        'rating_old': 'RatingOld',
        'rating_new': 'RatingNew',
        'impact_on_price': 'ImpactOnPrice',
        'currency': 'Currency',
        'rating_date': 'RatingDate',
        'collection_timestamp': 'CollectionTimestamp',
        'source': 'Source'
    }

    def __init__(self, ticker=None, action=None, brokerage=None, price_target_old=None, price_target_new=None, rating_old=None, rating_new=None, impact_on_price=None, currency=None, rating_date=None, collection_timestamp=None, source=None):  # noqa: E501
        """StockRatingDto - a model defined in Swagger"""  # noqa: E501
        self._ticker = None
        self._action = None
        self._brokerage = None
        self._price_target_old = None
        self._price_target_new = None
        self._rating_old = None
        self._rating_new = None
        self._impact_on_price = None
        self._currency = None
        self._rating_date = None
        self._collection_timestamp = None
        self._source = None
        self.discriminator = None
        if ticker is not None:
            self.ticker = ticker
        if action is not None:
            self.action = action
        if brokerage is not None:
            self.brokerage = brokerage
        if price_target_old is not None:
            self.price_target_old = price_target_old
        if price_target_new is not None:
            self.price_target_new = price_target_new
        if rating_old is not None:
            self.rating_old = rating_old
        if rating_new is not None:
            self.rating_new = rating_new
        if impact_on_price is not None:
            self.impact_on_price = impact_on_price
        if currency is not None:
            self.currency = currency
        if rating_date is not None:
            self.rating_date = rating_date
        if collection_timestamp is not None:
            self.collection_timestamp = collection_timestamp
        if source is not None:
            self.source = source

    @property
    def ticker(self):
        """Gets the ticker of this StockRatingDto.  # noqa: E501


        :return: The ticker of this StockRatingDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this StockRatingDto.


        :param ticker: The ticker of this StockRatingDto.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def action(self):
        """Gets the action of this StockRatingDto.  # noqa: E501


        :return: The action of this StockRatingDto.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this StockRatingDto.


        :param action: The action of this StockRatingDto.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def brokerage(self):
        """Gets the brokerage of this StockRatingDto.  # noqa: E501


        :return: The brokerage of this StockRatingDto.  # noqa: E501
        :rtype: str
        """
        return self._brokerage

    @brokerage.setter
    def brokerage(self, brokerage):
        """Sets the brokerage of this StockRatingDto.


        :param brokerage: The brokerage of this StockRatingDto.  # noqa: E501
        :type: str
        """

        self._brokerage = brokerage

    @property
    def price_target_old(self):
        """Gets the price_target_old of this StockRatingDto.  # noqa: E501


        :return: The price_target_old of this StockRatingDto.  # noqa: E501
        :rtype: float
        """
        return self._price_target_old

    @price_target_old.setter
    def price_target_old(self, price_target_old):
        """Sets the price_target_old of this StockRatingDto.


        :param price_target_old: The price_target_old of this StockRatingDto.  # noqa: E501
        :type: float
        """

        self._price_target_old = price_target_old

    @property
    def price_target_new(self):
        """Gets the price_target_new of this StockRatingDto.  # noqa: E501


        :return: The price_target_new of this StockRatingDto.  # noqa: E501
        :rtype: float
        """
        return self._price_target_new

    @price_target_new.setter
    def price_target_new(self, price_target_new):
        """Sets the price_target_new of this StockRatingDto.


        :param price_target_new: The price_target_new of this StockRatingDto.  # noqa: E501
        :type: float
        """

        self._price_target_new = price_target_new

    @property
    def rating_old(self):
        """Gets the rating_old of this StockRatingDto.  # noqa: E501


        :return: The rating_old of this StockRatingDto.  # noqa: E501
        :rtype: str
        """
        return self._rating_old

    @rating_old.setter
    def rating_old(self, rating_old):
        """Sets the rating_old of this StockRatingDto.


        :param rating_old: The rating_old of this StockRatingDto.  # noqa: E501
        :type: str
        """

        self._rating_old = rating_old

    @property
    def rating_new(self):
        """Gets the rating_new of this StockRatingDto.  # noqa: E501


        :return: The rating_new of this StockRatingDto.  # noqa: E501
        :rtype: str
        """
        return self._rating_new

    @rating_new.setter
    def rating_new(self, rating_new):
        """Sets the rating_new of this StockRatingDto.


        :param rating_new: The rating_new of this StockRatingDto.  # noqa: E501
        :type: str
        """

        self._rating_new = rating_new

    @property
    def impact_on_price(self):
        """Gets the impact_on_price of this StockRatingDto.  # noqa: E501


        :return: The impact_on_price of this StockRatingDto.  # noqa: E501
        :rtype: str
        """
        return self._impact_on_price

    @impact_on_price.setter
    def impact_on_price(self, impact_on_price):
        """Sets the impact_on_price of this StockRatingDto.


        :param impact_on_price: The impact_on_price of this StockRatingDto.  # noqa: E501
        :type: str
        """

        self._impact_on_price = impact_on_price

    @property
    def currency(self):
        """Gets the currency of this StockRatingDto.  # noqa: E501


        :return: The currency of this StockRatingDto.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this StockRatingDto.


        :param currency: The currency of this StockRatingDto.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def rating_date(self):
        """Gets the rating_date of this StockRatingDto.  # noqa: E501


        :return: The rating_date of this StockRatingDto.  # noqa: E501
        :rtype: int
        """
        return self._rating_date

    @rating_date.setter
    def rating_date(self, rating_date):
        """Sets the rating_date of this StockRatingDto.


        :param rating_date: The rating_date of this StockRatingDto.  # noqa: E501
        :type: int
        """

        self._rating_date = rating_date

    @property
    def collection_timestamp(self):
        """Gets the collection_timestamp of this StockRatingDto.  # noqa: E501


        :return: The collection_timestamp of this StockRatingDto.  # noqa: E501
        :rtype: int
        """
        return self._collection_timestamp

    @collection_timestamp.setter
    def collection_timestamp(self, collection_timestamp):
        """Sets the collection_timestamp of this StockRatingDto.


        :param collection_timestamp: The collection_timestamp of this StockRatingDto.  # noqa: E501
        :type: int
        """

        self._collection_timestamp = collection_timestamp

    @property
    def source(self):
        """Gets the source of this StockRatingDto.  # noqa: E501


        :return: The source of this StockRatingDto.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this StockRatingDto.


        :param source: The source of this StockRatingDto.  # noqa: E501
        :type: str
        """

        self._source = source

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
        if issubclass(StockRatingDto, dict):
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
        if not isinstance(other, StockRatingDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
