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

class StockNews(object):
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
        'creation_timestamp': 'int',
        'publication_timestamp': 'int',
        'title': 'str',
        'title_slug': 'str',
        'ticker_slug': 'str',
        'summary': 'str',
        'tickers': 'list[str]',
        'tags': 'list[str]',
        'signature': 'str',
        'category_coarse': 'str',
        'category_fine': 'str',
        'status': 'StockNewsStatus',
        'allow_overwrite': 'bool',
        'stock_prices': 'list[LatestPriceDto]',
        'news_source': 'NewsSource',
        'image_url': 'str',
        'sector': 'str',
        'highlight_ids': 'list[str]',
        'image_source': 'str',
        'news_url': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'creation_timestamp': 'CreationTimestamp',
        'publication_timestamp': 'PublicationTimestamp',
        'title': 'Title',
        'title_slug': 'TitleSlug',
        'ticker_slug': 'TickerSlug',
        'summary': 'Summary',
        'tickers': 'Tickers',
        'tags': 'Tags',
        'signature': 'Signature',
        'category_coarse': 'CategoryCoarse',
        'category_fine': 'CategoryFine',
        'status': 'Status',
        'allow_overwrite': 'AllowOverwrite',
        'stock_prices': 'StockPrices',
        'news_source': 'NewsSource',
        'image_url': 'ImageUrl',
        'sector': 'Sector',
        'highlight_ids': 'HighlightIds',
        'image_source': 'ImageSource',
        'news_url': 'NewsUrl'
    }

    def __init__(self, id=None, creation_timestamp=None, publication_timestamp=None, title=None, title_slug=None, ticker_slug=None, summary=None, tickers=None, tags=None, signature=None, category_coarse=None, category_fine=None, status=None, allow_overwrite=None, stock_prices=None, news_source=None, image_url=None, sector=None, highlight_ids=None, image_source=None, news_url=None):  # noqa: E501
        """StockNews - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._creation_timestamp = None
        self._publication_timestamp = None
        self._title = None
        self._title_slug = None
        self._ticker_slug = None
        self._summary = None
        self._tickers = None
        self._tags = None
        self._signature = None
        self._category_coarse = None
        self._category_fine = None
        self._status = None
        self._allow_overwrite = None
        self._stock_prices = None
        self._news_source = None
        self._image_url = None
        self._sector = None
        self._highlight_ids = None
        self._image_source = None
        self._news_url = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if publication_timestamp is not None:
            self.publication_timestamp = publication_timestamp
        if title is not None:
            self.title = title
        if title_slug is not None:
            self.title_slug = title_slug
        if ticker_slug is not None:
            self.ticker_slug = ticker_slug
        if summary is not None:
            self.summary = summary
        if tickers is not None:
            self.tickers = tickers
        if tags is not None:
            self.tags = tags
        if signature is not None:
            self.signature = signature
        if category_coarse is not None:
            self.category_coarse = category_coarse
        if category_fine is not None:
            self.category_fine = category_fine
        if status is not None:
            self.status = status
        if allow_overwrite is not None:
            self.allow_overwrite = allow_overwrite
        if stock_prices is not None:
            self.stock_prices = stock_prices
        if news_source is not None:
            self.news_source = news_source
        if image_url is not None:
            self.image_url = image_url
        if sector is not None:
            self.sector = sector
        if highlight_ids is not None:
            self.highlight_ids = highlight_ids
        if image_source is not None:
            self.image_source = image_source
        if news_url is not None:
            self.news_url = news_url

    @property
    def id(self):
        """Gets the id of this StockNews.  # noqa: E501


        :return: The id of this StockNews.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StockNews.


        :param id: The id of this StockNews.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this StockNews.  # noqa: E501


        :return: The creation_timestamp of this StockNews.  # noqa: E501
        :rtype: int
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this StockNews.


        :param creation_timestamp: The creation_timestamp of this StockNews.  # noqa: E501
        :type: int
        """

        self._creation_timestamp = creation_timestamp

    @property
    def publication_timestamp(self):
        """Gets the publication_timestamp of this StockNews.  # noqa: E501


        :return: The publication_timestamp of this StockNews.  # noqa: E501
        :rtype: int
        """
        return self._publication_timestamp

    @publication_timestamp.setter
    def publication_timestamp(self, publication_timestamp):
        """Sets the publication_timestamp of this StockNews.


        :param publication_timestamp: The publication_timestamp of this StockNews.  # noqa: E501
        :type: int
        """

        self._publication_timestamp = publication_timestamp

    @property
    def title(self):
        """Gets the title of this StockNews.  # noqa: E501


        :return: The title of this StockNews.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this StockNews.


        :param title: The title of this StockNews.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def title_slug(self):
        """Gets the title_slug of this StockNews.  # noqa: E501


        :return: The title_slug of this StockNews.  # noqa: E501
        :rtype: str
        """
        return self._title_slug

    @title_slug.setter
    def title_slug(self, title_slug):
        """Sets the title_slug of this StockNews.


        :param title_slug: The title_slug of this StockNews.  # noqa: E501
        :type: str
        """

        self._title_slug = title_slug

    @property
    def ticker_slug(self):
        """Gets the ticker_slug of this StockNews.  # noqa: E501


        :return: The ticker_slug of this StockNews.  # noqa: E501
        :rtype: str
        """
        return self._ticker_slug

    @ticker_slug.setter
    def ticker_slug(self, ticker_slug):
        """Sets the ticker_slug of this StockNews.


        :param ticker_slug: The ticker_slug of this StockNews.  # noqa: E501
        :type: str
        """

        self._ticker_slug = ticker_slug

    @property
    def summary(self):
        """Gets the summary of this StockNews.  # noqa: E501


        :return: The summary of this StockNews.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this StockNews.


        :param summary: The summary of this StockNews.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def tickers(self):
        """Gets the tickers of this StockNews.  # noqa: E501


        :return: The tickers of this StockNews.  # noqa: E501
        :rtype: list[str]
        """
        return self._tickers

    @tickers.setter
    def tickers(self, tickers):
        """Sets the tickers of this StockNews.


        :param tickers: The tickers of this StockNews.  # noqa: E501
        :type: list[str]
        """

        self._tickers = tickers

    @property
    def tags(self):
        """Gets the tags of this StockNews.  # noqa: E501


        :return: The tags of this StockNews.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this StockNews.


        :param tags: The tags of this StockNews.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def signature(self):
        """Gets the signature of this StockNews.  # noqa: E501


        :return: The signature of this StockNews.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this StockNews.


        :param signature: The signature of this StockNews.  # noqa: E501
        :type: str
        """

        self._signature = signature

    @property
    def category_coarse(self):
        """Gets the category_coarse of this StockNews.  # noqa: E501


        :return: The category_coarse of this StockNews.  # noqa: E501
        :rtype: str
        """
        return self._category_coarse

    @category_coarse.setter
    def category_coarse(self, category_coarse):
        """Sets the category_coarse of this StockNews.


        :param category_coarse: The category_coarse of this StockNews.  # noqa: E501
        :type: str
        """

        self._category_coarse = category_coarse

    @property
    def category_fine(self):
        """Gets the category_fine of this StockNews.  # noqa: E501


        :return: The category_fine of this StockNews.  # noqa: E501
        :rtype: str
        """
        return self._category_fine

    @category_fine.setter
    def category_fine(self, category_fine):
        """Sets the category_fine of this StockNews.


        :param category_fine: The category_fine of this StockNews.  # noqa: E501
        :type: str
        """

        self._category_fine = category_fine

    @property
    def status(self):
        """Gets the status of this StockNews.  # noqa: E501


        :return: The status of this StockNews.  # noqa: E501
        :rtype: StockNewsStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StockNews.


        :param status: The status of this StockNews.  # noqa: E501
        :type: StockNewsStatus
        """

        self._status = status

    @property
    def allow_overwrite(self):
        """Gets the allow_overwrite of this StockNews.  # noqa: E501


        :return: The allow_overwrite of this StockNews.  # noqa: E501
        :rtype: bool
        """
        return self._allow_overwrite

    @allow_overwrite.setter
    def allow_overwrite(self, allow_overwrite):
        """Sets the allow_overwrite of this StockNews.


        :param allow_overwrite: The allow_overwrite of this StockNews.  # noqa: E501
        :type: bool
        """

        self._allow_overwrite = allow_overwrite

    @property
    def stock_prices(self):
        """Gets the stock_prices of this StockNews.  # noqa: E501


        :return: The stock_prices of this StockNews.  # noqa: E501
        :rtype: list[LatestPriceDto]
        """
        return self._stock_prices

    @stock_prices.setter
    def stock_prices(self, stock_prices):
        """Sets the stock_prices of this StockNews.


        :param stock_prices: The stock_prices of this StockNews.  # noqa: E501
        :type: list[LatestPriceDto]
        """

        self._stock_prices = stock_prices

    @property
    def news_source(self):
        """Gets the news_source of this StockNews.  # noqa: E501


        :return: The news_source of this StockNews.  # noqa: E501
        :rtype: NewsSource
        """
        return self._news_source

    @news_source.setter
    def news_source(self, news_source):
        """Sets the news_source of this StockNews.


        :param news_source: The news_source of this StockNews.  # noqa: E501
        :type: NewsSource
        """

        self._news_source = news_source

    @property
    def image_url(self):
        """Gets the image_url of this StockNews.  # noqa: E501


        :return: The image_url of this StockNews.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this StockNews.


        :param image_url: The image_url of this StockNews.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def sector(self):
        """Gets the sector of this StockNews.  # noqa: E501


        :return: The sector of this StockNews.  # noqa: E501
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this StockNews.


        :param sector: The sector of this StockNews.  # noqa: E501
        :type: str
        """

        self._sector = sector

    @property
    def highlight_ids(self):
        """Gets the highlight_ids of this StockNews.  # noqa: E501


        :return: The highlight_ids of this StockNews.  # noqa: E501
        :rtype: list[str]
        """
        return self._highlight_ids

    @highlight_ids.setter
    def highlight_ids(self, highlight_ids):
        """Sets the highlight_ids of this StockNews.


        :param highlight_ids: The highlight_ids of this StockNews.  # noqa: E501
        :type: list[str]
        """

        self._highlight_ids = highlight_ids

    @property
    def image_source(self):
        """Gets the image_source of this StockNews.  # noqa: E501


        :return: The image_source of this StockNews.  # noqa: E501
        :rtype: str
        """
        return self._image_source

    @image_source.setter
    def image_source(self, image_source):
        """Sets the image_source of this StockNews.


        :param image_source: The image_source of this StockNews.  # noqa: E501
        :type: str
        """

        self._image_source = image_source

    @property
    def news_url(self):
        """Gets the news_url of this StockNews.  # noqa: E501


        :return: The news_url of this StockNews.  # noqa: E501
        :rtype: str
        """
        return self._news_url

    @news_url.setter
    def news_url(self, news_url):
        """Sets the news_url of this StockNews.


        :param news_url: The news_url of this StockNews.  # noqa: E501
        :type: str
        """

        self._news_url = news_url

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
        if issubclass(StockNews, dict):
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
        if not isinstance(other, StockNews):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
