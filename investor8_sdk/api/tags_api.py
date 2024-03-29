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


class TagsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_tags_info(self, **kwargs):  # noqa: E501
        """get_all_tags_info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_tags_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool refresh_cache:
        :return: dict(str, TagInfoDto)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_tags_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_tags_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_tags_info_with_http_info(self, **kwargs):  # noqa: E501
        """get_all_tags_info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_tags_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool refresh_cache:
        :return: dict(str, TagInfoDto)
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
                    " to method get_all_tags_info" % key
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
            '/Tags/all/info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, TagInfoDto)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_ticker_tags(self, **kwargs):  # noqa: E501
        """get_all_ticker_tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_ticker_tags(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool refresh_cache:
        :return: dict(str, list[str])
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_ticker_tags_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_ticker_tags_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_ticker_tags_with_http_info(self, **kwargs):  # noqa: E501
        """get_all_ticker_tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_ticker_tags_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool refresh_cache:
        :return: dict(str, list[str])
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
                    " to method get_all_ticker_tags" % key
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
            '/Tags/all/ticker', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, list[str])',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tag_details(self, tag_id, **kwargs):  # noqa: E501
        """get_tag_details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tag_details(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag_id: (required)
        :param bool require_price:
        :return: TagDetailsDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tag_details_with_http_info(tag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tag_details_with_http_info(tag_id, **kwargs)  # noqa: E501
            return data

    def get_tag_details_with_http_info(self, tag_id, **kwargs):  # noqa: E501
        """get_tag_details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tag_details_with_http_info(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag_id: (required)
        :param bool require_price:
        :return: TagDetailsDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_id', 'require_price']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tag_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_id' is set
        if ('tag_id' not in params or
                params['tag_id'] is None):
            raise ValueError("Missing the required parameter `tag_id` when calling `get_tag_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag_id' in params:
            path_params['tagId'] = params['tag_id']  # noqa: E501

        query_params = []
        if 'require_price' in params:
            query_params.append(('requirePrice', params['require_price']))  # noqa: E501

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
            '/Tags/{tagId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagDetailsDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
