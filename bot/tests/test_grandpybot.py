import pytest

from ..grandpybot import grandpy_bot
from .config import *


class TestGrandpyBot:

    def setup_method(self):
        self.route = "Cité Paradis"

    def test_grandpy_bot_no_result(self):
        """
        Test that sending a message works
        :return: return FAILED if msg_Bot doesn't exist and location si empty
        """
        msg_bot, location = grandpy_bot(MSG_TEST_NO_RESULT)
        assert len(msg_bot) != 0 and len(location['geometry']) == 0 and len(location['route']) == 0

    def test_grandpy_bot_result(self):
        """
        Test that we have a location result
        :return: return FAILED if route is different of 'Cité Paradis'
        """
        msg_bot, location = grandpy_bot(MSG_TEST_OC)
        assert location['route'] == self.route