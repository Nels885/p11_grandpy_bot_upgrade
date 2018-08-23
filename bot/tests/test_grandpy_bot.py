from urllib import request
from flask_testing import LiveServerTestCase

from .. import app
from ..package.googlemaps import GoogleMaps
from ..package.parser import Parser
from ..grandpybot import grandpy_bot
from .config import *


class TestGrand(LiveServerTestCase):

    def create_app(self):
        app.config.from_object('bot.tests.config')
        return app

    def test_server_is_up_and_running(self):
        """
        Test if the server is started.
        :return:
        """
        response = request.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

    def test_grandpy_bot(self):
        """
        Test that sending a message works
        :return:
        """
        msg_bot, location = grandpy_bot(MSG_TEST)
        assert len(msg_bot) != 0 and len(location) == 0


class TestGoogleMaps:

    def setup_method(self):
        self.gmaps = GoogleMaps(GOOGLE_KEY)
        self.gmaps.geo_search(SEARCH)

    def test_formatted_address(self):
        """
        Test access to API of Google Maps
        :return: Fomatted address of the research
        """
        format_address = self.gmaps.formatted_address()
        assert format_address == FORMATTED_ADDRESS

    def test_location(self):
        """
        test access to API of Google Maps
        :return: location of the research in the dict format
        """
        location = self.gmaps.geo_location()
        assert location == LOCATION


class TestParser:

    def setup_method(self):
        self.parser = Parser(STOP_WORDS_JSON, MSG_TEST)

    def test_type_result(self):
        result = self.parser.msg_analysis()
        assert isinstance(result, list)

