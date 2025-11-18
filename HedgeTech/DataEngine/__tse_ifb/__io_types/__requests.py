# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from dataclasses import (
    dataclass,
    field
)
from typing import (
    List
)


# ========================================|======================================== #
#                                 Class Definitions                                 #
# ========================================|======================================== #

@dataclass
class SymbolNames:
    symbol_names: List[str] = field(metadata={"description": "List of symbol names"})

# +--------------------------------------------------------------------------------------+ #

@dataclass
class SymbolIsins:
    symbol_isins: List[str] = field(metadata={"description": "List of symbol isin"})
    
# +--------------------------------------------------------------------------------------+ #


def test(input:SymbolNames)-> SymbolIsins:
    """_summary_

    Args:
        input (SymbolNames): _description_

    Returns:
        SymbolIsins: _description_
    """
    ...