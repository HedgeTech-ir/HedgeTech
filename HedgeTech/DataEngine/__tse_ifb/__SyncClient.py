# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from HedgeTech.Auth import AuthSyncClient
from typing import (
    Literal,
)
from .__io_types import (
    InstrumentsSearch
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
    
    
    def instruments_search(
        self,
        market : Literal[
            "SecuritiesAndFunds",
            "TreasuryBonds",
            "StockOptions",
            "StockFutures",  
        ],
        Search_char : str,
    )-> InstrumentsSearch | None:
        
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