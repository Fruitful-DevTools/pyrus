from contextlib import contextmanager
from collections import ChainMap
import csv
from typing import Dict, List, Tuple, TextIO


class Librarian:
    
    LIBRARY = 'library/'

    def __init__(self):
        pass

    @contextmanager
    def get_collection(self, collection):

        file = None

        try:
            file = open(collection, 'r', newline='', encoding='utf-8-sig')
            yield file

        except Exception as e:
            raise e

        finally:
            if file:
                file.close()

    def lookup(self, collection: str, *keys: str):

        collection_filepath = f'{self.LIBRARY}{collection}.csv'

        with self.get_collection(collection_filepath) as file:
            open_file = csv.reader(file)
            unmapped_dicts = self.extrapolate_dicts(open_file)
            result_map = self.create_datamap(*unmapped_dicts)
            print(result_map)
            for key in keys:
                if key in result_map:
                    result_map = result_map[key]

            return result_map
    
    def extrapolate_dicts(self, open_file: TextIO) -> Tuple[Dict[str, Dict[str, str]], Dict[str, str], List[List[str]], List[str]]:
        
        rows = list(open_file)
        parent_keys = rows[0]
        child_dict = {}

        for row in rows[1:]:
            child_key = row[0]
            child_value = row[1]
            child_dict[child_key] = child_value

        parent_dict = dict(zip(parent_keys, [child_dict] * len(parent_keys)))
        return parent_dict, child_dict, rows, parent_keys
        
    def create_datamap(self, parent_dict: dict, child_dict: dict, rows: list, parent_keys: tuple) -> ChainMap:

        for row in rows[1:]:
            child_key = row[0]
            child_value = row[1]
            child_dict[child_key] = child_value

        parent_dict = dict(zip(parent_keys, [child_dict] * len(parent_keys)))
        data_map = ChainMap(parent_dict, child_dict)
        return data_map