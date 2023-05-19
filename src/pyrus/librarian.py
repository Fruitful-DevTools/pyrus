from contextlib import contextmanager

class Librarian:

    @contextmanager
    def get_collection(self, collection):
        
        file = None
        
        try:
            file = open(collection, 'r', newline='')
            yield file
        
        finally:
            if file:
                file.close()

    def lookup(self, collection, *keys):  
        
        file = self.get_collection(collection)

        result = dict(file)
        
        for key in keys:
            if key in result:
                result = result[key]
        
        return result
        