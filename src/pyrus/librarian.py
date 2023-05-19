from contextlib import contextmanager
from collections import ChainMap
from pandas import read_csv
import csv


class Librarian:
    LIBRARY = 'library/'

    def __init__(self, custom_library):
        self.custom_library = custom_library

    @contextmanager
    def get_collection(self, collection):

        file = None

        try:
            file = open(collection, 'r', newline='')
            yield file

        except Exception as e:
            raise e

        finally:
            if file:
                file.close()

    def lookup(self, collection: str, *keys: str):

        collection_filepath = f'{self.LIBRARY}{collection}.csv'

        with self.get_collection(collection_filepath) as file:
            result_dict = csv.DictReader(file)
            print(result_dict)
            result_map = ChainMap(result_dict)

            for key in keys:
                if key in result_map:
                    result_file = result_map[key]

            return result_file
