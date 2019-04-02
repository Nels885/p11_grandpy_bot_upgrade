import requests

from ..controller import log


class OpenWeatherMap:
    URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL_ICON = "https://openweathermap.org/img/w/"

    def __init__(self, params):
        self.params = params

    def result(self, city, country):
        if len(country) == 0:
            self.params["q"] = city.upper()
        else:
            self.params["q"] = city.upper() + "," + country.upper()
        data = self.get_request()
        temp = data["main"]["temp"]
        print("température: %d" % temp)
        return data

    def get_request(self):
        response = requests.get(self.URL, params=self.params)
        data = response.json()
        log.info("WEATHER - DATA : %s" % data)
        return data

    def icon(self, data):
        icon_id = data["weather"][0]["icon"]
        return self.URL_ICON + icon_id + ".png"

