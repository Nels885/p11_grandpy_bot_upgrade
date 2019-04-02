from ..grandpybot import grandpy_bot, gmaps
from .config import MSG_TEST_NO_RESULT, MSG_TEST_OC

from .. import app


class TestGrandpyBot:

    def setup_method(self):
        self.route = "Cité Paradis"
        self.address = "7 Cité Paradis, 75010 Paris, France"
        self.location = {'geometry': {"lng": 2.350564700000001, "lat": 48.8747578}, 'route': "Cité Paradis"}

    def test_grandpy_bot_result(self, monkeypatch):
        """
        Test that we have a location result
        :return: return FAILED if route is different of 'Cité Paradis'
        """
        for msgTestOc in MSG_TEST_OC:

            def mockreturn(grandpybot):
                gmaps.location = self.location
                gmaps.format_address = self.address
                return True
            monkeypatch.setattr(gmaps, "geo_search", mockreturn)

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
            assert len(location['geometry']) == 0 and len(location['route']) == 0

    def test_grandpy_bot_message(self, monkeypatch):
        """

        :return: return FAILED if route is different of 'Cité Paradis'
        """
        for msg in MSG_TEST_NO_RESULT:
            msg_bot, location, weath = grandpy_bot(msg)
            assert msg_bot[0] in app.config["MSG_BOT_ERROR"]
        for msgTestOc in MSG_TEST_OC:

            def mockreturn(grandpybot):
                gmaps.location = self.location
                gmaps.format_address = self.address
                return True
            monkeypatch.setattr(gmaps, "geo_search", mockreturn)

            msg_bot, location, weath = grandpy_bot(msgTestOc)
            assert location['route'] == self.route
            assert msg_bot[0] not in app.config["MSG_BOT_ERROR"]
