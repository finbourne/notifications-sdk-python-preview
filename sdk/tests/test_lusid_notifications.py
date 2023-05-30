import logging
import unittest
import os

import lusid_notification
from fbnsdkutilities import ApiClientFactory


class MockApiResponse(object):
    def __init__(self, status=None):
        self.status = status
        self.headers = {}


class LusidNotificationsTests(unittest.TestCase):

    logger = None
    api_factory = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.INFO)


        if os.getenv("FBN_ACCESS_TOKEN", None) is not None:
            cls.api_factory = ApiClientFactory(lusid_notification, token=os.environ.get("FBN_ACCESS_TOKEN"))
        else:
            cls.api_factory = ApiClientFactory(lusid_notification, api_secrets_filename="secrets.json")

        cls.api = cls.api_factory.build(lusid_notification.api.EventTypesApi)

    def test_get_types(self):
        response = self.api.list_event_types().values
        self.assertGreaterEqual(len(response), 1)


if __name__ == '__main__':
    unittest.main()
