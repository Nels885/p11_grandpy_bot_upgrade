from config import *
from .package.parser import *
from .package.googlemaps import *

gmaps = googlemaps.Client(key=GOOGLE_KEY)

MSG_START = "Bien sûr mon poussin ! La voici : {}."
MSG_BOT_ERROR = "Je ne comprends pas la question !!"


def bot_analysis(message):
    """
    ## Analysis of the question by GrandPy Bot
    :param message: User's question
    :return: GrandPy Bot's answer
    """
    msgs_bot = []
    location = {}

    # Parsing of user's message
    pars = Parser(STOP_WORDS_JSON, message)
    key_words = pars.msg_analysis()

    # search with keywords using google map and mediawiki APIs
    if len(key_words) != 0 and "adresse" in key_words:

        gmaps = GoogleMaps(GOOGLE_KEY)
        format_address, location = gmaps.geo_search(key_words)

        msgs_bot.append(MSG_START.format(format_address))
        info_bot = "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? "
        msgs_bot.append(info_bot)
    else:
        msgs_bot.append(MSG_BOT_ERROR)

    return msgs_bot, location
