from urllib import request
from flask_testing import LiveServerTestCase, TestCase

from .. import app


class TestController(LiveServerTestCase, TestCase):

    render_templates = False

    def create_app(self):
        self.headers = {"content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
        app.config.from_object("bot.tests.config")
        return app

    def test_server_is_up_and_running(self):
        """
        Test if the server is started.
        :return: return FAILED if different from code 200
        """
        response = request.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

    def test_html_slash(self):
        """
        test the template index.html
        :return: return FAILED if index.html isn't used
        """
        response = self.client.get("/")
        assert "" != response.data

    def test_html_index(self):
        """
        test the template index.html
        :return: return FAILED if index.html isn't used
        """
        response = self.client.get("/index/")
        assert "" != response.data

    def test_msg_bot_invalid_content_type(self):
        """
        Test if invalid Content-Type
        :return: return FAILED if different from code 400
        """
        response = self.client.post("/")
        self.assertEqual(response.status_code, 400)

    def test_msg_bot_invalid_request(self):
        """
        Test if invalid request
        :return: return FAILED if different from code 405
        """
        response = self.client.post("/", headers=self.headers)
        self.assertEqual(response.status_code, 405)

    def test_msg_bot_valid_form(self):
        """
        Test if valid request
        :return: return FAILED if different from code 200
        """
        params = {"content": "test"}
        response = self.client.post("/", data=params, headers=self.headers)
        self.assertEqual(response.status_code, 200)




