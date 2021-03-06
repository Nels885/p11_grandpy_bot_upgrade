from bot.grandpybot import grandpy_bot, gmaps
from .config import MSG_TEST_NO_RESULT, MSG_TEST_OC, LOCATION, FORMATTED_ADDRESS

from bot import app


def mock_geo_search(key_words):
    gmaps.location = LOCATION[0]
    gmaps.format_address = FORMATTED_ADDRESS[0]
    return True


class TestGrandpyBot:

    def setup_method(self):
        self.route = "Cité Paradis"

    def test_grandpy_bot_result(self, monkeypatch):
        """
        Test that we have a location result
        :return: return FAILED if route is different of 'Cité Paradis'
        """
        for msgTestOc in MSG_TEST_OC:

            monkeypatch.setattr(gmaps, "geo_search", mock_geo_search)

            msg_bot, location, weath = grandpy_bot(msgTestOc)
            assert location['route'] == self.route
            assert msg_bot[0] not in app.config["MSG_BOT_ERROR"]

    def test_grandpy_bot_no_result(self):
        """
        Test that sending a message works
        :return: return FAILED if msg_Bot doesn't exist and location si empty
        """
        for msg in MSG_TEST_NO_RESULT:
            msg_bot, location, weath = grandpy_bot(msg)
            assert msg_bot[0] in app.config["MSG_BOT_ERROR"]
            assert location is None

    def test_grandpy_bot_message(self, monkeypatch):
        """

        :return: return FAILED if route is different of 'Cité Paradis'
        """
        for msg in MSG_TEST_NO_RESULT:
            msg_bot, location, weath = grandpy_bot(msg)
            assert msg_bot[0] in app.config["MSG_BOT_ERROR"]
        for msgTestOc in MSG_TEST_OC:

            monkeypatch.setattr(gmaps, "geo_search", mock_geo_search)

            msg_bot, location, weath = grandpy_bot(msgTestOc)
            assert location['route'] == self.route
            assert msg_bot[0] not in app.config["MSG_BOT_ERROR"]
