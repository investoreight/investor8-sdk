# investor8_sdk.MetricsApi

All URIs are relative to *https://api.investoreight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aggregated_earning_returns**](MetricsApi.md#get_aggregated_earning_returns) | **GET** /Metrics/earning/{tk_fyq} | 
[**get_aggregated_earning_returns_by_ticker**](MetricsApi.md#get_aggregated_earning_returns_by_ticker) | **GET** /Metrics/earning/ticker/{ticker} | 
[**get_all_latest_daily_metrics**](MetricsApi.md#get_all_latest_daily_metrics) | **GET** /Metrics/daily/all/latest | 
[**get_all_latest_financial_metrics**](MetricsApi.md#get_all_latest_financial_metrics) | **GET** /Metrics/financial/all/latest | 
[**get_all_latest_value_metrics**](MetricsApi.md#get_all_latest_value_metrics) | **GET** /Metrics/value/all/latest | 
[**get_current_metrics**](MetricsApi.md#get_current_metrics) | **GET** /Metrics/current | 
[**get_current_metrics_0**](MetricsApi.md#get_current_metrics_0) | **GET** /Metrics/current/v2 | 
[**get_current_momentum**](MetricsApi.md#get_current_momentum) | **GET** /Metrics/momentum/current/{ticker} | 
[**get_distinct_metric_metadata_properties**](MetricsApi.md#get_distinct_metric_metadata_properties) | **GET** /Metrics/metadata/properties/distinct | 
[**get_historical_daily_metrics**](MetricsApi.md#get_historical_daily_metrics) | **GET** /Metrics/historical/daily/{ticker} | 
[**get_historical_growth_metrics**](MetricsApi.md#get_historical_growth_metrics) | **GET** /Metrics/growth/historical/{ticker} | 
[**get_historical_indicators**](MetricsApi.md#get_historical_indicators) | **GET** /Metrics/historical/indicators/{ticker} | 
[**get_historical_metrics**](MetricsApi.md#get_historical_metrics) | **GET** /Metrics/historical | 
[**get_historical_momentum**](MetricsApi.md#get_historical_momentum) | **GET** /Metrics/momentum/historical/{ticker} | 
[**get_historical_value**](MetricsApi.md#get_historical_value) | **GET** /Metrics/historical/value/{ticker} | 
[**get_latest_financials_period**](MetricsApi.md#get_latest_financials_period) | **GET** /Metrics/financials/latest/period | 
[**get_latest_growth_metrics**](MetricsApi.md#get_latest_growth_metrics) | **GET** /Metrics/growth/latest/{ticker} | 
[**get_list_financial_metrics_metadata**](MetricsApi.md#get_list_financial_metrics_metadata) | **GET** /Metrics/metadata/list/financials | 
[**get_list_metrics_metadata**](MetricsApi.md#get_list_metrics_metadata) | **GET** /Metrics/metadata/list | 
[**get_market_index_returns**](MetricsApi.md#get_market_index_returns) | **GET** /Metrics/merket/returns/{ticker} | 
[**get_metrics_metadata**](MetricsApi.md#get_metrics_metadata) | **GET** /Metrics/metadata/{name} | 
[**get_monthly_returns**](MetricsApi.md#get_monthly_returns) | **GET** /Metrics/returns/monthly/{ticker}/{sinceYear} | 
[**get_raw_historical_returns**](MetricsApi.md#get_raw_historical_returns) | **GET** /Metrics/earning/raw/historical/{ticker} | 
[**get_sector_returns**](MetricsApi.md#get_sector_returns) | **GET** /Metrics/sector/returns | 

# **get_aggregated_earning_returns**
> list[HistoricalReturn] get_aggregated_earning_returns(tk_fyq, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
tk_fyq = 'tk_fyq_example' # str | 
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_aggregated_earning_returns(tk_fyq, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_aggregated_earning_returns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tk_fyq** | **str**|  | 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[HistoricalReturn]**](HistoricalReturn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregated_earning_returns_by_ticker**
> list[HistoricalReturn] get_aggregated_earning_returns_by_ticker(ticker, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_aggregated_earning_returns_by_ticker(ticker, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_aggregated_earning_returns_by_ticker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[HistoricalReturn]**](HistoricalReturn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_latest_daily_metrics**
> dict(str, DailyMetricsDto) get_all_latest_daily_metrics(refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_latest_daily_metrics(refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_all_latest_daily_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**dict(str, DailyMetricsDto)**](DailyMetricsDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_latest_financial_metrics**
> dict(str, LatestFinancialMetricsDto) get_all_latest_financial_metrics(refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_latest_financial_metrics(refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_all_latest_financial_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**dict(str, LatestFinancialMetricsDto)**](LatestFinancialMetricsDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_latest_value_metrics**
> dict(str, ValueMetricsDto) get_all_latest_value_metrics(refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_latest_value_metrics(refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_all_latest_value_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**dict(str, ValueMetricsDto)**](ValueMetricsDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_metrics**
> SymbolsCurrentMetricsDto get_current_metrics(symbols=symbols, metrics=metrics, period_offset=period_offset)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
symbols = 'symbols_example' # str |  (optional)
metrics = 'metrics_example' # str |  (optional)
period_offset = 0 # int |  (optional) (default to 0)

try:
    api_response = api_instance.get_current_metrics(symbols=symbols, metrics=metrics, period_offset=period_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_current_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**|  | [optional] 
 **metrics** | **str**|  | [optional] 
 **period_offset** | **int**|  | [optional] [default to 0]

### Return type

[**SymbolsCurrentMetricsDto**](SymbolsCurrentMetricsDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_metrics_0**
> SymbolsCurrentMetricsDto get_current_metrics_0(symbols=symbols, metrics=metrics)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
symbols = 'symbols_example' # str |  (optional)
metrics = 'metrics_example' # str |  (optional)

try:
    api_response = api_instance.get_current_metrics_0(symbols=symbols, metrics=metrics)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_current_metrics_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**|  | [optional] 
 **metrics** | **str**|  | [optional] 

### Return type

[**SymbolsCurrentMetricsDto**](SymbolsCurrentMetricsDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_momentum**
> CurrentMomentumMetricsDto get_current_momentum(ticker, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_current_momentum(ticker, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_current_momentum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**CurrentMomentumMetricsDto**](CurrentMomentumMetricsDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distinct_metric_metadata_properties**
> MetadataPropertiesDto get_distinct_metric_metadata_properties()



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))

try:
    api_response = api_instance.get_distinct_metric_metadata_properties()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_distinct_metric_metadata_properties: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetadataPropertiesDto**](MetadataPropertiesDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_daily_metrics**
> list[HistoricalDailyMetricsDto] get_historical_daily_metrics(ticker, period=period, from_date=from_date, to_date=to_date)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
period = 56 # int |  (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.get_historical_daily_metrics(ticker, period=period, from_date=from_date, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_historical_daily_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **period** | **int**|  | [optional] 
 **from_date** | **datetime**|  | [optional] 
 **to_date** | **datetime**|  | [optional] 

### Return type

[**list[HistoricalDailyMetricsDto]**](HistoricalDailyMetricsDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_growth_metrics**
> HistoricalFinancialMetrics get_historical_growth_metrics(ticker, size=size, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
size = 8 # int |  (optional) (default to 8)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_historical_growth_metrics(ticker, size=size, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_historical_growth_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **size** | **int**|  | [optional] [default to 8]
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**HistoricalFinancialMetrics**](HistoricalFinancialMetrics.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_indicators**
> list[HistoricalIndicatorDto] get_historical_indicators(ticker, indicators=indicators, from_date=from_date, to_date=to_date)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
indicators = 'indicators_example' # str |  (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.get_historical_indicators(ticker, indicators=indicators, from_date=from_date, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_historical_indicators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **indicators** | **str**|  | [optional] 
 **from_date** | **datetime**|  | [optional] 
 **to_date** | **datetime**|  | [optional] 

### Return type

[**list[HistoricalIndicatorDto]**](HistoricalIndicatorDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_metrics**
> SymbolsHistoricalMetricsDto get_historical_metrics(symbols=symbols, metrics=metrics, from_period_offset=from_period_offset, to_period_offset=to_period_offset, from_date=from_date, to_date=to_date)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
symbols = 'symbols_example' # str |  (optional)
metrics = 'metrics_example' # str |  (optional)
from_period_offset = 56 # int |  (optional)
to_period_offset = 56 # int |  (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.get_historical_metrics(symbols=symbols, metrics=metrics, from_period_offset=from_period_offset, to_period_offset=to_period_offset, from_date=from_date, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_historical_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**|  | [optional] 
 **metrics** | **str**|  | [optional] 
 **from_period_offset** | **int**|  | [optional] 
 **to_period_offset** | **int**|  | [optional] 
 **from_date** | **datetime**|  | [optional] 
 **to_date** | **datetime**|  | [optional] 

### Return type

[**SymbolsHistoricalMetricsDto**](SymbolsHistoricalMetricsDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_momentum**
> list[MomentumMetricDto] get_historical_momentum(ticker, from_date=from_date, to_date=to_date, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_historical_momentum(ticker, from_date=from_date, to_date=to_date, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_historical_momentum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **from_date** | **datetime**|  | [optional] 
 **to_date** | **datetime**|  | [optional] 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[MomentumMetricDto]**](MomentumMetricDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_value**
> HistoricalValueMetrics get_historical_value(ticker)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 

try:
    api_response = api_instance.get_historical_value(ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_historical_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**HistoricalValueMetrics**](HistoricalValueMetrics.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_financials_period**
> dict(str, str) get_latest_financials_period(period_type=period_type, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
period_type = 'period_type_example' # str |  (optional)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_latest_financials_period(period_type=period_type, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_latest_financials_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period_type** | **str**|  | [optional] 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

**dict(str, str)**

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_growth_metrics**
> StockFinancialMetrics get_latest_growth_metrics(ticker, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_latest_growth_metrics(ticker, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_latest_growth_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**StockFinancialMetrics**](StockFinancialMetrics.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_financial_metrics_metadata**
> list[FinancialMetricMetadataDto] get_list_financial_metrics_metadata()



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))

try:
    api_response = api_instance.get_list_financial_metrics_metadata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_list_financial_metrics_metadata: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FinancialMetricMetadataDto]**](FinancialMetricMetadataDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_metrics_metadata**
> list[MetricsMetadata] get_list_metrics_metadata(category=category, type=type, display_format=display_format, data_format=data_format, name=name, page_index=page_index, page_size=page_size)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
category = 'category_example' # str |  (optional)
type = 'type_example' # str |  (optional)
display_format = 'display_format_example' # str |  (optional)
data_format = 'data_format_example' # str |  (optional)
name = 'name_example' # str |  (optional)
page_index = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)

try:
    api_response = api_instance.get_list_metrics_metadata(category=category, type=type, display_format=display_format, data_format=data_format, name=name, page_index=page_index, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_list_metrics_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **display_format** | **str**|  | [optional] 
 **data_format** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **page_index** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**list[MetricsMetadata]**](MetricsMetadata.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_index_returns**
> list[PeriodReturn] get_market_index_returns(ticker, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_market_index_returns(ticker, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_market_index_returns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[PeriodReturn]**](PeriodReturn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics_metadata**
> MetricsMetadata get_metrics_metadata(name)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.get_metrics_metadata(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_metrics_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**MetricsMetadata**](MetricsMetadata.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monthly_returns**
> list[MonthlyMetrics] get_monthly_returns(ticker, since_year)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
since_year = 56 # int | 

try:
    api_response = api_instance.get_monthly_returns(ticker, since_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_monthly_returns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **since_year** | **int**|  | 

### Return type

[**list[MonthlyMetrics]**](MonthlyMetrics.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_historical_returns**
> list[HistoricalReturnsDto] get_raw_historical_returns(ticker, size=size)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
size = 10 # int |  (optional) (default to 10)

try:
    api_response = api_instance.get_raw_historical_returns(ticker, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_raw_historical_returns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **size** | **int**|  | [optional] [default to 10]

### Return type

[**list[HistoricalReturnsDto]**](HistoricalReturnsDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sector_returns**
> list[PeriodReturn] get_sector_returns(sector=sector, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.MetricsApi(investor8_sdk.ApiClient(configuration))
sector = 'sector_example' # str |  (optional)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_sector_returns(sector=sector, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_sector_returns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sector** | **str**|  | [optional] 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[PeriodReturn]**](PeriodReturn.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

