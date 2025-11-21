HedgeTech Python SDK

HedgeTech Python SDK is a professional, lightweight, and modular Python package designed to provide seamless access to HedgeTech services. The SDK is crafted for developers, data analysts, and algorithmic traders who want to interact with the Tehran Stock Exchange (TSE) using a clean, reliable, and easy-to-use API. It supports both synchronous and asynchronous workflows, offering maximum flexibility and performance for different application scenarios.

## Features

* Secure authentication with both async and sync clients.
* Real-time and historical market data retrieval from TSE.
* Modular and maintainable architecture.
* Structured request and response types for robust data handling.
* Fully asynchronous support for high-performance applications.
* Easy to integrate into trading bots, analytics pipelines, and dashboards.

## Installation

Install HedgeTech SDK via PyPI:

```
pip install HedgeTech
```

## Usage

## Authentication

### Async Authentication

```python
from HedgeTech.Auth import AuthAsyncClient

auth_client = AuthAsyncClient(api_key="YOUR_API_KEY", secret="YOUR_SECRET")
await auth_client.login()
user_info = await auth_client.get_user_info()
print(user_info)
```

### Sync Authentication

```python
from HedgeTech.Auth import AuthSyncClient

auth_client = AuthSyncClient(api_key="YOUR_API_KEY", secret="YOUR_SECRET")
auth_client.login()
user_info = auth_client.get_user_info()
print(user_info)
```

## DataEngine / TSE IFB

### Async Data Client

```python
from HedgeTech.DataEngine import TSEAsyncClient

client = TSEAsyncClient(auth=auth_client)
data = await client.fetch_market_data(symbol="IRO1ABC0001")
print(data)
```

### Sync Data Client

```python
from HedgeTech.DataEngine import TSESyncClient

client = TSESyncClient(auth=auth_client)
data = client.fetch_market_data(symbol="IRO1ABC0001")
print(data)
```

## Modules Overview

### HedgeTech.Auth

Handles all authentication-related operations. Provides both async (`AuthAsyncClient`) and sync (`AuthSyncClient`) interfaces. Ensures secure and reliable login, token management, and user information retrieval.

### HedgeTech.DataEngine.__tse_ifb

Handles all interactions with the Tehran Stock Exchange IFB. Includes:

* Async and sync clients for fetching market data.
* Structured request and response types for robust and predictable data handling.
* Methods for fetching historical and live trading data.
* Designed for scalable, maintainable integration into larger projects.

### HedgeTech.DataEngine

Top-level module that initializes the DataEngine and manages imports for TSE clients. Provides clean and simple access to the underlying async and sync interfaces.

## Contributing

We welcome contributions from the community! Please follow standard Python coding conventions, write clear documentation for any new features, and submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for full details.

## Support

For questions or issues, please open a GitHub issue or contact the HedgeTech team directly. We aim to provide timely support and guidance for all developers using the SDK.
