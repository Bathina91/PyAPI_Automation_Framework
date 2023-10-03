


import pytest

#payload, base url, verify

from src.constants.apiconstants import url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers
from src.helpers.Common_verification import *


class TestIntegrationTC1(object):


    def test_verify_create_booking_by_updating_deleting(self):
        pass

        # response = post_request(url_create_booking(), headers=common_headers(), auth=None,
        #                         payload=payload_create_booking(), in_json=False)
        # verify_bookingId_key(response.json()["bookingid"])
        # verify_http_code(response, expected_data=200)