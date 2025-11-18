# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from HedgeTech.Auth import AuthAsyncClient
from typing import (
    Literal,
    List,
)
from .__io_types import (
    Instruments
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
    )-> Instruments | None:
        
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
    
    async def Get_instruments_by_name(self,symbol_names : List[str])-> Instruments | None:
        
        data = await self.__AuthAsyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/static/data/instruments/symbol/name',
            params=[('symbol_names', name) for name in symbol_names]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
    # +--------------------------------------------------------------------------------------+ #