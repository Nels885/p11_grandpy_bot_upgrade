import googlemaps

from ..controler import log


class GoogleMaps:

    def __init__(self, google_key):
        self.gooMaps = googlemaps.Client(key=google_key)
        self.geocode_result = None

    def geo_search(self, key_words):
        search = " ".join(key_words)
        self.geocode_result = self.gooMaps.geocode(search, language="fr")
        format_address = self.formatted_address()
        location = self.geo_location()
        log.info("GOOGLE_MAPS - OUT : ADDRESS : {} - LOCATION : {} - ROUTE : {}"
                 .format(format_address, location["geometry"], location["route"]))
        return format_address, location

    def formatted_address(self):
        return self.geocode_result[0]["formatted_address"]

    def geo_location(self):
        route = self.geocode_result[0]["address_components"][1]["long_name"]
        geo = self.geocode_result[0]["geometry"]["location"]
        return {'geometry': geo, 'route': route}
