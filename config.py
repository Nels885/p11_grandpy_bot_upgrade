import os


SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

basedir = os.path.abspath(os.path.dirname(__file__))

# Stop Words file
STOP_WORDS_JSON = os.path.join(basedir, 'fr.json')

# Parameters for MediaWiki
WIKI_URL = "https://fr.wikipedia.org/w/api.php?"
WIKI_PARA_SEARCH = {
    "action": "query",
    "list": "search",
    "srlimit": "1",
    "format": "json",
    "formatversion": "2"
}
WIKI_PARA_PAGE_ID = {
    "action": "query",
    "prop": "extracts",
    "explaintext": "true",
    "exsentences": "3",
    "format": "json",
    "formatversion": "2"
}