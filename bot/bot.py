import googlemaps

from config import *
from .package.parser import *

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
    geo_location = None
    # Parsing of user's message
    pars = Parser(STOP_WORDS_JSON, message)
    key_words = pars.msg_analysis()

    # search with keywords using google map and mediawiki APIs
    if len(key_words) != 0 and "adresse" in key_words:
        search = "+".join(key_words)
        # geocode_result = gmaps.geocode(search)
        geocode_result = gmaps.geocode(search, language="fr")
        addr_result = geocode_result[0]["formatted_address"]
        geo_location = geocode_result[0]["geometry"]["location"]
        route_result = geocode_result[0]["address_components"][1]["long_name"]
        log.warning(
            "Result address: %s - Result location: %s - Result route: %s" % (addr_result, geo_location, route_result))

        msgs_bot.append(MSG_START.format(addr_result))
        info_bot = "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? "
        msgs_bot.append(info_bot)
    else:
        msgs_bot.append(MSG_BOT_ERROR)

    return msgs_bot, geo_location
