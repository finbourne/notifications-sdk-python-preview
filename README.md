![LUSID_by_Finbourne](./resources/Finbourne_Logo_Teal.svg)

# Deprecated

Please note that this repository is deprecated and will be archived early 2024.

All functionality is now contained, in the [notifications-sdk-python](https://github.com/finbourne/notifications-sdk-python) repository on the `main` branch.

# LUSID<sup>®</sup> Notifications Python Preview SDK

![PyPI](https://img.shields.io/pypi/v/lusid-notifications-sdk-preview?color=blue)

## Installation

The PyPi package for the LUSID Notifications Preview SDK can installed using the following:

```
$ pip install lusid-notifications-sdk-preview finbourne-sdk-utilities
```

## Usage

```
import lusid_notifications
from fbnsdkutilities import ApiClientFactory

api_factory = ApiClientFactory(lusid_notifications, api_secrets_filename="secrets.json")
event_types_api = api_factory.build(lusid_notifications.api.EventTypesApi)

response = event_types_api.list_event_types().values
print(response)
```
