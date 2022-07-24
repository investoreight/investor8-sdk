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

class StockInfoMasterDto(object):
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
        'summary': 'StockSummaryDto',
        'latest_earning': 'StockEarningDto',
        'upcoming_earning': 'StockEarningDto',
        'latest_financials': 'LatestFinancialsWithGrowthDto',
        'second_latest_financials': 'LatestFinancialsWithGrowthDto',
        'previous_year_financials': 'LatestFinancialsWithGrowthDto',
        'price_returns': 'dict(str, float)',
        'monthly_returns': 'dict(str, dict(str, float))',
        'sector_returns': 'dict(str, float)',
        'spx_returns': 'dict(str, float)',
        'dow_returns': 'dict(str, float)',
        'ndx_returns': 'dict(str, float)',
        'metrics': 'Metrics',
        'current_momentum': 'CurrentMomentumMetricsDto',
        'latest_rating': 'StockRatingDto'
    }

    attribute_map = {
        'ticker': 'Ticker',
        'summary': 'Summary',
        'latest_earning': 'LatestEarning',
        'upcoming_earning': 'UpcomingEarning',
        'latest_financials': 'LatestFinancials',
        'second_latest_financials': 'SecondLatestFinancials',
        'previous_year_financials': 'PreviousYearFinancials',
        'price_returns': 'PriceReturns',
        'monthly_returns': 'MonthlyReturns',
        'sector_returns': 'SectorReturns',
        'spx_returns': 'SpxReturns',
        'dow_returns': 'DowReturns',
        'ndx_returns': 'NdxReturns',
        'metrics': 'Metrics',
        'current_momentum': 'CurrentMomentum',
        'latest_rating': 'LatestRating'
    }

    def __init__(self, ticker=None, summary=None, latest_earning=None, upcoming_earning=None, latest_financials=None, second_latest_financials=None, previous_year_financials=None, price_returns=None, monthly_returns=None, sector_returns=None, spx_returns=None, dow_returns=None, ndx_returns=None, metrics=None, current_momentum=None, latest_rating=None):  # noqa: E501
        """StockInfoMasterDto - a model defined in Swagger"""  # noqa: E501
        self._ticker = None
        self._summary = None
        self._latest_earning = None
        self._upcoming_earning = None
        self._latest_financials = None
        self._second_latest_financials = None
        self._previous_year_financials = None
        self._price_returns = None
        self._monthly_returns = None
        self._sector_returns = None
        self._spx_returns = None
        self._dow_returns = None
        self._ndx_returns = None
        self._metrics = None
        self._current_momentum = None
        self._latest_rating = None
        self.discriminator = None
        if ticker is not None:
            self.ticker = ticker
        if summary is not None:
            self.summary = summary
        if latest_earning is not None:
            self.latest_earning = latest_earning
        if upcoming_earning is not None:
            self.upcoming_earning = upcoming_earning
        if latest_financials is not None:
            self.latest_financials = latest_financials
        if second_latest_financials is not None:
            self.second_latest_financials = second_latest_financials
        if previous_year_financials is not None:
            self.previous_year_financials = previous_year_financials
        if price_returns is not None:
            self.price_returns = price_returns
        if monthly_returns is not None:
            self.monthly_returns = monthly_returns
        if sector_returns is not None:
            self.sector_returns = sector_returns
        if spx_returns is not None:
            self.spx_returns = spx_returns
        if dow_returns is not None:
            self.dow_returns = dow_returns
        if ndx_returns is not None:
            self.ndx_returns = ndx_returns
        if metrics is not None:
            self.metrics = metrics
        if current_momentum is not None:
            self.current_momentum = current_momentum
        if latest_rating is not None:
            self.latest_rating = latest_rating

    @property
    def ticker(self):
        """Gets the ticker of this StockInfoMasterDto.  # noqa: E501


        :return: The ticker of this StockInfoMasterDto.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this StockInfoMasterDto.


        :param ticker: The ticker of this StockInfoMasterDto.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def summary(self):
        """Gets the summary of this StockInfoMasterDto.  # noqa: E501


        :return: The summary of this StockInfoMasterDto.  # noqa: E501
        :rtype: StockSummaryDto
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this StockInfoMasterDto.


        :param summary: The summary of this StockInfoMasterDto.  # noqa: E501
        :type: StockSummaryDto
        """

        self._summary = summary

    @property
    def latest_earning(self):
        """Gets the latest_earning of this StockInfoMasterDto.  # noqa: E501


        :return: The latest_earning of this StockInfoMasterDto.  # noqa: E501
        :rtype: StockEarningDto
        """
        return self._latest_earning

    @latest_earning.setter
    def latest_earning(self, latest_earning):
        """Sets the latest_earning of this StockInfoMasterDto.


        :param latest_earning: The latest_earning of this StockInfoMasterDto.  # noqa: E501
        :type: StockEarningDto
        """

        self._latest_earning = latest_earning

    @property
    def upcoming_earning(self):
        """Gets the upcoming_earning of this StockInfoMasterDto.  # noqa: E501


        :return: The upcoming_earning of this StockInfoMasterDto.  # noqa: E501
        :rtype: StockEarningDto
        """
        return self._upcoming_earning

    @upcoming_earning.setter
    def upcoming_earning(self, upcoming_earning):
        """Sets the upcoming_earning of this StockInfoMasterDto.


        :param upcoming_earning: The upcoming_earning of this StockInfoMasterDto.  # noqa: E501
        :type: StockEarningDto
        """

        self._upcoming_earning = upcoming_earning

    @property
    def latest_financials(self):
        """Gets the latest_financials of this StockInfoMasterDto.  # noqa: E501


        :return: The latest_financials of this StockInfoMasterDto.  # noqa: E501
        :rtype: LatestFinancialsWithGrowthDto
        """
        return self._latest_financials

    @latest_financials.setter
    def latest_financials(self, latest_financials):
        """Sets the latest_financials of this StockInfoMasterDto.


        :param latest_financials: The latest_financials of this StockInfoMasterDto.  # noqa: E501
        :type: LatestFinancialsWithGrowthDto
        """

        self._latest_financials = latest_financials

    @property
    def second_latest_financials(self):
        """Gets the second_latest_financials of this StockInfoMasterDto.  # noqa: E501


        :return: The second_latest_financials of this StockInfoMasterDto.  # noqa: E501
        :rtype: LatestFinancialsWithGrowthDto
        """
        return self._second_latest_financials

    @second_latest_financials.setter
    def second_latest_financials(self, second_latest_financials):
        """Sets the second_latest_financials of this StockInfoMasterDto.


        :param second_latest_financials: The second_latest_financials of this StockInfoMasterDto.  # noqa: E501
        :type: LatestFinancialsWithGrowthDto
        """

        self._second_latest_financials = second_latest_financials

    @property
    def previous_year_financials(self):
        """Gets the previous_year_financials of this StockInfoMasterDto.  # noqa: E501


        :return: The previous_year_financials of this StockInfoMasterDto.  # noqa: E501
        :rtype: LatestFinancialsWithGrowthDto
        """
        return self._previous_year_financials

    @previous_year_financials.setter
    def previous_year_financials(self, previous_year_financials):
        """Sets the previous_year_financials of this StockInfoMasterDto.


        :param previous_year_financials: The previous_year_financials of this StockInfoMasterDto.  # noqa: E501
        :type: LatestFinancialsWithGrowthDto
        """

        self._previous_year_financials = previous_year_financials

    @property
    def price_returns(self):
        """Gets the price_returns of this StockInfoMasterDto.  # noqa: E501


        :return: The price_returns of this StockInfoMasterDto.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._price_returns

    @price_returns.setter
    def price_returns(self, price_returns):
        """Sets the price_returns of this StockInfoMasterDto.


        :param price_returns: The price_returns of this StockInfoMasterDto.  # noqa: E501
        :type: dict(str, float)
        """

        self._price_returns = price_returns

    @property
    def monthly_returns(self):
        """Gets the monthly_returns of this StockInfoMasterDto.  # noqa: E501


        :return: The monthly_returns of this StockInfoMasterDto.  # noqa: E501
        :rtype: dict(str, dict(str, float))
        """
        return self._monthly_returns

    @monthly_returns.setter
    def monthly_returns(self, monthly_returns):
        """Sets the monthly_returns of this StockInfoMasterDto.


        :param monthly_returns: The monthly_returns of this StockInfoMasterDto.  # noqa: E501
        :type: dict(str, dict(str, float))
        """

        self._monthly_returns = monthly_returns

    @property
    def sector_returns(self):
        """Gets the sector_returns of this StockInfoMasterDto.  # noqa: E501


        :return: The sector_returns of this StockInfoMasterDto.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._sector_returns

    @sector_returns.setter
    def sector_returns(self, sector_returns):
        """Sets the sector_returns of this StockInfoMasterDto.


        :param sector_returns: The sector_returns of this StockInfoMasterDto.  # noqa: E501
        :type: dict(str, float)
        """

        self._sector_returns = sector_returns

    @property
    def spx_returns(self):
        """Gets the spx_returns of this StockInfoMasterDto.  # noqa: E501


        :return: The spx_returns of this StockInfoMasterDto.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._spx_returns

    @spx_returns.setter
    def spx_returns(self, spx_returns):
        """Sets the spx_returns of this StockInfoMasterDto.


        :param spx_returns: The spx_returns of this StockInfoMasterDto.  # noqa: E501
        :type: dict(str, float)
        """

        self._spx_returns = spx_returns

    @property
    def dow_returns(self):
        """Gets the dow_returns of this StockInfoMasterDto.  # noqa: E501


        :return: The dow_returns of this StockInfoMasterDto.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._dow_returns

    @dow_returns.setter
    def dow_returns(self, dow_returns):
        """Sets the dow_returns of this StockInfoMasterDto.


        :param dow_returns: The dow_returns of this StockInfoMasterDto.  # noqa: E501
        :type: dict(str, float)
        """

        self._dow_returns = dow_returns

    @property
    def ndx_returns(self):
        """Gets the ndx_returns of this StockInfoMasterDto.  # noqa: E501


        :return: The ndx_returns of this StockInfoMasterDto.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._ndx_returns

    @ndx_returns.setter
    def ndx_returns(self, ndx_returns):
        """Sets the ndx_returns of this StockInfoMasterDto.


        :param ndx_returns: The ndx_returns of this StockInfoMasterDto.  # noqa: E501
        :type: dict(str, float)
        """

        self._ndx_returns = ndx_returns

    @property
    def metrics(self):
        """Gets the metrics of this StockInfoMasterDto.  # noqa: E501


        :return: The metrics of this StockInfoMasterDto.  # noqa: E501
        :rtype: Metrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this StockInfoMasterDto.


        :param metrics: The metrics of this StockInfoMasterDto.  # noqa: E501
        :type: Metrics
        """

        self._metrics = metrics

    @property
    def current_momentum(self):
        """Gets the current_momentum of this StockInfoMasterDto.  # noqa: E501


        :return: The current_momentum of this StockInfoMasterDto.  # noqa: E501
        :rtype: CurrentMomentumMetricsDto
        """
        return self._current_momentum

    @current_momentum.setter
    def current_momentum(self, current_momentum):
        """Sets the current_momentum of this StockInfoMasterDto.


        :param current_momentum: The current_momentum of this StockInfoMasterDto.  # noqa: E501
        :type: CurrentMomentumMetricsDto
        """

        self._current_momentum = current_momentum

    @property
    def latest_rating(self):
        """Gets the latest_rating of this StockInfoMasterDto.  # noqa: E501


        :return: The latest_rating of this StockInfoMasterDto.  # noqa: E501
        :rtype: StockRatingDto
        """
        return self._latest_rating

    @latest_rating.setter
    def latest_rating(self, latest_rating):
        """Sets the latest_rating of this StockInfoMasterDto.


        :param latest_rating: The latest_rating of this StockInfoMasterDto.  # noqa: E501
        :type: StockRatingDto
        """

        self._latest_rating = latest_rating

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
        if issubclass(StockInfoMasterDto, dict):
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
        if not isinstance(other, StockInfoMasterDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
