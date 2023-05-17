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
    lowercase_string = string.lower()

    # Strip the string of all whitespace
    stripped_string = lowercase_string.strip()

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

        # Turn non-exception words in title case
        for word in words:

            # Find corresponding index of word in words list
            i = words.index(str(word))

            # If the word is 'and' and there are no ampersands in the words list,
            # change the word to ampersand
            if word == 'and' and '&' not in words:
                words[i] = '&'

            # If the word is an exception, leave as lower case.
            if word in self.TITLE_EXCEPTIONS:
                continue

            # Otherwise, change to title case.
            else:
                words[i] = word.title()

        title = ' '.join(words)
        return title


class NamePresenter(Presenter):
    pass
