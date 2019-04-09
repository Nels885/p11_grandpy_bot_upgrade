from bot.package.googlemaps import GoogleMaps
from .config import RESULT, KEY_WORDS_TEST, FORMATTED_ADDRESS, LOCATION

from bot import app


# noinspection PyAttributeOutsideInit,SpellCheckingInspection
class TestGoogleMaps:

    def setup_method(self):
        app.config.from_object("config")
        self.gmaps = GoogleMaps(app.config["GOOGLE_KEY"])

    def test_api_return_openclassrooms_values(self, monkeypatch):
        """
        Test if the API returns information through mocks
        :param monkeypatch: use mocks
        :return: FAILED if results are different from values in config.py
        """
        script = self.gmaps

        def mock_geocode(address):
            return RESULT[0]

        monkeypatch.setattr(script.gooMaps, "geocode", mock_geocode)
        script.geo_search(KEY_WORDS_TEST[0])
        assert script.format_address == FORMATTED_ADDRESS[0] and script.location == LOCATION[0]

    def test_api_return_liberty_statue_values(self, monkeypatch):
        """
        Test if the API returns information through mocks
        :param monkeypatch: use mocks
        :return: FAILED if results are different from values in config.py
        """
        script = self.gmaps

        def mock_geocode(address):
            return RESULT[1]

        monkeypatch.setattr(script.gooMaps, "geocode", mock_geocode)
        script.geo_search(KEY_WORDS_TEST[1])
        assert script.format_address == FORMATTED_ADDRESS[1] and script.location == LOCATION[1]

    def test_api_no_found(self, monkeypatch):
        """
        Test if The API is no found
        :param monkeypatch: use mocks
        :return: FAILED if different to 0
        """
        script = self.gmaps

        def mock_geocode(address):
            return []

        monkeypatch.setattr(script.gooMaps, "geocode", mock_geocode)
        script.geo_search(KEY_WORDS_TEST[0])
        assert len(script.format_address) == 0 and script.location is None

    def test_api_no_key_words(self):
        """
        Test the API if there are no keywords
        :return: FAILED if different to 0
        """
        script = self.gmaps
        script.geo_search("")
        assert len(script.format_address) == 0 and script.location is None

    def test_geo_search_error(self):
        """
        Test if heo_search function return error
        :return: FAILED if different de False
        """
        script = self.gmaps
        script.geo_search([])
        assert not script.error
