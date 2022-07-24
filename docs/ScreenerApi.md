# investor8_sdk.ScreenerApi

All URIs are relative to *https://api.investoreight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_sectors_returns**](ScreenerApi.md#get_all_sectors_returns) | **GET** /Screener/sectors/all_returns | 
[**get_all_sectors_returns_today_sa**](ScreenerApi.md#get_all_sectors_returns_today_sa) | **GET** /Screener/sa/sector/returns/today | 
[**get_dow_tickers**](ScreenerApi.md#get_dow_tickers) | **GET** /Screener/dow/tickers | 
[**get_list_ip_os**](ScreenerApi.md#get_list_ip_os) | **GET** /Screener/ipo/list | 
[**get_top_stocks**](ScreenerApi.md#get_top_stocks) | **GET** /Screener/top/{category} | 
[**get_upcoming_ipos**](ScreenerApi.md#get_upcoming_ipos) | **GET** /Screener/ipo/upcoming | 

# **get_all_sectors_returns**
> dict(str, list[SectorReturnsDto]) get_all_sectors_returns(period=period, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.ScreenerApi(investor8_sdk.ApiClient(configuration))
period = 56 # int |  (optional)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_sectors_returns(period=period, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenerApi->get_all_sectors_returns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **int**|  | [optional] 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

**dict(str, list[SectorReturnsDto])**

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_sectors_returns_today_sa**
> list[SASectorPriceDto] get_all_sectors_returns_today_sa()



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
api_instance = investor8_sdk.ScreenerApi(investor8_sdk.ApiClient(configuration))

try:
    api_response = api_instance.get_all_sectors_returns_today_sa()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenerApi->get_all_sectors_returns_today_sa: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SASectorPriceDto]**](SASectorPriceDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dow_tickers**
> list[str] get_dow_tickers(refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.ScreenerApi(investor8_sdk.ApiClient(configuration))
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_dow_tickers(refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenerApi->get_dow_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_ip_os**
> list[StockIpo] get_list_ip_os(status=status, page_index=page_index, page_size=page_size)



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
api_instance = investor8_sdk.ScreenerApi(investor8_sdk.ApiClient(configuration))
status = 'status_example' # str |  (optional)
page_index = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    api_response = api_instance.get_list_ip_os(status=status, page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenerApi->get_list_ip_os: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 
 **page_index** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**list[StockIpo]**](StockIpo.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_stocks**
> list[DetailedLatestPriceDto] get_top_stocks(category, _date=_date, sector=sector, count=count, exchange=exchange, index=index, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.ScreenerApi(investor8_sdk.ApiClient(configuration))
category = 'category_example' # str | 
_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
sector = 'all' # str |  (optional) (default to all)
count = 10 # int |  (optional) (default to 10)
exchange = 'exchange_example' # str |  (optional)
index = 'index_example' # str |  (optional)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_top_stocks(category, _date=_date, sector=sector, count=count, exchange=exchange, index=index, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenerApi->get_top_stocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | 
 **_date** | **datetime**|  | [optional] 
 **sector** | **str**|  | [optional] [default to all]
 **count** | **int**|  | [optional] [default to 10]
 **exchange** | **str**|  | [optional] 
 **index** | **str**|  | [optional] 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[DetailedLatestPriceDto]**](DetailedLatestPriceDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upcoming_ipos**
> list[StockIpo] get_upcoming_ipos(cutoff=cutoff, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.ScreenerApi(investor8_sdk.ApiClient(configuration))
cutoff = 5 # int |  (optional) (default to 5)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_upcoming_ipos(cutoff=cutoff, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenerApi->get_upcoming_ipos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cutoff** | **int**|  | [optional] [default to 5]
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[StockIpo]**](StockIpo.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

