from config import *
from .package.parser import *

MSG_START = "Bien sûr mon poussin !"
MSG_BOT_ERROR = "Je ne comprends pas la question !!"


def bot_analysis(message):
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
    if len(key_words) != 0:
        msgs_bot.append(MSG_START + " La voici : 7 cité Paradis, 75010 Paris.")
        info_bot = "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? "
        msgs_bot.append(info_bot)
    else:
        msgs_bot.append(MSG_BOT_ERROR)

    return msgs_bot, key_words
