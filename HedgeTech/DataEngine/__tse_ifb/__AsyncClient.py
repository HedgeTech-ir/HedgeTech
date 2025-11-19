# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from HedgeTech.Auth import AuthAsyncClient
from typing import (
    Literal,
    List,
)
from .__io_types import (
    Instruments,
    OverviewResponse,
    BestLimitResponse,
    OrderBookResponse,
    AggregateResponse,
    Institutional_vs_IndividualItemResponse,
    ContractInfoResponse,
    FundInfoResponse,
    OHLCVLast1mResponse,
    
    OHLCVResponse,
    CorporateActionResponse,
    
    BestLimit_WS_symbolIsin,
    BestLimit_WS_symbolName,
    OrderBook_WS_symbolIsin,
    OrderBook_WS_symbolName,
    Aggregate_WS_symbolIsin,
    Aggregate_WS_symbolName,
    institutional_vs_individual_WS_symbolIsin,
    institutional_vs_individual_WS_symbolName,
    ContractInfo_WS_symbolIsin,
    ContractInfo_WS_symbolName,
    FundInfo_WS_symbolIsin,
    FundInfo_WS_symbolName,
)

# ========================================|======================================== #
#                                 Class Definitions                                 #
# ========================================|======================================== #

class DataEngine_TseIfb_AsyncClient:
    
    def __init__(
        self,
        AuthAsyncClient : AuthAsyncClient,
    ):

        
        self.__AuthAsyncClient = AuthAsyncClient
        
        
    # +--------------------------------------------------------------------------------------+ #
    
    async def search_instruments(
        self,
        market : Literal[
            "SecuritiesAndFunds",
            "TreasuryBonds",
            "StockOptions",
            "StockFutures",  
        ],
        Search_char : str,
    )-> Instruments :
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/static/data/instruments/search',
            params={
                'market' : market,
                'Search_char' : Search_char
            } 
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
    
    # +--------------------------------------------------------------------------------------+ #
    
    async def instruments_static_info_by_name(self,symbol_names : List[str])-> Instruments:
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/static/data/instruments/symbol/name',
            params=[('symbol_names', name) for name in symbol_names]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
    # +--------------------------------------------------------------------------------------+ #
    
    async def instruments_static_info_by_isin(self,symbol_isins : List[str])-> Instruments:
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/static/data/instruments/symbol/isin',
            params=[('symbol_isins', isin) for isin in symbol_isins]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
    # +--------------------------------------------------------------------------------------+ #
        
    async def live_overview_by_name(self,symbol_names : List[str])-> OverviewResponse:
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/overview/symbol/name',
            params=[('symbol_names', name) for name in symbol_names]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
        
    # +--------------------------------------------------------------------------------------+ #
    
    
    async def live_overview_by_isin(self,symbol_isins : List[str])-> OverviewResponse:
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/overview/symbol/isin',
            params=[('symbol_isins', isin) for isin in symbol_isins]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
    # +--------------------------------------------------------------------------------------+ #
        
    async def live_best_limit_by_name(self,symbol_names : List[str])-> BestLimitResponse:
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/best-limit/symbol/name',
            params=[('symbol_names', name) for name in symbol_names]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
        
    # +--------------------------------------------------------------------------------------+ #
    
    
    async def live_best_limit_by_isin(self,symbol_isins : List[str])-> BestLimitResponse:
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/best-limit/symbol/isin',
            params=[('symbol_isins', isin) for isin in symbol_isins]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
    # +--------------------------------------------------------------------------------------+ #
        
    async def live_order_book_by_name(self,symbol_names : List[str])-> OrderBookResponse :
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/order-book/symbol/name',
            params=[('symbol_names', name) for name in symbol_names]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
        
    # +--------------------------------------------------------------------------------------+ #
    
    
    async def live_order_book_by_isin(self,symbol_isins : List[str])-> OrderBookResponse:
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/order-book/symbol/isin',
            params=[('symbol_isins', isin) for isin in symbol_isins]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
    # +--------------------------------------------------------------------------------------+ #
        
    async def live_aggregate_by_name(self,symbol_names : List[str])-> AggregateResponse:
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/aggregate/symbol/name',
            params=[('symbol_names', name) for name in symbol_names]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
        
    # +--------------------------------------------------------------------------------------+ #
    
    
    async def live_aggregate_by_isin(self,symbol_isins : List[str])-> AggregateResponse :
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/aggregate/symbol/isin',
            params=[('symbol_isins', isin) for isin in symbol_isins]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
    # +--------------------------------------------------------------------------------------+ #
        
    async def live_institutional_vs_individual_by_name(self,symbol_names : List[str])-> Institutional_vs_IndividualItemResponse:
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/institutional-vs-individual/symbol/name',
            params=[('symbol_names', name) for name in symbol_names]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
        
    # +--------------------------------------------------------------------------------------+ #
    
    
    async def live_institutional_vs_individual_by_isin(self,symbol_isins : List[str])-> Institutional_vs_IndividualItemResponse :
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/institutional-vs-individual/symbol/isin',
            params=[('symbol_isins', isin) for isin in symbol_isins]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
    # +--------------------------------------------------------------------------------------+ #
        
    async def live_contract_info_by_name(self,symbol_names : List[str])-> ContractInfoResponse :
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/contract-info/symbol/name',
            params=[('symbol_names', name) for name in symbol_names]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
        
    # +--------------------------------------------------------------------------------------+ #
    
    
    async def live_contract_info_by_isin(self,symbol_isins : List[str])-> ContractInfoResponse :
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/contract-info/symbol/isin',
            params=[('symbol_isins', isin) for isin in symbol_isins]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
    # +--------------------------------------------------------------------------------------+ #
        
    async def live_fund_info_by_name(self,symbol_names : List[str])-> FundInfoResponse:
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/fund-info/symbol/name',
            params=[('symbol_names', name) for name in symbol_names]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
        
    # +--------------------------------------------------------------------------------------+ #
    
    
    async def live_fund_info_by_isin(self,symbol_isins : List[str])-> FundInfoResponse :
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/fund-info/symbol/isin',
            params=[('symbol_isins', isin) for isin in symbol_isins]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
    # +--------------------------------------------------------------------------------------+ #
        
    async def live_ohlcv_last1m_by_name(self,symbol_names : List[str])-> OHLCVLast1mResponse :
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/ohlcv-last-1m/symbol/name',
            params=[('symbol_names', name) for name in symbol_names]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
        
    # +--------------------------------------------------------------------------------------+ #
    
    
    async def live_ohlcv_last1m_by_isin(self,symbol_isins : List[str])-> OHLCVLast1mResponse:
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/live/data/instruments/ohlcv-last-1m/symbol/isin',
            params=[('symbol_isins', isin) for isin in symbol_isins]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
    # +--------------------------------------------------------------------------------------+ #
        
    async def historical_ohlcv_by_name(
        self,
        *,
        symbolName : str,
        start_timestamp : int,
        end_timestamp : int,
        AdjustedPrice : bool,
        Resolution : Literal["1m","5m","15m","30m","1h","D","W","M",]
    )-> OHLCVResponse:
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/historical/data/instruments/ohlcv/symbol/name',
            params={
                'symbolName' : symbolName,
                'start_timestamp' : start_timestamp,
                'end_timestamp' : end_timestamp,
                'AdjustedPrice' : AdjustedPrice,
                'Resolution' : Resolution,
            }
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
        
    # +--------------------------------------------------------------------------------------+ #
    
    
    async def historical_ohlcv_by_isin(
        self,
        *,
        isin : str,
        start_timestamp : int,
        end_timestamp : int,
        AdjustedPrice : bool,
        Resolution : Literal["1m","5m","15m","30m","1h","D","W","M",]
    )-> OHLCVResponse:
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/historical/data/instruments/ohlcv/symbol/isin',
            params={
                'isin' : isin,
                'start_timestamp' : start_timestamp,
                'end_timestamp' : end_timestamp,
                'AdjustedPrice' : AdjustedPrice,
                'Resolution' : Resolution,
            }
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
    # +--------------------------------------------------------------------------------------+ #
        
    async def historical_corporateactions_by_name(
        self,
        *,
        symbolName : str,
        start_timestamp : int,
        end_timestamp : int,
    )-> CorporateActionResponse :
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/historical/data/instruments/corporateactions/symbol/name',
            params={
                'symbolName' : symbolName,
                'start_timestamp' : start_timestamp,
                'end_timestamp' : end_timestamp,
            }
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
        
    # +--------------------------------------------------------------------------------------+ #
    
    
    async def historical_corporateactions_by_isin(
        self,
        *,
        isin : str,
        start_timestamp : int,
        end_timestamp : int,
    )-> CorporateActionResponse:
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/historical/data/instruments/corporateactions/symbol/isin',
            params={
                'isin' : isin,
                'start_timestamp' : start_timestamp,
                'end_timestamp' : end_timestamp,
            }
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))