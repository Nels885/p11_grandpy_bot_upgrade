import os
import json

"""
===============
Open JSON file
===============
"""
basedir = os.path.abspath(os.path.dirname(__file__))
json_file = json.load(open(os.path.join(basedir, "data.json"), 'r'))

"""
=====================
STOP WORDS for Parser
=====================
"""
STOP_WORDS_JSON = json_file["stop_words"]

"""
==========================
Parameters for Google Maps
==========================
"""
GOOGLE_KEY = "AIzaSyCNrhKGidYieUtSEjnrf9ORt7MMXrTwO0U"

"""
=================================
Different answers from GrandpyBot
=================================
"""
MSG_START = json_file["msg_start"]
INFO_BOT = json_file["info_bot"]
MSG_BOT_ERROR = json_file["msg_bot_error"]
MSG_BOT_ERROR_API = json_file["msg_bot_error_api"]

"""
========================
Parameters for MediaWiki
========================
"""
WIKI_URL_JS = "https://fr.wikipedia.org/w/api.php?callback=?"
WIKI_URL = "https://fr.wikipedia.org/w/api.php?"

WIKI_PARA_SEARCH = {
    "action": "query",
    "list": "geosearch",
    "gsradius": "10000",
    "gslimit": "100",
    "format": "json",
    "formatversion": "2"
}

WIKI_PARA_PAGE_ID = {
    "action": "query",
    "prop": "extracts",
    "explaintext": "true",
    "exsectionformat": "plain",
    "exintro": "true",
    "exsentences": "3",
    "format": "json",
    "formatversion": "2"
}

"""
=============================
Parameters for OpenWeatherMap
=============================
"""

OWM_KEY = "445d3f698420610fbda4f8e32f9d92a5"

OWM_URL = "https://api.openweathermap.org/data/2.5/weather?"

OWN_PARA = {
    "appid": OWM_KEY,
}
