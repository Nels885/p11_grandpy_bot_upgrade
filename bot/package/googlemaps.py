import googlemaps

from ..controler import log


class GoogleMaps:

    def __init__(self, google_key):
        self.gooMaps = googlemaps.Client(key=google_key)
        self.geocode_result = []
        self.format_address = ""
        self.location = {'geometry': '', 'route': ''}
        self.error = True

    def geo_search(self, key_words):
        if len(key_words) != 0:
            search = " ".join(key_words)
            self.geocode_result = self.gooMaps.geocode(search)
            log.info("GOOGLE_MAPS - RESULT : {}".format(self.geocode_result))
            self.formatted_address()
            self.geo_location()
            log.info("GOOGLE_MAPS - OUT : ADDRESS : {} - LOCATION : {} - ROUTE : {}"
                     .format(self.format_address, self.location["geometry"], self.location["route"]))
        else:
            self.error = False
        return self.error

    def formatted_address(self):
        if len(self.geocode_result) != 0:
            self.format_address = self.geocode_result[0]["formatted_address"]
        else:
            self.error = False

    def geo_location(self):
        if len(self.geocode_result) != 0:
            route = self.geocode_result[0]["address_components"][1]["long_name"]
            geo = self.geocode_result[0]["geometry"]["location"]
            self.location = {'geometry': geo, 'route': route}
        else:
            self.error = False
