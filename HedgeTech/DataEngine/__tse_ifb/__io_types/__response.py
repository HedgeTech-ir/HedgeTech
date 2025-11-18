# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from datetime import datetime
from typing import (
    List,
    Union,
    Dict,
    Optional,
    TypedDict,
)

# ========================================|======================================== #
#                                 Class Definitions                                 #
# ========================================|======================================== #


class StatusDescription(TypedDict):
    fa: str
    en: str


class Status(TypedDict):
    State: bool
    ServerTimeStamp: float
    Version: str
    Author: str
    Description: StatusDescription
    StatusCode: int

# +--------------------------------------------------------------------------------------+ #


class SecuritiesAndFunds(TypedDict):
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


class StockFutures(TypedDict):
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


class StockOptions(TypedDict):
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


class TreasuryBonds(TypedDict):
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


class Instruments(TypedDict):
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


class BestLimitItem(TypedDict):
    buy_order_count: int
    buy_quantity: int
    buy_price: int
    sell_order_count: int
    sell_quantity: int
    sell_price: int


class BestLimit(TypedDict):
    items: Dict[str, Dict[str, BestLimitItem]]


class BestLimitResponse(TypedDict):
    Data: BestLimit
    Status: Status
    
# +--------------------------------------------------------------------------------------+ #


class OrderItem(TypedDict):
    price: float
    quantity: int
    count: int


class OrderBook(TypedDict):
    Buy: List[OrderItem]
    Sell: List[OrderItem]


class OrderBookResponse(TypedDict):
    Data: Dict[str, OrderBook]
    Status: Status
    
# +--------------------------------------------------------------------------------------+ #



class Aggregate(TypedDict):
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


class AggregateResponse(TypedDict):
    Data: Dict[str, Aggregate]
    Status: Status
    
# +--------------------------------------------------------------------------------------+ #


class institutional_vs_individual(TypedDict):
    buy_count_individual: int
    buy_volume_individual: int
    buy_count_institution: int
    buy_volume_institution: int
    sell_count_individual: int
    sell_volume_individual: int
    sell_count_institution: int
    sell_volume_institution: int


class Institutional_vs_IndividualItemResponse(TypedDict):
    Data: Dict[str, institutional_vs_individual]
    Status: Status
    
# +--------------------------------------------------------------------------------------+ #


class ContractInfo(TypedDict):
    open_interest: int
    initial_margin: int
    required_margin: int


class ContractInfoResponse(TypedDict):
    Data: Dict[str, ContractInfo]
    Status: Status

# +--------------------------------------------------------------------------------------+ #
    

class FundInfo(TypedDict):
    nav: float
    units: int
    marketCap: int
    as_of: datetime


class FundInfoResponse(TypedDict):
    Data: Dict[str, FundInfo]
    Status: Status
    
# +--------------------------------------------------------------------------------------+ #


class OHLCV(TypedDict):
    open: float
    high: float
    low: float
    close: float
    volume: int


class OHLCVLast1mResponse(TypedDict):
    Data: Dict[str, OHLCV]
    Status: Status
    
# +--------------------------------------------------------------------------------------+ #


class OverviewSecuritiesAndFunds(SecuritiesAndFunds):
    BestLimit: Dict[str, BestLimitItem]
    Aggregate: Aggregate
    institutional_vs_individual: institutional_vs_individual
    FundInfo: FundInfo
    ContractInfo: ContractInfo


class OverviewTreasuryBonds(TreasuryBonds):
    BestLimit: Dict[str, BestLimitItem]
    Aggregate: Aggregate
    institutional_vs_individual: institutional_vs_individual
    FundInfo: FundInfo
    ContractInfo: ContractInfo


class OverviewStockOptions(StockOptions):
    BestLimit: Dict[str, BestLimitItem]
    Aggregate: Aggregate
    institutional_vs_individual: institutional_vs_individual
    FundInfo: FundInfo
    ContractInfo: ContractInfo


class OverviewStockFuturess(StockFutures):
    BestLimit: Dict[str, BestLimitItem]
    Aggregate: Aggregate
    institutional_vs_individual: institutional_vs_individual
    FundInfo: FundInfo
    ContractInfo: ContractInfo


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
 

class OHLCV(TypedDict):
    Date_timestamp: List[int]
    Open: List[Union[float, int]]
    High: List[Union[float, int]]
    Low: List[Union[float, int]]
    Close: List[Union[float, int]]
    Volume: List[int]
    symbolName: str
    symbolIsin: str



class OHLCVResponse(TypedDict):
    Data: OHLCV
    Status: Status

# +--------------------------------------------------------------------------------------+ #

class DividendAction(TypedDict):
    Date_timestamp: int
    corporateAction: str
    symbolName: str
    symbolIsin: str
    سود_تقسیم_شده: Optional[str]
    تاریخ: str


class CapitalIncreaseAction(TypedDict):
    Date_timestamp: int
    corporateAction: str
    symbolName: str
    symbolIsin: str
    سرمایه_قبلی: Optional[str]
    سرمایه_جدید: Optional[str]
    درصد_افزایش: Optional[str]
    تاریخ: str



class CorporateActionResponse(TypedDict): 
    Data: List[Union[DividendAction, CapitalIncreaseAction, None]]
    Status: Status