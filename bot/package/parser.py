import json

from ..controler import log


class Parser:
    SYMBOLS = ["!", "?", ",", ".", "'", "-", "*", "+", "=", "/"]
    WORD_SEARCH = ["adresse", "nom"]
    WORD_GREETING = ["salut", "bonjour", "coucou", "hello", "grandpy", "bot", "papy", "robot", "papybot"]

    def __init__(self, file, message):
        """
        ## Initialyse class KillParser
        :param file: File in json format grouping the words to be deleted from the message
        :param message: User's question
        :return:
        """
        self.message = message.lower()
        self.keyWords = []
        self.stopWordsList = json.load(open(file, 'r'))

    def msg_analysis(self):
        """
        ## Analysis of the question posed by the user
        :return: Answer of GrandPy Bot
        """
        words_list = self._msg_filter()
        log.info("PARSER - KEY WORDS IN : %s" % words_list)
        for word in words_list:
            if word not in self.WORD_GREETING:
                self.keyWords.append(word)
        log.info("PARSER - KEY WORDS OUT : %s" % self.keyWords)
        return self.keyWords

    def _msg_filter(self):
        """
        ## Filtering the question to keep only the keywords
        :return: List of keywords
        """
        words_list = self.__symbol_replace()
        log.info("PARSER - FORMAT THE QUESTION : %s" % words_list)
        for stopWord in self.stopWordsList:
            if stopWord in words_list:
                words_list.remove(stopWord)
        return words_list

    def __symbol_replace(self):
        """
        ## Turns the question into a word list
        :return: Word list
        """
        msg = self.message
        for symbol in self.SYMBOLS:
            msg = msg.replace(symbol, " ")
        return msg.split()
