from ..package.parser import Parser
from .config import MSG_TEST_NO_RESULT, MSG_TEST_OC, KEY_WORDS_TEST

from .. import app


class TestParser:

    def setup_method(self):
        stop_words = app.config["STOP_WORDS_JSON"]
        self.parser = Parser(stop_words)

    def test_type_result(self):
        """
        Test the type of result
        :return: return FAILED if type is different of list()
        """
        result = self.parser.msg_analysis(MSG_TEST_NO_RESULT[0])
        assert isinstance(result, list)

    def test_no_key_words(self):
        """
        Test the absence of keywords
        :return: return FAILED if result is different of 0
        """
        for msg_test in MSG_TEST_NO_RESULT:
            result = self.parser.msg_analysis(msg_test)
            assert len(result) == 0

    def test_key_words_oc(self):
        """
        Test the keywords from OpenClassRooms
        :return: return FAILED if result is different of the list("adresse","openclassrooms")
        """
        for msg_test in MSG_TEST_OC:
            result = self.parser.msg_analysis(msg_test)
            assert result == KEY_WORDS_TEST
