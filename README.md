HedgeTech Python SDK

HedgeTech Python SDK is a professional, lightweight, and modular Python package designed to provide seamless access to HedgeTech services. The SDK is crafted for developers, data analysts, and algorithmic traders who want to interact with the Tehran Stock Exchange (TSE & IFB) using a clean, reliable, and easy-to-use API. It supports both synchronous and asynchronous workflows, offering maximum flexibility and performance for different application scenarios.

## Features

* Secure authentication with both async and sync clients.
* Real-time and historical market data retrieval from TSE & IFB.
* Modular and maintainable architecture, designed to support multiple engines (DataEngine engines, etc.).
* Structured request and response types for robust data handling.
* Fully asynchronous support for high-performance applications.
* Easy to integrate into trading bots, analytics pipelines, dashboards, or WebSocket feeds.

## Installation

Install HedgeTech SDK via PyPI:

```
pip install HedgeTech
```

## Usage

The SDK exposes all major clients through the top-level modules, so you generally do **not** need to import internal files like `__AuthAsyncClient` or `__AuthSyncClient` directly.

### Authentication

> **Note:** Make sure to use the matching async or sync Auth client depending on your workflow.

#### Async Authentication

```python
from HedgeTech.Auth import AuthAsyncClient

auth_client = AuthAsyncClient(api_key="YOUR_API_KEY", secret="YOUR_SECRET")
await auth_client.login()
user_info = await auth_client.get_user_info()
print(user_info)
```

#### Sync Authentication

```python
from HedgeTech.Auth import AuthSyncClient

auth_client = AuthSyncClient(api_key="YOUR_API_KEY", secret="YOUR_SECRET")
auth_client.login()
user_info = auth_client.get_user_info()
print(user_info)
```

### DataEngine / TSE IFB

The DataEngine is structured to support multiple engines. Each engine can have its own async and sync clients, as well as IO types for requests and responses.

#### Async Data Client

```python
from HedgeTech.DataEngine.__tse_ifb import TSEAsyncClient

client = TSEAsyncClient(auth=auth_client)
data = await client.fetch_market_data(symbol="IRO1ABC0001")
print(data)
```

#### Sync Data Client

```python
from HedgeTech.DataEngine.__tse_ifb import TSESyncClient

client = TSESyncClient(auth=auth_client)
data = client.fetch_market_data(symbol="IRO1ABC0001")
print(data)
```

#### WebSocket Support (Example)

```python
from HedgeTech.DataEngine import TSEWebSocketClient

ws_client = TSEWebSocketClient(auth=auth_client)
await ws_client.connect()
await ws_client.subscribe(symbols=["IRO1ABC0001", "IRO1DEF0002"])
data = await ws_client.receive()
print(data)
```

## Modules Overview

### HedgeTech.Auth

Handles authentication for all HedgeTech clients. The async (`AuthAsyncClient`) and sync (`AuthSyncClient`) versions are exposed through the top-level Auth module.

### HedgeTech.DataEngine.__tse_ifb

Handles interactions with the Tehran Stock Exchange IFB. Includes:

* Async and sync clients for fetching market data.
* Structured request and response types for robust and predictable data handling.
* Designed for modular integration with other engines.

### HedgeTech.DataEngine

Top-level module that initializes engines and manages imports for clients. The modular design allows adding new engines such as WebSocket clients or other future DataEngines without changing the main interface.

## Contributing

We welcome contributions from the community! Please follow standard Python coding conventions, write clear documentation for any new features, and submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for full details.

## Support

For questions or issues, please open a GitHub issue or contact the HedgeTech team directly. We aim to provide timely support and guidance for all developers using the SDK.
