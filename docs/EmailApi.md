# investor8_sdk.EmailApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedule_email**](EmailApi.md#schedule_email) | **POST** /Email/schedule | 
[**send_email**](EmailApi.md#send_email) | **POST** /Email/send | 

# **schedule_email**
> schedule_email(body=body)



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
api_instance = investor8_sdk.EmailApi(investor8_sdk.ApiClient(configuration))
body = investor8_sdk.SendEmailDto() # SendEmailDto |  (optional)

try:
    api_instance.schedule_email(body=body)
except ApiException as e:
    print("Exception when calling EmailApi->schedule_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendEmailDto**](SendEmailDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email**
> send_email(body=body)



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
api_instance = investor8_sdk.EmailApi(investor8_sdk.ApiClient(configuration))
body = investor8_sdk.SendEmailDto() # SendEmailDto |  (optional)

try:
    api_instance.send_email(body=body)
except ApiException as e:
    print("Exception when calling EmailApi->send_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendEmailDto**](SendEmailDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

