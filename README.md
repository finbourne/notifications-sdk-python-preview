# LUSID<sup>®</sup> Notification Python Preview SDK

![LUSID_by_Finbourne](https://content.finbourne.com/LUSID_repo.png)

| branch | status |
| --- | --- |
| `master` |  ![PyPI](https://img.shields.io/pypi/v/lusid-notifications-sdk-preview?color=blue)

## Installation

The PyPi package for the LUSID Notification Preview SDK can installed using the following:

```
$ pip install lusid-notification-sdk-preview finbourne-sdk-utilities
```

## Usage

```
import lusid_notification
from fbnsdkutilities import ApiClientFactory

api_factory = ApiClientFactory(lusid_notification, api_secrets_filename="secrets.json")
event_types_api = api_factory.build(lusid_notification.api.EventTypesApi)

response = event_types_api.list_event_types().values
print(response)
```
