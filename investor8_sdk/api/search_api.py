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


class SearchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search_stocks(self, query, size, **kwargs):  # noqa: E501
        """search_stocks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_stocks(query, size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: (required)
        :param int size: (required)
        :return: list[StockInfoDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_stocks_with_http_info(query, size, **kwargs)  # noqa: E501
        else:
            (data) = self.search_stocks_with_http_info(query, size, **kwargs)  # noqa: E501
            return data

    def search_stocks_with_http_info(self, query, size, **kwargs):  # noqa: E501
        """search_stocks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_stocks_with_http_info(query, size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: (required)
        :param int size: (required)
        :return: list[StockInfoDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_stocks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `search_stocks`")  # noqa: E501
        # verify the required parameter 'size' is set
        if ('size' not in params or
                params['size'] is None):
            raise ValueError("Missing the required parameter `size` when calling `search_stocks`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'query' in params:
            path_params['query'] = params['query']  # noqa: E501
        if 'size' in params:
            path_params['size'] = params['size']  # noqa: E501

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
            '/Search/{query}/{size}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[StockInfoDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
