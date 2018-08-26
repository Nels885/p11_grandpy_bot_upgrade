import pytest

from ..package.googlemaps import GoogleMaps
from .config import *


class TestGoogleMaps:

    def setup_method(self):
        self.results = [{
                    "address_components": [{"long_name": "7"}, {"long_name": "Cité Paradis"}],
                    "geometry": {"location": {"lng": 2.350564700000001, "lat": 48.8747578}, "route": "Cité Paradis"},
                    "formatted_address": "7 Cité Paradis, 75010 Paris, France",
                    }]
        self.gmaps = GoogleMaps(GOOGLE_KEY)

    def test_api_return(self, monkeypatch):
        script = self.gmaps

        def mockreturn(gooMaps):
            return self.results

        monkeypatch.setattr(script.gooMaps, 'geocode', mockreturn)
        script.geo_search(KEY_WORDS)
        assert script.format_address == FORMATTED_ADDRESS and script.location == LOCATION

    def test_api_no_found(self, monkeypatch):
        script = self.gmaps

        def mockreturn(gooMaps):
            return []

        monkeypatch.setattr(script.gooMaps, 'geocode', mockreturn)
        script.geo_search(KEY_WORDS)
        assert len(script.format_address) == 0 and len(script.location['geometry']) == 0

    def test_api_no_key_words(self):
        script = self.gmaps
        script.geo_search("")
        assert len(script.format_address) == 0 and len(script.location['geometry']) == 0
