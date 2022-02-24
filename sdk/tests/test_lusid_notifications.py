import logging
import unittest

import lusid_notifications
from fbnsdkutilities import ApiClientFactory


class MockApiResponse(object):
     def __init__(self, status=None):
         self.status = status
         self.headers = {}


class LusidNotificationsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.INFO)

        cls.api_factory = ApiClientFactory(lusid_notifications, api_secrets_filename="secrets.json")
        cls.api = cls.api_factory.build(lusid_notifications.api.EventTypesApi)

    def test_get_types(self):

        response = self.api.list_event_types().values
        self.assertEqual(1, len(response))  


if __name__ == '__main__':
    unittest.main()
