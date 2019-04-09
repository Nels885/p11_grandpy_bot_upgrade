import requests
import json

from bot.package.openweathermap import OpenWeatherMap

from bot import app


class FakeResponse:
    def __init__(self, response):
        self.response = json.dumps(response)

    def json(self):
        return json.loads(self.response)


# noinspection PyAttributeOutsideInit,SpellCheckingInspection,PyUnusedLocal
class TestOpenWeatherMap:

    def setup_method(self):
        self.city = "Paris"
        self.country = "Fr"
        self.result = {
            "coord": {"lon": 6.29, "lat": 48.37},
            "weather": [{"id": 800, "main": "Clear", "description": "ciel dégagé", "icon": "01d"}],
            "main": {"temp": 5.32, "pressure": 1000, "humidity": 86, "temp_min": 4, "temp_max": 6.67},
            "wind": {"speed": 3.1, "deg": 240},
            "cod": 200,
        }
        app.config.from_object("config")
        self.weather = OpenWeatherMap(app.config["OWM_PARA"])

    def test_weather_result(self, monkeypatch):
        """
        Test if the API returns information through mocks
        :param monkeypatch: use mocks
        :return: FAILED if results are different from values
        """
        def mockreturn(api_url, params):
            return FakeResponse(self.result)

        monkeypatch.setattr(requests, "get", mockreturn)
        data = self.weather.result(self.city, self.country)
        assert data["temp"] == "5°C"
        assert data["desc"] == "ciel dégagé"

    def test_weather_icon(self, monkeypatch):
        """
        Test if the API returns icon through mocks
        :param monkeypatch: use mocks
        :return: FAILED if results are different from the icon link
        """
        def mockreturn(api_url, params):
            return FakeResponse(self.result)

        monkeypatch.setattr(requests, "get", mockreturn)
        data = self.weather.result(self.city, self.country)
        assert data["icon"] == "https://openweathermap.org/img/w/01d.png"

    def test_weather_no_result(self, monkeypatch):
        """
        Test if the API returns no result
        :param monkeypatch: use mocks
        :return: FAILED if results are different of None
        """
        def mockreturn(api_url, params):
            response = {'cod': '400', 'message': 'Nothing to geocode'}
            return FakeResponse(response)

        monkeypatch.setattr(requests, "get", mockreturn)
        data = self.weather.result("", "")
        assert data is None

    def test_temp_format(self):
        """
        Test if temperatures is formatted
        :return: FAILED if all temperatures is not formatted
        """
        data = self.result["main"]
        data = self.weather.temp_format(data)
        assert data["temp"] == "5°C"
        assert data["temp_min"] == "4°C"
        assert data["temp_max"] == "6°C"
