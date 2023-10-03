'''
Author: Pramod
Objective: Create and Verify by Post Request
TC#1 - Verify the Status Code, Headers
TC#2 - Verify the Body --> Booking ID
TC#3 - Verify the JSON Schema is Valid
'''

import pytest

#payload, base url, verify

from src.constants.apiconstants import url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers
from src.helpers.Common_verification import *


class TestIntegration(object):

    def test_create_booking_tc1(self):
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_bookingId_key(response.json()["bookingid"])
        verify_http_code(response, expected_data=200)


    # def test_create_booking_tc2(self):
    #     assert True == False
    #
    # def test_create_booking_tc3(self):
    #     assert True == True
