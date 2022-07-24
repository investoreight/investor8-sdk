# investor8_sdk.PriceApi

All URIs are relative to *https://api.investoreight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_latest_prices**](PriceApi.md#get_all_latest_prices) | **GET** /Price/latest/all | 
[**get_all_previous_closes**](PriceApi.md#get_all_previous_closes) | **GET** /Price/close/all | 
[**get_historical_prices**](PriceApi.md#get_historical_prices) | **GET** /Price/historical | 
[**get_latest_market_indices**](PriceApi.md#get_latest_market_indices) | **GET** /Price/latest/market_indices | 
[**get_latest_price**](PriceApi.md#get_latest_price) | **POST** /Price/latest | 
[**get_today_intraday_prices**](PriceApi.md#get_today_intraday_prices) | **GET** /Price/intraday/today | 

# **get_all_latest_prices**
> dict(str, LatestPriceDto) get_all_latest_prices(refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.PriceApi(investor8_sdk.ApiClient(configuration))
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_latest_prices(refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceApi->get_all_latest_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**dict(str, LatestPriceDto)**](LatestPriceDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_previous_closes**
> PreviousCloseDto get_all_previous_closes(refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.PriceApi(investor8_sdk.ApiClient(configuration))
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_previous_closes(refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceApi->get_all_previous_closes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**PreviousCloseDto**](PreviousCloseDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_prices**
> list[StockPrice] get_historical_prices(ticker=ticker, period=period, throttle=throttle, from_date=from_date, to_date=to_date, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.PriceApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str |  (optional)
period = 56 # int |  (optional)
throttle = true # bool |  (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_historical_prices(ticker=ticker, period=period, throttle=throttle, from_date=from_date, to_date=to_date, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceApi->get_historical_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | [optional] 
 **period** | **int**|  | [optional] 
 **throttle** | **bool**|  | [optional] 
 **from_date** | **datetime**|  | [optional] 
 **to_date** | **datetime**|  | [optional] 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[StockPrice]**](StockPrice.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_market_indices**
> dict(str, LatestPriceDto) get_latest_market_indices()



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
api_instance = investor8_sdk.PriceApi(investor8_sdk.ApiClient(configuration))

try:
    api_response = api_instance.get_latest_market_indices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceApi->get_latest_market_indices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, LatestPriceDto)**](LatestPriceDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_price**
> list[LatestPriceDto] get_latest_price(body=body)



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
api_instance = investor8_sdk.PriceApi(investor8_sdk.ApiClient(configuration))
body = ['body_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_latest_price(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceApi->get_latest_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**list[LatestPriceDto]**](LatestPriceDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_today_intraday_prices**
> dict(str, list[LatestPriceDto]) get_today_intraday_prices(tickers=tickers, size=size)



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
api_instance = investor8_sdk.PriceApi(investor8_sdk.ApiClient(configuration))
tickers = 'tickers_example' # str |  (optional)
size = 10 # int |  (optional) (default to 10)

try:
    api_response = api_instance.get_today_intraday_prices(tickers=tickers, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PriceApi->get_today_intraday_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tickers** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 10]

### Return type

**dict(str, list[LatestPriceDto])**

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

