from decouple import config
API_KEY = config("ALPHA_VANTAGE_API_KEY")

import pprint
pp = pprint.PrettyPrinter(indent=4)

from alpha_vantage.timeseries import TimeSeries
from ...internal.alphavantage import (
    get_alphavantage_data_symbol,
    update_alphavantage_data_symbol
)

async def update_intraday(symbol):
    ts = TimeSeries(API_KEY, rapidapi=True, output_format='json')
    data, meta_data = ts.get_intraday(symbol=symbol,interval='1min', outputsize='full')

    if data and len(data) > 0:
        symbol = meta_data["2. Symbol"]
        function = "TIME_SERIES_INTRADAY"
        alphavantage = await get_alphavantage_data_symbol(function, symbol)
        time_series = {}
        if alphavantage.get("data"):
            time_series = alphavantage["data"]["time_series"]
        
        updated_alphavantage = {
            "function": function,
            "symbol": symbol,
            "meta_data": meta_data,
            "time_series": {**time_series, **data}
        }
        await update_alphavantage_data_symbol(function, symbol, updated_alphavantage)
    return

async def update_daily(symbol):
    ts = TimeSeries(API_KEY, rapidapi=True, output_format='json')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
    if data and len(data) > 0:
        symbol = meta_data["2. Symbol"]
        function = "TIME_SERIES_DAILY"
        alphavantage = await get_alphavantage_data_symbol(function, symbol)
        time_series = {}
        if alphavantage.get("data"):
            time_series = alphavantage["data"]["time_series"]

        updated_alphavantage = {
            "symbol": symbol,
            "function":  function,
            "meta_data": meta_data,
            "time_series": {**data, **time_series}
        }

        await update_alphavantage_data_symbol(function, symbol, updated_alphavantage)
    return
