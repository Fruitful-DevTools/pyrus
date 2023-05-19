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
from pyrus import librarian

librarian = librarian.Librarian()

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


class Presenter:

    def __init__(self):
        self.articles_conjunctions_prepositions = librarian.lookup(
            collection='articles_conjunctions_prepositions')

    def present_title(self, string_data, linguistic_convention=None):

        title = string_normaliser(string_data)

        words_to_case = title.split()

        if linguistic_convention == 'en':
            cased_title = self.english_convention(words_to_case)
            title = ' '.join(cased_title)

        elif linguistic_convention == 'fr':
            cased_title = self.french_convention(words_to_case)
            title = ' '.join(cased_title)

        elif linguistic_convention in ('de', 'nl'):
            cased_title = self.german_dutch_convention(words_to_case)
            title = ' '.join(cased_title)

        elif linguistic_convention == 'es':
            cased_title = self.spanish_convention(words_to_case)
            title = ' '.join(cased_title)

        elif linguistic_convention in ('it', 'pt', 'no', 'sv', 'da', 'fi'):
            cased_title = self.italo_portuguese_nordic_convention(
                words_to_case)
            title = ' '.join(cased_title)

        elif linguistic_convention is None:
            cased_title = self.no_convention(words_to_case)
            title = ' '.join(cased_title)

        return title

    def no_convention(self, words_to_case):
        cased_title_words = [word if word in self.articles_conjunctions_prepositions else
                             '&' if word == 'and' and '&' not
                             in words_to_case else word.title() for word in words_to_case]
        return cased_title_words

    def english_convention(self, words_to_case):
        cased_title_words = [word if word in self.articles_conjunctions_prepositions['en'] else
                             '&' if word == 'and' and '&' not
                             in words_to_case else word.title() for word in words_to_case]

        return cased_title_words

    def french_convention(self, words_to_case):
        cased_title_words = [
            word.title() if word not in self.articles_conjunctions_prepositions['fr'] or i == 0
            else word
            for i, word in enumerate(words_to_case)
        ]
        return cased_title_words

    def german_dutch_convention(self, words_to_case):
        """
        This method takes the lower case title, and capitalises the first letter of each word,
        in conformation with title convention in German and Dutch:

        Articles, conjunctions, and prepositions are typically not 
        capitalized unless they are the first or last word, or if they have four or more letters.

        Args:
            words_to_case (list): The words of the title in lowercase, put into a list, ready to be capitalised.

        Returns:
            cased_title_words   
        """
        cased_title_words = [
            word.title() if word not in self.articles_conjunctions_prepositions['de'] or i in (0, len(words_to_case) - 1)
            else word
            for i, word in enumerate(words_to_case)
        ]

        return cased_title_words

    def spanish_convention(self, words_to_case):
        cased_title_words = [
            word.title() if word not in self.articles_conjunctions_prepositions['es'] or i in (0, len(words_to_case) - 1)
            else word
            for i, word in enumerate(words_to_case)
        ]
        return cased_title_words

    def italo_portuguese_nordic_convention(self, words_to_case):
        cased_title_words = [
            word.title() if word not in self.articles_conjunctions_prepositions['it']
            or word not in self.articles_conjunctions_prepositions['pt']
            or word not in self.articles_conjunctions_prepositions['no']
            or word not in self.articles_conjunctions_prepositions['sv']
            or word not in self.articles_conjunctions_prepositions['da']
            or word not in self.articles_conjunctions_prepositions['fi']
            or i in (0, len(words_to_case) - 1)
            else word
            for i, word in enumerate(words_to_case)
        ]
        return cased_title_words


class NamePresenter(Presenter):
    pass
