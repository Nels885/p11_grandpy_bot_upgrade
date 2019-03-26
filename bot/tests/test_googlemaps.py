from ..package.googlemaps import GoogleMaps
from .config import KEY_WORDS, FORMATTED_ADDRESS, LOCATION

from .. import app


class TestGoogleMaps:

    def setup_method(self):
        self.results = [{
                    "address_components": [{"long_name": "7"}, {"long_name": "Cité Paradis"}],
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
        script.geo_search(KEY_WORDS)
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
        script.geo_search(KEY_WORDS)
        assert len(script.format_address) == 0 and len(script.location["geometry"]) == 0

    def test_api_no_key_words(self):
        """
        Test the API if there are no keywords
        :return: FAILED if different to 0
        """
        script = self.gmaps
        script.geo_search("")
        assert len(script.format_address) == 0 and len(script.location["geometry"]) == 0
