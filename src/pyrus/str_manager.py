"""
The str_manager.py module holds multiple classes and functions for managing and handling
string data inside of python.

Functions:
    string_normaliser: A function for normalising string data.

Classes:
    TitleStringPresenter():
    NameStringPresenter():
"""
from unidecode import unidecode
import unicodedata
import regex as re
import string

whitespace = string.whitespace


def string_normaliser(string, normalise_encoding=False):
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
    lowercase_string = string.casefold()

    # Strip the string of all whitespace
    stripped_string = lowercase_string.strip()
    stripped_string = stripped_string.replace(whitespace, '')

    # While the string contains double spaces
    # This ensures triple and more spaces are replaced
    while '  ' in stripped_string:
        # Turn double spaces into single spaces
        stripped_string = stripped_string.replace('  ', ' ')

    single_spaced_string = stripped_string

    if normalise_encoding:
        # Transform string into canonical representation
        unicode_normalised_string = unicodedata.normalize(
            'NFKD', single_spaced_string)

        # Encode string into ASCII format,
        # Ignore letters that can't be turned into ASCII
        single_spaced_string = unidecode(unicode_normalised_string)

    pattern = re.compile(r'[^\p{L}\s]')

    # Remove special characters from the string
    normalised_string = pattern.sub('', single_spaced_string)

    return normalised_string

def email_normaliser(email):
    
    lowercase_email = email.lower()
    normalised_email = re.sub(r'[^a-z0-9@.]', '', lowercase_email)

    return normalised_email

class Presenter():

    def __init__(self, string):
        self.string = string

    def present(self):
        string = string_normaliser(self.string)
        return string
    
"""
Conventions on Articles, Conjunctions, Prepositions:

    Group 1: Articles, conjunctions, and prepositions are usually not capitalized in titles, unless they are the first word or part of a proper noun.

    French

    Group 2: Articles, conjunctions, and prepositions are typically not capitalized unless they are the first or last word, or if they have four or more letters.

    German
    Dutch

    Group 3: Articles, conjunctions, and prepositions are generally not capitalized in titles, unless they are the first or last word, or if they are stressed as part of the title's style or emphasis.

    Spanish

    Group 4: Articles, conjunctions, and prepositions are typically not capitalized in titles, except when they are the first or last word, or if they have special emphasis or are part of proper nouns.

    Italian
    Portuguese

    Group 5: Articles, conjunctions, and prepositions are generally not capitalized in titles unless they are the first or last word, or if they have special emphasis or are part of proper nouns.

    Norwegian
    Swedish
    Danish
    Finnish
"""

class TitlePresenter(Presenter):

    TITLE_EXCEPTIONS = {}
    def __init__(self, string):
        self.string = string
        super().__init__(string)

    def present_title(self, language=None):

        title = self.present()

        lowercase_title_words = title.split()

        if language == 'en':
            cased_title = self.english_convention(lowercase_title_words)
            title = ' '.join(cased_title)

        elif language == 'fr':
            cased_title = self.french_convention(lowercase_title_words)
            title = ' '.join(cased_title)

        elif language in ('de', 'nl'):
            cased_title = self.german_dutch_convention(lowercase_title_words)
            title = ' '.join(cased_title)

        elif language == 'es':
            cased_title = self.spanish_convention(lowercase_title_words)
            title = ' '.join(cased_title)

        elif language in ('it', 'pt'):
            cased_title = self.italo_portuguese_convention(lowercase_title_words)
            title = ' '.join(cased_title)

        elif language in ('no', 'sv', 'da', 'fi'):
            cased_title = self.nordic_convention(lowercase_title_words)
            title = ' '.join(cased_title)
        
        elif language is None:
            cased_title = self.no_convention(lowercase_title_words)
            title = ' '.join(cased_title)
        
        return title
    
    def no_convention(self, lowercase_title_words):
        return lowercase_title_words


    def english_convention(self, lowercase_title_words):
        
        # Turn non-exception lowercase_title_words in title case
        for word in lowercase_title_words:

            # Find corresponding index of word in lowercase_title_words list
            i = lowercase_title_words.index(str(word))

            # If the word is 'and' and there are no ampersands in the lowercase_title_words list,
            # change the word to ampersand
            if word == 'and' and '&' not in lowercase_title_words:
                lowercase_title_words[i] = '&'

            # If the word is an exception, leave as lower case.
            if word in self.TITLE_EXCEPTIONS['en']:
                continue

            # Otherwise, change to title case.
            else:
                lowercase_title_words[i] = word.title()
        
        return lowercase_title_words

    def french_convention(self, lowercase_title_words):
        return lowercase_title_words
    
    def german_dutch_convention(self, lowercase_title_words):
        """
        This method takes the lower case title, and capitalises the first letter of each word,
        in conformation with title convention in German and Dutch:
        
        Articles, conjunctions, and prepositions are typically not 
        capitalized unless they are the first or last word, or if they have four or more letters.

        Args:
            lowercase_title_words (list): The words of the title in lowercase, put into a list, ready to be capitalised.

        Returns:
            cased_title_words   
        """
        cased_title_words = [
        word.title() if word not in self.TITLE_EXCEPTIONS['de'] or i in (0, len(lowercase_title_words) - 1)
        else word
        for i, word in enumerate(lowercase_title_words)
        ]

        return cased_title_words

    def spanish_convention(self, lowercase_title_words):
        cased_title_words = [
            word.title() if word not in self.TITLE_EXCEPTIONS['es'] or i in(0, len(lowercase_title_words) -1) 
            else word
            for i, word in enumerate(lowercase_title_words)
        ]

        return cased_title_words

    def italo_portuguese_convention(self, lowercase_title_words):
        cased_title_words = [
        word.title() if word not in self.TITLE_EXCEPTIONS['it'] or word not in self.TITLE_EXCEPTIONS['pt'] or i in(0, len(lowercase_title_words) -1) 
        else word
        for i, word in enumerate(lowercase_title_words)
        ]

        return cased_title_words

    def nordic_convention(self, lowercase_title_words):
        return lowercase_title_words
        

class NamePresenter(Presenter):
    pass