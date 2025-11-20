# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from typing import (
    List,
    TypedDict
)


# ========================================|======================================== #
#                                 Class Definitions                                 #
# ========================================|======================================== #


class SymbolNames(TypedDict):
    """
    Represents a collection of instrument symbol names for batch API requests.

    Attributes:
        symbol_names (List[str]): A list of instrument symbol names (strings) to be queried.

    Example:
        >>> symbols: SymbolNames = {"symbol_names": ["ETF001", "FUT002", "STK003"]}
        >>> symbols["symbol_names"][0]
        'ETF001'
    """
    symbol_names: List[str]

# +--------------------------------------------------------------------------------------+ #


class SymbolIsins(TypedDict):
    """
    Represents a collection of instrument ISIN identifiers for batch API requests.

    Attributes:
        symbol_isins (List[str]): A list of instrument ISIN codes (strings) to be queried.

    Example:
        >>> isins: SymbolIsins = {"symbol_isins": ["IR0001234567", "IR0009876543"]}
        >>> isins["symbol_isins"][1]
        'IR0009876543'
    """
    symbol_isins: List[str]
    
# +--------------------------------------------------------------------------------------+ #