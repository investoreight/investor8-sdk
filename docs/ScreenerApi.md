# investor8_sdk.ScreenerApi

All URIs are relative to *https://api.investoreight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_sectors_returns**](ScreenerApi.md#get_all_sectors_returns) | **GET** /Screener/sectors/all_returns | 
[**get_all_sectors_returns_today_sa**](ScreenerApi.md#get_all_sectors_returns_today_sa) | **GET** /Screener/sa/sector/returns/today | 
[**get_dow_tickers**](ScreenerApi.md#get_dow_tickers) | **GET** /Screener/dow/tickers | 
[**get_list_ip_os**](ScreenerApi.md#get_list_ip_os) | **GET** /Screener/ipo/list | 
[**get_list_screening_profiles**](ScreenerApi.md#get_list_screening_profiles) | **GET** /Screener/profile/list | 
[**get_screening_profile**](ScreenerApi.md#get_screening_profile) | **GET** /Screener/profile/{id} | 
[**get_screening_profile_by_name**](ScreenerApi.md#get_screening_profile_by_name) | **GET** /Screener/profile/name/{name} | 
[**get_top_stocks**](ScreenerApi.md#get_top_stocks) | **GET** /Screener/top/{category} | 
[**get_upcoming_ipos**](ScreenerApi.md#get_upcoming_ipos) | **GET** /Screener/ipo/upcoming | 
[**search**](ScreenerApi.md#search) | **GET** /Screener/search | 

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

# **get_list_screening_profiles**
> list[GetListScreeningProfilesDto] get_list_screening_profiles()



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
    api_response = api_instance.get_list_screening_profiles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenerApi->get_list_screening_profiles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetListScreeningProfilesDto]**](GetListScreeningProfilesDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screening_profile**
> GetScreeningProfileDto get_screening_profile(id)



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
id = 'id_example' # str | 

try:
    api_response = api_instance.get_screening_profile(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenerApi->get_screening_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GetScreeningProfileDto**](GetScreeningProfileDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screening_profile_by_name**
> GetScreeningProfileDto get_screening_profile_by_name(name)



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
name = 'name_example' # str | 

try:
    api_response = api_instance.get_screening_profile_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenerApi->get_screening_profile_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**GetScreeningProfileDto**](GetScreeningProfileDto.md)

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

# **search**
> list[str] search(conditions=conditions, order_by=order_by, order_direction=order_direction)



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
conditions = 'conditions_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)
order_direction = 'desc' # str |  (optional) (default to desc)

try:
    api_response = api_instance.search(conditions=conditions, order_by=order_by, order_direction=order_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreenerApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conditions** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **order_direction** | **str**|  | [optional] [default to desc]

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

