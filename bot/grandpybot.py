from random import randint

from config import STOP_WORDS_JSON, GOOGLE_KEY, MSG_START, INFO_BOT, MSG_BOT_ERROR, OWM_PARA
from .package.parser import Parser
from .package.googlemaps import GoogleMaps
from .package.openweathermap import OpenWeatherMap
from .controller import log

pars = Parser(STOP_WORDS_JSON)
gmaps = GoogleMaps(GOOGLE_KEY)
weather = OpenWeatherMap(OWM_PARA)


def grandpy_bot(message):
    """
    ## Analysis of the question by GrandPy Bot
    :param message: User's question
    :return: GrandPy Bot's answer
    """
    msgs_bot = []
    weath = None
    # Parsing of user's message
    key_words = pars.msg_analysis(message)

    # search with keywords using google map and mediawiki APIs
    if gmaps.geo_search(key_words):
        msgs_bot.append(random_msg_start(MSG_START).format(address=gmaps.format_address))
        msgs_bot.append(random_msg_start(INFO_BOT))
        weath = weather.result(gmaps.location["city"], gmaps.location["country"])
    else:
        msgs_bot.append(random_msg_start(MSG_BOT_ERROR))

    log.info("GRANDY_BOT - ANSWERS : %s - LOCATION : %s" % (msgs_bot, gmaps.location))
    return msgs_bot, gmaps.location, weath


def random_msg_start(msg):
    """
    ## Choose a random GrandPy Bot answer
    :param msg: Answers lists
    :return: Answer chosen
    """
    number = randint(0, len(msg) - 1)
    return msg[number]
