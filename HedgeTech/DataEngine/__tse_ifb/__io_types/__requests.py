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