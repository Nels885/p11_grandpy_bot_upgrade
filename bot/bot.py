from config import *
from .package.parser import *
from .package.mediawiki import data_extract


def bot_analysis(message):
    """
    ## Analysis of the question by GrandPy Bot
    :param message: User's question
    :return: GrandPy Bot's answer
    """
    msgs_bot = []
    # Parsing of user's message
    pars = Parser(STOP_WORDS_JSON, message)
    msg_bot, key_words = pars.msg_analysis()

    # search with keywords using google map and mediawiki APIs
    if len(key_words) != 0:
        msgs_bot.append(msg_bot + " La voici : 7 cité Paradis, 75010 Paris.")

        citation = data_extract("cité Paradis, Paris")
        print(citation)
        info_bot = "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? " + citation
        msgs_bot.append(info_bot)
    else:
        msgs_bot.append(msg_bot)

    return msgs_bot
