# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from dataclasses import dataclass
from typing import List, Union, Optional

# ========================================|======================================== #
#                                 Class Definitions                                 #
# ========================================|======================================== #

@dataclass
class StatusDescription:
    fa: str
    en: str

@dataclass
class Status:
    State: bool
    ServerTimeStamp: float
    Version: str
    Author: str
    Description: StatusDescription
    StatusCode: int

# +--------------------------------------------------------------------------------------+ #

@dataclass
class SecuritiesAndFunds:
    symbolIsin: str
    symbolName: str
    title: str

    buyCommission: float
    sellCommission: float

    minValidBuyVolume: int
    maxValidBuyVolume: int
    minValidSellVolume: int
    maxValidSellVolume: int

    canBuy: bool
    canSell: bool

    minAllowedPrice: float
    maxAllowedPrice: float

    is_ETF: bool
    baseVolume: float
    minDealablePrice: float
    minDealableCount: int

    owner: str
    hidePrice: int
    dataClass: str

# +--------------------------------------------------------------------------------------+ #

@dataclass
class StockFutures:
    symbolIsin: str
    title: str
    symbolName: str

    csize: int
    firstMargin: float
    minimumMargin: float

    UnderlyingAssets_symbolIsin: str
    UnderlyingAssets_title: str
    UnderlyingAssets_symbolName: str
    UnderlyingAssets_is_ETF: bool

    roundFactor: int
    ExpirationDate: str
    DaysToExpiration: int

    buyCommission: float
    sellCommission: float

    minValidBuyVolume: int
    maxValidBuyVolume: int
    minValidSellVolume: int
    maxValidSellVolume: int

    canBuy: bool
    canSell: bool

    minAllowedPrice: float
    maxAllowedPrice: float

    minDealableCount: int
    minDealablePrice: float

    owner: str

    ExerciseFeePhysical: float
    ExerciseFeeCash: float
    ExerciseSellTax: float

    OpenPositionLimitInstitution: int
    OpenPositionLimitIndividual: int
    OpenPositionLimitMarket: int

    dataClass: str

# +--------------------------------------------------------------------------------------+ #

@dataclass
class StockOptions:
    symbolIsin: str
    symbolName: str
    title: str

    buyCommission: float
    sellCommission: float

    minValidBuyVolume: int
    maxValidBuyVolume: int
    minValidSellVolume: int
    maxValidSellVolume: int

    canBuy: bool
    canSell: bool

    minAllowedPrice: float
    maxAllowedPrice: float

    minDealablePrice: float
    minDealableCount: int

    owner: str

    strikePrice: float
    csize: int
    optionType: str
    ExpirationDate: str
    DaysToExpiration: int

    UnderlyingAssets_symbolIsin: str
    UnderlyingAssets_title: str
    UnderlyingAssets_symbolName: str
    UnderlyingAssets_is_ETF: bool

    ExerciseFeePhysical: float
    ExerciseFeeCash: float
    ExerciseSellTax: float

    OpenPositionLimitInstitution: int
    OpenPositionLimitIndividual: int
    OpenPositionLimitMarket: int

    dataClass: str

# +--------------------------------------------------------------------------------------+ #

@dataclass
class TreasuryBonds:
    symbolIsin: str
    symbolName: str
    title: str

    buyCommission: float
    sellCommission: float

    minValidBuyVolume: int
    maxValidBuyVolume: int
    minValidSellVolume: int
    maxValidSellVolume: int

    canBuy: bool
    canSell: bool

    minAllowedPrice: float
    maxAllowedPrice: float

    baseVol: float
    minDealablePrice: float
    minDealableCount: int

    owner: str
    hidePrice: int
    is_ETF: bool

    ExpirationDate: str
    DaysToExpiration: int

    dataClass: str

# +--------------------------------------------------------------------------------------+ #

@dataclass
class Instruments:
    Data: List[
        Union[
            SecuritiesAndFunds,
            StockFutures,
            StockOptions,
            TreasuryBonds,
            None
        ]
    ]
    Status: Status
    
# +--------------------------------------------------------------------------------------+ #