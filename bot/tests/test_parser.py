import pytest

from ..package.parser import Parser
from .config import *


class TestParser:

    def setup_method(self):
        self.parser = Parser(STOP_WORDS_JSON, MSG_TEST_NO_RESULT)

    def test_type_result(self):
        """
        Test the type of result
        :return: return FAILED if type is different of list()
        """
        result = self.parser.msg_analysis()
        assert isinstance(result, list)

    def test_no_key_words(self):
        """
        Test the absence of keywords
        :return: return FAILED if result is different of 0
        """
        result = self.parser.msg_analysis()
        assert len(result) == 0

    def test_key_words_oc(self):
        """
        Test the keywords from OpenClassRooms
        :return: return FAILED if result is different of the list("adresse","openclassrooms")
        """
        self.parser = Parser(STOP_WORDS_JSON, MSG_TEST_OC)
        result = self.parser.msg_analysis()
        assert result == KEY_WORDS
