# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from HedgeTech.Auth import AuthSyncClient
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

class DataEngine_TseIfb_SyncClient:
    
    def __init__(
        self,
        AuthSyncClient : AuthSyncClient,
    ):

        
        self.__AuthSyncClient = AuthSyncClient
        
    
    # +--------------------------------------------------------------------------------------+ #
    
    def search_instruments(
        self,
        market : Literal[
            "SecuritiesAndFunds",
            "TreasuryBonds",
            "StockOptions",
            "StockFutures",  
        ],
        Search_char : str,
    )-> Instruments | None:
        
        data = self.__AuthSyncClient.httpx_Client.get(
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
    
    def Get_instruments_by_name(self,symbol_names : List[str])-> Instruments | None:
        
        data = self.__AuthSyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/data-engine/tse-ifb/static/data/instruments/symbol/name',
            params=[('symbol_names', name) for name in symbol_names]
        )
        
        if data.is_success :
            
            return data.json()
        
        else :
            
            raise ValueError(data.json().get('detail'))
        
        
    # +--------------------------------------------------------------------------------------+ #