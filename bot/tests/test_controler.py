import pytest

from urllib import request
from flask_testing import LiveServerTestCase, TestCase

from .. import app


class TestControler(LiveServerTestCase, TestCase):

    def create_app(self):
        self.headers = {"content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
        app.config.from_object('bot.tests.config')
        return app

    def test_server_is_up_and_running(self):
        """
        Test if the server is started.
        :return: return FAILED if
        """
        response = request.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

    def test_msg_bot_invalid_content_type(self):
        response = self.client.post("/")
        self.assertEqual(response.status_code, 400)

    def test_msg_bot_invalid_request(self):
        response = self.client.post("/", headers=self.headers)
        self.assertEqual(response.status_code, 405)

    def test_msg_bot_valid_form(self):
        params = {"content": "test"}
        response = self.client.post("/", data=params, headers=self.headers)
        self.assertEqual(response.status_code, 200)




