import regex as re

class EmailValidator:

    EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    def __init__(self):
        pass

    def validate(self, email):
        
        if re.match(self.EMAIL_REGEX, email):
            return True
        else:
            return False