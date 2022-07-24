# investor8_sdk.TagsApi

All URIs are relative to *https://api.investoreight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_tags_info**](TagsApi.md#get_all_tags_info) | **GET** /Tags/all/info | 
[**get_all_ticker_tags**](TagsApi.md#get_all_ticker_tags) | **GET** /Tags/all/ticker | 
[**get_tag_details**](TagsApi.md#get_tag_details) | **GET** /Tags/{tagId} | 

# **get_all_tags_info**
> dict(str, TagInfoDto) get_all_tags_info(refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.TagsApi(investor8_sdk.ApiClient(configuration))
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_tags_info(refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_all_tags_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**dict(str, TagInfoDto)**](TagInfoDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ticker_tags**
> dict(str, list[str]) get_all_ticker_tags(refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.TagsApi(investor8_sdk.ApiClient(configuration))
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_ticker_tags(refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_all_ticker_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

**dict(str, list[str])**

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_details**
> TagDetailsDto get_tag_details(tag_id, require_price=require_price)



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
api_instance = investor8_sdk.TagsApi(investor8_sdk.ApiClient(configuration))
tag_id = 'tag_id_example' # str | 
require_price = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_tag_details(tag_id, require_price=require_price)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tag_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**|  | 
 **require_price** | **bool**|  | [optional] [default to false]

### Return type

[**TagDetailsDto**](TagDetailsDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

