# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from HedgeTech.Auth import AuthAsyncClient
from typing import (
    Literal,
)
from .__io_types import (
    InstrumentsSearch
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
    
    async def instruments_search(
        self,
        market : Literal[
            "SecuritiesAndFunds",
            "TreasuryBonds",
            "StockOptions",
            "StockFutures",  
        ],
        Search_char : str,
    )-> InstrumentsSearch | None:
        
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