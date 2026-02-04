# HedgeTech Python SDK

HedgeTech Python SDK is a professional, lightweight, and modular Python package designed to provide seamless access to HedgeTech services. The SDK is crafted for developers, data analysts, and algorithmic traders who want to interact with the Tehran Stock Exchange (TSE & IFB) using a clean, reliable, and easy-to-use API. It supports both synchronous and asynchronous workflows, offering maximum flexibility and performance for different application scenarios.

> **Note:** This SDK requires Python >= 3.10 and is currently in Beta. Some APIs may change in future releases, but it is stable enough for daily use.

## Features

* Secure authentication with both async and sync clients.
* Real-time and historical market data retrieval from TSE & IFB.
* Full EMS Engine order management (buy/sell, edit, status, delete) for both Sync and Async workflows.
* Modular and maintainable architecture, designed to support multiple engines (DataEngine engines, WebSocket clients, etc.).
* Structured request and response types for robust data handling.
* Fully asynchronous support for high-performance applications.
* Easy to integrate into trading bots, analytics pipelines, dashboards, or WebSocket feeds.

## Installation

Install HedgeTech SDK via PyPI:

```
pip install HedgeTech
```

### Updating the Package

To update HedgeTech SDK to the latest version in your environment, use:

```
pip install --upgrade HedgeTech
```

## Usage

The SDK exposes all major clients through the top-level modules, so you generally do **not** need to import internal implementation files directly.

## Authentication

> **Note:** Make sure to use the matching async or sync Auth client depending on your workflow.

### Async Authentication

```python
from HedgeTech.Auth import AuthAsyncClient

auth_async_client = await AuthAsyncClient.login(
    UserName_or_Email='<YOUR UserName_or_Email>',
    Password='<YOUR Password>'
)
print(auth_async_client.token)
```

### Sync Authentication

```python
from HedgeTech.Auth import AuthSyncClient

auth_sync_client = AuthSyncClient.login(
    UserName_or_Email='<YOUR UserName_or_Email>',
    Password='<YOUR Password>'
)
print(auth_sync_client.token)
```

## DataEngine / TSE IFB

The DataEngine is designed to support multiple engines in a modular way. Each engine provides its own async and sync clients, structured request and response types, and can be integrated with other engines such as WebSocket clients.

> **Important Note on Sync vs Async:** All clients have the **same method names and behavior** in both Sync and Async versions. The only difference is how they execute: Sync runs in a blocking manner, while Async requires `await` and an event loop. This design allows you to switch between Sync and Async without changing the logic or input/output of your code.

### Async Data Client

```python
from HedgeTech.DataEngine import DataEngine_TseIfb_AsyncClient

client = DataEngine_TseIfb_AsyncClient(auth_async_client)
data = await client.live_best_limit_by_isin(
    symbol_isins=['IRT1AHRM0001','IRO1IKCO0001']
)
print(data)

# websocket Example

async for update in client.websocket_by_name(
    channels=["best-limit", "order-book"],
    symbol_names=["فملی","اطلس"]
):
    print(update["data"])
```

### Sync Data Client

```python
from HedgeTech.DataEngine import DataEngine_TseIfb_SyncClient

client = DataEngine_TseIfb_SyncClient(auth_sync_client)
data = client.historical_ohlcv_by_name(
    symbolName='مهرگان',
    start_timestamp=0,
    end_timestamp='1763411432',
    AdjustedPrice=True,
    Resolution='D'
)
print(data)

# websocket Example

for update in client.websocket_by_isin(
    channels=["best-limit", "order-book"],
    symbol_isins=["IR1234567890"]
):
    print(update["data"])
```

## EMS Engine / Order Management

The SDK provides full **order lifecycle management** for TSE/IFB markets. You can create, edit, delete, and check the status of buy/sell orders with both Sync and Async clients.

### Features

* Create buy/sell orders by symbol name or ISIN.
* Edit orders (price, volume, validity type/date).
* Retrieve current order status including executed and remaining volume.
* Delete/cancel orders.
* Fully Async/Sync compatible with identical method names.

### Async Example

```python
from HedgeTech.EMSEngine import EmsEngine_TseIfb_AsyncClient

ems_client = EmsEngine_TseIfb_AsyncClient(auth_async_client)

# Login to OMS
await ems_client.oms_login("username", "password", "captcha_value")

# Create a buy order
order = await ems_client.Buy_by_Name(
    symbolName="اطلس",
    Price=100000,
    Volume=10
)
await order.send()

# Check status
status = await order.Status()
print(status)

# Edit order
await order.Edit(Price=105000, Volume=12)

# Delete order
await order.Delete()
print(order.is_deleted)  # True
```

### Sync Example

```python
from HedgeTech.EMSEngine import EmsEngine_TseIfb_SyncClient

ems_client = EmsEngine_TseIfb_SyncClient(auth_sync_client)

# Login to OMS
ems_client.oms_login("username", "password", "captcha_value")

# Create a sell order
order = ems_client.Sell_by_Name(
    symbolName="فملی",
    Price=50000,
    Volume=5
)
order.send()

# Check status
status = order.Status()
print(status)

# Edit order
order.Edit(Price=52000, Volume=6)

# Delete order
order.Delete()
print(order.is_deleted)  # True
```

> All methods for Async and Sync clients have the same parameters and naming for easy switching.

## Important Notes for Users

* This SDK requires Python >=3.10.
* The SDK is currently in **Beta** — APIs may change in future releases, but it is usable for most workflows.
* Always install dependencies with the specified versions to avoid compatibility issues.
* Async clients require an asyncio event loop.
* All main clients are exposed through top-level modules; you do not need to access internal files.
* Keywords and classifiers are chosen to make the SDK easy to find for developers working in finance, trading, and data analysis.

## Modules Overview

### HedgeTech.Auth

Handles authentication for all HedgeTech clients. The async (`AuthAsyncClient`) and sync (`AuthSyncClient`) clients are exposed through the top-level Auth module.

### HedgeTech.DataEngine

Handles interactions with the Tehran Stock Exchange IFB and other engines. Provides:

* Async and sync clients for fetching market data.
* Structured request and response types for predictable and robust data handling.
* Modular design that allows integration of additional engines, such as WebSocket clients or future data engines, without modifying the main interface.

### HedgeTech.EMSEngine

Handles TSE/IFB order management (EMS Engine):

* `EmsEngine_TseIfb_AsyncClient` / `EmsEngine_TseIfb_SyncClient`
* `Order` class for individual order lifecycle
* Methods: `Buy_by_Name`, `Sell_by_Name`, `Buy_by_isin`, `Sell_by_isin`, `Edit`, `Status`, `Delete`
* Fully compatible with both Async and Sync workflows

## Contributing

We welcome contributions from the community! Please follow standard Python coding conventions, write clear documentation for any new features, and submit pull requests for improvements or bug fixes.

## License

This project is licensed under the **Apache License 2.0**. See the LICENSE file for full details.

## Support

For questions or issues, please open a GitHub issue or contact the HedgeTech team directly. We aim to provide timely support and guidance for all developers using the SDK.
