"""
    tests for translaor.py
"""
import unittest
from translator import english_to_french, french_to_english

class TestMyTranslator(unittest.TestCase):
    """
      test method for english to french
    """
    def test_english_to_french(self):
        """
            Checking for None
        """
        self.assertNotEqual(english_to_french("None"), '')
        self.assertNotEqual(english_to_french(0), 0)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        
    ##
    #    test method from french to english
    #
    def test_french_to_english(self):
        """
            Checking for None
        """
        self.assertNotEqual(french_to_english("None"), '')
        self.assertNotEqual(french_to_english(0), 0)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        
##
# calling the main code to test the class
#
if __name__=='__main__':
    unittest.main()
