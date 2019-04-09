from bot.package.googlemaps import GoogleMaps
from .config import KEY_WORDS_TEST, FORMATTED_ADDRESS, LOCATION

from bot import app


# noinspection PyAttributeOutsideInit,SpellCheckingInspection
class TestGoogleMaps:

    def setup_method(self):
        self.results = [{
                    "address_components": [
                        {"long_name": "7"}, {"long_name": "Cité Paradis"}, {"long_name": "Paris"},
                        {"long_name": "Arrondissement de Paris"}, {"long_name": "Île-de-France"}, {"short_name": "FR"}
                    ],
                    "geometry": {"location": {"lng": 2.350564700000001, "lat": 48.8747578}, "route": "Cité Paradis"},
                    "formatted_address": "7 Cité Paradis, 75010 Paris, France",
                    }]
        app.config.from_object("config")
        self.gmaps = GoogleMaps(app.config["GOOGLE_KEY"])

    def test_api_return(self, monkeypatch):
        """
        Test if the API returns information through mocks
        :param monkeypatch: use mocks
        :return: FAILED if results are different from values in config.py
        """
        script = self.gmaps

        def mockreturn(gooMaps):
            return self.results

        monkeypatch.setattr(script.gooMaps, "geocode", mockreturn)
        script.geo_search(KEY_WORDS_TEST)
        assert script.format_address == FORMATTED_ADDRESS and script.location == LOCATION

    def test_api_no_found(self, monkeypatch):
        """
        Test if The API is no found
        :param monkeypatch: use mocks
        :return: FAILED if different to 0
        """
        script = self.gmaps

        def mockreturn(gooMaps):
            return []

        monkeypatch.setattr(script.gooMaps, "geocode", mockreturn)
        script.geo_search(KEY_WORDS_TEST)
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
