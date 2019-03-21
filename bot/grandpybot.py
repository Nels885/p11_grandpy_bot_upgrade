from random import randint

from config import *
from .package.parser import Parser
from .package.googlemaps import GoogleMaps
from .controller import log


def grandpy_bot(message):
    """
    ## Analysis of the question by GrandPy Bot
    :param message: User's question
    :return: GrandPy Bot's answer
    """
    msgs_bot = []

    # Parsing of user's message
    pars = Parser(STOP_WORDS_JSON, message)
    key_words = pars.msg_analysis()

    # search with keywords using google map and mediawiki APIs
    gmaps = GoogleMaps(GOOGLE_KEY)
    if len(key_words) != 0:
        gmaps.geo_search(key_words)
        msgs_bot.append(random_msg_start(MSG_START).format(gmaps.format_address))
        msgs_bot.append(random_msg_start(INFO_BOT))
    else:
        msgs_bot.append(random_msg_start(MSG_BOT_ERROR))

    log.info("GRANDY_BOT - ANSWERS : %s - LOCATION : %s" % (msgs_bot, gmaps.location))
    return msgs_bot, gmaps.location


def random_msg_start(msg):
    """
    ## Choose a random GrandPy Bot answer
    :param msg: Answers lists
    :return: Answer chosen
    """
    number = randint(0, len(msg) - 1)
    return msg[number]
