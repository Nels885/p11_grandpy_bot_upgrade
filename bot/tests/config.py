import os

"""
===============
Stop Words file
===============
"""
basedir = os.path.abspath(os.path.dirname(__file__))
STOP_WORDS_JSON = os.path.join(basedir, "fr.json")


"""
=======================================
Constants for Tests and active debugger
=======================================
"""
ENV = ""
DEBUG = True
TESTING = True
LIVESERVER_PORT = 8943
LIVESERVER_TIMEOUT = 10

KEY_WORDS = ["adresse", "openclassrooms"]
FORMATTED_ADDRESS = "7 Cité Paradis, 75010 Paris, France"
LOCATION = {'geometry': {'lng': 2.350564700000001, 'lat': 48.8747578}, 'route': "Cité Paradis"}

MSG_TEST_NO_RESULT = "Salut Grandpy Bot, comment vas-tu ?"
MSG_TEST_OC = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"


"""
==========================
Parameters for Google Maps
==========================
"""
GOOGLE_KEY = "<YOUR_GOOGLE_API_KEY>"


"""
=================================
Different answers from GrandpyBot
=================================
"""
MSG_START = ["Bien sûr mon poussin ! La voici : {}.",
             "La voici mon seigneur : {}",
             "Cher(e) Anonyme, la réponse est : {}"]

INFO_BOT = "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? "

MSG_BOT_ERROR = "Je n'ai pas trouvé de réponse à votre question !!"

MSG_BOT_ERROR_API = "Je suis désolé, je ne peux pas vous répondre pour le moment, mon cerveau est en surchauffe :( !!"


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
    "exsentences": "3",
    "format": "json",
    "formatversion": "2"
}
