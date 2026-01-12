# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from typing import (
    NewType,
    TypedDict,
    Literal,
)

# ========================================|======================================== #
#                                 Class Definitions                                 #
# ========================================|======================================== #

HexUUID = NewType("HexUUID", str)

# +--------------------------------------------------------------------------------------+ #

class OrderStatus(TypedDict):
    
    order_uuid : HexUUID
    order_status : Literal['InQueue','Cancelled','Broken','Settled']
    Price : int
    Volume : int
    RemainedVolume : int
    ExecutedVolume : int
    OrderSide : Literal['Buy','Sell']
    ValidityType : Literal['DAY','GTC','GTD']
    ValidityDate : int