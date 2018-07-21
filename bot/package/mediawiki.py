from config import *

from ..package.apirest import ApiRest


def data_extract(key_works):

    # MediaWiki search
    parameters = WIKI_PARA_SEARCH
    parameters["srsearch"] = key_works
    wiki = ApiRest(WIKI_URL)
    data = wiki.get_request(parameters)
    page_id = str(data["query"]["search"][0]["pageid"])

    # Extracting data from the MediaWiki page
    parameters = WIKI_PARA_PAGE_ID
    parameters["pageids"] = page_id
    data = wiki.get_request(parameters)
    extract = data["query"]["pages"][0]["extract"]

    return extract[extract.find("==\n") + 2:].strip()
