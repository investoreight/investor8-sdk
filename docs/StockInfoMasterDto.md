# StockInfoMasterDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** |  | [optional] 
**summary** | [**StockSummaryDto**](StockSummaryDto.md) |  | [optional] 
**latest_earning** | [**StockEarningDto**](StockEarningDto.md) |  | [optional] 
**upcoming_earning** | [**StockEarningDto**](StockEarningDto.md) |  | [optional] 
**latest_financials** | [**LatestFinancialsWithGrowthDto**](LatestFinancialsWithGrowthDto.md) |  | [optional] 
**second_latest_financials** | [**LatestFinancialsWithGrowthDto**](LatestFinancialsWithGrowthDto.md) |  | [optional] 
**previous_year_financials** | [**LatestFinancialsWithGrowthDto**](LatestFinancialsWithGrowthDto.md) |  | [optional] 
**price_returns** | **dict(str, float)** |  | [optional] 
**monthly_returns** | **dict(str, dict(str, float))** |  | [optional] 
**sector_returns** | **dict(str, float)** |  | [optional] 
**spx_returns** | **dict(str, float)** |  | [optional] 
**dow_returns** | **dict(str, float)** |  | [optional] 
**ndx_returns** | **dict(str, float)** |  | [optional] 
**metrics** | [**Metrics**](Metrics.md) |  | [optional] 
**current_momentum** | [**CurrentMomentumMetricsDto**](CurrentMomentumMetricsDto.md) |  | [optional] 
**latest_rating** | [**StockRatingDto**](StockRatingDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

