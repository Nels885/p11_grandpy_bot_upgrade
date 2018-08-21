import requests

from config import *


class MediaWiki:

    def __init__(self, url):
        self.url = url

    def get_request(self, parameters):
        response = requests.get(self.url, params=parameters)
        data = response.json()
        print(data)
        return data

    def data_extract(self, key_works):
        # MediaWiki search
        parameters = WIKI_PARA_SEARCH
        parameters["srsearch"] = key_works
        data = self.get_request(parameters)
        page_id = str(data["query"]["search"][0]["pageid"])

        # Extracting data from the MediaWiki page
        parameters = WIKI_PARA_PAGE_ID
        parameters["pageids"] = page_id
        data = wiki.get_request(parameters)
        extract = data["query"]["pages"][0]["extract"]

        return extract[extract.find("==\n") + 2:].strip()
