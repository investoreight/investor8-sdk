# investor8-sdk
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.1
- Package version: 1.1.56
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://www.investoreight.com](https://www.investoreight.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/investoreight/investor8-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/investoreight/investor8-sdk.git`)

Then import the package:
```python
import investor8_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import investor8_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.investoreight.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EarningsApi* | [**get_earnings_by_date**](docs/EarningsApi.md#get_earnings_by_date) | **GET** /Earnings/by_date | 
*EarningsApi* | [**get_historical_earnings**](docs/EarningsApi.md#get_historical_earnings) | **GET** /Earnings/historical/{ticker} | 
*EarningsApi* | [**get_recent_earnings**](docs/EarningsApi.md#get_recent_earnings) | **GET** /Earnings/recent | 
*EarningsApi* | [**get_today_earnings**](docs/EarningsApi.md#get_today_earnings) | **GET** /Earnings/today | 
*EarningsApi* | [**get_upcoming_earning**](docs/EarningsApi.md#get_upcoming_earning) | **GET** /Earnings/upcoming/{ticker} | 
*EarningsApi* | [**get_upcoming_earnings**](docs/EarningsApi.md#get_upcoming_earnings) | **GET** /Earnings/upcoming/all | 
*FinancialsApi* | [**get_all_latest_financials**](docs/FinancialsApi.md#get_all_latest_financials) | **GET** /Financials/all/latest | 
*FinancialsApi* | [**get_dict_available_standardized_financials**](docs/FinancialsApi.md#get_dict_available_standardized_financials) | **GET** /Financials/available/{ticker}/dict | 
*FinancialsApi* | [**get_financials_by_id**](docs/FinancialsApi.md#get_financials_by_id) | **GET** /Financials/byid/{id} | 
*FinancialsApi* | [**get_financials_single**](docs/FinancialsApi.md#get_financials_single) | **GET** /Financials/single | 
*FinancialsApi* | [**get_historical_financials**](docs/FinancialsApi.md#get_historical_financials) | **GET** /Financials/historical/{ticker}/{size} | 
*FinancialsApi* | [**get_latest_financials**](docs/FinancialsApi.md#get_latest_financials) | **GET** /Financials/latest/{ticker} | 
*FinancialsApi* | [**get_latest_standardized_financials**](docs/FinancialsApi.md#get_latest_standardized_financials) | **GET** /Financials/std/latest/{ticker} | 
*FinancialsApi* | [**get_list_available_standardized_financials**](docs/FinancialsApi.md#get_list_available_standardized_financials) | **GET** /Financials/available/{ticker}/list | 
*FinancialsApi* | [**get_list_standardized_financials**](docs/FinancialsApi.md#get_list_standardized_financials) | **GET** /Financials/list/{ticker} | 
*MetricsApi* | [**get_aggregated_earning_returns**](docs/MetricsApi.md#get_aggregated_earning_returns) | **GET** /Metrics/earning/{tk_fyq} | 
*MetricsApi* | [**get_aggregated_earning_returns_by_ticker**](docs/MetricsApi.md#get_aggregated_earning_returns_by_ticker) | **GET** /Metrics/earning/ticker/{ticker} | 
*MetricsApi* | [**get_all_latest_daily_metrics**](docs/MetricsApi.md#get_all_latest_daily_metrics) | **GET** /Metrics/daily/all/latest | 
*MetricsApi* | [**get_all_latest_financial_metrics**](docs/MetricsApi.md#get_all_latest_financial_metrics) | **GET** /Metrics/financial/all/latest | 
*MetricsApi* | [**get_all_latest_value_metrics**](docs/MetricsApi.md#get_all_latest_value_metrics) | **GET** /Metrics/value/all/latest | 
*MetricsApi* | [**get_current_metrics**](docs/MetricsApi.md#get_current_metrics) | **GET** /Metrics/current | 
*MetricsApi* | [**get_current_momentum**](docs/MetricsApi.md#get_current_momentum) | **GET** /Metrics/momentum/current/{ticker} | 
*MetricsApi* | [**get_distinct_metric_metadata_properties**](docs/MetricsApi.md#get_distinct_metric_metadata_properties) | **GET** /Metrics/metadata/properties/distinct | 
*MetricsApi* | [**get_distinct_metric_metadata_screening_conditions**](docs/MetricsApi.md#get_distinct_metric_metadata_screening_conditions) | **GET** /Metrics/metadata/screeningconditions/distinct | 
*MetricsApi* | [**get_historical_daily_metrics**](docs/MetricsApi.md#get_historical_daily_metrics) | **GET** /Metrics/historical/daily/{ticker} | 
*MetricsApi* | [**get_historical_growth_metrics**](docs/MetricsApi.md#get_historical_growth_metrics) | **GET** /Metrics/growth/historical/{ticker} | 
*MetricsApi* | [**get_historical_indicators**](docs/MetricsApi.md#get_historical_indicators) | **GET** /Metrics/historical/indicators/{ticker} | 
*MetricsApi* | [**get_historical_metrics**](docs/MetricsApi.md#get_historical_metrics) | **GET** /Metrics/historical | 
*MetricsApi* | [**get_historical_momentum**](docs/MetricsApi.md#get_historical_momentum) | **GET** /Metrics/momentum/historical/{ticker} | 
*MetricsApi* | [**get_historical_value**](docs/MetricsApi.md#get_historical_value) | **GET** /Metrics/historical/value/{ticker} | 
*MetricsApi* | [**get_latest_financials_period**](docs/MetricsApi.md#get_latest_financials_period) | **GET** /Metrics/financials/latest/period | 
*MetricsApi* | [**get_latest_growth_metrics**](docs/MetricsApi.md#get_latest_growth_metrics) | **GET** /Metrics/growth/latest/{ticker} | 
*MetricsApi* | [**get_list_financial_metrics_metadata**](docs/MetricsApi.md#get_list_financial_metrics_metadata) | **GET** /Metrics/metadata/list/financials | 
*MetricsApi* | [**get_list_metrics_metadata**](docs/MetricsApi.md#get_list_metrics_metadata) | **GET** /Metrics/metadata/list | 
*MetricsApi* | [**get_market_index_returns**](docs/MetricsApi.md#get_market_index_returns) | **GET** /Metrics/merket/returns/{ticker} | 
*MetricsApi* | [**get_metrics_metadata**](docs/MetricsApi.md#get_metrics_metadata) | **GET** /Metrics/metadata/{name} | 
*MetricsApi* | [**get_monthly_returns**](docs/MetricsApi.md#get_monthly_returns) | **GET** /Metrics/returns/monthly/{ticker}/{sinceYear} | 
*MetricsApi* | [**get_raw_historical_returns**](docs/MetricsApi.md#get_raw_historical_returns) | **GET** /Metrics/earning/raw/historical/{ticker} | 
*MetricsApi* | [**get_sector_returns**](docs/MetricsApi.md#get_sector_returns) | **GET** /Metrics/sector/returns | 
*NewsApi* | [**get**](docs/NewsApi.md#get) | **GET** /News/{id} | 
*NewsApi* | [**get_aggregated_ticker_news**](docs/NewsApi.md#get_aggregated_ticker_news) | **GET** /News/aggregated/{ticker} | 
*NewsApi* | [**get_all_sectors_news**](docs/NewsApi.md#get_all_sectors_news) | **GET** /News/sector/all/{size} | 
*NewsApi* | [**get_latest_highlight_news**](docs/NewsApi.md#get_latest_highlight_news) | **GET** /News/highlight/latest | 
*NewsApi* | [**get_latest_news**](docs/NewsApi.md#get_latest_news) | **GET** /News/latest | 
*NewsApi* | [**get_list_highlights_by_id**](docs/NewsApi.md#get_list_highlights_by_id) | **GET** /News/highlight/list/byid | 
*NewsApi* | [**get_market_highlight**](docs/NewsApi.md#get_market_highlight) | **GET** /News/highlight/{id} | 
*NewsApi* | [**get_market_highlights**](docs/NewsApi.md#get_market_highlights) | **GET** /News/highlight/list | 
*NewsApi* | [**get_news_by_category**](docs/NewsApi.md#get_news_by_category) | **GET** /News/list/{category} | 
*NewsApi* | [**get_news_by_sector**](docs/NewsApi.md#get_news_by_sector) | **GET** /News/sector/{sector} | 
*NewsApi* | [**get_news_categories**](docs/NewsApi.md#get_news_categories) | **GET** /News/categories | 
*NewsApi* | [**get_news_list**](docs/NewsApi.md#get_news_list) | **GET** /News/list/filter | 
*NewsApi* | [**get_ticker_news**](docs/NewsApi.md#get_ticker_news) | **GET** /News/stock/{ticker} | 
*NewsApi* | [**get_tickers_with_news**](docs/NewsApi.md#get_tickers_with_news) | **GET** /News/tickers | 
*NewsApi* | [**get_top_news**](docs/NewsApi.md#get_top_news) | **GET** /News/list/top | 
*PriceApi* | [**get_all_latest_prices**](docs/PriceApi.md#get_all_latest_prices) | **GET** /Price/latest/all | 
*PriceApi* | [**get_all_previous_closes**](docs/PriceApi.md#get_all_previous_closes) | **GET** /Price/close/all | 
*PriceApi* | [**get_historical_prices**](docs/PriceApi.md#get_historical_prices) | **GET** /Price/historical | 
*PriceApi* | [**get_latest_market_indices**](docs/PriceApi.md#get_latest_market_indices) | **GET** /Price/latest/market_indices | 
*PriceApi* | [**get_latest_price**](docs/PriceApi.md#get_latest_price) | **POST** /Price/latest | 
*PriceApi* | [**get_today_intraday_prices**](docs/PriceApi.md#get_today_intraday_prices) | **GET** /Price/intraday/today | 
*ScreenerApi* | [**get_all_sectors_returns**](docs/ScreenerApi.md#get_all_sectors_returns) | **GET** /Screener/sectors/all_returns | 
*ScreenerApi* | [**get_all_sectors_returns_today_sa**](docs/ScreenerApi.md#get_all_sectors_returns_today_sa) | **GET** /Screener/sa/sector/returns/today | 
*ScreenerApi* | [**get_dow_tickers**](docs/ScreenerApi.md#get_dow_tickers) | **GET** /Screener/dow/tickers | 
*ScreenerApi* | [**get_list_ip_os**](docs/ScreenerApi.md#get_list_ip_os) | **GET** /Screener/ipo/list | 
*ScreenerApi* | [**get_top_stocks**](docs/ScreenerApi.md#get_top_stocks) | **GET** /Screener/top/{category} | 
*ScreenerApi* | [**get_upcoming_ipos**](docs/ScreenerApi.md#get_upcoming_ipos) | **GET** /Screener/ipo/upcoming | 
*ScreenerApi* | [**search**](docs/ScreenerApi.md#search) | **GET** /Screener/search | 
*SearchApi* | [**search_stocks**](docs/SearchApi.md#search_stocks) | **GET** /Search/{query}/{size} | 
*SettingsApi* | [**check_i8t_version**](docs/SettingsApi.md#check_i8t_version) | **GET** /Settings/i8terminal/version/check/{version} | 
*SettingsApi* | [**get_i8t_version**](docs/SettingsApi.md#get_i8t_version) | **GET** /Settings/i8terminal/version | 
*SettingsApi* | [**set_i8t_version**](docs/SettingsApi.md#set_i8t_version) | **PUT** /Settings/i8terminal/version | 
*StockInfoApi* | [**get_all_active_companies**](docs/StockInfoApi.md#get_all_active_companies) | **GET** /StockInfo/companies/active | 
*StockInfoApi* | [**get_all_stock_info**](docs/StockInfoApi.md#get_all_stock_info) | **GET** /StockInfo/all/{marketIndex} | 
*StockInfoApi* | [**get_all_stocks_popularity**](docs/StockInfoApi.md#get_all_stocks_popularity) | **GET** /StockInfo/popularity/all | 
*StockInfoApi* | [**get_company_info**](docs/StockInfoApi.md#get_company_info) | **GET** /StockInfo/companyinfo/{ticker} | 
*StockInfoApi* | [**get_latest_rating**](docs/StockInfoApi.md#get_latest_rating) | **GET** /StockInfo/rating/latest/{ticker} | 
*StockInfoApi* | [**get_list_exchange_sector**](docs/StockInfoApi.md#get_list_exchange_sector) | **GET** /StockInfo/list/exchangesector | 
*StockInfoApi* | [**get_stock_info**](docs/StockInfoApi.md#get_stock_info) | **GET** /StockInfo/{ticker} | 
*StockInfoApi* | [**get_stock_info_list**](docs/StockInfoApi.md#get_stock_info_list) | **GET** /StockInfo/list | 
*StockInfoApi* | [**get_stock_info_master**](docs/StockInfoApi.md#get_stock_info_master) | **GET** /StockInfo/{ticker}/master | 
*StockInfoApi* | [**get_stock_info_multi**](docs/StockInfoApi.md#get_stock_info_multi) | **GET** /StockInfo/multi | 
*StockInfoApi* | [**get_stock_summary**](docs/StockInfoApi.md#get_stock_summary) | **GET** /StockInfo/{ticker}/summary | 
*StockInfoApi* | [**get_stock_summary_multi**](docs/StockInfoApi.md#get_stock_summary_multi) | **GET** /StockInfo/summary | 
*StockInfoApi* | [**get_stocks_popularity**](docs/StockInfoApi.md#get_stocks_popularity) | **GET** /StockInfo/popularity | 
*StockInfoApi* | [**get_stocks_popularity_by_sector**](docs/StockInfoApi.md#get_stocks_popularity_by_sector) | **GET** /StockInfo/popularity/bysector | 
*StockInfoApi* | [**get_top_stocks_popularity**](docs/StockInfoApi.md#get_top_stocks_popularity) | **GET** /StockInfo/popularity/top | 
*StockInfoApi* | [**get_trading_calendar**](docs/StockInfoApi.md#get_trading_calendar) | **GET** /StockInfo/calendar | 
*StockInfoApi* | [**healthy_check**](docs/StockInfoApi.md#healthy_check) | **GET** /health | 
*TagsApi* | [**get_all_tags_info**](docs/TagsApi.md#get_all_tags_info) | **GET** /Tags/all/info | 
*TagsApi* | [**get_all_ticker_tags**](docs/TagsApi.md#get_all_ticker_tags) | **GET** /Tags/all/ticker | 
*TagsApi* | [**get_tag_details**](docs/TagsApi.md#get_tag_details) | **GET** /Tags/{tagId} | 
*UserApi* | [**add_to_watchlist**](docs/UserApi.md#add_to_watchlist) | **POST** /User/watchlist/add | 
*UserApi* | [**create_login_authentication_request**](docs/UserApi.md#create_login_authentication_request) | **POST** /User/authentication/request/login | 
*UserApi* | [**create_plot**](docs/UserApi.md#create_plot) | **POST** /User/plot | 
*UserApi* | [**create_watchlist**](docs/UserApi.md#create_watchlist) | **POST** /User/watchlist | 
*UserApi* | [**get_aggregated_terminal_os_and_versions**](docs/UserApi.md#get_aggregated_terminal_os_and_versions) | **GET** /User/terminal/os/versions | 
*UserApi* | [**get_roles**](docs/UserApi.md#get_roles) | **GET** /User/roles | 
*UserApi* | [**get_terminal_log**](docs/UserApi.md#get_terminal_log) | **GET** /User/terminal/log/{id} | 
*UserApi* | [**get_terminal_logs**](docs/UserApi.md#get_terminal_logs) | **GET** /User/terminal/list/log | 
*UserApi* | [**get_watchlist**](docs/UserApi.md#get_watchlist) | **GET** /User/watchlist/{id} | 
*UserApi* | [**get_watchlist_by_name_user_id**](docs/UserApi.md#get_watchlist_by_name_user_id) | **GET** /User/watchlist/byname | 
*UserApi* | [**get_watchlists_by_user**](docs/UserApi.md#get_watchlists_by_user) | **GET** /User/watchlist/byuser/{userId} | 
*UserApi* | [**log_terminal_usage**](docs/UserApi.md#log_terminal_usage) | **POST** /User/terminal/log | 
*UserApi* | [**login_user**](docs/UserApi.md#login_user) | **POST** /User/login | 
*UserApi* | [**login_with_code**](docs/UserApi.md#login_with_code) | **POST** /User/login/code | 
*UserApi* | [**remove_from_watchlist**](docs/UserApi.md#remove_from_watchlist) | **POST** /User/watchlist/remove | 

## Documentation For Models

 - [ActiveCompanyDto](docs/ActiveCompanyDto.md)
 - [AddToWatchlistDto](docs/AddToWatchlistDto.md)
 - [AuthenticationRequest](docs/AuthenticationRequest.md)
 - [AuthenticationSource](docs/AuthenticationSource.md)
 - [CompanyInfoDto](docs/CompanyInfoDto.md)
 - [CreateAuthReqDto](docs/CreateAuthReqDto.md)
 - [CreatePlotDto](docs/CreatePlotDto.md)
 - [CreateWatchlistDto](docs/CreateWatchlistDto.md)
 - [CurrentMetricsDto](docs/CurrentMetricsDto.md)
 - [CurrentMomentumMetricsDto](docs/CurrentMomentumMetricsDto.md)
 - [DailyMetricsDto](docs/DailyMetricsDto.md)
 - [DetailedLatestPriceDto](docs/DetailedLatestPriceDto.md)
 - [DiscoverySource](docs/DiscoverySource.md)
 - [EarningMetricsDto](docs/EarningMetricsDto.md)
 - [FinancialMetricMetadataDto](docs/FinancialMetricMetadataDto.md)
 - [FinancialReportDto](docs/FinancialReportDto.md)
 - [FinancialTag](docs/FinancialTag.md)
 - [FinancialsGrowth](docs/FinancialsGrowth.md)
 - [GetWatchlistsByUserDto](docs/GetWatchlistsByUserDto.md)
 - [HistoricalDailyMetricsDto](docs/HistoricalDailyMetricsDto.md)
 - [HistoricalFinancialMetrics](docs/HistoricalFinancialMetrics.md)
 - [HistoricalIndicatorDto](docs/HistoricalIndicatorDto.md)
 - [HistoricalMetricValueDto](docs/HistoricalMetricValueDto.md)
 - [HistoricalReturn](docs/HistoricalReturn.md)
 - [HistoricalReturnsDto](docs/HistoricalReturnsDto.md)
 - [HistoricalValueMetrics](docs/HistoricalValueMetrics.md)
 - [HistoryLength](docs/HistoryLength.md)
 - [I8TerminalCheckVersionDto](docs/I8TerminalCheckVersionDto.md)
 - [I8TerminalVersion](docs/I8TerminalVersion.md)
 - [I8TerminalVersionDto](docs/I8TerminalVersionDto.md)
 - [LatestFinancialMetricsDto](docs/LatestFinancialMetricsDto.md)
 - [LatestFinancialsDto](docs/LatestFinancialsDto.md)
 - [LatestFinancialsWithGrowthDto](docs/LatestFinancialsWithGrowthDto.md)
 - [LatestPriceDto](docs/LatestPriceDto.md)
 - [ListExchangeSectorDto](docs/ListExchangeSectorDto.md)
 - [LogTerminalUsage](docs/LogTerminalUsage.md)
 - [LoginUserDto](docs/LoginUserDto.md)
 - [LoginWithCodeDto](docs/LoginWithCodeDto.md)
 - [MarketHighlightDto](docs/MarketHighlightDto.md)
 - [MarketHighlightStatus](docs/MarketHighlightStatus.md)
 - [MetadataPropertiesDto](docs/MetadataPropertiesDto.md)
 - [Metrics](docs/Metrics.md)
 - [MetricsMetadata](docs/MetricsMetadata.md)
 - [MetricsMetadataResponseDto](docs/MetricsMetadataResponseDto.md)
 - [MomentumMetricDto](docs/MomentumMetricDto.md)
 - [MonthlyMetrics](docs/MonthlyMetrics.md)
 - [MonthlyReturns](docs/MonthlyReturns.md)
 - [NewsCategoriesDto](docs/NewsCategoriesDto.md)
 - [NewsSource](docs/NewsSource.md)
 - [PeriodMetricValue](docs/PeriodMetricValue.md)
 - [PeriodReturn](docs/PeriodReturn.md)
 - [PlotResponseDto](docs/PlotResponseDto.md)
 - [PreviousCloseDto](docs/PreviousCloseDto.md)
 - [ProfileName](docs/ProfileName.md)
 - [RecentEarningDto](docs/RecentEarningDto.md)
 - [RemoveFromWatchlistDto](docs/RemoveFromWatchlistDto.md)
 - [ReqType](docs/ReqType.md)
 - [ResultField](docs/ResultField.md)
 - [ReturnMetrics](docs/ReturnMetrics.md)
 - [SAAttributesPrices](docs/SAAttributesPrices.md)
 - [SASectorPriceDto](docs/SASectorPriceDto.md)
 - [ScreeningCondition](docs/ScreeningCondition.md)
 - [SectorReturnsDto](docs/SectorReturnsDto.md)
 - [StandardizedFinancial](docs/StandardizedFinancial.md)
 - [StockEarningDto](docs/StockEarningDto.md)
 - [StockFinancial](docs/StockFinancial.md)
 - [StockFinancialMetrics](docs/StockFinancialMetrics.md)
 - [StockInfoDto](docs/StockInfoDto.md)
 - [StockInfoMasterDto](docs/StockInfoMasterDto.md)
 - [StockIpo](docs/StockIpo.md)
 - [StockNews](docs/StockNews.md)
 - [StockNewsDetails](docs/StockNewsDetails.md)
 - [StockNewsStatus](docs/StockNewsStatus.md)
 - [StockPopularityDetailsDto](docs/StockPopularityDetailsDto.md)
 - [StockPopularityDto](docs/StockPopularityDto.md)
 - [StockPrice](docs/StockPrice.md)
 - [StockPriceDto](docs/StockPriceDto.md)
 - [StockRatingDto](docs/StockRatingDto.md)
 - [StockSummaryDto](docs/StockSummaryDto.md)
 - [SymbolsCurrentMetricsDto](docs/SymbolsCurrentMetricsDto.md)
 - [SymbolsHistoricalMetricsDto](docs/SymbolsHistoricalMetricsDto.md)
 - [TagDetailsDto](docs/TagDetailsDto.md)
 - [TagInfoDto](docs/TagInfoDto.md)
 - [TerminalLogDto](docs/TerminalLogDto.md)
 - [TerminalLogOSVersionsDto](docs/TerminalLogOSVersionsDto.md)
 - [TradingCalendarDetailsDto](docs/TradingCalendarDetailsDto.md)
 - [UpcomingEarningDto](docs/UpcomingEarningDto.md)
 - [UserDto](docs/UserDto.md)
 - [ValueMetricsDto](docs/ValueMetricsDto.md)
 - [Watchlist](docs/Watchlist.md)
 - [WatchlistDto](docs/WatchlistDto.md)

## Documentation For Authorization


## apiKey

- **Type**: API key
- **API key parameter name**: apiKey
- **Location**: URL query string

## bearerCoreAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

info@investoreight.com
