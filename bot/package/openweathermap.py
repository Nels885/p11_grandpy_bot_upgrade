import requests

from ..controller import log


class OpenWeatherMap:

    def __init__(self, url, key):
        self.url = url
        self.key = key

    def result(self, city, country):
        parameters = {
            "q": city + "," + country,
            "appid": self.key
        }
        return self.get_request(parameters)

    def get_request(self, parameters):
        response = requests.get(self.url, params=parameters)
        data = response.json()
        log.info("WEATHER - DATA : %s" % data)
        return data
