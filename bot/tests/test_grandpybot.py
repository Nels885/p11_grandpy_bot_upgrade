import pytest

from ..grandpybot import grandpy_bot
from .config import *


class TestGrandpyBot:

    def setup_method(self):
        pass

    def test_grandpy_bot_no_result(self):
        """
        Test that sending a message works
        :return:
        """
        msg_bot, location = grandpy_bot(MSG_TEST_NO_RESULT)
        assert len(msg_bot) != 0 and len(location['geometry']) == 0 and len(location['route']) == 0

    def test_grandpy_bot_result(self):
        """

        :return:
        """
        msg_bot, location = grandpy_bot(MSG_TEST_OC)
        assert location['route'] == "Cité Paradis"