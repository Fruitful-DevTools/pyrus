from pyrus import backoff
import asyncio
import unittest
import time

class TestBackoff(unittest.TestCase):

    def setUp(self):
        self.backoff = backoff.Backoff()

    def test_backoff_with_no_retries(self):

        # Create a backoff object with no retries
        backoff = self.backoff(lambda: 1)

        # Call the backoff object
        result = backoff

        # Assert that the result is 1
        self.assertEqual(result, 1)

    def test_backoff_with_one_retry(self):

        # Create a backoff object with one retry
        backoff = self.backoff(lambda: 1, max_retries=1)

        # Call the backoff object
        result = backoff

        # Assert that the result is 1
        self.assertEqual(result, 1)

    def test_backoff_with_multiple_retries(self):

        # Create a backoff object with multiple retries
        backoff = self.backoff(lambda: 1, max_retries=3)

        # Call the backoff object multiple times
        for i in range(4):
            result = backoff

        # Assert that the result is 1
        self.assertEqual(result, 1)

    async def test_backoff_with_exponential_backoff(self):

        # Create a backoff object with exponential backoff
        backoff = self.backoff(lambda: 1, max_retries=4, backoff=2)

        # Call the backoff object multiple times
        for i in range(4):
            start = time.time()
            result = await backoff()
            end = time.time()
            print('START:' + str(start))

            # Assert that the result is 1
            self.assertEqual(result, 1)

            # Assert that the time between retries increases exponentially
            self.assertGreater(end - start, i * backoff)


class AsyncBackoffTest(unittest.TestCase):

    async def test_retry_with_exponential_backoff(self):
        backoff = backoff.AsyncBackoff(max_retries=3, delay=1, backoff=2)

        @asyncio.coroutine
        def func():
            raise Exception("This function will always fail")

        with self.assertRaises(Exception):
            await backoff(func)

        self.assertEqual(backoff.attempts, 3)
        self.assertEqual(backoff.delay, 8)

    async def test_retry_with_fixed_backoff(self):
        backoff = backoff.AsyncBackoff(max_retries=3, delay=1)

        @asyncio.coroutine
        def func():
            raise Exception("This function will always fail")

        with self.assertRaises(Exception):
            await backoff(func)

        self.assertEqual(backoff.attempts, 3)
        self.assertEqual(backoff.delay, 1)

    async def test_cancel_retry(self):
        backoff = backoff.AsyncBackoff(max_retries=3, delay=1)

        @asyncio.coroutine
        def func():
            yield from asyncio.sleep(10)
            return "This function will always succeed"

        task = asyncio.ensure_future(backoff(func))
        task.cancel()

        with self.assertRaises(asyncio.CancelledError):
            await task

        self.assertEqual(backoff.attempts, 0)
        self.assertEqual(backoff.delay, 1)


unittest.main()
