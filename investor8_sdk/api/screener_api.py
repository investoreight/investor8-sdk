# coding: utf-8

"""
    Investoreight Core API

    Investoreight API Documentation:  https://api.investoreight.com/api-docs/index.html  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: info@investoreight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from investor8_sdk.api_client import ApiClient


class ScreenerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_sectors_returns(self, **kwargs):  # noqa: E501
        """get_all_sectors_returns  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_sectors_returns(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int period:
        :param bool refresh_cache:
        :return: dict(str, list[SectorReturnsDto])
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_sectors_returns_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_sectors_returns_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_sectors_returns_with_http_info(self, **kwargs):  # noqa: E501
        """get_all_sectors_returns  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_sectors_returns_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int period:
        :param bool refresh_cache:
        :return: dict(str, list[SectorReturnsDto])
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['period', 'refresh_cache']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_sectors_returns" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if 'refresh_cache' in params:
            query_params.append(('refreshCache', params['refresh_cache']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'bearerCoreAuth']  # noqa: E501

        return self.api_client.call_api(
            '/Screener/sectors/all_returns', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, list[SectorReturnsDto])',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_sectors_returns_today_sa(self, **kwargs):  # noqa: E501
        """get_all_sectors_returns_today_sa  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_sectors_returns_today_sa(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[SASectorPriceDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_sectors_returns_today_sa_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_sectors_returns_today_sa_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_sectors_returns_today_sa_with_http_info(self, **kwargs):  # noqa: E501
        """get_all_sectors_returns_today_sa  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_sectors_returns_today_sa_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[SASectorPriceDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_sectors_returns_today_sa" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'bearerCoreAuth']  # noqa: E501

        return self.api_client.call_api(
            '/Screener/sa/sector/returns/today', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SASectorPriceDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dow_tickers(self, **kwargs):  # noqa: E501
        """get_dow_tickers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dow_tickers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool refresh_cache:
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dow_tickers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_dow_tickers_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_dow_tickers_with_http_info(self, **kwargs):  # noqa: E501
        """get_dow_tickers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dow_tickers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool refresh_cache:
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['refresh_cache']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dow_tickers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'refresh_cache' in params:
            query_params.append(('refreshCache', params['refresh_cache']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'bearerCoreAuth']  # noqa: E501

        return self.api_client.call_api(
            '/Screener/dow/tickers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_list_ip_os(self, **kwargs):  # noqa: E501
        """get_list_ip_os  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list_ip_os(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status:
        :param int page_index:
        :param int page_size:
        :return: list[StockIpo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_list_ip_os_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_list_ip_os_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_list_ip_os_with_http_info(self, **kwargs):  # noqa: E501
        """get_list_ip_os  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_list_ip_os_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status:
        :param int page_index:
        :param int page_size:
        :return: list[StockIpo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status', 'page_index', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_list_ip_os" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'page_index' in params:
            query_params.append(('pageIndex', params['page_index']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'bearerCoreAuth']  # noqa: E501

        return self.api_client.call_api(
            '/Screener/ipo/list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[StockIpo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_top_stocks(self, category, **kwargs):  # noqa: E501
        """get_top_stocks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_top_stocks(category, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str category: (required)
        :param datetime _date:
        :param str sector:
        :param int count:
        :param str exchange:
        :param str index:
        :param bool refresh_cache:
        :return: list[DetailedLatestPriceDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_top_stocks_with_http_info(category, **kwargs)  # noqa: E501
        else:
            (data) = self.get_top_stocks_with_http_info(category, **kwargs)  # noqa: E501
            return data

    def get_top_stocks_with_http_info(self, category, **kwargs):  # noqa: E501
        """get_top_stocks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_top_stocks_with_http_info(category, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str category: (required)
        :param datetime _date:
        :param str sector:
        :param int count:
        :param str exchange:
        :param str index:
        :param bool refresh_cache:
        :return: list[DetailedLatestPriceDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category', '_date', 'sector', 'count', 'exchange', 'index', 'refresh_cache']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_top_stocks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category' is set
        if ('category' not in params or
                params['category'] is None):
            raise ValueError("Missing the required parameter `category` when calling `get_top_stocks`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'category' in params:
            path_params['category'] = params['category']  # noqa: E501

        query_params = []
        if '_date' in params:
            query_params.append(('date', params['_date']))  # noqa: E501
        if 'sector' in params:
            query_params.append(('sector', params['sector']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'exchange' in params:
            query_params.append(('exchange', params['exchange']))  # noqa: E501
        if 'index' in params:
            query_params.append(('index', params['index']))  # noqa: E501
        if 'refresh_cache' in params:
            query_params.append(('refreshCache', params['refresh_cache']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'bearerCoreAuth']  # noqa: E501

        return self.api_client.call_api(
            '/Screener/top/{category}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DetailedLatestPriceDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_upcoming_ipos(self, **kwargs):  # noqa: E501
        """get_upcoming_ipos  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_upcoming_ipos(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int cutoff:
        :param bool refresh_cache:
        :return: list[StockIpo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_upcoming_ipos_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_upcoming_ipos_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_upcoming_ipos_with_http_info(self, **kwargs):  # noqa: E501
        """get_upcoming_ipos  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_upcoming_ipos_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int cutoff:
        :param bool refresh_cache:
        :return: list[StockIpo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cutoff', 'refresh_cache']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_upcoming_ipos" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cutoff' in params:
            query_params.append(('cutoff', params['cutoff']))  # noqa: E501
        if 'refresh_cache' in params:
            query_params.append(('refreshCache', params['refresh_cache']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'bearerCoreAuth']  # noqa: E501

        return self.api_client.call_api(
            '/Screener/ipo/upcoming', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[StockIpo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search(self, **kwargs):  # noqa: E501
        """search  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str conditions:
        :param str order_by:
        :param str order_direction:
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_with_http_info(self, **kwargs):  # noqa: E501
        """search  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str conditions:
        :param str order_by:
        :param str order_direction:
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conditions', 'order_by', 'order_direction']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conditions' in params:
            query_params.append(('conditions', params['conditions']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501
        if 'order_direction' in params:
            query_params.append(('orderDirection', params['order_direction']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'bearerCoreAuth']  # noqa: E501

        return self.api_client.call_api(
            '/Screener/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
