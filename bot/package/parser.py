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
        self.stopWordsList = stop_words

    def msg_analysis(self, message):
        """
        ## Analysis of the question posed by the user
        :return: Answer of GrandPy Bot
        """
        self.message = message.lower()
        words_list = self._msg_filter()
        log.info("PARSER - KEY WORDS IN : %s" % words_list)
        words_list = self._identify_message(words_list)
        # for word in words_list:
        #     if word not in self.stopWordsList["greeting"]:
        #         self.keyWords.append(word)

        log.info("PARSER - KEY WORDS OUT : %s" % words_list)
        return words_list

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

    def _search_keyword(self, words_list):
        """
        ## Search the mandatory keyword
        :return: keyword position has been found
        """
        pos = None
        for word in words_list:
            # print(word)
            if word in self.stopWordsList["key_words"]:
                pos = words_list.index(word)
        return pos

    def _identify_message(self, words_list):
        pos = self._search_keyword(words_list)
        if pos is not None:
            words_list[pos] = self.MANDATORY_KEYWORD
            if len(words_list[pos:]) > 1:
                return words_list[pos:]
        return []
