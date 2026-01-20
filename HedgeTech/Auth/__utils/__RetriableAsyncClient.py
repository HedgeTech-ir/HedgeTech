# ========================================|======================================== #
#                                      Exports                                      #
# ========================================|======================================== #

__all__ = [
    'RetriableAsyncClient'
]

# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from httpx import (
    AsyncClient,
    
    ConnectTimeout,
    PoolTimeout,
    ReadTimeout,
    WriteTimeout,
)

# ========================================|======================================== #
#                                 Class Definitions                                 #
# ========================================|======================================== #


class RetriableAsyncClient:
    
    def __init__(
        self,
        client: AsyncClient,
        retries: int = 10,
    )-> AsyncClient:
        
        self._client = client
        self._retries = retries

    async def _request(self, method: str, **kwargs):
        attempt = self._retries

        while True:
            try:
                return await getattr(self._client, method)(**kwargs)

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
            async def wrapper(**kwargs):
                return await self._request(name, **kwargs)
            return wrapper

        return attr