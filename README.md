# LUSID<sup>®</sup> Notifications Python Preview SDK

![LUSID_by_Finbourne](https://content.finbourne.com/LUSID_repo.png)

| branch | status |
| --- | --- |
| `master` |  ![PyPI](https://img.shields.io/pypi/v/lusid-notifications-sdk-preview?color=blue)

## Installation

The PyPi package for the LUSID Notifications Preview SDK can installed using the following:

```
$ pip install lusid-notifications-sdk-preview finbourne-sdk-utilities
```

## Usage

```
import lusid_notifications
from fbnsdkutilities import ApiClientFactory

api_factory = ApiClientFactory(lusid_notifications, api_secrets_filename="secrets.json")
api = cls.api_factory.build(lusid_notifications.api.EventTypesApi)

response = self.api.list_event_types().values
print(response)
```
