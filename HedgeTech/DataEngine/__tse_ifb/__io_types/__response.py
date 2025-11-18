# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from dataclasses import dataclass
from datetime import datetime
from typing import (
    List,
    Union,
    Dict,
    Optional,
)

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

@dataclass
class BestLimitItem:
    buy_order_count: int
    buy_quantity: int
    buy_price: int
    sell_order_count: int
    sell_quantity: int
    sell_price: int

@dataclass
class BestLimit:
    items: Dict[str, Dict[str, BestLimitItem]]

@dataclass
class BestLimitResponse:
    Data: BestLimit
    Status: Status
    
# +--------------------------------------------------------------------------------------+ #

@dataclass
class OrderItem:
    price: float
    quantity: int
    count: int

@dataclass
class OrderBook:
    Buy: List[OrderItem]
    Sell: List[OrderItem]

@dataclass
class OrderBookResponse:
    Data: Dict[str, OrderBook]
    Status: Status
    
# +--------------------------------------------------------------------------------------+ #


@dataclass
class Aggregate:
    date: str
    time: str
    trade_count: int
    total_volume: int
    total_value: int
    closing_price: float
    last_price: float
    low_price: float
    high_price: float
    open_price: float
    previous_close: float

@dataclass
class AggregateResponse:
    Data: Dict[str, Aggregate]
    Status: Status
    
# +--------------------------------------------------------------------------------------+ #

@dataclass
class institutional_vs_individual:
    buy_count_individual: int
    buy_volume_individual: int
    buy_count_institution: int
    buy_volume_institution: int
    sell_count_individual: int
    sell_volume_individual: int
    sell_count_institution: int
    sell_volume_institution: int

@dataclass
class Institutional_vs_IndividualItemResponse:
    Data: Dict[str, institutional_vs_individual]
    Status: Status
    
# +--------------------------------------------------------------------------------------+ #

@dataclass
class ContractInfo:
    open_interest: int
    initial_margin: int
    required_margin: int

@dataclass
class ContractInfoResponse:
    Data: Dict[str, ContractInfo]
    Status: Status

# +--------------------------------------------------------------------------------------+ #
    
@dataclass
class FundInfo:
    nav: float
    units: int
    marketCap: int
    as_of: datetime

@dataclass
class FundInfoResponse:
    Data: Dict[str, FundInfo]
    Status: Status
    
# +--------------------------------------------------------------------------------------+ #

@dataclass
class OHLCV:
    open: float
    high: float
    low: float
    close: float
    volume: int

@dataclass
class OHLCVLast1mResponse:
    Data: Dict[str, OHLCV]
    Status: Status
    
# +--------------------------------------------------------------------------------------+ #

@dataclass
class OverviewSecuritiesAndFunds(SecuritiesAndFunds):
    BestLimit: Dict[str, BestLimitItem]
    Aggregate: Aggregate
    institutional_vs_individual: institutional_vs_individual
    FundInfo: FundInfo
    ContractInfo: ContractInfo

@dataclass
class OverviewTreasuryBonds(TreasuryBonds):
    BestLimit: Dict[str, BestLimitItem]
    Aggregate: Aggregate
    institutional_vs_individual: institutional_vs_individual
    FundInfo: FundInfo
    ContractInfo: ContractInfo

@dataclass
class OverviewStockOptions(StockOptions):
    BestLimit: Dict[str, BestLimitItem]
    Aggregate: Aggregate
    institutional_vs_individual: institutional_vs_individual
    FundInfo: FundInfo
    ContractInfo: ContractInfo

@dataclass
class OverviewStockFuturess(StockFutures):
    BestLimit: Dict[str, BestLimitItem]
    Aggregate: Aggregate
    institutional_vs_individual: institutional_vs_individual
    FundInfo: FundInfo
    ContractInfo: ContractInfo

@dataclass
class OverviewResponse:
    Data : Dict[
        str,Optional[
            Union[
                OverviewSecuritiesAndFunds,
                OverviewTreasuryBonds,
                OverviewStockOptions,
                OverviewStockFuturess
            ]
        ]
    ]
    Status: Status
    
# +--------------------------------------------------------------------------------------+ #
 
@dataclass
class OHLCV:
    Date_timestamp: List[int]
    Open: List[Union[float, int]]
    High: List[Union[float, int]]
    Low: List[Union[float, int]]
    Close: List[Union[float, int]]
    Volume: List[int]
    symbolName: str
    symbolIsin: str


@dataclass
class OHLCVResponse:  # EXPOSE
    Data: OHLCV
    Status: Status

# +--------------------------------------------------------------------------------------+ #

class DividendAction:
    Date_timestamp: int
    corporateAction: str
    symbolName: str
    symbolIsin: str
    سود_تقسیم_شده: Optional[str]
    تاریخ: str


@dataclass
class CapitalIncreaseAction:
    Date_timestamp: int
    corporateAction: str
    symbolName: str
    symbolIsin: str
    سرمایه_قبلی: Optional[str]
    سرمایه_جدید: Optional[str]
    درصد_افزایش: Optional[str]
    تاریخ: str


@dataclass
class CorporateActionResponse:  # EXPOSE
    Data: List[Union[DividendAction, CapitalIncreaseAction, None]]
    Status: Status