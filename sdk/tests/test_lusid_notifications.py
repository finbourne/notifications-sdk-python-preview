import unittest
import json
import logging
import os
from unittest.mock import patch, Mock

import lusid_notifications
from lusid_notifications import EventTypesApi
from lusid_notifications.utilities import ApiClientFactory
from lusid_notifications.utilities import ApiConfigurationLoader

class MockApiResponse(object):
     def __init__(self, status=None):
         self.status = status
         self.headers = {}


class LusidNotificationsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.INFO)

        config = ApiConfigurationLoader.load("secrets.json")

        cls.api_factory = ApiClientFactory(token=config.api_token, api_url=config.drive_url)
        cls.api = cls.api_factory.build(lusid_notifications.api.EventTypesApi)

    def test_get_types(self):

        response = self.api.get_event_types().values
        self.assertEqual(2, len(response))  


if __name__ == '__main__':
    unittest.main()
