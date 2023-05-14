from . import *

"""
def log(msg):
    logging.info(msg)


def validate_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None


def get_timestamp():
    return int(time.time())


def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def download_file(url, filename):
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)


def parse_arguments(args):
    params = {}
    for arg in args:
        key, value = arg.split('=')
        params[key] = value
    return params


def flatten_list(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened += flatten_list(item)
        else:
            flattened.append(item)
    return flattened
"""