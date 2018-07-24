import json
import logging as log


class Parser:
    SYMBOLS = ["!", "?", ",", ".", "'", "-", "*", "+", "=", "/"]
    MSG_START = "Bien sûr mon poussin !"
    MSG_BOT_ERROR = "Je ne comprends pas la question !!"
    WORD_SEARCH = ["adresse", "nom"]
    WORD_GREETING = ["bonjour", "coucou", "hello", "grandpy", "bot", "papy", "robot", "papybot"]

    def __init__(self, file, message):
        """
        ## Initialyse class KillParser
        :param file: File in json format grouping the words to be deleted from the message
        :param message: User's question
        :return:
        """
        self.message = message.lower()
        self.keyWords = []
        log.basicConfig(level=log.INFO)
        self.stopWordsList = json.load(open(file, 'r'))

    def msg_analysis(self):
        """
        ## Analysis of the question posed by the user
        :return: Answer of GrandPy Bot
        """
        words_list = self._msg_filter()
        log.info("mots-clés: %s" % words_list)
        answer = self.MSG_START
        for word in words_list:
            if word in self.WORD_GREETING:
                answer = self.MSG_START
            else:
                self.keyWords.append(word)
        log.info("mots-clés restants: %s" % self.keyWords)
        if len(self.keyWords) == 0:
            answer = self.MSG_BOT_ERROR
        return answer, self.keyWords

    def _msg_filter(self):
        """
        ## Filtering the question to keep only the keywords
        :return: List of keywords
        """
        words_list = self.__symbol_replace()
        log.info("Mise en forme question: %s" % words_list)
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
