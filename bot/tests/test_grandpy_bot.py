import urllib
from flask_testing import LiveServerTestCase

from .. import app


class TestGrand(LiveServerTestCase):

    def create_app(self):
        app.config.from_object('bot.tests.config')
        return app

# test si le serveur est bien démarré.
    def test_server_is_up_and_running(self):
        response = urllib.request.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)
