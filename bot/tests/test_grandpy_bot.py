import urllib
from flask_testing import LiveServerTestCase

from .. import app


class TestGrand(LiveServerTestCase):

    def create_app(self):
        app.config.from_object('bot.tests.config')
        return app

    def test_server_is_up_and_running(self):
        """
        Test if the server is started.
        :return:
        """
        response = urllib.request.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

    def test_message(self):
        """
        Test that sending a message works
        :return:
        """

    def test_api_google_maps(self):
        """
        Test access to API of Google Maps
        :return:
        """

    def test_api_media_wiki(self):
        """
        Test access to API of media Wiki
        :return:
        """