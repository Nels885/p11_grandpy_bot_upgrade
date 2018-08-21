import googlemaps

from ..controler import log


class GoogleMaps:

    def __init__(self, google_key):
        self.gooMaps = googlemaps.Client(key=google_key)

    def geo_search(self, key_words):
        search = " ".join(key_words)
        geocode_result = self.gooMaps.geocode(search, language="fr")
        format_address = geocode_result[0]["formatted_address"]
        route_location = geocode_result[0]["address_components"][1]["long_name"]
        geo_location = geocode_result[0]["geometry"]["location"]
        log.warning(
            "Result address: %s - Result location: %s - Result route: %s" % (
            format_address, geo_location, route_location))
        location = {'geometry': geo_location, 'route': route_location}
        return format_address, location
