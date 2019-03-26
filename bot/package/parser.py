import re

from ..controller import log


class Parser:
    WORD_SEARCH = ["adresse", "trouve", "rue"]
    MANDATORY_KEYWORD = "adresse"

    def __init__(self, stop_words):
        """
        ## Initialize class KillParser
        :param file: File in json format grouping the words to be deleted from the message
        :param message: User's question
        :return:
        """
        self.message = None
        self.keyWords = []
        self.stopWordsList = stop_words

    def msg_analysis(self, message):
        """
        ## Analysis of the question posed by the user
        :return: Answer of GrandPy Bot
        """
        self.message = message.lower()
        words_list = self._msg_filter()
        log.info("PARSER - KEY WORDS IN : %s" % words_list)
        for word in words_list:
            if word not in self.stopWordsList["greeting"]:
                self.keyWords.append(word)
        if not self._search_keyword():
            self.keyWords = []
        log.info("PARSER - KEY WORDS OUT : %s" % self.keyWords)
        return self.keyWords

    def _msg_filter(self):
        """
        ## Filtering the question to keep only the keywords
        :return: List of keywords
        """
        words_list = self._symbol_replace()
        log.info("PARSER - FORMAT THE QUESTION : %s" % words_list)
        for stopWord in self.stopWordsList["fr_words"]:
            if stopWord in words_list:
                words_list.remove(stopWord)
        return words_list

    def _symbol_replace(self):
        """
        ## Turns the question into a word list
        :return: Word list
        """
        msg = re.sub(r"[^\w\s]+", " ", self.message)
        log.info("PARSER - SUP PUNCTUATION : %s" % msg)
        return msg.split()

    def _search_keyword(self):
        """
        ## Search the mandatory keyword
        :return: True if keyword has been found
        """
        for word in self.keyWords:
            # print(word)
            if len(self.keyWords) > 1 and word in self.stopWordsList["key_words"]:
                pos = self.keyWords.index(word)
                self.keyWords[pos] = self.MANDATORY_KEYWORD
                return True
        return False

    def _identify_request(self):
        pass
