from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class AlphavantageSchema(BaseModel):
    function: Optional[str] = Field(None, description='TIME_SERIES_DAILY, TIME_SERIES_INTRADAY')
    symbol: Optional[str] = Field(None, description='the symbol for the equity')
    meta_data: Optional[dict] = Field(None, description='the symbol for the equity, time interval between and etc.')
    time_series: Optional[dict] = Field(None, description='intraday or daily time series')

    class Config:
        schema_extra = {
            "example": {
                "function": "TIME_SERIES_DAILY",
                "symbol": "TSLA",
                "meta_data": {
                    "information": "Daily Prices (open, high, low, close) and Volumes",
                    "symbol": "TSLA",
                    "last_refreshed": "2023-01-06",
                    "output_size": "Full size",
                    "time_zone": "US/Eastern"
                },
                "time_series": {
                    "2019-12-02": {
                        "1. open": "151.8100",
                        "2. high": "151.8300",
                        "3. low": "148.3200",
                        "4. close": "149.5500",
                        "5. volume": "24770986"
                    },
                    "2019-11-29": {
                        "1. open": "152.1000",
                        "2. high": "152.3000",
                        "3. low": "151.2800",
                        "4. close": "151.3800",
                        "5. volume": "11977300"
                    }
                }
            }
        }

class UpdateAlphavantageModel(BaseModel):
    function: Optional[str]
    symbol: Optional[str]
    meta_data: Optional[dict]
    time_series: Optional[dict]

    class Config:
        schema_extra = {
            "example": {
                "function": "TIME_SERIES_DAILY",
                "symbol": "TSLA",
                "meta_data": {
                    "information": "Daily Prices (open, high, low, close) and Volumes",
                    "symbol": "TSLA",
                    "last_refreshed": "2023-01-06",
                    "output_size": "Full size",
                    "time_zone": "US/Eastern"
                },
                "time_series": {
                    "2019-12-02": {
                        "1. open": "151.8100",
                        "2. high": "151.8300",
                        "3. low": "148.3200",
                        "4. close": "149.5500",
                        "5. volume": "24770986"
                    },
                    "2019-11-29": {
                        "1. open": "152.1000",
                        "2. high": "152.3000",
                        "3. low": "151.2800",
                        "4. close": "151.3800",
                        "5. volume": "11977300"
                    }
                }
            }
        }

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
