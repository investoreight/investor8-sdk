# investor8_sdk.SettingsApi

All URIs are relative to *https://api.investoreight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_i8t_version**](SettingsApi.md#check_i8t_version) | **GET** /Settings/i8terminal/version/check/{version} | 
[**get_i8t_version**](SettingsApi.md#get_i8t_version) | **GET** /Settings/i8terminal/version | 
[**set_i8t_version**](SettingsApi.md#set_i8t_version) | **PUT** /Settings/i8terminal/version | 

# **check_i8t_version**
> I8TerminalCheckVersionDto check_i8t_version(version)



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
api_instance = investor8_sdk.SettingsApi(investor8_sdk.ApiClient(configuration))
version = 'version_example' # str | 

try:
    api_response = api_instance.check_i8t_version(version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->check_i8t_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 

### Return type

[**I8TerminalCheckVersionDto**](I8TerminalCheckVersionDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_i8t_version**
> I8TerminalVersionDto get_i8t_version()



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
api_instance = investor8_sdk.SettingsApi(investor8_sdk.ApiClient(configuration))

try:
    api_response = api_instance.get_i8t_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_i8t_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**I8TerminalVersionDto**](I8TerminalVersionDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_i8t_version**
> I8TerminalVersion set_i8t_version(body=body)



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
api_instance = investor8_sdk.SettingsApi(investor8_sdk.ApiClient(configuration))
body = investor8_sdk.I8TerminalVersionDto() # I8TerminalVersionDto |  (optional)

try:
    api_response = api_instance.set_i8t_version(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->set_i8t_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**I8TerminalVersionDto**](I8TerminalVersionDto.md)|  | [optional] 

### Return type

[**I8TerminalVersion**](I8TerminalVersion.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

