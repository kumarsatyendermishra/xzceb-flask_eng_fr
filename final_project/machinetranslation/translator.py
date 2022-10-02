"""
  language translator
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()
# Api key and url
apikey = os.environ['apikey']
url = os.environ['url']
# authenticating the apikey
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=authenticator)
language_translator.set_service_url(url)

##
#  Translates english to french
#
def english_to_french(english_text):
    """
     Translate text from english to french
    """
    french_text = language_translator.translate(
        text=english_text, model_id="en-fr").get_result()
    return french_text.get("translations")[0].get("translation")

##
#  Translates french to english
#
def french_to_english(french_text):
    """
     Translate text from french to english
    """
    english_text = language_translator.translate(
        text=french_text, model_id="fr-en").get_result()
    return english_text.get("translations")[0].get("translation")
