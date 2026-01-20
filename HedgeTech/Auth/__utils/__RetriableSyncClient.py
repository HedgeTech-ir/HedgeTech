# ========================================|======================================== #
#                                      Exports                                      #
# ========================================|======================================== #

__all__ = [
    'RetriableSyncClient'
]

# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from httpx import (
    Client,
    
    ConnectTimeout,
    PoolTimeout,
    ReadTimeout,
    WriteTimeout,
)

# ========================================|======================================== #
#                                 Class Definitions                                 #
# ========================================|======================================== #


class RetriableSyncClient:
    
    def __init__(
        self,
        client: Client,
        retries: int = 10,
    )-> Client:
        
        self._client = client
        self._retries = retries

    def _request(self, method: str, **kwargs):
        attempt = self._retries

        while True:
            try:
                return getattr(self._client, method)(**kwargs)

            except (
                ConnectTimeout,
                PoolTimeout,
                ReadTimeout,
                WriteTimeout,
            ):
                if attempt <= 0:
                    raise
                attempt -= 1

    def __getattr__(self, name: str):
        
        attr = getattr(self._client, name)

        if name in {"get", "post", "put", "delete", "patch", "options", "head"}:
            
            def wrapper(**kwargs):
                return self._request(name, **kwargs)
            return wrapper

        return attr