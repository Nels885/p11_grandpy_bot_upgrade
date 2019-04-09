import googlemaps

from ..controller import log


class GoogleMaps:

    def __init__(self, google_key):
        """
        ## Initialize class GoogleMaps
        :param google_key: API_KEY for Google Cloud Platform
        """
        self.gooMaps = googlemaps.Client(key=google_key)
        self.geocode_result = []
        self.format_address = ""
        self.location = None
        self.error = True

    def geo_search(self, key_words):
        """
        ## Search geolocation of a place
        :param key_words: keywords to do research
        :return: Booleen based on information found by geocoding API
        """
        self.error = True
        self.location = None
        if len(key_words) != 0:
            search = " ".join(key_words)
            self.geocode_result = self.gooMaps.geocode(search)
            log.info("GOOGLE_MAPS - RESULT : {}".format(self.geocode_result))
            self._formatted_address()
            self._geo_location()
            log.info("GOOGLE_MAPS - OUT : ADDRESS : {} - LOCATION : {}"
                     .format(self.format_address, self.location))
        else:
            self.error = False
        return self.error

    def _formatted_address(self):
        """
        ## Format address of place
        :return: String of address
        """
        if len(self.geocode_result) != 0:
            self.format_address = self.geocode_result[0]["formatted_address"]
        else:
            self.error = False

    def _geo_location(self):
        """
        ## Format location of place
        :return: Dict with geometry and route
        """
        if len(self.geocode_result) != 0:
            route = city = country = None
            for component in self.geocode_result[0]["address_components"]:
                if component["types"][0] in ["route", "establishment", "park", "point_of_interest"]:
                    route = component["long_name"]
                if component["types"][0] == "locality":
                    city = component["long_name"]
                if component["types"][0] == "country":
                    country = component["short_name"]

            geo = self.geocode_result[0]["geometry"]["location"]
            self.location = {'geometry': geo, 'route': route, 'city': city, 'country': country}
        else:
            self.error = False
