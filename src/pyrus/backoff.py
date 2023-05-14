from __init__ import *
import asyncio


class Backoff:
    def __init__(self):
        self.attempts = 0

    def __call__(self, func, max_retries=5, delay=1, backoff=2):
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

class AsyncBackoff:
    def __init__(self):
        self.attempts = 0

    async def __call__(self, func, max_retries=5, delay=1, backoff=2):
        while self.attempts <= max_retries:
            try:
                return await func()
            except Exception as e:
                if self.attempts == max_retries:
                    raise e
                else:
                    self.attempts += 1
                    await asyncio.sleep(delay)
                    delay *= backoff