"""
The data.py module holds multiple classes and functions for managing and handling
data inside of python.
"""

import datetime
import unicodedata


"""
Normalise: These classes provide functionality for normalising data for pre and post-processing.

SuperClasses:
    Normalise():

SubClasses:
    NormaliseString(Normalise): A subclass for normalising string data.
    NormaliseInt(Normalise): A subclass for normalising integer data.
    NormaliseFlt(Normalise): A subclass for normalising float data.
"""

class Normalise:
    
    def __init__(self, data):
        self.data = data

    def normalise(self):

        if isinstance(self.data, str):
            return NormaliseString.normalise()
        
        elif isinstance(self.data, int):
            return NormaliseInt.normalise()
        
        elif isinstance(self.data, float):
            return NormaliseFlt.normalise()
        
        else:
            raise TypeError("Normalise input must be string, integer or float datatype.")

class NormaliseString(Normalise):
    """A subclass of Normalise that normalizes string data.
    
    This subclass provides a method for normalizing string data by performing
    several operations:
    - Converting all characters to lowercase
    - Removing leading/trailing white space
    - Removing double spaces
    - Replacing accented and special characters with their ASCII equivalents
    """
    def normalise(self) -> str:
        """Normalize the string data.
        
        This method normalises string data by performing several operations:
        - Converting all characters to lowercase
        - Removing leading/trailing white space
        - Removing double spaces
        - Replacing accented and special characters with their ASCII equivalents
        
        Returns:
            data (str): The normalized string data.
        """
        data = self.data.lower()
        data = data.strip()
        data = data.replace('  ', ' ')
        data = unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore').decode()
        return data

class NormaliseInt(Normalise):

    def normalise(self):
        pass

class NormaliseFlt(Normalise):

    def normalise(self):
        pass

"""
Present: These classes provide functionality for putting string data into a nice, tidy format.

SuperClasses:
    Present(Normalise)

SubClasses:
    PresentJobTitleString(Present): A sub class for presenting Job Titles.
    PresentNameString(Present): A sub class for presenting people's Names.
"""

class Present(Normalise):

    def __init__(self, string):
        self.string = string
    
    def present(self):
        string = self.normalise(self.string)
        return string

class PresentJobTitleString(Present):
    
    def __init__(self):

        #List of articles, conjunctions and prepositions 
        #not to be put into title case:
        self.title_exceptions = ['of', 
                                'and', 
                                'but', 
                                'or', 
                                'for', 
                                'yet', 
                                'so', 
                                'a', 
                                'an', 
                                'the']
        
    def present_job_title(self, string):

        string = self.present(string)

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
            if word in self.title_exceptions:
                continue

            #Otherwise, change to title case.
            else:
                words[i] = word.title()
        
        title = ' '.join(words)
        return title

class PresentNameString(Present):
    pass


class Clean:
    pass