"""The STOPWORDS from CONFIG is a list of unwanted words"""
import re
from papybot.config import STOPWORDS

class Parser():
    """This class will contain methods to parse different string data
    to return a different string usable for the next steps of the
    programm
    """
    def __init__(self):
        pass

    @staticmethod
    def parse_sentence(string):
        """This method take the given string, split into a list of words
        then parse each word according to their length or if they
        belong to the STOPWORDS list
        """
        result = ''
        if len(string) > 99:
            return result
        words = string.split()
        for word in words:
            try:
                if int(word):
                    if not result:
                        result += word
                    else:
                        result += ' ' + word
            except ValueError:
                if len(word) > 2 and word not in STOPWORDS:
                    #This part is to get ride of apostrophe
                    word = word.split("'")
                    if not result:
                        result += word[-1]
                    else:
                        result += ' ' + word[-1]
        return result

    @staticmethod
    def remove_number(string):
        """This method will remove the numbers.
        UPDATE : Not used anymore but keeping it just in case...
        """
        result = ''
        words = string.split()
        for word in words:
            try:
                int(word)
            except ValueError:
                if not result:
                    result += word
                else:
                    result += ' ' + word
        return result

    @staticmethod
    def remove_titles(string):
        """The data retrivied from Wiki Media API return some
        unwanted titles like " == Title == " so this method
        erase them and return the new string
        """
        sentence = re.sub("={2}\s.*\s={2}\s", "", string)
        return sentence
