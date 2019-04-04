import requests

from ..controller import log


class OpenWeatherMap:
    URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL_ICON = "https://openweathermap.org/img/w/"

    def __init__(self, params):
        self.params = params

    def result(self, city, country):
        """
        ## Shows the different values of the weather for the city you are looking for
        :param city: Name of the city sought
        :param country: Name of the country
        :return: Weather data dictionary
        """
        data = self.get_request(city, country)
        if data["cod"] == 200:
            weather = dict([
                ("desc", data["weather"][0]["description"]),
                ("icon", self.icon(data)),
            ])
            weather.update(data["main"])
            weather = self.temp_format(weather)
            log.info("WEATHER - RESULT : %s" % weather)
            return weather
        return None

    def get_request(self, city, country):
        """
        ## Queries to the OpenWeatherMap API
        :param city: Name of the city sought
        :param country: Name of the country
        :return: Raw data in json format
        """
        if len(country) == 0:
            self.params["q"] = city.upper()
        else:
            self.params["q"] = city.upper() + "," + country.upper()
        response = requests.get(self.URL, params=self.params)
        data = response.json()
        log.info("WEATHER - DATA : %s" % data)
        return data

    def icon(self, data):
        """
        ## Get the link to the icon that corresponds to the weather
        :param data: Raw data in json format
        :return: Icon link OpenWeatherMap
        """
        icon_id = data["weather"][0]["icon"]
        return self.URL_ICON + icon_id + ".png"

    @staticmethod
    def temp_format(data):
        for key, value in data.items():
            if "temp" in key:
                data[key] = "%d°C" % value
        return data
