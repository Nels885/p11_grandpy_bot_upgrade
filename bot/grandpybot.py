from random import randint

from config import *
from .package.parser import *
from .package.googlemaps import *
from .controler import log


def grandpy_bot(message):
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

        msgs_bot.append(random_msg_start(MSG_START).format(format_address))
        msgs_bot.append(INFO_BOT)
    else:
        msgs_bot.append(MSG_BOT_ERROR)

    log.info("GRANDY_BOT - ANSWERS : %s" % msgs_bot)
    return msgs_bot, location


def random_msg_start(msg):
    number = randint(0, len(msg) - 1)
    return msg[number]
