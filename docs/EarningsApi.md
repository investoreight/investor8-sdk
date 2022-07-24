# investor8_sdk.EarningsApi

All URIs are relative to *https://api.investoreight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_earnings_by_date**](EarningsApi.md#get_earnings_by_date) | **GET** /Earnings/by_date | 
[**get_historical_earnings**](EarningsApi.md#get_historical_earnings) | **GET** /Earnings/historical/{ticker} | 
[**get_recent_earnings**](EarningsApi.md#get_recent_earnings) | **GET** /Earnings/recent | 
[**get_today_earnings**](EarningsApi.md#get_today_earnings) | **GET** /Earnings/today | 
[**get_upcoming_earning**](EarningsApi.md#get_upcoming_earning) | **GET** /Earnings/upcoming/{ticker} | 
[**get_upcoming_earnings**](EarningsApi.md#get_upcoming_earnings) | **GET** /Earnings/upcoming/all | 

# **get_earnings_by_date**
> list[StockEarningDto] get_earnings_by_date(from_date=from_date, to_date=to_date, ticker=ticker)



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
api_instance = investor8_sdk.EarningsApi(investor8_sdk.ApiClient(configuration))
from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
ticker = 'ticker_example' # str |  (optional)

try:
    api_response = api_instance.get_earnings_by_date(from_date=from_date, to_date=to_date, ticker=ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EarningsApi->get_earnings_by_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_date** | **datetime**|  | [optional] 
 **to_date** | **datetime**|  | [optional] 
 **ticker** | **str**|  | [optional] 

### Return type

[**list[StockEarningDto]**](StockEarningDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_earnings**
> list[StockEarningDto] get_historical_earnings(ticker, size=size)



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
api_instance = investor8_sdk.EarningsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
size = 8 # int |  (optional) (default to 8)

try:
    api_response = api_instance.get_historical_earnings(ticker, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EarningsApi->get_historical_earnings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **size** | **int**|  | [optional] [default to 8]

### Return type

[**list[StockEarningDto]**](StockEarningDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_earnings**
> list[RecentEarningDto] get_recent_earnings(size=size, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.EarningsApi(investor8_sdk.ApiClient(configuration))
size = 300 # int |  (optional) (default to 300)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_recent_earnings(size=size, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EarningsApi->get_recent_earnings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**|  | [optional] [default to 300]
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[RecentEarningDto]**](RecentEarningDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_today_earnings**
> list[StockEarningDto] get_today_earnings()



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
api_instance = investor8_sdk.EarningsApi(investor8_sdk.ApiClient(configuration))

try:
    api_response = api_instance.get_today_earnings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EarningsApi->get_today_earnings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[StockEarningDto]**](StockEarningDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upcoming_earning**
> StockEarningDto get_upcoming_earning(ticker, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.EarningsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_upcoming_earning(ticker, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EarningsApi->get_upcoming_earning: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**StockEarningDto**](StockEarningDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upcoming_earnings**
> list[UpcomingEarningDto] get_upcoming_earnings(size=size, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.EarningsApi(investor8_sdk.ApiClient(configuration))
size = 300 # int |  (optional) (default to 300)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_upcoming_earnings(size=size, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EarningsApi->get_upcoming_earnings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**|  | [optional] [default to 300]
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[UpcomingEarningDto]**](UpcomingEarningDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

