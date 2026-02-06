# HedgeTech Python SDK

HedgeTech Python SDK is a professional, lightweight, and modular Python
package designed to provide seamless access to HedgeTech services. The
SDK is crafted for developers, data analysts, and algorithmic traders
who want to interact with the Tehran Stock Exchange (TSE & IFB) using a
clean, reliable, and easy-to-use API.

It supports both synchronous and asynchronous workflows, offering
maximum flexibility and performance for different application scenarios.

> **Note:** This SDK requires Python >= 3.10 and is production-ready.
> Development Status: **5 - Production/Stable**.
> The public APIs are stable and safe for long-term use.

------------------------------------------------------------------------

## Features

-   Secure authentication with async and sync clients.
-   Real-time and historical market data from TSE & IFB.
-   Full EMS Engine order lifecycle management.
-   Modular architecture (Auth, DataEngine, EMSEngine).
-   Structured request/response types.
-   High-performance asyncio support.
-   Easy integration with trading bots and dashboards.

------------------------------------------------------------------------

## Installation

Install via PyPI:

``` bash
pip install HedgeTech
```

### Update

``` bash
pip install --upgrade HedgeTech
```

------------------------------------------------------------------------

## Package Structure

    HedgeTech/
     ├── Auth/
     ├── DataEngine/
     ├── EMSEngine/
     └── __init__.py

------------------------------------------------------------------------

## Authentication

All services require authentication.

> Use matching Sync/Async clients.

### Async Authentication

``` python
from HedgeTech.Auth import AuthAsyncClient

auth_async_client = await AuthAsyncClient.login(
    UserName_or_Email="user@example.com",
    Password="password"
)

print(auth_async_client.token)
```

### Sync Authentication

``` python
from HedgeTech.Auth import AuthSyncClient

auth_sync_client = AuthSyncClient.login(
    UserName_or_Email="user@example.com",
    Password="password"
)

print(auth_sync_client.token)
```

------------------------------------------------------------------------

## DataEngine (Market Data)

The DataEngine module provides unified access to:

-   Live market data
-   Historical OHLCV
-   Order books
-   Best limits
-   WebSocket streams

All engines follow identical Sync/Async APIs.

------------------------------------------------------------------------

### Async Data Example

``` python
from HedgeTech.DataEngine import DataEngine_TseIfb_AsyncClient

client = DataEngine_TseIfb_AsyncClient(auth_async_client)

data = await client.live_best_limit_by_isin(
    symbol_isins=["IRT1AHRM0001","IRO1IKCO0001"]
)

print(data)

async for update in client.websocket_by_name(
    channels=["best-limit","order-book"],
    symbol_names=["فملی","اطلس"]
):
    print(update["data"])
```

------------------------------------------------------------------------

### Sync Data Example

``` python
from HedgeTech.DataEngine import DataEngine_TseIfb_SyncClient

client = DataEngine_TseIfb_SyncClient(auth_sync_client)

data = client.historical_ohlcv_by_name(
    symbolName="مهرگان",
    start_timestamp=0,
    end_timestamp="1763411432",
    AdjustedPrice=True,
    Resolution="D"
)

print(data)

for update in client.websocket_by_isin(
    channels=["best-limit","order-book"],
    symbol_isins=["IR1234567890"]
):
    print(update["data"])
```

------------------------------------------------------------------------

## EMSEngine (Order Management)

The EMSEngine module handles complete order management.

Supported markets: - TSE - IFB

------------------------------------------------------------------------

### EMSEngine Features

-   Buy/Sell by Name or ISIN
-   Edit Orders
-   Cancel/Delete Orders
-   Real-time Status
-   Async/Sync Compatibility
-   Order Object Lifecycle

------------------------------------------------------------------------

## Order Lifecycle

1.  Create Order
2.  Send
3.  Monitor Status
4.  Edit (Optional)
5.  Settle or Delete

------------------------------------------------------------------------

## Async Trading Example

``` python
from HedgeTech.EMSEngine import EmsEngine_TseIfb_AsyncClient

ems = EmsEngine_TseIfb_AsyncClient(auth_async_client)

captcha = await ems.Get_Captcha("Omex | Parsian")
captcha.show()

await ems.oms_login(
    username="user",
    password="pass",
    captcha_value="1234"
)

order = await ems.Buy_by_Name(
    symbolName="اطلس",
    Price=100000,
    Volume=10
)

await order.send()

status = await order.Status()
print(status)

await order.Edit(Price=105000, Volume=12)

await order.Delete()
```

------------------------------------------------------------------------

## Sync Trading Example

``` python
from HedgeTech.EMSEngine import EmsEngine_TseIfb_SyncClient

ems = EmsEngine_TseIfb_SyncClient(auth_sync_client)

captcha = ems.Get_Captcha("Omex | Parsian")
captcha.show()

ems.oms_login(
    username="user",
    password="pass",
    captcha_value="1234"
)

order = ems.Sell_by_Name(
    symbolName="فملی",
    Price=50000,
    Volume=5
)

order.send()

status = order.Status()
print(status)

order.Edit(Price=52000, Volume=6)

order.Delete()
```

------------------------------------------------------------------------

## Unified API Design

All Sync and Async clients share:

-   Same method names
-   Same parameters
-   Same return types

Only execution model differs.

This enables seamless switching between modes.

------------------------------------------------------------------------

## Error Handling

-   Invalid credentials raise ValueError
-   Network errors should be handled by user
-   Failed requests may return None

Recommended: wrap calls in try/except.

------------------------------------------------------------------------

## Performance

-   Non-blocking Async I/O
-   Connection pooling
-   Optimized request batching
-   Suitable for HFT and Algo Trading

------------------------------------------------------------------------

## Security

-   JWT Authentication
-   Encrypted Transport (HTTPS)
-   No password storage
-   Session isolation

------------------------------------------------------------------------

## Best Practices

-   Refresh tokens regularly
-   Monitor order status
-   Avoid duplicate send()
-   Validate inputs
-   Log critical operations

------------------------------------------------------------------------

## Modules Overview

### HedgeTech.Auth

Provides:

-   AuthAsyncClient
-   AuthSyncClient
-   Token management
-   Session handling

------------------------------------------------------------------------

### HedgeTech.DataEngine

Provides:

-   Market data APIs
-   Historical data
-   WebSocket feeds
-   Modular engine design

------------------------------------------------------------------------

### HedgeTech.EMSEngine

Provides:

-   EmsEngine_TseIfb_AsyncClient
-   EmsEngine_TseIfb_SyncClient
-   Order class
-   Lifecycle management

------------------------------------------------------------------------

## Roadmap

-   Auto session refresh
-   Smart retry system
-   Risk control module
-   Order batching
-   Metrics & Monitoring
-   Strategy framework

------------------------------------------------------------------------

## Contributing

We welcome contributions.

Guidelines:

-   Follow PEP8
-   Add tests
-   Update documentation
-   Submit Pull Requests

------------------------------------------------------------------------

## License

Licensed under Apache License 2.0.

See LICENSE file.

------------------------------------------------------------------------

## Support

GitHub Issues: https://github.com/HedgeTech-ir/HedgeTech/issues

Email: info@hedgetech.ir

------------------------------------------------------------------------

© 2026 HedgeTech. All rights reserved.
