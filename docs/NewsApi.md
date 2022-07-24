# investor8_sdk.NewsApi

All URIs are relative to *https://api.investoreight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](NewsApi.md#get) | **GET** /News/{id} | 
[**get_aggregated_ticker_news**](NewsApi.md#get_aggregated_ticker_news) | **GET** /News/aggregated/{ticker} | 
[**get_all_sectors_news**](NewsApi.md#get_all_sectors_news) | **GET** /News/sector/all/{size} | 
[**get_latest_highlight_news**](NewsApi.md#get_latest_highlight_news) | **GET** /News/highlight/latest | 
[**get_latest_news**](NewsApi.md#get_latest_news) | **GET** /News/latest | 
[**get_list_highlights_by_id**](NewsApi.md#get_list_highlights_by_id) | **GET** /News/highlight/list/byid | 
[**get_market_highlight**](NewsApi.md#get_market_highlight) | **GET** /News/highlight/{id} | 
[**get_market_highlights**](NewsApi.md#get_market_highlights) | **GET** /News/highlight/list | 
[**get_news_by_category**](NewsApi.md#get_news_by_category) | **GET** /News/list/{category} | 
[**get_news_by_sector**](NewsApi.md#get_news_by_sector) | **GET** /News/sector/{sector} | 
[**get_news_categories**](NewsApi.md#get_news_categories) | **GET** /News/categories | 
[**get_news_list**](NewsApi.md#get_news_list) | **GET** /News/list/filter | 
[**get_ticker_news**](NewsApi.md#get_ticker_news) | **GET** /News/stock/{ticker} | 
[**get_tickers_with_news**](NewsApi.md#get_tickers_with_news) | **GET** /News/tickers | 
[**get_top_news**](NewsApi.md#get_top_news) | **GET** /News/list/top | 

# **get**
> StockNewsDetails get(id)



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
api_instance = investor8_sdk.NewsApi(investor8_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**StockNewsDetails**](StockNewsDetails.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregated_ticker_news**
> list[StockNews] get_aggregated_ticker_news(ticker, page_index=page_index, page_size=page_size)



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
api_instance = investor8_sdk.NewsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
page_index = 0 # int |  (optional) (default to 0)
page_size = 20 # int |  (optional) (default to 20)

try:
    api_response = api_instance.get_aggregated_ticker_news(ticker, page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_aggregated_ticker_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **page_index** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 20]

### Return type

[**list[StockNews]**](StockNews.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_sectors_news**
> dict(str, list[StockNews]) get_all_sectors_news(size, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.NewsApi(investor8_sdk.ApiClient(configuration))
size = 56 # int | 
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_sectors_news(size, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_all_sectors_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**|  | 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

**dict(str, list[StockNews])**

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_highlight_news**
> StockNews get_latest_highlight_news()



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
api_instance = investor8_sdk.NewsApi(investor8_sdk.ApiClient(configuration))

try:
    api_response = api_instance.get_latest_highlight_news()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_latest_highlight_news: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StockNews**](StockNews.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_news**
> list[StockNews] get_latest_news(page_index=page_index, page_size=page_size, has_alert_filter=has_alert_filter)



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
api_instance = investor8_sdk.NewsApi(investor8_sdk.ApiClient(configuration))
page_index = 0 # int |  (optional) (default to 0)
page_size = 20 # int |  (optional) (default to 20)
has_alert_filter = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_latest_news(page_index=page_index, page_size=page_size, has_alert_filter=has_alert_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_latest_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_index** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 20]
 **has_alert_filter** | **bool**|  | [optional] [default to false]

### Return type

[**list[StockNews]**](StockNews.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_highlights_by_id**
> list[MarketHighlightDto] get_list_highlights_by_id(highlight_ids=highlight_ids)



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
api_instance = investor8_sdk.NewsApi(investor8_sdk.ApiClient(configuration))
highlight_ids = 'highlight_ids_example' # str |  (optional)

try:
    api_response = api_instance.get_list_highlights_by_id(highlight_ids=highlight_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_list_highlights_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **highlight_ids** | **str**|  | [optional] 

### Return type

[**list[MarketHighlightDto]**](MarketHighlightDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_highlight**
> MarketHighlightDto get_market_highlight(id)



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
api_instance = investor8_sdk.NewsApi(investor8_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_market_highlight(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_market_highlight: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**MarketHighlightDto**](MarketHighlightDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_highlights**
> list[MarketHighlightDto] get_market_highlights(_date=_date, page_index=page_index, page_size=page_size, status=status)



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
api_instance = investor8_sdk.NewsApi(investor8_sdk.ApiClient(configuration))
_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page_index = 0 # int |  (optional) (default to 0)
page_size = 20 # int |  (optional) (default to 20)
status = 56 # int |  (optional)

try:
    api_response = api_instance.get_market_highlights(_date=_date, page_index=page_index, page_size=page_size, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_market_highlights: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **datetime**|  | [optional] 
 **page_index** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 20]
 **status** | **int**|  | [optional] 

### Return type

[**list[MarketHighlightDto]**](MarketHighlightDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_news_by_category**
> list[StockNews] get_news_by_category(category, page_index=page_index, page_size=page_size)



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
api_instance = investor8_sdk.NewsApi(investor8_sdk.ApiClient(configuration))
category = 'category_example' # str | 
page_index = 0 # int |  (optional) (default to 0)
page_size = 20 # int |  (optional) (default to 20)

try:
    api_response = api_instance.get_news_by_category(category, page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_news_by_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | 
 **page_index** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 20]

### Return type

[**list[StockNews]**](StockNews.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_news_by_sector**
> list[StockNews] get_news_by_sector(sector, page_index=page_index, page_size=page_size, include_highlight=include_highlight)



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
api_instance = investor8_sdk.NewsApi(investor8_sdk.ApiClient(configuration))
sector = 'sector_example' # str | 
page_index = 0 # int |  (optional) (default to 0)
page_size = 20 # int |  (optional) (default to 20)
include_highlight = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_news_by_sector(sector, page_index=page_index, page_size=page_size, include_highlight=include_highlight)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_news_by_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sector** | **str**|  | 
 **page_index** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 20]
 **include_highlight** | **bool**|  | [optional] [default to true]

### Return type

[**list[StockNews]**](StockNews.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_news_categories**
> NewsCategoriesDto get_news_categories()



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
api_instance = investor8_sdk.NewsApi(investor8_sdk.ApiClient(configuration))

try:
    api_response = api_instance.get_news_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_news_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NewsCategoriesDto**](NewsCategoriesDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_news_list**
> list[StockNews] get_news_list(category_coarse=category_coarse, tickers=tickers, source=source, status=status, sector=sector, page_index=page_index, page_size=page_size, include_highlight=include_highlight, order=order)



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
api_instance = investor8_sdk.NewsApi(investor8_sdk.ApiClient(configuration))
category_coarse = 'category_coarse_example' # str |  (optional)
tickers = 'tickers_example' # str |  (optional)
source = investor8_sdk.NewsSource() # NewsSource |  (optional)
status = investor8_sdk.StockNewsStatus() # StockNewsStatus |  (optional)
sector = 'sector_example' # str |  (optional)
page_index = 0 # int |  (optional) (default to 0)
page_size = 20 # int |  (optional) (default to 20)
include_highlight = true # bool |  (optional) (default to true)
order = 'PublicationTimestamp' # str |  (optional) (default to PublicationTimestamp)

try:
    api_response = api_instance.get_news_list(category_coarse=category_coarse, tickers=tickers, source=source, status=status, sector=sector, page_index=page_index, page_size=page_size, include_highlight=include_highlight, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_news_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_coarse** | **str**|  | [optional] 
 **tickers** | **str**|  | [optional] 
 **source** | [**NewsSource**](.md)|  | [optional] 
 **status** | [**StockNewsStatus**](.md)|  | [optional] 
 **sector** | **str**|  | [optional] 
 **page_index** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 20]
 **include_highlight** | **bool**|  | [optional] [default to true]
 **order** | **str**|  | [optional] [default to PublicationTimestamp]

### Return type

[**list[StockNews]**](StockNews.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ticker_news**
> list[StockNews] get_ticker_news(ticker, page_index=page_index, page_size=page_size)



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
api_instance = investor8_sdk.NewsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
page_index = 0 # int |  (optional) (default to 0)
page_size = 20 # int |  (optional) (default to 20)

try:
    api_response = api_instance.get_ticker_news(ticker, page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_ticker_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **page_index** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 20]

### Return type

[**list[StockNews]**](StockNews.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tickers_with_news**
> list[str] get_tickers_with_news()



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
api_instance = investor8_sdk.NewsApi(investor8_sdk.ApiClient(configuration))

try:
    api_response = api_instance.get_tickers_with_news()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_tickers_with_news: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_news**
> list[StockNews] get_top_news(category_coarse=category_coarse, sector=sector, size=size, has_alert_filter=has_alert_filter)



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
api_instance = investor8_sdk.NewsApi(investor8_sdk.ApiClient(configuration))
category_coarse = 'category_coarse_example' # str |  (optional)
sector = 'sector_example' # str |  (optional)
size = 20 # int |  (optional) (default to 20)
has_alert_filter = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_top_news(category_coarse=category_coarse, sector=sector, size=size, has_alert_filter=has_alert_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_top_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_coarse** | **str**|  | [optional] 
 **sector** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 20]
 **has_alert_filter** | **bool**|  | [optional] [default to false]

### Return type

[**list[StockNews]**](StockNews.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

