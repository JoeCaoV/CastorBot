"""Importing unittest and class Parser to test the parser
"""
import json
import unittest
from unittest.mock import patch

import wikipedia

from papybot.classes.parser import Parser
from papybot.classes.google_api import GmApi
from papybot.classes.wiki_api import WikiApi


class TestParserApi(unittest.TestCase):
    """Class containing variable test to check if the parser is OK"""

    def setUp(self):
        """setting Parser class"""
        self.parser = Parser()

    def test_empty_string(self):
        """Method to test the parser result on a empty string"""
        response = ''
        string = ''
        self.assertEqual(self.parser.parse_sentence(string), response)

    def test_shorts_words(self):
        """Method to test the parser result on a string containing
        only words under 3 characters length
        """
        response = ''
        string = 'Je te lu un BD'
        self.assertEqual(self.parser.parse_sentence(string), response)

    def test_apostrophe(self):
        """Method to test if the parser get rid of apostrophe"""
        response = 'Donne adresse Openclassrooms'
        string = "Donne moi l'adresse d'Openclassrooms"
        self.assertEqual(self.parser.parse_sentence(string), response)

    def test_simple_string(self):
        """Method to test a basic string"""
        response = 'trouver magasin jouet Paris'
        string = "Où puis je trouver un magasin de jouet à Paris ?"
        self.assertEqual(self.parser.parse_sentence(string), response)

    def test_long_string(self):
        """Method to test a string too long (above 100 characters)"""
        response = ''
        string = "Je cherche un restaurant végétarien sans gluten pas cher et " \
                 "ouvert jusqu'à 1H du matin avec des séances de Yoga en digestif"
        self.assertEqual(self.parser.parse_sentence(string), response)

class TestParserName(unittest.TestCase):
    """Class containing the tests for the parser removing the "==" """

    def setUp(self):
        """setting Parser class"""
        self.parser = Parser()

    def test_empty_string(self):
        """Test if the string is empty"""
        response = ''
        self.assertEqual(self.parser.remove_titles(response), response)

    def test_no_match_string(self):
        """Testing if the string stay unchanged if there is nothing to remove"""
        response = 'Unchanged string cause there is no double ='
        self.assertEqual(self.parser.remove_titles(response), response)

    def test_matching_string(self):
        """Testing if the string correctly remove the unwanted "== " """
        response = 'Text. Text again'
        string = 'Text. == title == Text again'
        self.assertEqual(self.parser.remove_titles(string), response)

class TestApiRequests(unittest.TestCase):
    """Class containing the tests for the Api requests"""
    def setUp(self):
        """Setting the Api Classes"""
        self.api_gm = GmApi('key')
        self.wiki_api = WikiApi()

    @patch('papybot.classes.google_api.requests.get')
    def test_http_return(self, mock_api):
        """Trying a wanted result"""
        result = {
            "results" :[
                {
                    'place_id' : "ChIJIZX8lhRu5kcRGwYk8Ce3Vc8"
                }
            ],
            "status" : 'OK'
        }
        mock_api.return_value.status_code = 200
        mock_api.return_value.json.return_value = result
        response = self.api_gm.request_search('String')
        self.assertEqual(response, {'place_id' : "ChIJIZX8lhRu5kcRGwYk8Ce3Vc8"})

    @patch('papybot.classes.google_api.requests.get')
    def test_error_return(self, mock_api):
        """Trying an unwanted result"""
        mock_api.return_value.status_code = 403
        response = self.api_gm.request_search('String')
        self.assertEqual(response, False)

    @patch('papybot.classes.google_api.requests.get')
    def test_bad_details_requestt(self, mock_api):
        """Trying a bad Api details request result"""
        result = {
            "results" :[
                {
                    'Nothing' : "The wanted element doesn't exist"
                }
            ],
            "status" : 'OK'
        }
        mock_api.return_value.json.return_value = result
        response = self.api_gm.request_details('String')
        self.assertFalse(response)

    @patch('papybot.classes.google_api.requests.get')
    def test_bad_details_requestt(self, mock_api):
        """Trying a good Api details request result"""
        result = {
            "result" :
                {
                    'formatted_address' : "66 Rue Rivole, Paris France",
                    'address_components' : [
                        {
                            "long_name": "Cité Paradis",
                            "short_name": "Cité Paradis",
                            "types": ["route"]
                        }
                    ],
                    'name' : 'Openclassrooms',
                },
            "status" : 'OK'
        }
        mock_api.return_value.json.return_value = result
        response = self.api_gm.request_details('String')
        self.assertEqual(response, {'address' : '66 Rue Rivole, Paris France', 'route' : 'Cité Paradis'})

    @patch('wikipedia.search', return_value="title")
    @patch('wikipedia.page')
    @patch('wikipedia.summary', return_value="summary")
    def test_good_request(self, mock_summary, mock_page, mock_search):
        """Trying a wanted result"""
        class Page:
            """creating a objet Page to return for wikipidia page mock"""
            def __init__(self):
                self.url = 'url'
        mock_page.return_value = Page()
        self.assertEqual(self.wiki_api.get_data('mock'), {"text" : "summary", "url" : "url"})

    @patch('wikipedia.search', side_effect=wikipedia.exceptions.DisambiguationError('', ''))
    @patch('wikipedia.page')
    @patch('wikipedia.summary', return_value="summary")
    def test_wrong_request(self, mock_summary, mock_page, mock_search):
        """Trying to raise an Exception"""
        class Page:
            """creating a objet Page to return for wikipidia page mock"""
            def __init__(self):
                self.url = 'url'
        mock_page.return_value = Page()
        self.assertEqual(self.wiki_api.get_data('mock'), {"text" : "", "url" : False})

if __name__ == "__main__":
    unittest.main()
