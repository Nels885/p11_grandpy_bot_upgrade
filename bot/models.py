import json
import logging as log

"""
Provisional list of GrandyBot messages
"""
answerBot = {"Hello PapyBot": ["Bonjour Je suis PapyBot, bienvenue sur mon site !"],
             "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?":
                 ["Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris.",
                  "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? "
                  "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.\n"
                  "Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au\n"
                  "57 rue d'Hauteville et la troisième en impasse. [En savoir plus sur Wikipedia]"]}


class KillParser:
    SYMBOLS = ["!", "?", ",", ".", "'"]
    MSG_START = "Bien sûr mon poussin !"
    MSG_BOT_ERROR = "Je ne comprends pas la question !!"
    WORD_SEARCH = ["adresse", "nom"]
    WORD_GREETING = ["bonjour", "coucou", "hello", "grandpy", "bot"]

    def __init__(self, file):
        """
        ## Initialyse class KillParser
        :param file: File in json format grouping the words to be deleted from the message
        :return:
        """
        log.basicConfig(level=log.INFO)
        self.stopWordsList = json.load(open(file, 'r'))

    def msg_analysis(self, message):
        """
        ## Analysis of the question posed by the user
        :param message: User's question
        :return: Answer of GrandPy Bot
        """
        wordsList = self._msg_filter(message)
        log.info("mots-clés: %s" % wordsList)
        answer = [self.MSG_BOT_ERROR]
        for word in wordsList:
            if word in self.WORD_GREETING:
                answer = [self.MSG_START]
        return answer

    def _msg_filter(self, message):
        """
        ## Filtering the question to keep only the keywords
        :param message: User's question
        :return: List of keywords
        """
        wordsList = self.__symbol_replace(message)
        log.info("Mise en forme question: %s" % wordsList)
        for stopWord in self.stopWordsList:
            if stopWord in wordsList:
                wordsList.remove(stopWord)
        return wordsList

    def __symbol_replace(self, message):
        """
        ## Turns the question into a word list
        :param message: User's question
        :return: Word list
        """
        message = message.lower()
        for symbol in self.SYMBOLS:
            message = message.replace(symbol, " ")
        return message.split()
