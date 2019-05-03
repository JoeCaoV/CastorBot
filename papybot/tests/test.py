"""Importing unittest and class Parser to test the parser
"""
import unittest

from papybot.classes.parser import Parser

class test_parser_api(unittest.TestCase):
	"""Class containing variable test to check if the parser is OK"""

	def test_empty_string(self):
		"""Method to test the parser result on a empty string"""
		self.parser = Parser()
		response = ''
		string = ''
		self.assertEqual(self.parser.parse_sentence(string), response)

	def test_shorts_words(self):
		"""Method to test the parser result on a string containing
		only words under 3 characters length
		"""
		self.parser = Parser()
		response = ''
		string = 'Je te lu un BD'
		self.assertEqual(self.parser.parse_sentence(string), response)

	def test_apostrophe(self):
		"""Method to test if the parser get rid of apostrophe"""
		self.parser = Parser()
		response = 'Donne adresse Openclassrooms'
		string = "Donne moi l'adresse d'Openclassrooms"
		self.assertEqual(self.parser.parse_sentence(string), response)

	def test_simple_string(self):
		"""Method to test a basic string"""
		self.parser = Parser()
		response = 'trouver magasin jouet Paris'
		string = "Où puis je trouver un magasin de jouet à Paris ?"
		self.assertEqual(self.parser.parse_sentence(string), response)

	def test_long_string(self):
		"""Method to test a string too long (above 100 characters)"""
		self.parser = Parser()
		response = ''
		string = "Je cherche un restaurant végétarien sans gluten pas cher et " \
		         "ouvert jusqu'à 1H du matin avec des séances de Yoga en digestif"
		self.assertEqual(self.parser.parse_sentence(string), response)

class test_parser_text(unittest.TestCase):
	"""Class containing variable test to check if the parser is OK"""

	def test_no_match_string(self):
		"""Testing if the string stay unchanged if there is nothing to remove"""
		self.parser = Parser()
		response = 'Unchanged string cause there is no double ='
		self.assertEqual(self.parser.remove_titles(response), response)

	def test_matching_string(self):
		"""Testing if the string correctly remove the unwanted "== " """
		self.parser = Parser()
		response = 'Text. Text again'
		string = 'Text. == title == Text again'
		self.assertEqual(self.parser.remove_titles(string), response)
		
if __name__ == "__main__":
	unittest.main()