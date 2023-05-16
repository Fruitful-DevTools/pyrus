"""
The str_manager.py module holds multiple classes and functions for managing and handling
string data inside of python.

Functions:
    string_normaliser: A function for normalising string data.

Classes:
    TitleStringPresenter():
    NameStringPresenter():
"""
import unicodedata
import re

def string_normaliser(string):
    """Normalises string data.
    
    This method normalises string data by performing several operations:
    - Converting all characters to lowercase
    - Removing leading/trailing white space
    - Removing double spaces
    - Replacing accented and special characters with their ASCII equivalents
    Args:
        string (str): The string to be normalised.
    Returns:
        normalised_string (str): The normalized string data.
    """
    
    
    # Turn the entire string to lowercase
    lowercase_string = string.lower()

    # Remove special characters from the string
    pattern = r'[^a-zA-Z0-9\s]'
    no_special_characters_string = re.sub(pattern, '', lowercase_string)
    
    # Strip the string of all whitespace
    stripped_string = no_special_characters_string.strip()
    
    # Turn double spaces into single spaces
    single_spaced_string = stripped_string.replace('  ', ' ')
    
    # Transform string into canonical representation
    unicode_normalised_string = unicodedata.normalize('NFKD', single_spaced_string)
    
    # Encode string into ASCII format,
    # Ignore letters that can't be turned into ASCII
    encoded_string = unicode_normalised_string.encode('ASCII', 'ignore')
    
    # Decode string back to UTF-8 format
    normalised_string = encoded_string.decode()
    return normalised_string

class Presenter():

    def __init__(self, string):
        self.string = string
    
    def present(self):
        string = string_normaliser(self.string)
        return string

class TitlePresenter(Presenter):
    
    TITLE_EXCEPTIONS = {'of', 
                        'and', 
                        'but', 
                        'or', 
                        'for', 
                        'yet', 
                        'so', 
                        'a', 
                        'an', 
                        'the'}
    
    def __init__(self, string):
        self.string = string
        super().__init__(string)
    def present_title(self):

        string = self.present()

        words = string.split()
        
        #Turn non-exception words in title case
        for word in words:

            #Find corresponding index of word in words list
            i = words.index(str(word))

            #If the word is 'and' and there are no ampersands in the words list, 
            #change the word to ampersand
            if word == 'and' and '&' not in words:
                words[i] = '&'

            #If the word is an exception, leave as lower case.
            if word in self.TITLE_EXCEPTIONS:
                continue

            #Otherwise, change to title case.
            else:
                words[i] = word.title()
        
        title = ' '.join(words)
        return title

class NamePresenter(Presenter):
    pass
