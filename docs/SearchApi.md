# investor8_sdk.SearchApi

All URIs are relative to *https://api.investoreight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_stocks**](SearchApi.md#search_stocks) | **GET** /Search/{query}/{size} | 

# **search_stocks**
> list[StockInfoDto] search_stocks(query, size)



### Example
```python
from __future__ import print_function
import time
import investor8_sdk
from investor8_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = investor8_sdk.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'
# Configure API key authorization: bearerCoreAuth
configuration = investor8_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = investor8_sdk.SearchApi(investor8_sdk.ApiClient(configuration))
query = 'query_example' # str | 
size = 56 # int | 

try:
    api_response = api_instance.search_stocks(query, size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_stocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **size** | **int**|  | 

### Return type

[**list[StockInfoDto]**](StockInfoDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

