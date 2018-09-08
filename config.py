import os

"""
===============
Stop Words file
===============
"""
basedir = os.path.abspath(os.path.dirname(__file__))
STOP_WORDS_JSON = os.path.join(basedir, "fr.json")

"""
==========================
Parameters for Google Maps
==========================
"""
GOOGLE_KEY = "AIzaSyCOLBY258bj559lN6Isf6h7sTWVKqaTHnc"

"""
=================================
Different answers from GrandpyBot
=================================
"""
MSG_START = ["Bien sûr mon poussin ! La voici : {}.",
             "La voici mon seigneur : {}",
             "Cher(e) Anonyme, la réponse est : {}"]

INFO_BOT = ["Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? ",
            "J'ai une petite histoire à te raconter sur ce quartier. "]

MSG_BOT_ERROR = ["Je n'ai pas trouvé de réponse à votre question !! Êtes-vous sûr que ce lieu existe ?",
                 "Désolé mon poussin, je ne sais répondre qu'à des questions sur des lieux !!",
                 "Je ne comprends pas la question !! Êtes-vous sur ne pas avoir fait de fautes d'orthographe ?"]

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
