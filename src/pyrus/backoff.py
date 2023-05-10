from __init__ import *


class Backoff:
    def __init__(self):
        self.attempts = 0

    def __call__(self, func, max_retries, delay, backoff):
        while self.attempts <= max_retries:
            try:
                return func()
            except Exception as e:
                if self.attempts == max_retries:
                    raise e
                else:
                    self.attempts += 1
                    time.sleep(delay)
                    delay *= backoff