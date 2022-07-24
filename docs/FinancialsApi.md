# investor8_sdk.FinancialsApi

All URIs are relative to *https://api.investoreight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_latest_financials**](FinancialsApi.md#get_all_latest_financials) | **GET** /Financials/all/latest | 
[**get_dict_available_standardized_financials**](FinancialsApi.md#get_dict_available_standardized_financials) | **GET** /Financials/available/{ticker}/dict | 
[**get_financials_by_id**](FinancialsApi.md#get_financials_by_id) | **GET** /Financials/byid/{id} | 
[**get_financials_single**](FinancialsApi.md#get_financials_single) | **GET** /Financials/single | 
[**get_historical_financials**](FinancialsApi.md#get_historical_financials) | **GET** /Financials/historical/{ticker}/{size} | 
[**get_latest_financials**](FinancialsApi.md#get_latest_financials) | **GET** /Financials/latest/{ticker} | 
[**get_latest_standardized_financials**](FinancialsApi.md#get_latest_standardized_financials) | **GET** /Financials/std/latest/{ticker} | 
[**get_list_available_standardized_financials**](FinancialsApi.md#get_list_available_standardized_financials) | **GET** /Financials/available/{ticker}/list | 
[**get_list_standardized_financials**](FinancialsApi.md#get_list_standardized_financials) | **GET** /Financials/list/{ticker} | 

# **get_all_latest_financials**
> dict(str, LatestFinancialsDto) get_all_latest_financials(refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.FinancialsApi(investor8_sdk.ApiClient(configuration))
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_latest_financials(refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialsApi->get_all_latest_financials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**dict(str, LatestFinancialsDto)**](LatestFinancialsDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dict_available_standardized_financials**
> dict(str, dict(str, dict(str, list[str]))) get_dict_available_standardized_financials(ticker)



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
api_instance = investor8_sdk.FinancialsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 

try:
    api_response = api_instance.get_dict_available_standardized_financials(ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialsApi->get_dict_available_standardized_financials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

**dict(str, dict(str, dict(str, list[str])))**

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financials_by_id**
> StandardizedFinancial get_financials_by_id(id)



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
api_instance = investor8_sdk.FinancialsApi(investor8_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_financials_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialsApi->get_financials_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**StandardizedFinancial**](StandardizedFinancial.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financials_single**
> StandardizedFinancial get_financials_single(ticker=ticker, stat_code=stat_code, fiscal_period=fiscal_period, fiscal_year=fiscal_year, report_type=report_type)



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
api_instance = investor8_sdk.FinancialsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str |  (optional)
stat_code = 'stat_code_example' # str | Valid values are `balance_sheet_statement`, `income_statement`, `calculations`, `cash_flow_statement` (optional)
fiscal_period = 'fiscal_period_example' # str |  (optional)
fiscal_year = 'fiscal_year_example' # str |  (optional)
report_type = 'report_type_example' # str | Valid values are `reported`, `restated`, `calculated`, null (optional)

try:
    api_response = api_instance.get_financials_single(ticker=ticker, stat_code=stat_code, fiscal_period=fiscal_period, fiscal_year=fiscal_year, report_type=report_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialsApi->get_financials_single: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | [optional] 
 **stat_code** | **str**| Valid values are &#x60;balance_sheet_statement&#x60;, &#x60;income_statement&#x60;, &#x60;calculations&#x60;, &#x60;cash_flow_statement&#x60; | [optional] 
 **fiscal_period** | **str**|  | [optional] 
 **fiscal_year** | **str**|  | [optional] 
 **report_type** | **str**| Valid values are &#x60;reported&#x60;, &#x60;restated&#x60;, &#x60;calculated&#x60;, null | [optional] 

### Return type

[**StandardizedFinancial**](StandardizedFinancial.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_financials**
> list[StockFinancial] get_historical_financials(ticker, size, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.FinancialsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
size = 56 # int | 
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_historical_financials(ticker, size, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialsApi->get_historical_financials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **size** | **int**|  | 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**list[StockFinancial]**](StockFinancial.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_financials**
> StockFinancial get_latest_financials(ticker, refresh_cache=refresh_cache)



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
api_instance = investor8_sdk.FinancialsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_latest_financials(ticker, refresh_cache=refresh_cache)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialsApi->get_latest_financials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

[**StockFinancial**](StockFinancial.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_standardized_financials**
> dict(str, StandardizedFinancial) get_latest_standardized_financials(ticker, stat_code=stat_code)



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
api_instance = investor8_sdk.FinancialsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
stat_code = 'stat_code_example' # str | Valid values are `balance_sheet_statement`, `income_statement`, `calculations`, `cash_flow_statement` (optional)

try:
    api_response = api_instance.get_latest_standardized_financials(ticker, stat_code=stat_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialsApi->get_latest_standardized_financials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **stat_code** | **str**| Valid values are &#x60;balance_sheet_statement&#x60;, &#x60;income_statement&#x60;, &#x60;calculations&#x60;, &#x60;cash_flow_statement&#x60; | [optional] 

### Return type

[**dict(str, StandardizedFinancial)**](StandardizedFinancial.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_available_standardized_financials**
> list[FinancialReportDto] get_list_available_standardized_financials(ticker)



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
api_instance = investor8_sdk.FinancialsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 

try:
    api_response = api_instance.get_list_available_standardized_financials(ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialsApi->get_list_available_standardized_financials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**list[FinancialReportDto]**](FinancialReportDto.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_standardized_financials**
> list[StandardizedFinancial] get_list_standardized_financials(ticker, stat_code=stat_code, period_type=period_type, report_type=report_type, end_year=end_year, all_history=all_history)



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
api_instance = investor8_sdk.FinancialsApi(investor8_sdk.ApiClient(configuration))
ticker = 'ticker_example' # str | 
stat_code = 'stat_code_example' # str | Valid values are `balance_sheet_statement`, `income_statement`, `calculations`, `cash_flow_statement` (optional)
period_type = 'period_type_example' # str | Valid values for `balance_sheet_statement` are `Q` and `FY` and for others are `Q`, `FY`, `YTD`, `TTM` (optional)
report_type = 'report_type_example' # str | Valid values are `reported`, `restated`, `calculated`, `restatedFirst`, `reportedFirst` (optional)
end_year = 'end_year_example' # str |  (optional)
all_history = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_list_standardized_financials(ticker, stat_code=stat_code, period_type=period_type, report_type=report_type, end_year=end_year, all_history=all_history)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialsApi->get_list_standardized_financials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 
 **stat_code** | **str**| Valid values are &#x60;balance_sheet_statement&#x60;, &#x60;income_statement&#x60;, &#x60;calculations&#x60;, &#x60;cash_flow_statement&#x60; | [optional] 
 **period_type** | **str**| Valid values for &#x60;balance_sheet_statement&#x60; are &#x60;Q&#x60; and &#x60;FY&#x60; and for others are &#x60;Q&#x60;, &#x60;FY&#x60;, &#x60;YTD&#x60;, &#x60;TTM&#x60; | [optional] 
 **report_type** | **str**| Valid values are &#x60;reported&#x60;, &#x60;restated&#x60;, &#x60;calculated&#x60;, &#x60;restatedFirst&#x60;, &#x60;reportedFirst&#x60; | [optional] 
 **end_year** | **str**|  | [optional] 
 **all_history** | **bool**|  | [optional] [default to false]

### Return type

[**list[StandardizedFinancial]**](StandardizedFinancial.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerCoreAuth](../README.md#bearerCoreAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

