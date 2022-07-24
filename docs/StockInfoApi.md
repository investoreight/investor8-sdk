# investor8_sdk.StockInfoApi

All URIs are relative to *https://api.investoreight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_active_companies**](StockInfoApi.md#get_all_active_companies) | **GET** /StockInfo/companies/active | 
[**get_all_stock_info**](StockInfoApi.md#get_all_stock_info) | **GET** /StockInfo/all/{marketIndex} | 
[**get_all_stocks_popularity**](StockInfoApi.md#get_all_stocks_popularity) | **GET** /StockInfo/popularity/all | 
[**get_company_info**](StockInfoApi.md#get_company_info) | **GET** /StockInfo/companyinfo/{ticker} | 
[**get_latest_rating**](StockInfoApi.md#get_latest_rating) | **GET** /StockInfo/rating/latest/{ticker} | 
[**get_list_exchange_sector**](StockInfoApi.md#get_list_exchange_sector) | **GET** /StockInfo/list/exchangesector | 
[**get_stock_info**](StockInfoApi.md#get_stock_info) | **GET** /StockInfo/{ticker} | 
[**get_stock_info_list**](StockInfoApi.md#get_stock_info_list) | **GET** /StockInfo/list | 
[**get_stock_info_master**](StockInfoApi.md#get_stock_info_master) | **GET** /StockInfo/{ticker}/master | 
[**get_stock_info_multi**](StockInfoApi.md#get_stock_info_multi) | **GET** /StockInfo/multi | 
[**get_stock_summary**](StockInfoApi.md#get_stock_summary) | **GET** /StockInfo/{ticker}/summary | 
[**get_stock_summary_multi**](StockInfoApi.md#get_stock_summary_multi) | **GET** /StockInfo/summary | 
[**get_stocks_popularity**](StockInfoApi.md#get_stocks_popularity) | **GET** /StockInfo/popularity | 
[**get_stocks_popularity_by_sector**](StockInfoApi.md#get_stocks_popularity_by_sector) | **GET** /StockInfo/popularity/bysector | 
[**get_top_stocks_popularity**](StockInfoApi.md#get_top_stocks_popularity) | **GET** /StockInfo/popularity/top | 
[**get_trading_calendar**](StockInfoApi.md#get_trading_calendar) | **GET** /StockInfo/calendar | 
[**healthy_check**](StockInfoApi.md#healthy_check) | **GET** /health | 

# **get_all_active_companies**
> list[ActiveCompanyDto] get_all_active_companies(refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_active_companies(refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_all_active_companies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[ActiveCompanyDto]**](ActiveCompanyDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_stock_info**
> dict(str, StockInfoDto) get_all_stock_info(market_index, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))
market_index = 'market_index_example' # str | 
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_stock_info(market_index, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_all_stock_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_index** | **str**|  | 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**dict(str, StockInfoDto)**](StockInfoDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_stocks_popularity**
> list[StockPopularityDto] get_all_stocks_popularity(refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_stocks_popularity(refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_all_stocks_popularity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[StockPopularityDto]**](StockPopularityDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_info**
> CompanyInfoDto get_company_info(ticker)



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 

try:
    api_response = api_instance.get_company_info(ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_company_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**CompanyInfoDto**](CompanyInfoDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_rating**
> StockRatingDto get_latest_rating(ticker, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_latest_rating(ticker, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_latest_rating: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**StockRatingDto**](StockRatingDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_exchange_sector**
> ListExchangeSectorDto get_list_exchange_sector(refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_list_exchange_sector(refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_list_exchange_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**ListExchangeSectorDto**](ListExchangeSectorDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_info**
> StockInfoDto get_stock_info(ticker)



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 

try:
    api_response = api_instance.get_stock_info(ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_stock_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**StockInfoDto**](StockInfoDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_info_list**
> list[StockPriceDto] get_stock_info_list(page_index=page_index, page_size=page_size, exchange=exchange, sector=sector, market_index=market_index, is_active=is_active, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))
page_index = 0 # int |  (optional) (default to 0)
page_size = 20 # int |  (optional) (default to 20)
exchange = 'exchange_example' # str |  (optional)
sector = 'sector_example' # str |  (optional)
market_index = 'market_index_example' # str |  (optional)
is_active = true # bool |  (optional)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_stock_info_list(page_index=page_index, page_size=page_size, exchange=exchange, sector=sector, market_index=market_index, is_active=is_active, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_stock_info_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_index** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 20]
 **exchange** | **str**|  | [optional] 
 **sector** | **str**|  | [optional] 
 **market_index** | **str**|  | [optional] 
 **is_active** | **bool**|  | [optional] 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[StockPriceDto]**](StockPriceDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_info_master**
> StockInfoMasterDto get_stock_info_master(ticker, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_stock_info_master(ticker, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_stock_info_master: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**StockInfoMasterDto**](StockInfoMasterDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_info_multi**
> list[StockInfoDto] get_stock_info_multi(tickers=tickers)



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))
tickers = 'tickers_example' # str |  (optional)

try:
    api_response = api_instance.get_stock_info_multi(tickers=tickers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_stock_info_multi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tickers** | **str**|  | [optional] 

### Return type

[**list[StockInfoDto]**](StockInfoDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_summary**
> StockSummaryDto get_stock_summary(ticker, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_stock_summary(ticker, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_stock_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**StockSummaryDto**](StockSummaryDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_summary_multi**
> list[StockSummaryDto] get_stock_summary_multi(tickers=tickers, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))
tickers = 'tickers_example' # str |  (optional)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_stock_summary_multi(tickers=tickers, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_stock_summary_multi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tickers** | **str**|  | [optional] 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[StockSummaryDto]**](StockSummaryDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stocks_popularity**
> list[StockPopularityDto] get_stocks_popularity(tickers=tickers, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))
tickers = 'tickers_example' # str |  (optional)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_stocks_popularity(tickers=tickers, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_stocks_popularity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tickers** | **str**|  | [optional] 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[StockPopularityDto]**](StockPopularityDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stocks_popularity_by_sector**
> dict(str, list[StockPopularityDetailsDto]) get_stocks_popularity_by_sector(cutoff=cutoff, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))
cutoff = 56 # int |  (optional)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_stocks_popularity_by_sector(cutoff=cutoff, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_stocks_popularity_by_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cutoff** | **int**|  | [optional] 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

**dict(str, list[StockPopularityDetailsDto])**

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_stocks_popularity**
> list[StockPopularityDetailsDto] get_top_stocks_popularity(cutoff=cutoff, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))
cutoff = 56 # int |  (optional)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_top_stocks_popularity(cutoff=cutoff, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_top_stocks_popularity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cutoff** | **int**|  | [optional] 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[StockPopularityDetailsDto]**](StockPopularityDetailsDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trading_calendar**
> TradingCalendarDetailsDto get_trading_calendar()



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))

try:
    api_response = api_instance.get_trading_calendar()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->get_trading_calendar: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TradingCalendarDetailsDto**](TradingCalendarDetailsDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **healthy_check**
> bool healthy_check()



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
api_instance = investor8_sdk.StockInfoApi(investor8_sdk.ApiClient(configuration))

try:
    api_response = api_instance.healthy_check()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockInfoApi->healthy_check: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

